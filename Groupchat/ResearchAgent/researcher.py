import autogen

import os
os.environ["OPENAI_API_KEY"] = "dummy_api_key"

llm_config = {"config_list": [{
    "model": "gpt-3.5-turbo"
}]}

llm_config_local = {"config_list": [{
    "model": "llama-3.2-3b-instruct",
    "base_url": "http://localhost:1234/v1" 
}]}

user_proxy = autogen.UserProxyAgent(
    name = "Admin",
    system_message = "A human admin. Interact with the planner to discuss the plan. Plan execution needs to be approved by this admin.",
    code_execution_config = {
        "work_dir": "code",
        "use_docker": False
    },
    human_input_mode="TERMINATE",
)

engineer = autogen.AssistantAgent(
    name="Engineer",
    llm_config=llm_config_local,
    system_message="""Engineer. You follow an approved plan. Make sure you save code to disk.  You write python/shell 
    code to solve tasks. Wrap the code in a code block that specifies the script type and the name of the file to 
    save to disk.""",
)

scientist = autogen.AssistantAgent(
    name="Scientist",
    llm_config=llm_config_local,
    system_message="""Scientist. You follow an approved plan. You are able to categorize papers after seeing their 
    abstracts printed. You don't write code.""",
)

planner = autogen.AssistantAgent(
    name="Planner",
    system_message="""Planner. Suggest a plan. Revise the plan based on feedback from admin and critic, until admin approval.
The plan may involve an engineer who can write code and a scientist who doesn't write code.
Explain the plan first. Be clear which step is performed by an engineer, and which step is performed by a scientist.
""",
    llm_config=llm_config_local,
)

critic = autogen.AssistantAgent(
    name="Critic",
    system_message="Critic. Double check plan, claims, code from other agents and provide feedback. Check whether the "
                   "plan includes adding verifiable info such as source URL.",
    llm_config=llm_config_local,
)

group_chat = autogen.GroupChat(
    agents=[user_proxy, engineer, scientist, planner, critic], messages=[], max_round=12, speaker_selection_method = "round_robin"
)

manager = autogen.GroupChatManager(
    groupchat = group_chat,
    code_execution_config = {"use_docker": False},
    llm_config = llm_config_local, 
)

user_proxy.initiate_chat(
    manager,
    message="""
Find papers on LLM applications from google scholar in the last week, create a markdown table of different domains.
""",
)


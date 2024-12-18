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
    name = "User",
    system_message = "Executor. Execute the code written by the coder and suggest some updates if there are errors. Make sure to save the file to the disk",
    code_execution_config = {
        "work_dir": "code",
        "use_docker": False
    },
    human_input_mode="TERMINATE",
)

coder = autogen.AssistantAgent(
    name="coder",
    llm_config=llm_config_local,
    system_message="""coder. If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as Coder. Your job is to write and compelete code. You are an expert game programmer. Make sure to save the code to the disk """,
)

pm = autogen.AssistantAgent(
    name = "product_manager",
    llm_config=llm_config_local,
    system_message = "Help plan out to create games"
)

group_chat = autogen.GroupChat(
    agents = [user_proxy, coder, pm],
    messages = [],
    max_round=15
)

manager = autogen.GroupChatManager(
    groupchat = group_chat,
    code_execution_config = {"use_docker": False},
    llm_config = llm_config_local, 
)

user_proxy.initiate_chat(
    manager,
    message="""
I would like to create a snake game in Python!  Make sure the game ends when the player hits the side of the screen and there should be apples, when the snake collects those apples the score should be increased by 1.
""",
)
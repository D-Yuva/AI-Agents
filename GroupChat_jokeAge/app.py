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


bob = autogen.AssistantAgent(
    name = "bob",
    system_message = "You love telling jokes",
    llm_config = llm_config_local
)

alice = autogen.AssistantAgent(
    name = "alice",
    system_message = "Criticise the joke and then just reply 'TERMINATE'",
    llm_config = llm_config_local
)

def termination_message(msg):
    return "TERMINATE" in str(msg.get("content",""))

user_proxy = autogen.UserProxyAgent(
    name = "user_proxy",
    code_execution_config = {"use_docker": False},
    is_termination_msg = termination_message,
    human_input_mode = "NEVER"
)

groupchat = autogen.GroupChat(
    agents = [bob,alice,user_proxy],
    messages = [],
    speaker_selection_method = "round_robin"
)

manager = autogen.GroupChatManager(
    groupchat = groupchat,
    code_execution_config = {"use_docker": False},
    llm_config = llm_config_local, 
    is_termination_msg = termination_message
)

user_proxy.initiate_chat(
    manager, 
    message="Tell another joke"
)
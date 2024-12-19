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

assistant_quote1 = autogen.AssistantAgent(
    name = "assistant1",
    system_message = "You are an assistant who gives quotes. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config_local
)

assistant_quote2 = autogen.AssistantAgent(
    name = "assistant2",
    system_message = "You are anotehr assistant who gives quotes. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config_local,
    max_consecutive_auto_reply = 1
)

assistant_create_new = autogen.AssistantAgent(
    name = "assistant3",
    system_message = "You will create a new quote based on others. Return 'TERMINATE' when the task is done.",
    llm_config = llm_config_local,
    max_consecutive_auto_reply = 1
)

user_proxy = autogen.UserProxyAgent(
    name = "user_proxy",
    is_termination_msg = lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode = "NEVER",
    max_consecutive_auto_reply = 1,
    code_execution_config = False
)

user_proxy.initiate_chats(
    [
        {
            "recipient": assistant_quote1,
            "message": "Give a quote from famous author",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm" #Will take the whole chat convo from the agent1 summarize it and feed it to agent 2
            #Whereas last_message another method will feed the agent 2 with only the last message

        },
                {
            "recipient": assistant_quote2,
            "message": "Give another quote from famous author",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm" #Will take the whole chat convo from the agent1 summarize it and feed it to agent 2
            #Whereas last_message another method will feed the agent 2 with only the last message
            
        },

                {
            "recipient": assistant_create_new,
            "message": "Based on the previous quotes, come up with a new one",
            "clear_history": True,
            "silent": False,
            "summary_method": "reflection_with_llm" #Will take the whole chat convo from the agent1 summarize it and feed it to agent 2
            #Whereas last_message another method will feed the agent 2 with only the last message
            
        }
    ]
)



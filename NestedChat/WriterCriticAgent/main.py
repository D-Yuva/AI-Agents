import autogen

import os
os.environ["OPENAI_API_KEY"] = "dummy_api_key"

llm_config = {"config_list": [{
    "model": "gpt-3.5-turbo",
    "cache_seed": 45, 
    "temperature": 0,
    "timeout": 120,
}]}

llm_config_local = {"config_list": [{
    "model": "llama-3.2-3b-instruct",
    "base_url": "http://localhost:1234/v1" 
}]}

task = "Write a consice but engaing blog post about Meta."

writer = autogen.AssistantAgent(
    name="Writer",
    llm_config=llm_config_local,
    system_message="""
    You are a professional writer, known for your insightful and engaging articles.
    You transform complex concepts into compelling narratives.
    You should improve the quality of the content based on the feedback from the user.
    """,
)

user_proxy = autogen.UserProxyAgent(
    name="User",
    human_input_mode="NEVER",
    is_termination_msg=lambda x: x.get("content", "").find("TERMINATE") >= 0,
    code_execution_config={
        "last_n_messages": 1,
        "work_dir": "my_code",
        "use_docker": False,
    }
)

critic = autogen.AssistantAgent(
    name="Critic",
    llm_config=llm_config_local,
    system_message="""
    You are a critic, known for your thoroughness and commitment to standards.
    Your task is to scrutinize content for any harmful elements or regulatory violations, ensuring
    all materials align with required guidelines.
    For code
    """,
)


def reflection_message(recipient, messages, sender, config):
    print("Reflecting...")
    return f"Reflect and provide critique on the following writing. \n\n {recipient.chat_messages_for_summary(sender)[-1]['content']}"


user_proxy.register_nested_chats(
    [
        {
            "recipient": critic,
            "message": reflection_message,
            "summary_method": "last_msg",
            "max_turns": 1
         }
    ],
    trigger=writer
)

user_proxy.initiate_chat(recipient=writer, message=task, max_turns=2, summary_method="last_msg")
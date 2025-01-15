import os
from autogen import AssistantAgent, UserProxyAgent

# Configure
config_list = [{
    "model": "llama-3.2-90b-vision-preview",
    "api_key": os.environ.get("GROQ_API_KEY"),
    "api_type": "groq"
}]

# Create an AI assistant
assistant = AssistantAgent(
    name="groq_assistant",
    system_message="You are a helpful AI assistant.",
    llm_config={"config_list": config_list}
)

# Create a user proxy agent (no code execution in this example)
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

# Start a conversation between the agents
user_proxy.initiate_chat(
    assistant,
    message="Open chrome browser"
)

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


def main():
    assistant = autogen.AssistantAgent(
        name="Assistant",
        llm_config=llm_config_local
    )

    user_proxy = autogen.UserProxyAgent(
        name="user",
        human_input_mode="NEVER",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    user_proxy.initiate_chat(assistant, message="Plot a chart of META and TESLA stock price change.")


if __name__ == "__main__":
    main()
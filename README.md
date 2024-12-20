# AI Agents

    Use qwen 32B or llama3 70B for much better results 

    pip install pyautogen

    Download LM Studio
      - Download the required model 
      - Start the model's server 
      - Copy the curl of the model and run it in the terminal 
      - copy the CURL address (EX: http://localhost:1234/v1) and place it in the base URL

### Solar Agent: 
  Finds the mass of the planet and performs arthemetic operations 

### Group Chat Agent: 

#### Research Agent

![Group Chat](https://github.com/user-attachments/assets/02d3f7b5-84f2-49f5-874e-7d53c11be935)

#### Jokes Agent
  Bob, Alice, user_proxy and manager- 4 AI Agents communicates with each other
  
    Bob: Tells a joke
  
    Alice: Creticises the joke
  
    user_proxy: Terminates the joke if alice says so
  
    manager: Manages the other 3 agents 

### Coding Agent 
  
   Consists of two agents, User and Assistant

      The Assistant Agent creates a folder coding, and under the file creates a python script 

      The User Agent launches the code and finds out the error present in the assistants code, sends it back to the assistant to fix it, 
      this prcoess continues until the desired, fulling functing code is completed

### Sequential Chat

Sequential chat in AI is when the AI remembers the flow of the conversation and responds based on what was said earlier. It keeps track of previous messages so it can give more relevant and connected answers, making the conversation feel natural and ongoing.

![Group Chat (1)](https://github.com/user-attachments/assets/82f5c3f9-f07f-43fa-bd60-b69c145ba114)

    reflection_with_llm- You can take the entire conversation from Agent 1, summarize it, and give that summary to Agent.
    
    last_message- Alternatively, you can use the "last_message" method to only pass the most recent message to Agent 2.

In the particular QuotesAgent we have used reflection_with_llm

![Group Chat (2)](https://github.com/user-attachments/assets/c5a06e95-f7b4-44cb-a59b-4c73b773c33e)

### Nested Agent

![4](https://github.com/user-attachments/assets/e06023a2-32b7-4b03-9077-9fd214b992ce)

![5](https://github.com/user-attachments/assets/0eda6481-64e7-4064-a5ee-b7f546f9a038)

  

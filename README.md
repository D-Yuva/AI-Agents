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

  

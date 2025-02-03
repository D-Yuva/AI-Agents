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
        human_input_mode="TERMINATE",
        code_execution_config={
            "work_dir": "coding",
            "use_docker": False
        }
    )

    task_prompt = """
    Create a Python program using matplotlib to visualize population and GDP data for different countries and years. The program should:

    1. Set up the required imports:
       - matplotlib.pyplot
       - pandas (for data handling)
       - numpy (if needed)

    2. Ask the user for:
       - Specific years to analyze
       - Specific countries to analyze
       - Any particular quantities they want to analyze or understand (e.g., population growth, GDP per capita)

    3. Create or import sample data for the specified countries and years including:
       - Country names
       - Population sizes
       - GDP values
       You can either create a CSV file or include the data directly in the code.

    4. Implement the following visualizations:
       a) Bar charts comparing:
          - Population sizes across countries for each specified year
          - GDP values across countries for each specified year
       b) Pie charts showing:
          - Distribution of total global GDP by country for each specified year
          - Distribution of total global population by country for each specified year

    5. Requirements:
       - Use appropriate matplotlib functions for plotting
       - Include proper labels, titles, and legends
       - Format numbers appropriately (e.g., millions, billions)
       - Add comments explaining the code
       - Ensure the visualizations are clear and professional
       - Use plt.figure() to create separate figures for each plot
       - Implement proper sizing and layout

    6. Extra features:
       - Add color coding for better visualization
       - Include percentage labels in pie charts
       - Sort data in bar charts for better comparison
       - Add grid lines where appropriate
       - Use plt.style to enhance visual appeal

    Please write the complete Python code to accomplish this task, including data creation/import and all visualizations.
    Make sure to use matplotlib's object-oriented interface (fig, ax = plt.subplots()) for better control over the plots.
    """

    user_proxy.initiate_chat(assistant, message=task_prompt)

if __name__ == "__main__":
    main()

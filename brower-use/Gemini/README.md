# Browser Use with Gemini Integration

A Python-based browser automation tool that uses Gemini AI to control web browsers for automated tasks.

### Prerequisites

* Python 3.11 or higher
* Gemini API key
* Playwright

## Installation

1. Install the package using pip:

        pip install browser-use

2. Install Playwright:

        playwright install

3. Set up your environment variables by creating a .env file in your project root:

        GEMINI_API_KEY=your_api_key_here

## Configuration Options

* max_actions_per_step: Maximum number of actions the agent can take per step (default: 4)
* max_steps: Maximum number of steps the agent can take overall (default: 25)
* model: Currently using 'gemini-2.0-flash-exp'

## Features

* Automated browser control using AI
* Support for complex web navigation tasks
* Configurable action limits
* Asynchronous execution
* Environment variable management
* Error handling for missing API keys

## Dependencies

* browser-use
* langchain-google-genai
* python-dotenv
* pydantic
* playwright

  

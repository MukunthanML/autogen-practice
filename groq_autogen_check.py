from autogen import AssistantAgent, UserProxyAgent
import os

# Configuration for the AI model
config_list = [{
    "model": "llama-3.3-70b-versatile",
    "api_key": os.environ.get("GROQ_API_KEY"),
    "api_type": "groq"
}]

# Create an AI assistant agent with a specified system message and model configuration
assistant = AssistantAgent(
    name="groq_assistant",
    system_message="You are a helpful AI assistant.",
    llm_config={"config_list": config_list}
)

# Create a user proxy agent to simulate user interactions (code execution is disabled in this example)
user_proxy = UserProxyAgent(
    name="user_proxy",
    code_execution_config=False
)

# Function to handle multiple interactions
def chat_with_assistant():
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending chat.")
            break
        response = user_proxy.initiate_chat(assistant, message=user_input)
        print(f"Assistant: {response}")

# Start the chat loop
chat_with_assistant()

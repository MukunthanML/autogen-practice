from autogen import AssistantAgent, UserProxyAgent
import os

def get_config():
    """Retrieve the configuration for the AI model."""
    return [{
        "model": "llama-3.3-70b-versatile",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "api_type": "groq"
    }]

def create_assistant(config_list):
    """Create an AI assistant agent."""
    return AssistantAgent(
        name="groq_assistant",
        system_message="You are a helpful AI assistant.",
        llm_config={"config_list": config_list}
    )

def create_user_proxy():
    """Create a user proxy agent."""
    return UserProxyAgent(
        name="user_proxy",
        code_execution_config=False
    )

def chat_with_assistant(user_proxy, assistant):
    """Handle multiple interactions with the assistant."""
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Ending chat.")
            break
        response = user_proxy.initiate_chat(assistant, message=user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    config_list = get_config()
    assistant = create_assistant(config_list)
    user_proxy = create_user_proxy()
    chat_with_assistant(user_proxy, assistant)

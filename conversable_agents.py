import pprint
from autogen import ConversableAgent
import os

def get_config():
    """Retrieve the configuration for the AI model."""
    return [{
        "model": "llama-3.3-70b-versatile",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "api_type": "groq"
    }]

def create_manual_tester():
    """Create a Manual Tester Agent."""
    return ConversableAgent(
        name="manual_tester",
        system_message="You are a Manual Tester. Your job is to perform exploratory and usability testing. Discuss testing approaches with the Automation Tester and your reply should be only one line.",
         llm_config={"config_list": config_list, "max_lines": 3}
    )

def create_automation_tester():
    """Create an Automation Tester Agent."""
    return ConversableAgent(
        name="automation_tester",
        system_message="You are an Automation Tester. Your job is to automate tests using Selenium, API testing tools, and CI/CD pipelines. Discuss automation benefits with the Manual Tester and your reply should be only one line.",
         llm_config={"config_list": config_list, "max_lines": 3})

def start_conversation(automation_tester, manual_tester):
    """Start a conversation between the automation tester and manual tester."""
    return automation_tester.initiate_chat(
        manual_tester,
        message="Do you think automation can replace manual testing completely?",
        max_turns=2
    )

if __name__ == "__main__":
    config_list = get_config()
    manual_tester = create_manual_tester()
    automation_tester = create_automation_tester()
    chat_result= start_conversation(automation_tester, manual_tester)
    print("\n\nSummary of the conversation:")
    print(chat_result.summary)
    pprint.pprint(chat_result.chat_history)
    pprint.pprint(chat_result.cost)


from autogen import ConversableAgent

# Create a Manual Tester Agent
manual_tester = ConversableAgent(
    name="manual_tester",
    system_message="You are a Manual Tester. Your job is to perform exploratory and usability testing. Discuss testing approaches with the Automation Tester."
)

# Create an Automation Tester Agent
automation_tester = ConversableAgent(
    name="automation_tester",
    system_message="You are an Automation Tester. Your job is to automate tests using Selenium, API testing tools, and CI/CD pipelines. Discuss automation benefits with the Manual Tester."
)

# Start a conversation between them for 5 rounds
conversation = automation_tester.initiate_chat(
    manual_tester,
    message="Do you think automation can replace manual testing completely?",
    max_turns=5
)

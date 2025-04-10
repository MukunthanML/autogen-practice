import os
from autogen.agentchat import GroupChat, GroupChatManager
from autogen.agentchat import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent


os.environ["AUTOGEN_USE_DOCKER"] = "False"


# LLM Config
llm_config = {
    "model": "llama-3.3-70b-versatile",
    "api_key": os.environ.get("GROQ_API_KEY"),
    "api_type": "groq"
}

def termination_msg(x):
    return isinstance(x, dict) and "TERMINATE" == str(x.get("content", ""))[-9:].upper()

# Test Case Writer Agent

test_manager = RetrieveUserProxyAgent(
    name="test_manager",
    is_termination_msg=termination_msg,
    system_message=(
        "You are a test manager. Take clear test case requirements or update requests "
        "for creating Salesforce test cases and pass them to test_case_writer."
    ),
    human_input_mode="NEVER",
    max_consecutive_auto_reply=3,
    llm_config=llm_config,
    retrieve_config={
        "task": "code",
        "docs_path": "docs",
        "chunk_token_size": 1000,
        "model": llm_config["model"],
        "get_or_create": True, # set to False if you don't want to reuse an existing collection
    },
    code_execution_config=False,  # We don't want to execute code in this case.
)

# Test Case Reviewer Agent
test_case_writer = AssistantAgent(
    name="test_case_writer",
     is_termination_msg=termination_msg,
    human_input_mode="NEVER",
    llm_config=llm_config,
    system_message="""
You are a Salesforce QA engineer. Write test cases in CSV format for the given scenarios and roles.
The test cases should be clear, concise, and follow the best practices for Salesforce testing.
The test cases should include all the requirement and scenarions provided by the test manager agent.  
"""
)

# Test Case Reviewer Agent
test_case_reviewer = AssistantAgent(
    name="test_case_reviewer",
     is_termination_msg=termination_msg,
    human_input_mode="NEVER",
    llm_config=llm_config,
    system_message="""
You are an ISTQB-certified reviewer. Review the test case CSV for structure, clarity, coverage, and Salesforce terminology as mentioned 
in the context
If any suggesions or improvements are needed, please provide them in a clear and concise manner. 
And share to the test_case_writer agent for updates.
Approve only if all review comments are addressed by test case writer agent.
Reply with either:
- Approved ✅
- Suggestions for improvement ❌
Once approved by reviewer, Reply `TERMINATE` in the end when everything is done.",
"""
)


groupchat = GroupChat(
    agents=[test_case_writer, test_case_reviewer],
    messages=[],
    max_round=12, speaker_selection_method="round_robin"
)

groupchat_manager = GroupChatManager(
    groupchat=groupchat,
    human_input_mode="NEVER",
    llm_config=llm_config,
)

# Run the framework
def generate_salesforce_test_suite():
    test_manager.reset()
    test_case_writer.reset()
    test_case_reviewer.reset()
    groupchat_manager.reset()  

    test_manager.initiate_chat(
        groupchat_manager,
        message=test_manager.message_generator,
        problem="""
        Create 2 tests cases for the Salesforce Sales Cloud application.
        "Scenario 1:** A Sales Rep creates a new Opportunity from scratch for admin role with test data."
        "Scenario 2:** A Sales Rep converts a Lead into an Opportunity for admin role with test data.
        """
    )

# 🚀 Launch the pipeline
generate_salesforce_test_suite()

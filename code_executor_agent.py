from autogen.coding import LocalCommandLineCodeExecutor
import tempfile
import os





from autogen import ConversableAgent
import os
def get_config():
    """Retrieve the configuration for the AI model."""
    return [{
        "model": "llama-3.3-70b-versatile",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "api_type": "groq"
    }]
def create_code_writer():
    """Create a Code Writer Agent."""


    # The code writer agent's system message is to instruct the LLM on how to use
    # the code executor in the code executor agent.
    code_writer_system_message = """You are a helpful AI assistant.
    Solve tasks using your coding and language skills.
    In the following cases, suggest Python code (in a Python coding block) for the user to execute.
    1. When you need to solve Python interview problems, generate complete Python programs demonstrating concepts, algorithms, and best practices.
    2. When a problem requires clarification, explain your approach before writing the Python code. Ensure the plan is clear before proceeding with execution.
    3. When executing code, provide a fully functional Python program that runs correctly. Use print()` for output.
    4. Follow best Python practices, such as meaningful variable names, proper indentation, and inline comments. When applicable, use object-oriented principles.
    5. If a file needs to be created, specify the filename with `// filename: <filename>.py` as the first line inside the code block.
    6. Suggest alternative or optimized solutions when possible, explaining trade-offs in time and space complexity.
    7. Validate code execution results. If errors occur, analyze, debug, and provide a corrected full Python program instead of partial fixes.
    8. Consider edge cases such as null inputs, empty collections, and large values. Provide sample inputs/outputs to demonstrate expected behavior.
    9. If required, iterate over different solutions to improve efficiency or readability.
    10. Verify answers carefully before concluding. Include relevant explanations or theoretical insights where applicable.

    Reply 'TERMINATE' in the end when everything is done.
    """

    return ConversableAgent(
    "code_writer_agent",
    system_message=code_writer_system_message,
     llm_config={"config_list": config_list},
    code_execution_config=False,  # Turn off code execution for this agent.
    )



# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

current_dir = os.getcwd()  # Get current working directory

executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=current_dir,  # Use the temporary directory to store the code files.
)


def create_code_executor():
    """Create a Code Executor Agent."""
    return ConversableAgent(
        name="code_executor_agent",
        llm_config=False,  # Turn off LLM for this agent.
        code_execution_config={"executor": executor},  # Use the local command line code executor.
        human_input_mode="ALWAYS",  # Always take human input for this agent for safety.
)


def start_conversation(code_writer, code_executor):
    chat_result = code_executor_agent.initiate_chat(code_writer_agent,
    message="Write Python code to calculate the sum of 10 prime numbers.",)
    return chat_result



if __name__ == "__main__":
    config_list = get_config()
    code_writer_agent = create_code_writer()
    code_executor_agent = create_code_executor()
    chat_result = start_conversation(code_writer_agent, code_executor_agent)
    print(os.listdir(temp_dir.name))
    
        

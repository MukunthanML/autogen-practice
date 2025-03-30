from autogen import AssistantAgent
from autogen.agentchat.contrib.retrieve_user_proxy_agent import RetrieveUserProxyAgent
import os


os.environ["AUTOGEN_USE_DOCKER"] = "False"

def get_config():
    """Retrieve the configuration for the AI model."""
    return [{
        "model": "llama-3.3-70b-versatile",
        "api_key": os.environ.get("GROQ_API_KEY"),
        "api_type": "groq",
         "timeout": 600,
        "cache_seed": 42,
    }]

def create_assitant_agent(llm_config):
    """Create an Assistant Agent."""    
    return AssistantAgent(
        name="assistant",
        system_message="You are a helpful assistant.",
        llm_config=llm_config,
    )

def create_ragproxy_agent():
    """Create a Retrieve User Proxy Agent."""
    return RetrieveUserProxyAgent(
        name="ragproxyagent",
        
        retrieve_config={
            "task": "qa",
            "docs_path": "story.txt",
            "get_or_create": True,  # set to False if you don't want to reuse an existing collection
            # Default vector db is "chroma" and Collection ag2-docs will be used
            # Default embedding model all-MiniLM-L6-v2 SentenceTransformerEmbeddingFunction("all-MiniLM-L6-v2") will be used
        },
    )

def start_conversation(assistant, ragproxyagent):
    """Start a conversation between the assistant and the RAG proxy agent."""
    assistant.reset()
    ragproxyagent.initiate_chat(assistant, message=ragproxyagent.message_generator, problem="Who is Lily?")

    # Disable context display in the output
    assistant.display_context = False

if __name__ == "__main__":
    config_list = get_config()
    assistant_agent = create_assitant_agent(config_list[0])
    ragproxy_agent = create_ragproxy_agent()
    start_conversation(assistant_agent, ragproxy_agent)


#pip install "autogen-agentchat[retrievechat]~=0.2"    



"""
Works with Local & Private Data 
Unlike online AI services, your data stays private because you control where and how files are stored, indexed, and retrieved.

Enables Multi-Agent Collaboration 
With AutoGen, multiple AI agents can collaborate using RAG—something you can’t achieve with simple file uploads in ChatGPT or Copilot.

Bottom Line: If you just need to summarize a document once, uploading files in ChatGPT /Copilot/any LLM is fine. 
But if you want long-term AI solutions that dynamically retrieve and process private/local data efficiently, RAG is the way to go
"""
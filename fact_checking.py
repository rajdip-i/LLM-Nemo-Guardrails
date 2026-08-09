"""
Simple Fact Checking with Basic Knowledge Retrieval

This example demonstrates a basic approach to fact checking and
knowledge retrieval in NeMo Guardrails.
"""
from nemoguardrails import RailsConfig, LLMRails

def load_rails_config():
    """Load the configuration for the local Ollama llama3.2 model."""
    print("Using local Ollama model: llama3.2 (http://localhost:11434)")
    return LLMRails(RailsConfig.from_path("./config_fact_checking"))

# Use the guardrails configuration
def test_guardrails(rails):
    # Test with a question about NVIDIA
    nvidia_response = rails.generate(messages=[{
        "role": "user",
        "content": "Who founded NVIDIA and when?"
    }])
    print("User: Who founded NVIDIA and when?")
    print(f"Assistant: {nvidia_response['content']}")
    
    # Test with a question about NeMo Guardrails
    nemo_response = rails.generate(messages=[{
        "role": "user",
        "content": "What is NeMo Guardrails and when was it released?"
    }])
    print("\nUser: What is NeMo Guardrails and when was it released?")
    print(f"Assistant: {nemo_response['content']}")
    
    # Test with a question that's not in our knowledge base
    unknown_response = rails.generate(messages=[{
        "role": "user",
        "content": "What is NVIDIA's financial performance in 2023?"
    }])
    print("\nUser: What is NVIDIA's financial performance in 2023?")
    print(f"Assistant: {unknown_response['content']}")

if __name__ == "__main__":
    rails = load_rails_config()
    test_guardrails(rails)

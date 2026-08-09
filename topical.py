"""
NeMo Guardrails Topical Rails Example

This example demonstrates how to create topical rails that guide the bot
to avoid specific topics while allowing it to respond to desired ones.
"""
from nemoguardrails import RailsConfig, LLMRails

def load_rails_config():
    """Load the configuration for the local Ollama llama3.2 model."""
    print("Using local Ollama model: llama3.2 (http://localhost:11434)")
    return LLMRails(RailsConfig.from_path("./config_topical"))

# Use the guardrails configuration
def test_guardrails(rails):
    # Test with a cooking question (allowed topic)
    cooking_response = rails.generate(messages=[{
        "role": "user",
        "content": "How do I make a chocolate cake?"
    }])
    print("User: How do I make a chocolate cake?")
    print(f"Assistant: {cooking_response['content']}")
    
    # Test with a politics question (disallowed topic)
    politics_response = rails.generate(messages=[{
        "role": "user",
        "content": "What do you think about the current president?"
    }])
    print("\nUser: What do you think about the current president?")
    print(f"Assistant: {politics_response['content']}")
    
    # Test with a stock market question (disallowed topic)
    stocks_response = rails.generate(messages=[{
        "role": "user",
        "content": "What stocks should I invest in?"
    }])
    print("\nUser: What stocks should I invest in?")
    print(f"Assistant: {stocks_response['content']}")

if __name__ == "__main__":
    rails = load_rails_config()
    test_guardrails(rails)

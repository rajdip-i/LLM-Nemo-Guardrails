"""
Minimal Working Custom Actions Example for NeMo Guardrails

This example creates a minimal configuration that uses custom actions.
"""
import datetime
from nemoguardrails import RailsConfig, LLMRails
from nemoguardrails.actions import action

# Define custom actions
@action(name="get_current_time")
async def get_current_time():
    """Get the current time."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return current_time

@action(name="get_current_date")
async def get_current_date():
    """Get the current date."""
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return current_date

@action(name="get_weather")
async def get_weather(location="Santa Clara"):
    """Get fake weather data for demonstration purposes."""
    return f"Sunny and 72°F in {location}"


# Use the guardrails configuration
def test_guardrails():
    """Run the custom-action examples against the local Ollama llama3.2 model."""
    print("Using local Ollama model: llama3.2 (http://localhost:11434)")
    rails = LLMRails(RailsConfig.from_path("./config_actions"))
    
    # Test with time question
    time_response = rails.generate(messages=[{
        "role": "user",
        "content": "What time is it?"
    }])
    print("User: What time is it?")
    print(f"Assistant: {time_response['content']}")
    
    # Test with date question
    date_response = rails.generate(messages=[{
        "role": "user",
        "content": "What date is it today?"
    }])
    print("\nUser: What date is it today?")
    print(f"Assistant: {date_response['content']}")
    
    # Test with weather question
    weather_response = rails.generate(messages=[{
        "role": "user",
        "content": "How's the weather?"
    }])
    print("\nUser: How's the weather?")
    print(f"Assistant: {weather_response['content']}")

if __name__ == "__main__":
    test_guardrails()

import os
import openai
from dotenv import load_dotenv
import yaml
import asyncio
from openai import OpenAIError

# Load environment variables
load_dotenv(dotenv_path="config/secrets.env")

# Initialize OpenAI API
openai.api_key = os.getenv("OPENAI_API_KEY")
if not openai.api_key:
    raise EnvironmentError("OPENAI_API_KEY not found in environment variables.")

# Create client
client = openai.AsyncOpenAI()

# Load configurations
def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

async def chat_with_agent(prompt, model="gpt-4", max_tokens=150):
    """
    Interact with the OpenAI API to generate a response based on a prompt.
    """
    try:
        response = await client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=max_tokens,
            temperature=0.7
        )

        return response.choices[0].message.content
    except OpenAIError as err:
        print(err)
        print(f"Error interacting with OpenAI API")
        return None

async def main():
    print("Welcome to the Private LLM Agent!")
    print("Type 'exit' to quit.\n")

    config = load_config()
    model = config.get("model", "gpt-4")
    max_tokens = config.get("max_tokens", 150)

    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        response = await chat_with_agent(user_input, model=model, max_tokens=max_tokens)
        if response:
            print(f"Agent: {response}")

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

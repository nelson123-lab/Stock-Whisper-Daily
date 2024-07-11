from dotenv import load_dotenv
import os
from openai import AsyncOpenAI
import asyncio

load_dotenv()

class ChatApp:
    def __init__(self):
        # Retrieve the OpenAI API key from the environment
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OpenAI API key not found. Please set it in the environment variables.")
        
        # Print the API key for debugging purposes (Optional: Remove this in production)
        print(f"Using OpenAI API key: {api_key[:5]}...")  # Print only the first 5 characters for security

        # Initialize the OpenAI client with the API key
        self.client = AsyncOpenAI(api_key=api_key)
        self.messages = [
            {"role": "system", "content": "You are an assistant that determines if news articles are relevant to the USA stock market data. Respond with 'Relevant' or 'Non-relevant' only."},
        ]

    async def determine_relevance(self, news_article):
        self.messages.append({"role": "user", "content": news_article})
        response = await self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages,
            max_tokens=5  # limiting the response length
        )
        relevance = response.choices[0].message.content.strip()
        self.messages.append({"role": "assistant", "content": relevance})
        return relevance

# Example usage
async def main():
    app = ChatApp()
    news_article = "The Dow Jones Industrial Average fell by 300 points today due to concerns over inflation."
    relevance = await app.determine_relevance(news_article)
    print(f"The article is: {relevance}")

# Run the example
asyncio.run(main())

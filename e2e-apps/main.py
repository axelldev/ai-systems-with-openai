from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "Hello, how are you"}],
    response_format={"type": "json_object"},
)

print(response.choices[0].message.content)

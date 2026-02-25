from dotenv import load_dotenv
from openai import AuthenticationError, OpenAI

load_dotenv()

client = OpenAI()


if __name__ == "__main__":
    try:
        response = client.chat.completions.create(
            model="gpt-5-mini",
            messages=[{"role": "user", "content": "Hello, how are you"}],
            response_format={"type": "json_object"},
        )

        print(response.choices[0].message.content)
    except AuthenticationError:
        print(
            "Please double check your authentication key and try again, the one provided is not valid."
        )

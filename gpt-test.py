import openai
from dotenv import dotenv_values

secret = dotenv_values(".env")

openai.api_key = secret["GPT_KEY"]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "write a haiku about AI"}
    ]
)
print(response['choices'][0]['message']['content'])

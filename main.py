#### Check out https://blog.finxter.com/openapi-cheat-sheet/
# syntx to set variable for open AI key
# setx OPENAI_API_KEY "your-api-key-here"
# echo %OPENAI_API_KEY%

# import os
from openai import OpenAI
# import OPEN AI library

client = OpenAI(
    api_key="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"
    # Add API Key
)

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Say this is a test"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")
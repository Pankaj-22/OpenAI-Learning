# import os
from openai import OpenAI
# import OPEN AI library

client = OpenAI(
    api_key="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"
    # Add API Key
)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo", 
# response_format={"type": "json_object"},
#   messages=[
#     {
#      "role": "user", 
#      "content": "whrite a poem on"
#      } 
#   ]
# )
# print(completion.choices[0].message)

####### Response In Jason formatt
# completion = client.chat.completions.create(
#     messages=[
#         {
#             "role": "user",
#             "content": "Can you generate an example json object describing a fruit?",
#         }
#     ],
#     model="gpt-3.5-turbo-1106",
#     response_format={"type": "json_object"},
# )
# print(completion.choices[0].message)

####### Only Response no extra details
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "write a short poem on AI"}],
    stream=True,
)
for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")




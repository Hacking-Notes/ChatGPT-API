import os
import openai

API_KEY = "API_KEY_HERE"

# can be expanded as user wish

ESCAPE_KEYS = ["Exit"]

openai.api_key = API_KEY


def makeCall(message_arr):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=message_arr)
    return completion.choices[0].message


flag = True

message_array = []

while flag:
    user_input = input("\nEnter the text: ")
    if user_input in ESCAPE_KEYS:
        flag = False
        continue
    message_obj = {"role": "user", "content": user_input}
    message_array.append(message_obj)
    response_message = makeCall(message_array)
    message_array.append(response_message)
    print("\nSystem: %s" % (response_message['content']))
        
        


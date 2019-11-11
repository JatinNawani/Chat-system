responses = {
    "what is your name?":[
        "my name is J7",
        "they call me J7",
        "I do not talk to strangers"
    ],
    "hi":[
        "hello",
        "Whats up",
        "greetings human"
    ]
}

import random

def respond(message):
    if message in responses:
        return random.choice(responses[message])

res = respond(input())
print(res)
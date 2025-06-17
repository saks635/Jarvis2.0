import random

def tell_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "Why did the computer show up at work late? It had a hard drive!",
        "Why do Java developers wear glasses? Because they can't C#!"
    ]
    return random.choice(jokes)

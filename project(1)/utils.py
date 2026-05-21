import time


def clean_text(text):

    text = text.lower().strip()

    return text


def typing_effect(text):

    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)

    print()
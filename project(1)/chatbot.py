from responses import responses
from utils import clean_text, typing_effect
import random
from colorama import init, Fore

init(autoreset=True)

print(Fore.MAGENTA + """
========================================
         AI CHATBOT SYSTEM 
         BY : NABIL K.DARWISH
========================================
""")

print(Fore.CYAN + "Status  : ONLINE")
print(Fore.GREEN + "Version : 1.0")
print(Fore.YELLOW + "Mode    : Rule-Based AI")
print(Fore.RED + "Type 'exit' to quit.\n")


while True:

    user_input = input(Fore.WHITE + " You: ")

    cleaned = clean_text(user_input)

    if cleaned in ["exit", "quit", "bye"]:

        typing_effect(
            Fore.RED +
            "\n Bot: Goodbye Engineer \n"
        )

        break

    reply = responses.get(cleaned)

    if reply:

        bot_reply = random.choice(reply)

        print()

        typing_effect(
            Fore.CYAN +
            " Bot: " + bot_reply
        )

        print()

    else:

        print()

        typing_effect(
            Fore.YELLOW +
            " Bot: Sorry, I don't understand that yet."
        )

        print()


        
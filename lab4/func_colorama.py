from colorama import Fore, Style


def print_color(text):
    # Fore.GREEN робить текст зеленим, Fore.RED - червоним
    print(Fore.GREEN + text)
    print(Fore.RED + text)
    # Style.RESET_ALL повертає звичайний колір
    print(Style.RESET_ALL + "Звичайний колір")

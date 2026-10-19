def main():
    greetings = [
        ("English", "Hello, world!"),
        ("Spanish", "¡Hola, mundo!"),
        ("French", "Bonjour le monde !"),
        ("German", "Hallo Welt!"),
        ("Italian", "Ciao, mondo!"),
        ("Portuguese", "Olá, mundo!"),
        ("Japanese", "こんにちは、世界！"),
        ("Chinese", "你好，世界！"),
    ]

    print("Choose a language:")
    for number, (language, _) in enumerate(greetings, start=1):
        print(f"{number}. {language}")

    while True:
        choice = input("Enter a number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(greetings):
            print(greetings[int(choice) - 1][1])
            return

        print(f"Please enter a number between 1 and {len(greetings)}.")


if __name__ == "__main__":
    main()
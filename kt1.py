import random

def babushka_dialog():
    print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!")

    pokas_count = 0
    while pokas_count < 3:
        user_input = input("> ").strip()

        if user_input.isupper():
            if user_input == "ПОКА!":
                pokas_count += 1
                if pokas_count < 3:
                    print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
            else:
                pokas_count = 0
                print(f"НЕТ, НИ РАЗУ С {random.randint(1930, 1950)} ГОДА!")
        else:
            pokas_count = 0
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")

    print("ДО СВИДАНИЯ, МИЛЫЙ!")

# Запускаем диалог с бабушкой
babushka_dialog()

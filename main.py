import random

HANGMANPICS = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========""",
]

COMMON_NOUNS = [
    "время",
    "человек",
    "год",
    "дело",
    "день",
    "рука",
    "раз",
    "город",
    "слово",
    "место",
    "лицо",
    "друг",
    "глаз",
    "вопрос",
    "дом",
    "сторона",
    "страна",
    "мир",
    "случай",
    "голова",
    "ребёнок",
    "сила",
    "конец",
    "вид",
    "система",
    "часть",
    "работа",
    "жизнь",
    "власть",
    "женщина",
    "дорога",
    "образ",
    "отец",
    "история",
    "нога",
    "вода",
    "война",
    "любовь",
    "минута",
    "право",
    "небо",
    "сын",
    "душа",
    "утро",
    "вечер",
    "месяц",
    "комната",
    "ночь",
    "мать",
    "утро",
    "вещь",
    "цель",
    "народ",
    "сердце",
    "шаг",
    "девушка",
    "машина",
    "уровень",
    "окно",
    "ответ",
    "условие",
    "начало",
    "свет",
    "действие",
    "век",
    "школа",
    "газета",
    "плечо",
    "путь",
    "дверь",
    "язык",
    "любовь",
    "порядок",
    "автор",
    "гость",
    "закон",
    "число",
    "идея",
    "смерть",
    "сон",
    "ресурс",
    "лес",
    "проблема",
    "искусство",
    "река",
    "проект",
    "журнал",
    "стена",
    "товарищ",
    "книга",
    "письмо",
    "помощь",
    "группа",
    "участие",
]

def main():
    print("Добро пожаловать в игру!")
    print("Попробуйте отгадать слово, прежде чем старыйбох будет повешен")

    while True:
        secret_slovo = random.choice(COMMON_NOUNS).lower()
        guessed_letters = [] #уже угаданные буквы
        wrong_guesses = 0 #кол-во ошибок
        word_progress = ["_"] * len(secret_slovo) #прогресс угадывания

        while wrong_guesses < len(HANGMANPICS) - 1:
            print(HANGMANPICS[wrong_guesses])
            print("Слово: " + " ".join(word_progress))
            print("Угаданные буквы: " + " ".join(guessed_letters))
            guess = input("Введите букву: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Введите одну букву!")
                continue
            if guess in guessed_letters:
                print("Вы уже пробовали эту букву!")
                continue
            
            guessed_letters.append(guess)

            if guess in secret_slovo:
                print("Правильно!")
                for i in range(len(secret_slovo)):
                    if secret_slovo[i] == guess:
                        word_progress[i] = guess
            else:
                print("Неправильно!")
                wrong_guesses += 1
                
            if "_" not in word_progress:
                print(HANGMANPICS[wrong_guesses])
                print("Поздравляем! Вы угадали слово: " + secret_slovo)
                break

        if "_" in word_progress:
            print(HANGMANPICS[wrong_guesses])
            print("Вы проиграли! Загаданное слово было: " + secret_slovo)
            break

if __name__ == "__main__":
    main()
 

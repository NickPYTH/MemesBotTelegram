import os

TOKEN = "1915448078:AAFeLNb530OJs1ycj8A6MHIiKshqVKazIf0"

BASE_DIR = "./"

EMOTIONS = [
    "Ахахаххах",
    "ХА-ХА-ХА",
    "Ха-Ха-Ха!",
    "Ору)",
    "Вроде смещно)",
    "Ахахах, обязательно скинь",
    "Кек)",
    "лол",
    "Ахах",
    "Смешно))",
    "Котики оценят",
]

ERRORS = {
    "drake_error_1": "Ошибка создания мема, ты забыл первую собаку. Пример ввода сообщения: #drakememecreate@Go sleep@Sit all night",
    "drake_error_2": "Ошибка создания мема, ты забыл вторую собаку. Пример ввода сообщения: #drakememecreate@Go sleep@Sit all night",
    "drake_error_3": "Ошибка создания мема, ты добавил лишнюю собаку. Пример ввода сообщения: #drakememecreate@Go sleep@Sit all night",
    "doge_error_1": "Ошибка создания мема, ты забыл первую собаку. Пример ввода сообщения: #dogememecreate@Kill all cats@afraid of mice",
    "doge_error_2": "Ошибка создания мема, ты забыл вторую собаку. Пример ввода сообщения: #dogememecreate@Kill all cats@afraid of mice",
    "doge_error_3": "Ошибка создания мема, ты добавил лишнюю собаку Пример ввода сообщения: #dogememecreate@Kill all cats@afraid of mice",
    "sqrt_error_1": "Ошибка создания мема, ты забыл первую собаку. Пример ввода сообщения: #sqrtmemecreate@60k$ Bitcoin",
    "sqrt_error_2": "Ошибка создания мема, ты добавил лишнюю собаку Пример ввода сообщения: #sqrtmemecreate@60k$ Bitcoin",
    "supermind_error_1": "Ошибка создания мема, ты забыл первую собаку. Пример ввода сообщения: #supermindmemecreate@use JS@use C++@use C@use Assembler",
    "supermind_error_2": "Ошибка создания мема, ты забыл вторую собаку Пример ввода сообщения: #supermindmemecreate@use JS@use C++@use C@use Assembler",
    "supermind_error_3": "Ошибка создания мема, ты забыл третью собаку Пример ввода сообщения: #supermindmemecreate@use JS@use C++@use C@use Assembler",
    "supermind_error_4": "Ошибка создания мема, ты написал лишнюю собаку Пример ввода сообщения: #supermindmemecreate@use JS@use C++@use C@use Assembler",
    "lazy_error_1": "Ошибка создания мема, ты забыл первую собаку. Пример ввода сообщения: #lazymemecreate@Let`s work!",
    "lazy_error_2": "Ошибка создания мема, ты добавил лишнюю собаку Пример ввода сообщения: #lazymemecreate@Let`s work!",
}

MEMES_DESCRIPTION = {
    "drake": "Для генерации мема введите две фразы для верхней подписи и нижней через символ собака(@). Максимальная длина 25 символов. Пример ввода сообщения: #drakememecreate@Go sleep@Sit all night",
    "doge": "Для генерации мема введите две фразы для левой подписи и правой через символ собака(@). Максимальная длина 25 символов. Пример ввода сообщения: #dogememecreate@Kill all cats@afraid of mice",
    "sqrt": "Для генерации мема введите фразу на надгробии после собаки(@). Максимальная длина 20 символов. Пример ввода сообщения: #sqrtmemecreate@60k$ Bitcoin",
    "supermind": "Для генерации мема введите 4 фразы через символ собака(@). Максимальная длина кажой 20 символов. Пример ввода сообщения: #supermindmemecreate@use JS@use C++@use C@use Assembler",
    "lazy": "Для генерации мема введите фразу после символа собаки(@). Максимальная длина 50 символов. Пример ввода сообщения: #lazymemecreate@Let`s work!",
}

MEMES_FOLDER = os.path.join(BASE_DIR, "memes/")

CREATED_MEMES_FOLDER = os.path.join(BASE_DIR, "created_memes/")

RANDOM_MEMES_FOLDER = os.path.join(BASE_DIR, "random_memes/")

MEMES_URL = {
    "drake": os.path.join(MEMES_FOLDER, "drake_meme.png"),
    "doge": os.path.join(MEMES_FOLDER, "doge_meme.png"),
    "sqrt": os.path.join(MEMES_FOLDER, "sqrt_meme.png"),
    "supermind": os.path.join(MEMES_FOLDER, "supermind_meme.png"),
    "lazy": os.path.join(MEMES_FOLDER, "lazy.png"),
}

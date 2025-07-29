import os
import time
from keyword_search import search_key_word
from film_search_by_genre_year import search_genre_and_year
from popular_search_queries import show_popular_queries


# Функция для очистки экрана
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Функция для медленного вывода текста
def slow_print(text, delay=0.02):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()


# Функция для отображения меню
def print_menu():
    print("=" * 60)
    print("{:^60}".format("🎬 Search 🎬"))
    print("=" * 60)
    print("""  
 Choose a search method:

   1. 🔍 By Keywords
   2. 🎭+🗓️  By Genre and Year
   3. 🌟 Show users's most searched queries
   4. 🚪 Exit
 """)
    print("=" * 60)


# Основная функция
def main():
    while True:
        clear_screen()
        print_menu()  # Печатаем меню
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            clear_screen()
            search_key_word()  # Вызываем функцию из keyword_search.py
        elif choice == '2':
            clear_screen()
            search_genre_and_year()  # Вызываем функцию из film_search_by_genre_year.py
        elif choice == '3':
            clear_screen()
            show_popular_queries()
        elif choice == '4':
            slow_print("👋 Goodbye!")
            break
        else:
            print("⚠️ Error: Please enter a valid number (1-4).")

        input("Press Enter to continue...")


if __name__ == "__main__":
    main()
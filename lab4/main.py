# Лабораторна робота 4. Точка входу.
# Кожна функція лежить в окремому файлі func_*.py

# 10 сторонніх бібліотек
from func_numpy import get_average
from func_pandas import make_table
from func_colorama import print_color
from func_tabulate import show_table
from func_tqdm import progress_bar
from func_jinja2 import make_greeting
from func_markdown import to_html
from func_networkx import find_path
from func_psutil import get_cpu_count
from func_dateutil import get_age

# 5 вбудованих бібліотек
from func_math import circle_area
from func_random import random_number
from func_json import to_json
from func_datetime import date_after
from func_collections import count_words


def main():
    print("1. numpy - середнє:", get_average([10, 20, 30, 40]))

    print("\n2. pandas - таблиця:")
    print(make_table(["Олена", "Іван", "Марія"], [90, 75, 88]))

    print("\n3. colorama - кольори:")
    print_color("Привіт")

    print("\n4. tabulate - таблиця:")
    print(show_table([["Олена", 90], ["Іван", 75], ["Марія", 88]]))

    print("\n5. tqdm:")
    print(progress_bar())

    print("6. jinja2:", make_greeting("Артеме"))

    print("\n7. markdown:", to_html("**жирний текст**"))

    print("\n8. networkx - шлях:", find_path("Львів", "Харків"))

    print("\n9. psutil - ядер процесора:", get_cpu_count())

    print("\n10. dateutil - вік:", get_age("2005-03-14", "2026-10-15"))

    print("\n11. math - площа круга:", circle_area(5))

    print("\n12. random - число:", random_number())

    print("\n13. json:", to_json({"предмет": "Python", "лаба": 4}))

    print("\n14. datetime - дата через 15 днів:", date_after(15))

    print("\n15. collections - слова:", count_words("лаба це лаба і це практика"))


main()

from tabulate import tabulate


def show_table(rows):
    # tabulate малює гарну таблицю з рядків
    return tabulate(rows, headers=["Імʼя", "Оцінка"], tablefmt="grid")

import pandas as pd


def make_table(names, marks):
    # DataFrame - це таблиця з колонками
    table = pd.DataFrame({"Імʼя": names, "Оцінка": marks})
    return table

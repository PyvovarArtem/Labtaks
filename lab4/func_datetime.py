from datetime import datetime, timedelta


def date_after(days):
    # datetime.now() - поточна дата і час
    today = datetime.now()
    # timedelta - це проміжок часу, який додаємо до дати
    result = today + timedelta(days=days)
    return result.strftime("%d.%m.%Y")

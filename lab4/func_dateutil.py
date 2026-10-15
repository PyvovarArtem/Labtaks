from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


def get_age(birth_text, today_text):
    # parse перетворює текст у дату
    birth = parse(birth_text)
    today = parse(today_text)
    # relativedelta рахує різницю між датами
    return relativedelta(today, birth).years

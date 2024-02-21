import datetime
import locale


def return_date1():
    locale.setlocale(locale.LC_ALL, '')
    now = datetime.datetime.now()
    distance = datetime.timedelta(days=15)
    return now.strftime("%x %X"), (now + distance).strftime("%x")


if __name__ == '__main__':
    print(return_date1())

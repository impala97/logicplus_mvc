from datetime import datetime


class dt:
    def custom(self, custom_format):
        return datetime.now().strftime(custom_format)

    def date(self):
        return datetime.now().strftime("%Y-%m-%d")

    def time(self):
        return datetime.now().strftime("%H:%M")

    def day_week(self):
        return datetime.now().strftime('%A')


if __name__ == '__main__' and __package__ is None:
    from os import path, sys
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    dt()
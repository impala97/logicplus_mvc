from .lpdb import dbcon
from datetime import datetime

class chat:
    def addchat(self, **chat_data):
        date = "".join(datetime.now().strftime('%Y-%m-%d'))
        time = "".join(datetime.now().strftime('%H:%M'))
        insert = "insert into lp.chat(name, message, date, time) values('%s','%s','%s','%s');" % (chat_data['name'], chat_data['message'], date, time)
        return dbcon().do_insert(insert)

    def getchat(self):
        select = "select * from lp.chat;"
        chat_data = dbcon().do_select(select)
        return chat_data


if __name__ == '__main__':
    chat()
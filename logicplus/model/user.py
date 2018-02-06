import datetime
from .lpdb import dbcon


class user:
    def adduser(self,username,pwd,email,mobile):
        valid_user = self.check_user_existance(username)
        if len(valid_user) == 0:
            insert = "insert into lp.user(username,password,email,mobile,live) values('%s','%s','%s','%s','0')" % (username, pwd, email, mobile)
            valid = dbcon().do_insert(insert)
            if valid is True:
                return self.__getId__(un)
            else:
                return False
        else:
            return False

    def check_user_existance(self, username):
        select = "select username from lp.user where username='%s'" % username
        return dbcon().do_select(select=select)

    def __getId__(self, username):
        select = "select id from lp.user where username='%s'" %username
        row = dbcon().do_select(select)
        return row[0][0]

    def do_login(self,username):
        select = "select * from lp.user where username='%s' and active='1';" % username
        return dbcon().do_select(select=select)

    def update_login(self,id):
        date = self.currentdate()
        update = "update lp.user set last_login = '%s',live='1' where id=%d;" % (date,id)
        return dbcon().do_insert(update)

    def update_logout(self, username):
        update = "update lp.user set live='0' where username='%s';" % username
        return dbcon().do_insert(update)

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

    def __getEmail__(self, id):
        select = "select email from lp.user where id=%d;" % id
        row = dbcon().do_select(select)
        if len(row) > 0:
            return row[0][0]
        else:
            return None

    def getuserdata(self):
        select = "select * from lp.user order by id;"
        return dbcon().do_select(select)

    def activateuser(self,id):
        update = "update lp.user set active='1' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def inactivateuser(self,id):
        update = "update lp.user set active='0' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def getuserdataById(self,id):
        select = "select * from lp.user where id=%d order by id"%int(id)
        return dbcon().do_select(select)

    def updateuserdata(self,id,username,password,email,mobile,active):
        update = "update lp.user set username='%s',password='%s',email='%s',mobile='%s',active='%s' where id=%d"%(username,password,email,mobile,active,int(id))
        return dbcon().do_insert(update)

    def changepwd(self,id,old_pwd,new_pwd):
        update = "update lp.user set password='%s' where id=%d and password='%s';"%(new_pwd,int(id),old_pwd)
        return dbcon().do_insert(update)

    def usercount(self):
        select = "select count(id) from lp.user;"
        count = dbcon().do_select(select)
        del select
        return count[0][0]


if __name__ == "__main__":
    user()
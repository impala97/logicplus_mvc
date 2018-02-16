from .lpdb import dbcon
import datetime


class inquiry():
    def addInquiry(self,name, email, phone, course, study, details, gender):
        insert = "insert into lp.inquiry_trnxs(name,email,phone,course,study,details,gender,date) values('%s','%s','%s','%s','%s','%s','%s','%s')"%(name, email, phone, course, study, details, gender,self.currentdate())
        return dbcon().do_insert(insert)

    def getinquiry(self):
        select = "select * from lp.inquiry_trnxs order by id;"
        return dbcon().do_select(select)

    def activateInquiry(self,id):
        update = "update lp.inquiry_trnxs set active='1' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def inactivateInquiry(self,id):
        update = "update lp.inquiry_trnxs set active='0' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def updateInquiry(self,id,name, email, phone, course, study, details, gender):
        update = "update lp.inquiry_trnxs set name='%s',email='%s',phone='%s',course='%s',study='%s',details='%s',gender='%s' where id=%d;"%(name, email, phone, course, study, details, gender,int(id))
        return dbcon().do_insert(update)

    def getdataById(self, iid):
        select = "select * from lp.inquiry_trnxs where id=%d;" % int(iid)
        return dbcon().do_select(select)

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d")


if __name__ == "__main__":
    inquiry()




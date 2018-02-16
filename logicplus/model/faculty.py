from .lpdb import dbcon


class faculty():
    def addFaculty(self,name, email, phone, website, company, post, dob, address, gender):
        insert = "insert into lp.faculty(name,email,phone,website,company,post,dob,address,gender) values('%s','%s','%s','%s','%s','%s','%s','%s','%s')"%(name,email,phone,website,company,post,dob,address,gender)
        if dbcon().do_insert(insert):
            return self.__getId__(email)

    def __getId__(self,email):
        select = "select id from lp.faculty where email='%s'" %email
        row = dbcon().do_select(select)
        return row[0][0]

    def updateimg(self,filename,id):
        update = "update lp.faculty set dp='%s' where id=%d"%(filename,int(id))
        return dbcon().do_insert(update)

    def getfacultydata(self):
        select = "select * from lp.faculty where active='1' order by id;"
        return dbcon().do_select(select)

    def activateFaculty(self,id):
        update = "update lp.faculty set active='1' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def inactivateFaculty(self,id):
        update = "update lp.faculty set active='0' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def updateFaculty(self,id,name, email, phone, website, company, post, dob, address, gender):
        update = "update lp.faculty set name='%s',email='%s',phone='%s',website='%s',company='%s',post='%s',dob='%s',address='%s',gender='%s' where id=%d;"%(name,email,phone,website,company,post,dob,address,gender,int(id))
        return dbcon().do_insert(update)

    def getdataById(self,id):
        select = "select * from lp.faculty where id=%d;"%int(id)
        return dbcon().do_select(select)

    def getFacultyName(self,id=None):
        if id is not None:
            select = "select name from lp.faculty where id=%d;" % int(id)
            row = dbcon().do_select(select)
            return row[0][0]
        else:
            select = "select id,name from lp.faculty where active='1' order by id;"
            return dbcon().do_select(select)

    def countid(self):
        select = "select count(id) from lp.faculty;"
        count = dbcon().do_select(select)
        return count[0][0]


if __name__ == "__main__":
    faculty()




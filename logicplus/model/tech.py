from .lpdb import dbcon


class tech():
    def gettechnology(self):
        select = "select tech,framework from lp.technology;"
        return dbcon().do_select(select)

    def getprograme(self,tech):
        select = "select * from lp.programe where framework='%s' order by id;"%tech
        return dbcon().do_select(select)

    def addtech(self,main,sub=None):
        insert = "insert into lp.technology(tech,framework) values('%s','%s');"%(main,sub)
        return dbcon().do_insert(insert)

    def getTech(self,id=None):
        if id is None:
            select = "select * from lp.technology order by id;"
        else:
            select = "select * from lp.technology where id=%d;"%int(id)
        row = dbcon().do_select(select)
        return row

    def inactivatetech(self,id):
        update = "update lp.technology set active='0' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def activatetech(self,id):
        update = "update lp.technology set active='1' where id=%d"%int(id)
        return dbcon().do_insert(update)

    def getuserdataById(self,id):
        select = "select * from lp.user where id=%d order by id"%int(id)
        return dbcon().do_select(select)

    def updateTechnology(self,id,technology,framework):
        update = "update lp.technology set tech='%s',framework='%s' where id=%d;"%(technology,framework,int(id))
        return dbcon().do_insert(update)


if __name__ == "__main__":
    tech()
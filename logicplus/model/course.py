from .lpdb import dbcon
from .batch import batch


class course:
    def addCourse(self,cname,duration,fees,details):
        insert = "insert into lp.course_trnxs(cname,duration,fees,details) values('%s','%s','%s','%s')"%(cname,duration,fees,details)
        return dbcon().do_insert(insert)

    def getCourseName(self, id=None):
        if id is not None:
            select = "select cname from lp.course_trnxs where id=%d and active='1';"%(int(id))
            row = dbcon().do_select(select)
            return row[0]
        else:
            select = "select cname,fees from lp.course_trnxs WHERE active='1';"
            return dbcon().do_select(select)

    def getCourseData(self, id=0):
        if id == 0:
            select = "select * from lp.course_trnxs order  by id;"
        else:
            select = "select * from lp.course_trnxs where id=%d;"%id
        return dbcon().do_select(select)

    def updateCourse(self,cname,duration,fees,details,id):
        update = "update lp.course_trnxs set cname='%s',duration='%s',fees='%s',details='%s' where id=%d;"%(cname,duration,fees,details,id)
        return dbcon().do_insert(update)

    def active(self,id):
        update = "update lp.course_trnxs set active='1' where id='%d';"%id
        return dbcon().do_insert(update)

    def delete(self, id):
        update = "update lp.course_trnxs set active='0' where id='%d';"%id
        return dbcon().do_insert(update)

    def getCourseList(self):
        select = "select id,cname from lp.course_trnxs where active='1' order by id;"
        return dbcon().do_select(select)

    def getFeesById(self,cid):
        select = "select fees from lp.course_trnxs where id=%d;" % int(cid)
        fees = dbcon().do_select(select)
        return fees[0][0]

    def getcname(self, aid):
        from .admission import admission_batch
        bid = admission_batch().getbid(aid)
        c = [None] * len(bid)

        for i in range(len(bid)):
            select = "select distinct(cname) from lp.course_trnxs inner join lp.batch_trnxs on lp.batch_trnxs.bid=%d and lp.course_trnxs.id=lp.batch_trnxs.cid;" % bid[i]
            cname = dbcon().do_select(select)
            c[i] = cname[0][0]

        return batch().make_str(c), self.getsumfees(aid)

    def getsumfees(self, aid):
        select = "select sum(lp.course_trnxs.fees) from lp.course_trnxs join lp.batch_trnxs on lp.batch_trnxs.cid = lp.course_trnxs.id join lp.admission_batch on lp.admission_batch.bid=lp.batch_trnxs.bid and lp.admission_batch.aid=%d;" % aid
        fees = dbcon().do_select(select)
        return fees[0][0]


if __name__ == "__main__":
    course()

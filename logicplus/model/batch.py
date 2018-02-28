from .lpdb import dbcon
from .faculty import faculty

class batch:
    def addBatch(self, clist, flist, dlist, tlist):
        dlist = self.make_str(dlist)
        tlist = self.make_str(tlist)
        insert = "insert into lp.batch_trnxs(cid,fid,day,time,active) values('%s','%s','%s','%s','1')" % (clist, flist, dlist, tlist)
        if dbcon().do_insert(insert):
            select = "select bid from lp.batch_trnxs where cid='%s' and fid='%s' and day='%s' and time='%s';"
            return dbcon().do_select(select)

    def updateBatch(self, clist, flist, dlist, tlist, bid):
        dlist = self.make_str(dlist)
        tlist = self.make_str(tlist)
        update = "update lp.batch_trnxs set cid='%s',fid='%s',day='%s',time='%s' where bid=%d;" % (
        clist, flist, dlist, tlist, int(bid))
        return dbcon().do_insert(update)

    def getbatch(self, cid=None):
        if cid is None:
            select = "select * from lp.batch_trnxs order by bid;"
            row = dbcon().do_select(select)
            for r in range(0, len(row)):
                row[r] = list(row[r])

            from .course import course
            for r in range(0, len(row)):
                c = course().getCourseName(row[r][1])
                row[r][1] = c[0]
                del c
                row[r][2] = faculty().getFacultyName(row[r][2])
            return row
        else:
            select = "select bid,day,time from lp.batch_trnxs where cid=%d order by bid;" % int(cid)
            row = dbcon().do_select(select)
            return self.reverse(row)

    def reverse(self, row):
        time = [None] * len(row)
        len_time = 0

        for r in range(0, len(row)):
            time[r] = row[r][2].split(',')
            len_time += len(time[r])

        ftop = 0
        id = [None] * len_time
        for r in range(0, len(time)):
            for c in range(0, len(time[r])):
                id[ftop] = row[r][0]
                ftop += 1

        ftop = 0
        dt = [None] * len_time
        for r in range(0, len(time)):
            for c in range(0, len(time[r])):
                dt[ftop] = row[r][1] + " " + time[r][c]
                ftop += 1

        return id, dt

    def Active(self, bid):
        update = "update lp.batch_trnxs set active='1' where bid=%d;" % int(bid)
        return dbcon().do_insert(update)

    def Delete(self, bid):
        update = "update lp.batch_trnxs set active='0' where bid=%d;" % int(bid)
        return dbcon().do_insert(update)

    def make_str(self, str):
        tmp = ""
        if len(str) > 1:
            for i in range(0, len(str)):
                if i == len(str) - 1:
                    tmp = tmp + str[i]
                else:
                    tmp = tmp + str[i] + ','
        else:
            print(type(str), len(str))
            return str[0]
        del str
        return tmp

    def getCid(self):
        select = "select distinct cid from lp.batch_trnxs order by cid;"
        row = dbcon().do_select(select)
        from .course import course
        for r in range(0, len(row)):
            row[r] += course().getCourseName(row[r][0])
        return row

    def getFid(self, bid=None):
        if bid is None:
            select = "select distinct fid from lp.batch_trnxs order by fid;"
            row = dbcon().do_select(select)
            result = [[None] * 2] * len(row)
            for r in range(0, len(row)):
                result[r][0] = row[r][0]
                result[r][1] = faculty().getFacultyName(row[r][0])
            del row
            return result
        else:
            select = "select fid from lp.batch_trnxs where bid=%d;"%int(bid)
            row = dbcon().do_select(select)
            return row[0][0]

    def updatecountall(self):
        select = "select lp.admission_batch.bid,count(lp.admission_batch.bid) from lp.admission_batch inner join lp.batch_trnxs on lp.admission_batch.bid=lp.batch_trnxs.bid group by lp.admission_batch.bid;"
        data_entry = dbcon().do_select(select)

        for de in data_entry:
            update = "update lp.batch_trnxs set entries=%d where bid=%d;" % (de[1], de[0])
            dbcon().do_insert(update)

    def updatecount(self, bid):
        select = "select count(bid) from lp.admission_batch where bid=%d;" % bid
        data_entry = dbcon().do_select(select)

        update = "update lp.batch_trnxs set entries=%d WHERE bid=%d;" % (data_entry[0][0], bid)
        return update
        return dbcon().do_insert(update)

    def getdtbybid(self, bid):
        select = "select day from lp.batch_trnxs where bid=%d;" % bid
        result = dbcon().do_select(select)
        return result[0]

    def getfacultynamebybid(self, bid):
        select = "select lp.faculty.name from lp.faculty inner join lp.batch_trnxs on lp.batch_trnxs.fid=lp.faculty.id and lp.batch_trnxs.bid=%d;" % bid
        result = dbcon().do_select(select)
        return result[0]


class batch_faculty:
    def add(self, fid, bid, time):
        select = "select id,time from lp.batch_faculty where fid=%d and bid=%d;" % (fid, bid)
        result = dbcon().do_select(select)
        # if there is no data
        if len(result) == 0:
            for t in time:
                self.__insert__(fid, bid, t)
        # to update exists data
        else:
            time, result = self.__compare__(time, result)
            print(time, result)
            # case-1 >
            if len(time) > len(result):
                for r in range(len(result)):
                    self.__update__(result[r][0], time[r])
                    del time[r]
                for t in time:
                    self.__insert__(fid, bid, t)
            # case-2 ==
            elif len(time) == len(result):
                for t in range(len(time)):
                    self.__update__(result[t][0], time[t])

            # case-3 <
            else:
                for t in range(len(time)):
                    self.__update__(result[t][0], time[t])
                    del result[t]
                for r in result:
                    self.__delete__(r[0])
        return True

    def __compare__(self, time, result):
        ctime = time[:]
        cresult = result[:]
        for i in range(len(time)):
            for j in range(len(result)):
                if time[i] == result[j][1]:
                    ctime.remove(time[i])
                    cresult.remove(result[j])

        return ctime, cresult

    def __insert__(self, fid, bid, time):
        insert = "insert into lp.batch_faculty(fid, bid, time) values(%d, %d,'%s');" % (fid, bid, time)
        return dbcon().do_insert(insert)

    def __update__(self, uid, time):
        update = "update lp.batch_faculty set time='%s' where id=%d;" % (time, uid)
        return dbcon().do_insert(update)

    def __delete__(self, uid):
        delete = "delete from lp.batch_faculty where id=%d;" % uid
        dbcon().do_insert(delete)

    def getdt(self, fid, day, time, bid=None):
        select = "select lp.batch_trnxs.bid,lp.batch_trnxs.day,lp.batch_faculty.time from lp.batch_trnxs inner join lp.batch_faculty on lp.batch_trnxs.fid=%d and lp.batch_faculty.bid=lp.batch_trnxs.bid;" % fid
        fdata = dbcon().do_select(select)
        time_clash = False
        print("batch=getdt=bid=", bid)
        if len(fdata) >= 1:
            if ',' in time:
                time = time.split(',')

            if ',' in day:
                day = day.split(',')

            for i in range(len(fdata)):
                if fdata[i][0] != int(bid):
                    if isinstance(day, list):
                        print("if", fdata[i], type(fdata[i][0]))
                        # check day and time clash
                        for d in day:
                            if d in fdata[i][1]:
                                if isinstance(time, list):
                                    for t in time:
                                        if t in fdata[i][2]:
                                            time_clash = True
                                            print("time match==", time_clash)
                                            return True
                                        else:
                                            time_clash = False
                                else:
                                    if time in fdata[i][2]:
                                        time_clash = True
                                        print("time match==", time_clash)
                                        return True
                                    else:
                                        time_clash = False
                    else:
                        if day in fdata[i][1]:
                            if isinstance(time, list):
                                print("else", fdata[i])
                                for t in time:
                                    if t in fdata[i][2]:
                                        time_clash = True
                                        print("time match==", time_clash)
                                        return True
                                    else:
                                        time_clash = False
                            else:
                                if time in fdata[i][2]:
                                    time_clash = True
                                    print("time match==", time_clash)
                                    return True
                                else:
                                    time_clash = False
                        else:
                            print("does not check time because day's are not clash.")
        print("return getdt")
        return time_clash


if __name__ == "__main__":
    batch()

from .lpdb import dbcon
from .course import course
from .batch import batch


class admission():
    def updatecourse(self, aid):
        cname, fees = course().getcname(aid)
        print("aid==%s==fees==%s" % (aid, fees))
        update = "update lp.admission_trnxs set course='%s',fees=%d where id=%d;" % (str(cname), fees, aid)
        print(update)
        print("len==cname==", len(cname))
        return dbcon().do_insert(update)

        """
        select = "select course,fees from lp.admission_trnxs WHERE id=%d;" % (int(data['aid']))
        print(select)
        ad_data = dbcon().do_select(select)
        if data['cname'] not in ad_data[0][0]:
            data['cname'] = ad_data[0][0] + ',' + str(data['cname'])
            fees = int(data['fees']) + ad_data[0][1]
            update = "update lp.admission_trnxs set course='%s',fees=%d WHERE id=%d;" % (data['cname'], fees, int(data['aid']))
            print(update)
            return dbcon().do_insert(update)
        """

    def addAdmission(self,name,phone,email,study,cname,address,gender,join,fees,details,bid):
        insert = "insert into lp.admission_trnxs(name,phone,email,study,course,address,gender,join_date,fees,active,dp,details,bid) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','1','%s','%s',%d);"%(name,phone,email,study,cname,address,gender,join,fees,'profile-pic.jpg',details,int(bid))
        if dbcon().do_insert(insert):
            aid = self.getIdByPhone(phone)
            return aid[0][0]

    def updateAddmission(self,name,phone,email,study,cname,address,gender,join,fees,details,bid,id):
        update = "update lp.admission_trnxs set name='%s',phone='%s',email='%s',study='%s',course='%s',address='%s',gender='%s',join_date='%s',fees=%d,details='%s',bid=%d where id=%d;"%(name,phone,email,study,cname,address,gender,join,int(fees),details,int(bid),int(id))
        return dbcon().do_insert(update)

    def getIdByPhone(self, phone):
        select = "select id from lp.admission_trnxs where phone='%s';"%(phone)
        return dbcon().do_select(select)

    def updatedpById(self, dp, id):
        update = "update lp.admission_trnxs set dp='%s' where id=%d;"%(dp,id)
        return dbcon().do_insert(update)

    def getAdmission(self, id=0):
        if id == 0:
            select = "select * from lp.admission_trnxs order by id;"
        else:
            select = "select * from lp.admission_trnxs where id=%d;"%id
        return dbcon().do_select(select)

    def active(self, id):
        update = "update lp.admission_trnxs set active='1' where id=%d;"%id
        return dbcon().do_insert(update)

    def delete(self, id):
        update = "update lp.admission_trnxs set active='0' where id=%d;"%id
        return dbcon().do_insert(update)

    def getstudentNameByCid(self, cid):
        course_name = course().getCourseName(cid)
        select = "select id,name from lp.admission_trnxs where course='%s';"%course_name[0]
        return dbcon().do_select(select)

    def getstudentImageById(self, id):
        select = "select dp,fees from lp.admission_trnxs where id=%d;" % int(id)
        return dbcon().do_select(select)

    def getInvoiceGeneratedata(self,id):
        select = "select id,name,phone,email,course,address,fees from lp.admission_trnxs where id=%d;"%int(id)
        return dbcon().do_select(select)

    def getstudentfees(self, aid):
        select = "select fees from lp.admission_trnxs where id=%d;"% aid
        return dbcon().do_select(select)

    def getInvoiceData(self, course_name=None, faculty_name=None):
        aid = list()
        if (course_name is None and faculty_name is None) or (course_name == 'ALL' and faculty_name == 'ALL'):
            print("case - 1")
            select = "select distinct aid from lp.admission_batch order by aid;"
            aid = dbcon().do_select(select)
        elif course_name == 'ALL' and faculty_name != 'ALL':
            print("case - 2")
            select = "select distinct lp.admission_batch.aid from lp.admission_batch inner join lp.batch_trnxs on lp.batch_trnxs.bid=lp.admission_batch.bid and lp.batch_trnxs.fid=%d order by lp.admission_batch.aid;" % faculty_name
            aid = dbcon().do_select(select)
        # get all admission data from batch_trnxs and admission_batch
        elif course_name != 'ALL' and faculty_name == 'ALL':
            print("case - 3")
            select = "select distinct lp.admission_batch.aid from lp.admission_batch inner join lp.batch_trnxs on lp.batch_trnxs.bid=lp.admission_batch.bid and lp.batch_trnxs.cid=%d order by lp.admission_batch.aid;" % course_name
            aid = dbcon().do_select(select)
        elif course_name != 'ALL' and faculty_name != 'ALL':
            print("case - 4")
            select = "select distinct lp.admission_batch.aid from lp.admission_batch inner join lp.batch_trnxs on lp.batch_trnxs.bid=lp.admission_batch.bid and lp.batch_trnxs.fid=%d and lp.batch_trnxs.cid=%d order by lp.admission_batch.aid;" % (faculty_name, course_name)
            aid = dbcon().do_select(select)
        else:
            print("else ")
            select = "select distinct aid from lp.admission_batch order by aid;"
            aid = dbcon().do_select(select)
        # set aid before execute
        print("aid===%s==len==%s" % (aid, len(aid)))
        result1 = []
        print("len==aid==", len(aid))
        for i in range(len(aid)):
            select = "select lp.admission_trnxs.id,name,course,lp.admission_trnxs.fees,(lp.admission_trnxs.fees-sum(lp.invoice_trnxs.fees)) as remaining_fees,phone,count(lp.invoice_trnxs.aid) as installment_no,lp.admission_trnxs.bid from lp.admission_trnxs inner join lp.invoice_trnxs on lp.invoice_trnxs.aid=lp.admission_trnxs.id where lp.admission_trnxs.id=%d group by lp.admission_trnxs.id;" % aid[i][0]
            result1.append(dbcon().do_select(select))
            result1[i][0] += batch().getfacultynamebybid(result1[i][0][7])

        return result1

    def coountid(self):
        select = "select count(id) from lp.admission_trnxs;"
        count = dbcon().do_select(select)
        return count[0][0]

    def getimgbyid(self, aid):
        select = "select dp from lp.admission_trnxs where id=%d;" % aid
        img_name = dbcon().do_select(select)
        return img_name[0][0]

    def deletecourse(self, aid, bid):
        select = "select fees from lp.admission_trnxs where id=%d;" % aid
        total_fees = dbcon().do_select(select)
        total_fees = total_fees[0][0]
        select = "select fees from lp.admission_batch WHERE aid=%d and bid=%d;" % (aid, bid)
        fees = dbcon().do_select(select)
        print(fees)
        fees = fees[0][0]
        update = "update lp.admission_trnxs set fees=%d where id=%d;" % (total_fees-fees, aid)
        if dbcon().do_insert(update):
            delete = "delete from lp.admission_batch where aid=%d and bid=%d;" % (aid ,bid)
            return dbcon().do_insert(delete)


class admission_batch():
    def add(self, aid, bid, time, fees):
        select = "select aid,bid from lp.admission_batch where aid=%d AND bid=%d;" % (aid, bid)
        result = dbcon().do_select(select)
        if len(result) == 0:
            insert = "insert into lp.admission_batch(aid, bid, time, fees) VALUES(%d,%d,'%s',%d);" % (aid, bid, time, fees)
            return dbcon().do_insert(insert)
        else:
            del aid, bid, select, result
            return True

    def getdt(self, aid, bdata):
        select = "select bid,time from lp.admission_batch where aid=%d;" % aid
        result = dbcon().do_select(select)

        for i in range(len(result)):
            result[i] = result[i] + batch().getdtbybid(result[i][0])

        time_clash = False
        error_str = ""
        # extract bid from batch data
        bdata = bdata.split('_')
        bid_org = bdata[0]
        print("getdt===bid", bid_org)

        # extract day and time from batch data
        dati = bdata[1].split(' ')
        time = dati[1]
        day = dati[0].split(',')
        print("bdata==", bdata)
        for i in range(len(result)):
            if time_clash is False:
                if int(bid_org) != result[i][0]:
                    print("if", result[i])
                    # check day and time clash
                    for d in day:
                        if d in result[i][2]:
                            if time in result[i][1]:
                                time_clash = True
                                error_str = "Your batch time is clash with another batch."
                            else:
                                time_clash = False
                else:
                    print("else", result[i])
                    if time in result[i][1]:
                        # if no time clashing
                        time_clash = True
                        error_str = "You have already added this batch."
                        print("id match==", time_clash)
                    else:
                        time_clash = False
            else:
                return time_clash, error_str
                print("time match==", time_clash)
        return time_clash, error_str

    def getbid(self, aid):
        select = "select bid from lp.admission_batch where aid=%d order by bid;" % aid
        bid = dbcon().do_select(select)

        for i in range(len(bid)):
            for j in range(len(bid[i])):
                bid[i] = bid[i][j]
        print(bid)
        return bid


if __name__ == "__main__":
    admission_batch(), admission()

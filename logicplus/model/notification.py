from logicplus.srmod.dt.dt import dt
from lpdb import dbcon


class notification:
    def getbid(self):
        select = "select bid,time,day from lp.batch_trnxs order by bid;"
        batch_data = dbcon().do_select(select)
        wday = dt().day_week()
        bid = []

        for bdata in batch_data:
            if wday in bdata[2]:
                bid.append(bdata[0])

        mail_details = self.getaid(bid)
        print(batch_data)
        print("bid===", bid)

    def getaid(self, bid):
        final_data = []
        for i in bid:
            select = "select lp.admission_trnxs.id,email from lp.admission_trnxs inner join lp.admission_batch on lp.admission_trnxs.id=lp.admission_batch.aid and lp.admission_batch.bid=%d;" % i
            raw_aid = dbcon().do_select(select)

            select = "select distinct(cname) from lp.course_trnxs inner join lp.batch_trnxs on lp.batch_trnxs.bid=%d and lp.course_trnxs.id=lp.batch_trnxs.cid;" % i
            raw_cid = dbcon().do_select(select)

            for i in range(len(raw_aid)):
                final_data.append(raw_aid[i]+raw_cid[0])
        print(final_data)
        return final_data


notification().getbid()


if __name__ == "__main__":
    notification()
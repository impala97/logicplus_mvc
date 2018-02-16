from .lpdb import dbcon


class invoice():
    def addInvoice(self,aid,fees,payment_type=None,bank=None,chq_no=None):
        select = "select nextval('lp.invoice_trnxs_id_seq');"
        nextval = dbcon().do_select(select)
        invoice_no = "lp" + str(nextval[0][0])

        valid = False
        if payment_type is None:
            insert = "insert into lp.invoice_trnxs(invoice_no,aid,fees,chq_no,active) values('%s',%d,%d,'-','1');"%(invoice_no,int(aid),int(fees))
            return dbcon().do_insert(insert)
        elif payment_type == 'True':
            insert = "insert into lp.invoice_trnxs(invoice_no,aid,fees,payment_type,bank,chq_no,active) values('%s',%d,%d,'1','%s','%s','1');"%(invoice_no,int(aid),int(fees),bank,chq_no)
            return dbcon().do_insert(insert)

    def getFeeSumByAid(self, aid=None):
        if aid is not None:
            select = "select sum(fees) from lp.invoice_trnxs where aid=%d;" % int(aid)
            return dbcon().do_select(select)
        else:
            select = "select sum(fees) from lp.invoice_trnxs;"
            fees = dbcon().do_select(select)
            return fees[0][0]



import psycopg2 as db


class dbcon:
    con = db.connect(dbname='logicplus', host='localhost', user='postgres', password='root')
    cursor = con.cursor()

    def __init__(self):
        pass

    def do_select(self, select):
        self.cursor.execute(select)
        row = self.cursor.fetchall()
        return row

    def do_insert(self, query):
        self.cursor.execute(query)
        self.con.commit()
        return True

    def do_bulk(self, query):
        if isinstance(query, list):
            try:
                self.cursor.execute("SAVEPOINT do_bulk;")
                self.cursor.execute("BEGIN;")
                print(query)
                for que in query:
                    self.cursor.execute(que)
            except db.Error as e:
                print(e.pgerror)
                self.cursor.execute("ROLLBACK TO SAVEPOINT do_bulk;")
            else:
                self.con.commit()
                return True
        """
        sub_str = ""
        for que in query:
            sub_str = sub_str + "\n\t" + que
        final_str = "BEGIN; savepoint do_bulk;\n\t %s \n ROLLBACK to savepoint do_bulk;" % sub_str
        print(final_str)
        self.do_insert(final_str)
        """


if __name__ == "__main__":
    dbcon()

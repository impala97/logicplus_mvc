import psycopg2 as db


class dbcon:
    con = None
    cursor = None

    def __init__(self):
        self.con = db.connect(dbname='logicplus', host='localhost', user='postgres', password='root')
        self.cursor = self.con.cursor()

    def do_select(self, select):
        try:
            self.cursor.execute(select)
            row = self.cursor.fetchall()
            return row
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            self.con.close()

    def do_insert(self, query,response=False):
        try:
            self.cursor.execute(query)
            if response is True:
                response = self.cursor.fetchone()[0]
                print("response==",response)
                return response
            return True
        except psycopg2.DatabaseError as error:
            print(error)
        finally:
            self.con.commit()
            self.con.close()

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
            finally:
                self.con.close()
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

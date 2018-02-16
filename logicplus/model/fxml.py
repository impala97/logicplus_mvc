import os
import datetime


class fxml():
    def mkdir(self):
        dp = "static/master/faculty/profile"
        if not os.path.exists(dp):
            os.mkdir(dp, 0777)

    def exists(self,dp):
        if os.path.exists(dp):
            return True
        else:
            return False

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M")


if __name__ == "__main__":
    fxml()
import os
import datetime


class tmp():
    path = 'logicplus/static/master/profile/faculty'

    def saveIMG(self, img, uid, ufolder=None):
        if ufolder is not None:
            self.path = ufolder
        ext = self.allowed_file(img.filename)

        if img and ext:
            filename = str(uid) + "_" + self.currentdate() + "." + ext
            img.save(os.path.join(self.path, filename))
            return filename

    def allowed_file(self, filename):
        allwoed_extensions = set(['png', 'jpg', 'jpeg', 'gif'])
        ext = filename.rsplit('.', 1)[1].lower()
        if ext in allwoed_extensions:
            return ext

    def currentdate(self):
        return datetime.datetime.now().strftime("%Y%m%d%H%M")

    def sort(self, data):
        t = 1
        l = [None for i in range(0, 5)]
        l[0] = data[0][0]

        for r in data:
            if r[0] in l:
                pass
            else:
                l[t] = r[0]
                t += 1
        udata = [None for i in range(0, 3)]
        udata[0] = filter(None,l)
        udata[1] = ['Flask', 'Odoo', 'Django']
        udata[2] = ['Hibernate', 'Spring', 'Struts']
        return udata

    def remove_img(self, path, img_name):
        file = path + '/' + img_name
        os.remove(file)
        # check if file exists or not
        if os.path.exists(path + '/' + img_name) is False:
            # file did not exists
            return True


if __name__ == "__main__":
    tmp()
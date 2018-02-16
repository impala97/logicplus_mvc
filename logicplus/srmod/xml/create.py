import xml.etree.ElementTree as ET
from xml.dom import minidom
import os


class create():
    data = ""
    filepath = ""
    root = ""
    tree = ""
    final = ""

    def __set__(self):
        page = ET.Element("page")
        ET.SubElement(page, "id").text = self.data[0]
        ET.SubElement(page, "name").text = self.data[1]
        ET.SubElement(page, "title").text = self.data[2]

        # insert at begin
        self.root.insert(0,page)

        # insert at end
        # self.root.append(page)

        # self.tree = ET.ElementTree(self.root)

    def generate_str(self):
        rough = ET.tostring(self.root,'UTF-8')
        parse = minidom.parseString(rough)
        self.final = parse.toprettyxml(indent='\t', newl='\n')
        del rough,parse

    def __connect__(self, filepath, data):
        self.filepath = filepath
        self.data = data
        del filepath,data

        self.tree = ET.parse(self.filepath)
        self.root = self.tree.getroot()

    def __main__(self):
        self.__set__()
        self.generate_str()
        self.__write__()

    def __write__(self):
        with open(self.filepath, mode='w') as output:
            self.final = os.linesep.join([s for s in self.final.splitlines() if s.strip()!=''])
            output.write(self.final)
        self.__clean__()

    def __clean__(self):
        del self.final,self.tree,self.root

    def __create__(self):
        self.root = ET.Element("blog")
        self.tree = ET.ElementTree(self.root)
        self.tree.write(self.filepath, "UTF-8", "1.0")


# ----------------------------------------------------------------------
if __name__ == "__main__":
    create()

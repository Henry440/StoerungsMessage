from bs4 import BeautifulSoup
class Treffer():

    def __init__(self, titel, html):
        self.titel = titel
        self.html = html

    def status(self):
        error = self.html.find(class_="danger sparkline")
        warn  = self.html.find(class_="warning sparkline")

        if(error != None):
            return 2
        elif (warn != None):
            return 1
        else:
            return 0

    def trend(self):
        #val1, val2, 0/1 0fallend | 1steigend
        svg = str(self.html.find("svg")).split("data-values=\"[")
        svg_data = (svg[1].split("]")[0]).split(",")
        val1 = svg_data[-2]
        val2 = svg_data[-1]
        t = 1
        if val1 > val2:
            t = 0
        data = [val1, val2, t]
        return data
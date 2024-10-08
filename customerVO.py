class CustomerVO :
    def __init__(self, num=None, name=None, tel=None) :
        self.num = num
        self.name = name
        self.tel = tel
        
    def __str__(self) :
        return "{:5}\t\t{:5}\t{:10}".format(self.num, self.name, self.tel)
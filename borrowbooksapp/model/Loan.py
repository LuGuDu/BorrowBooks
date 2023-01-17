class Loan:

    def __init__ (self, identificator, book, dateInit, dateFinish):
        self.identificator = identificator
        self.book = book
        self.dateInit = dateInit
        self.dateFinish = dateFinish

    def get_json(self):
        return {
            'identificator': self.identificator,
            'book': self.book,
            'dateInit': self.dateInit,
            'dateFinish': self.dateFinish
        }
    
    def get_identificator(self):
        return self.identificator
    
    def set_identificator(self, identificator):
        self.identificator = identificator

    def get_book(self):
        return self.book
    
    def set_book(self, book):
        self.book = book
    
    def get_dateInit(self):
        return self.dateInit
    
    def set_dateInit(self, dateInit):
        self.dateInit = dateInit
    
    def get_dateFinish(self):
        return self.dateFinish
    
    def set_dateFinish(self, dateFinish):
        self.dateFinish = dateFinish

    def to_string(self):
        return "Loan [id: " + self.identificator + ", book: " + self.book + ", dateInit: " + self.dateInit +", dateFinish: " + self.dateFinish + "]"
    

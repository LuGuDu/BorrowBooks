"""LoanDAO class"""

class LoanDAO:
    """Class with methods for loans persistance"""

    def save(self, mongo, loan):
        """Takes a loan and save it on mongoDB"""
        mongo.loans.insert_one(loan)

    def get_by_id(self, mongo, id):
        """Takes an id and returns the loan"""
        return mongo.loans.find_one({"identificator": id})

    def get_all(self, mongo):
        """Returns all the books as list"""
        return list(mongo.loans.find({}))

    def delete_by_id(self, mongo, id):
        """Takes a id and delete the loan from mongoDB"""
        mongo.loans.delete_one({"identificator": id})

    

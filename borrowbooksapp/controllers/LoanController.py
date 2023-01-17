import json
from datetime import datetime, timedelta
from flask import abort as fabort, make_response

from model.Loan import Loan
from dao.LoanDAO import LoanDAO

loan_dao = LoanDAO()


def abort(status_code, message):
    """Method to abort the request"""
    data = {"message": message, "status_code": status_code}
    response = make_response(json.dumps(data))
    response.status_code = status_code
    response.content_type = 'application/json'
    fabort(response)


def get_loans(mongo):
    """Method to obtains the loans list"""
    loans_list = loan_dao.get_all(mongo)

    for loan in loans_list:
        loan['_id'] = str(loan['_id'])
    return loans_list

def get_loan(data, mongo):
    """Method to obtain a loan"""
    identificator = json.loads(data.decode())["identificator"]
    loan = loan_dao.get_by_id(mongo, identificator)
    loan['_id'] = str(loan['_id'])
    return loan


def create_loan(data, mongo):
    """Method to create a new loan"""
    identificator = json.loads(data.decode())["identificator"]
    book = json.loads(data.decode())["book"]
    dateInit = datetime.now()
    dateFinish = dateInit + timedelta(days=30)

    loan = Loan(identificator, book, dateInit, dateFinish)
    loan_dao.save(mongo, loan.get_json())

def complete_loan(data, mongo):
    """Method to complete a existing loan"""
    identificator = json.loads(data.decode())["identificator"]
    loan_dao.delete_by_id(mongo, identificator)


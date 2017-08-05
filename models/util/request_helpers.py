
from flask import request
import datetime

def is_resilient():
    resilient = False
    try:
        if request.method == "GET":
            param = request.args.get("resilient")
            resilient = True if param == "True" or param == "true" else False
        elif request.method == "POST":
            pass
    except:
        pass

    return resilient

def is_valid_date(datestring, formatting):
    result = True
    try:
        datetime.datetime.strptime(datestring, formatting)
    except ValueError:
        raise ValueError("Incorrect data format, should be YYYY-MM-DD")
        result = False
    
    return result

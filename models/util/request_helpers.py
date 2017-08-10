"""
    request_helpers.py
    models.util

    Author:
        Nathaniel Moon
        nathaniel.c.moon@gmail.com
    
    Date:
        3 August 2017

    Description:
        Provides helper functions that are used widely in
        endpoints

"""

from flask import request
import datetime
import copy

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
    
    return result


def merge_dicts(d1, d2):
    d3 = d1.copy()
    d3.update(d2)
    return d3
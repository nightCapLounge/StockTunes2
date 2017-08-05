

from yahoo_finance import Share
from fix_yahoo_finance import download as yf_download
from pandas_datareader import data as pdr

def get_open(ticker, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share
            
        _open = share.get_open()
        response = {
            "errors" : [],
            "data" : {}
        }
        if _open is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            response["data"]["value"] = float(_open)
            response["data"]["unit"] = "$"
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response


def get_price(ticker, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share

        price = share.get_price()
        response = {
            "errors" : [],
            "data" : {}
        }
        if price is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            response["data"]["value"] = float(price)
            response["data"]["unit"] = "$"
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response


def get_avg_daily_volume(ticker, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share

        adv = share.get_avg_daily_volume()
        response = {
            "errors" : [],
            "data" : {}
        }
        if adv is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            response["data"]["value"] = int(adv)
            response["data"]["unit"] = "shares"
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response


def get_percent_change(ticker, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share

        p_change = share.get_percent_change()
        response = {
            "errors" : [],
            "data" : {}
        }
        if p_change is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            print(p_change)
            response["data"]["value"] = str(p_change)
            response["data"]["unit"] = "%"
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response


def get_volume(ticker, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share        

        volume = share.get_volume()
        response = {
            "errors" : [],
            "data" : {}
        }
        if volume is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            response["data"]["value"] = float(volume)
            response["data"]["unit"] = "shares"
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response



def get_historical(ticker, start, end):
    try:   
        data = yf_download(ticker, start=start, end=end)
        data = list(data.T.to_dict().values())
        response = {
            "errors" : [],
            "data" : {}
        }
        if data is None or len(data) == 0:
            response["errors"].append("Ticker doesn't exist.")
            return response
        else:
            response["data"] = data
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response



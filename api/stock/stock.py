

from yahoo_finance import Share

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



def get_historical(ticker, start, end, _share=None):
    try:
        share = None
        if _share is None:
            share = Share(ticker)
        else:
            share = _share        

        data = share.get_historical(start, end)
        response = {
            "errors" : [],
            "data" : {}
        }
        if data is None:
            response["errors"].append("Ticker doesn't exist.")
            return response  
        else:
            response["data"] = data
            return response
    except ValueError as e:
        response["errors"].append("Corrupt or incompatible data.")
        return response



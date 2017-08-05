"""
    endpoints.py
    api.stock.endpoints.endpoints

    Author:
        Nathaniel Moon
        nathaniel.c.moon@gmail.com
    
    Date:
        3 August 2017

    Description:
        Provides server endpoints for the api's stock namespace

        The api provides a general dump of information, as well as fine-grained
        searches for each data point. 

"""

from flask_restplus import Resource
from flask import request
import json
from yahoo_finance import Share
from pandas_datareader import data as pdr

from api.api_config import api
from api.stock.stock import get_open, get_price, get_avg_daily_volume, get_percent_change, get_volume, get_historical

from models.util.request_helpers import is_resilient, is_valid_date



# Create a namespace for the stock api domain
_namespace = api.namespace('stock', description='Operations related to stock information.')


@_namespace.route('/<string:ticker>')
class Stock(Resource):
    def get(self, ticker):
        """
            Stock::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                A dump of all available data for a stock

            Description:
                A general route that provides a dump of all information about a stock. 

                **Checks for resilience.

        """
        # Derive share here and pass it in to minimize network traffic
        share = Share(ticker)

        response = {
            "price" : get_price(ticker, _share=share),
            "open" : get_open(ticker, _share=share),
            "volume" : get_volume(ticker, _share=share),
            "avg-daily-volume" : get_avg_daily_volume(ticker, _share=share),
            "percent-change" : get_percent_change(ticker, _share=share),
            "nasty" : {"errors":["I'm nasty"]}
        }

        if is_resilient():
            return response
        else:
            errors = []
            for _, value in response.items():
                errors += value["errors"]
            
            if len(errors) > 0:
                api.abort(code=400, message=json.dumps(errors))
            else:
                return response



@_namespace.route('/<string:ticker>/price')
class Price(Resource):
    def get(self, ticker):
        """
            Price::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                The current price of a specific stock

            Description:
                A route to grab the current price of a stock.  

        """
        price = get_price(ticker)
        return price


@_namespace.route('/<string:ticker>/open')
class Open(Resource):
    def get(self, ticker):
        """
            Open::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                The opening price of a specific stock

            Description:
                A route to grab the opening price of a stock.  

        """
        _open = get_open(ticker)
        return _open


@_namespace.route('/<string:ticker>/volume')
class Volume(Resource):
    def get(self, ticker):
        """
            Volume::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                The volume of a specific stock

            Description:
                A route to grab the volume of a stock.  

        """
        volume = get_volume(ticker)
        return volume

@_namespace.route('/<string:ticker>/avg-daily-volume')
class AvgDailyVolume(Resource):
    def get(self, ticker):
        """
            AvgDailyVolume::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                The average daily volume of a specific stock

            Description:
                A route to grab the average daily volume of a stock.  

        """
        avd = get_avg_daily_volume(ticker)
        return avd



@_namespace.route('/<string:ticker>/percent-change')
class PercentChange(Resource):
    def get(self, ticker):
        """
            PercentChange::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock

            Returns:
                The percent change of a specific stock

            Description:
                A route to grab the percent change of a stock. Represented
                as a string value that contains the percent change with
                a directional prefix ('-' or '+'). e.g. '+0.13'

        """
        p_change = get_percent_change(ticker)
        return p_change



@_namespace.route('/<string:ticker>/historical')
class Historical(Resource):
    def get(self, ticker):
        """
            Historical::get

            Parameters:
                ticker:string
                    The ticker corresponding to a stock
                start:datestring
                    The start date for historical data
                    %Y-%m-%d
                end:datestring
                    The end date for historical data
                    %Y-%m-%d

            Returns:
                A list of dictionaries containing:
                    Volume:int
                    Open:float
                    Low:float
                    Adj Close:float
                    High:float
                    Close:float

            Description:
                Gets all historical data for a stock in a certain range of dates.

        """
        if request.args.get("start") is None:
            api.abort(code=400, message="GET Requests to '/<string:ticker>/historical' must contain a start date ('%Y-%m-%d')")  

        if request.args.get("end") is None:
            api.abort(code=400, message="GET Requests to '/<string:ticker>/historical' must contain an end date ('%Y-%m-%d')")

        start = request.args.get("start")
        end   = request.args.get("end")

        if not is_valid_date(start, '%Y-%m-%d'):
            api.abort(code=400, message="Start date must be of the format '%Y-%m-%d'")

        if not is_valid_date(end, '%Y-%m-%d'):
            api.abort(code=400, message="End date must be of the format '%Y-%m-%d'")
    
        data = get_historical(ticker, start, end)

        if len(data["errors"]) > 0:
            api.abort(code=500, message=data["errors"])

        return data




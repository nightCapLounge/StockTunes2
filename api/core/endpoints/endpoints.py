from flask_restplus import Resource
from flask import request, send_file
from api.api_config import api

from models.util.request_helpers import is_valid_date
from api.core.core import create_midi_file
from api.stock.stock import get_historical

_namespace = api.namespace('midi', description='Operations related to midi functionality.')

@_namespace.route('/<string:ticker>')
class MIDIGenerator(Resource):
    def get(self, ticker):
        """
            MIDIGenerator::get

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
                A midi file attachment of the music generated given a stock's
                historical data

            Description:
                Queries for a specific stock's historical data and generates a MIDI file
                from said data

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
        else: 
            midifile = create_midi_file(data["data"], "Adj Close")["file"]
            midifile.seek(0)
            return send_file(midifile, mimetype='audio/midi', as_attachment=True, attachment_filename = ticker + '.mid')



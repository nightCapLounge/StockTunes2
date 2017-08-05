import unittest
import requests
import json
from yahoo_finance import Share

from config import TEST_API_URI, TEST_STOCK, TEST_VERBOSE

class GetStock(unittest.TestCase):
    """Tests for `stock api`."""

    def test_full_dump(self):
        print("\t> Testing: /stock/<string:ticker>")

        share = Share(TEST_STOCK)
        test_data = {
            "price" : float(share.get_price()),
            "volume" : int(share.get_volume()),
            "avg-daily-volume" : int(share.get_avg_daily_volume()),
            "percent-change" : str(share.get_percent_change()),
            "open" : float(share.get_open())
        }

        uri = TEST_API_URI + "/stock/" + TEST_STOCK
        response = requests.get(uri)
        json_data = json.loads(response.text)

        successful = True
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(json.dumps(test_data, indent=2))
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        for key, val in json_data.items():
            if json_data[key]["data"]["value"] != test_data[key]:
                successful = False

        self.assertTrue(successful)

    def test_price(self):
        print("\t> Testing: /stock/<string:ticker>/price")

        share = Share(TEST_STOCK)
        test_data = float(share.get_price())

        uri = TEST_API_URI + "/stock/" + TEST_STOCK + "/price"
        response = requests.get(uri)
        json_data = json.loads(response.text)
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(test_data)
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        self.assertEqual(test_data, json_data["data"]["value"])



    def test_open(self):
        print("\t> Testing: /stock/<string:ticker>/open")

        share = Share(TEST_STOCK)
        test_data = float(share.get_open())

        uri = TEST_API_URI + "/stock/" + TEST_STOCK + "/open"
        response = requests.get(uri)
        json_data = json.loads(response.text)
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(test_data)
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        self.assertEqual(test_data, json_data["data"]["value"])



    def test_adv(self):
        print("\t> Testing: /stock/<string:ticker>/avg-daily-volume")

        share = Share(TEST_STOCK)
        test_data = int(share.get_avg_daily_volume())

        uri = TEST_API_URI + "/stock/" + TEST_STOCK + "/avg-daily-volume"
        response = requests.get(uri)
        json_data = json.loads(response.text)
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(test_data)
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        self.assertEqual(test_data, json_data["data"]["value"])


    def test_volume(self):
        print("\t> Testing: /stock/<string:ticker>/volume")

        share = Share(TEST_STOCK)
        test_data = int(share.get_volume())

        uri = TEST_API_URI + "/stock/" + TEST_STOCK + "/volume"
        response = requests.get(uri)
        json_data = json.loads(response.text)
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(test_data)
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        self.assertEqual(test_data, json_data["data"]["value"])



    def test_percent_change(self):
        print("\t> Testing: /stock/<string:ticker>/percent-change")

        share = Share(TEST_STOCK)
        test_data = str(share.get_percent_change())

        uri = TEST_API_URI + "/stock/" + TEST_STOCK + "/percent-change"
        response = requests.get(uri)
        json_data = json.loads(response.text)
        
        if TEST_VERBOSE:
            print("\t> Comparing:")
            print("\t\tTest Data:")
            print(test_data)
            print("\t\tResponse Data:")
            print(json.dumps(json_data, indent=2))

        self.assertEqual(test_data, json_data["data"]["value"])






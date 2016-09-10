'''
Created on Aug 26, 2016

@author: Maria Shpatserman
'''
import logging
import json
import requests
class TestWebService(object):
    '''
    classdocs
    '''
    logging.basicConfig(filename='../logs/testlog.log', level=logging.INFO)
    def testGetAlcoholProducts(self):
        headers = {'content-type': 'application/json'}

        # Example add method
        payload = {
                   "method": "get_alcohol_products",
                   "params": [],
                   "jsonrpc": "2.0",
                   "id": 0,
                   }
        data = json.dumps(payload)
        logging.info(data)
        response = requests.post(self.url, data, headers).json()
        logging.info(response)
        
        assert response["jsonrpc"]
        assert response["id"] == 0
        #
        
    def testGetEatableProducts(self):
        headers = {'content-type': 'application/json'}

        # Example add method
        payload = {
                   "method": "get_eatable_products",
                   "params": [],
                   "jsonrpc": "2.0",
                   "id": 0,
                   }
        data = json.dumps(payload)
        logging.info(data)
        response = requests.post(self.url, data, headers).json()
        logging.info(response)
        
        assert response["jsonrpc"]
        assert response["id"] == 0
        
    def testGetProducts(self):
        headers = {'content-type': 'application/json'}

        # Example add method
        payload = {
                   "method": "get_products",
                   "params": [],
                   "jsonrpc": "2.0",
                   "id": 0,
                   }
        data = json.dumps(payload)
        logging.info(data)
        response = requests.post(self.url, data, headers).json()
        logging.info(response)
        
        assert response["jsonrpc"]
        assert response["id"] == 0

    def __init__(self, host,port,):
        '''
        Constructor
        '''
        self.url = "http://"+host+":"+port+"/"
        logging.info("url = "+self.url)
        
test = TestWebService("localhost","4000")   
test.testGetAlcoholProducts()
test.testGetEatableProducts()
test.testGetProducts()
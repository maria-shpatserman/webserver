'''
Created on Aug 25, 2016

@author: Maria Shpatserman
'''
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
import xml.etree.ElementTree as ET
import logging
import ast
import json


class ServerJson(object):
    '''
    classdocs
    '''
    logging.basicConfig(filename='../logs/myapp.log', level=logging.INFO)
    

    def __init__(self):
        '''
        Constructor
        '''
        self.readJsonFile()
        
        logging.info(self.json_object)
        #for key, value in data.items():
         #   logging.info(msg) key, value
        logging.info("eatable products: "+str(self.json_object['products']['eatable']))
        logging.info("alcohol products: "+str(self.json_object["products"]["alcohol"]))
        
    def readJsonFile(self):
        with open('../data/products.json', 'r') as f:
            self.json_object = json.load(f) 
    
              
    
    @Request.application
    def application(self,request):
        logging.info(request.data)
        dispatcher["get_alcohol_products"] = self.get_alcohol_products
        dispatcher["get_eatable_products"] = self.get_eatable_products
        dispatcher["get_products"] = self.get_products
        response = JSONRPCResponseManager.handle(request.data, dispatcher)
        logging.info(response)
        logging.info(response.json)
    
        return Response(response.json, mimetype='application/json')
    def main(self):
        run_simple('localhost', 4000, self.application)
    
    def get_products(self):
        logging.info(self.json_object)
        return self.json_object
    
    def get_alcohol_products(self):        
        return self.json_object["products"]["alcohol"]
    
    
    def get_eatable_products(self):
        return self.json_object['products']['eatable']
    
if __name__ == '__main__':
    ServerJson().main()
   # Example().main()
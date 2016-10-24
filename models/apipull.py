'''
Created on Oct 20, 2016

@author: rockyh89
'''
import json
import requests
import pandas
import os
import contextlib
import csv
import io

def yahoo_api_call(symbols):
    #Yahoo API url
    url = "http://finance.yahoo.com/d/quotes.csv"
    #s = symbols, f = equity data fields
    api_parameters = {"s":symbols,"f":"snpb2b3ghl1t8ee9e7e8r2"}
    my_response = requests.get(url,params=api_parameters)
    print(my_response.encoding)
    print(my_response.headers)
    print(my_response.content)
    #decode response
    decoded_reponse = io.StringIO(my_response.content.decode('utf-8'))
    #decoded_headers = io.StringIO(my_response.headers.decode('utf-8'))
    #option_dictionary = json.loads(my_response.json())
    #pandas.dataFrame(my_response)
    #create dataframe
    option_dataframe = pandas.read_csv(decoded_reponse, names = my_response.headers)
    option_dataframe.to_csv(os.path.join(os.path.dirname(__file__),"..","data","options_test.csv"))


#===============================================================================
# def savetofile():
#     with contextlib.closing(requests.get(url, stream=True, params=api_parameters)) as r:
#         reader = csv.reader(r.iter_lines(),delimiter=',')
#         for row in reader:
#             print(row)
#     return
#===============================================================================

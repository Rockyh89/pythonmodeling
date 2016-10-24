'''
Created on Oct 19, 2016

@author: rockyh89
'''
import databasepull
import apipull

if __name__ == '__main__':
    databasepull.query_to_csv("""select * from raw_data.optionstats_history where quotedate = date '2015-02-03'""","/Users/rockyh89/Google_Drive/python_model_outputs/20150203_OptionsStats.csv")
    #apipull.yahoo_api_call("SPY,COF")
    pass
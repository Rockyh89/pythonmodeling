'''
Created on Oct 19, 2016

@author: rockyh89
'''

import psycopg2
import pandas


def query_to_csv(query,target_file_location,dbname="'options'", user="'postgres'", host="'localhost'", password=""''""):
#connect to database
    try:
        conn = psycopg2.connect("dbname="+dbname + "user="+user + "host="+host + "password="+password)
    except:
        print ("Database Connection Exception")
    
    cur = conn.cursor()
    
    #run query
    try:
        cur.execute(query)
    except:
        print ("Fetch Query Exception")
    
    rows = cur.fetchall()
    
    #add headers to output
    headers = []
    for header in cur.description:
        headers.append(header[0])
    
    #close connection
    if conn:
        conn.close()
    
    #create dataframe with headers and data
    df = pandas.DataFrame(rows, columns=headers)
    #output dataframe to csv file
    try:
        df.to_csv(target_file_location)
    except:
        print ("CSV Writer Exception")
    return
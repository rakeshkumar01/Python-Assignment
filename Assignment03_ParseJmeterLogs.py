import csv
import os
from datetime import datetime

#Open the jmeter log file (placed in the same directory)
def getFailedRowsFromLogFile():
    with open("Jmeter_log1.jtl") as f:
        data=csv.DictReader(f)
        count=0 
        failedRows=[] 
        for row in data:
            count = count + 1             
            if str(row['responseCode']) != "200":            
                print(f"Record falied at row no: {count+1}")
                failedRows.append({'label':row['label'], 'responseCode':row['responseCode'], 'responseMessage':row['responseMessage'], 'failureMessage':row['failureMessage'], 'timeStamp': str(datetime.fromtimestamp(int(row['timeStamp'])/1e3))})
    return failedRows                

#Add failed records to new csv
def createCSV(failedRows):
    with open("testfile.csv","w", newline='') as w:
        fieldnames = ['label', 'responseCode', 'responseMessage', 'failureMessage', 'timeStamp']
        csv_writer = csv.DictWriter(w,fieldnames=fieldnames)
        csv_writer.writeheader()   

        for tests in failedRows:
            csv_writer.writerow(tests)
        print("Please check 'testfile.csv' file for detail.") 
        
#Get the failed recrods from the log file
failedRows=getFailedRowsFromLogFile()

#Add falied records to new csv file
createCSV(failedRows)
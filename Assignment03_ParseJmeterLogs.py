import csv,os,pytz
from pytz import timezone
from datetime import datetime

#Open the jmeter log file (placed in the same directory)
def getFailedRowsFromLogFile(fileName):
    with open(fileName) as f:
        data=csv.DictReader(f)
        count=0 
        failedRows=[]         
        for row in data:
            count = count + 1             
            if str(row['responseCode']) != "200":            
                print(f"Record falied at row no: {count+1}")
                failedRows.append({'label':row['label'], 'responseCode':row['responseCode'], 'responseMessage':row['responseMessage'], 'failureMessage':row['failureMessage'], 'timeStamp': row['timeStamp']})
    return failedRows 

#Method to convert timestamp to timezone
def updateTimeZone(failedRows): 
    #Instantiate a timezone object
    timezone= pytz.timezone("US/Pacific")   
    for each in failedRows:        
        dt=each.get("timeStamp")        
        #Check if timestamp is empty
        if (dt.strip()):             
            each['timeStamp']=str(timezone.localize(datetime.fromtimestamp(int(dt)/1000)))            
        else:                
            continue
    return failedRows        

#Add failed records to new csv
def createCSV(failedRows):
    with open("testfile.csv","w", newline='') as w:
        fieldnames = ['label', 'responseCode', 'responseMessage', 'failureMessage', 'timeStamp']
        csv_writer = csv.DictWriter(w,fieldnames)
        csv_writer.writeheader()   

        for tests in failedRows:
            csv_writer.writerow(tests)
        print("Please check 'testfile.csv' file for detail.")         

#Pass the jmeter log file name for e.g. Jmeter_log1.jtl. Log file should be in the same folder in which this file is located.
#And get the faild records in failedRows obj
failedRows=getFailedRowsFromLogFile("Jmeter_log1.jtl")

#Call updateTimeZone method to update the timezone
failedRows=updateTimeZone(failedRows)

#Add falied records to new csv file
createCSV(failedRows)
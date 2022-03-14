import xml.etree.ElementTree as ET
import datetime
from datetime import timedelta
from datetime import date

#Method for getting depart and return values from user.
def getDepartAndReturnDays():
    X = int(input("Please enter the no. of days to DEPART: "))
    Y = int(input("Please enter the no. of days to RETURN: "))
    return X,Y

#Method for formatting the DEPART and RETURN values
def getDepartReturnValues(X,Y):
    #Get current date
    currentDate = date.today()
    #Calculate the DEPART and RETURN days in future from the current date
    X = currentDate+timedelta(days=X)
    Y = currentDate+timedelta(days=Y)
    #Format the dapartDate and retureDate in the requried format i.e. YYYYMMDD
    X=X.strftime('%Y%m%d')
    print("Depart date in udpated format >", X)
    Y=Y.strftime('%Y%m%d')
    print("Return date in udpated format >", Y)
    return X,Y

#Method for updating depart and return value in new xml file
def updateDepartReturn(X,Y):
    # Open test_payload1.xml file and parse in tree
    tree = ET.parse("test_payload1.xml")
    #Get the root element of tree
    root = tree.getroot()

    #Find DEPART and replace it's value with X
    for depart in root.iter('DEPART'):
        depart.text=str(X)

    #Find RETURN and replace it's value with Y
    for ret in root.iter('RETURN'):
        ret.text=str(Y)
    
    #Write the content to new file "Updated File.xml"
    print("Values of DEPART and RETURN are updated in 'updated_payload.xml'")
    return tree.write('updated_payload.xml')


#Get values of DEPART and RETURN in X and Y
departGrtReturn=True
while(departGrtReturn):
    X,Y=getDepartAndReturnDays()    
    print(f"Values entered for DEPART and RETURN are > {X} and {Y}")    
    #If Departure days are more than reture days, collect the again
    if X > Y:
        print("Departure days can't be more than Return days!\nPlease try again.")
        departGrtReturn=True   
    else:            
        departGrtReturn=False
        

X,Y= getDepartReturnValues(X,Y)

#Update the Depart and Return value and create a new file
updateDepartReturn(X,Y)
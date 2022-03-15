import json
from textwrap import indent

#Open file and display the JSON elements to  user for selection of element that s/he wants to delete.
def getData():
    with open('test_payload.json') as f:
        #return data as dict. in python object
        data= json.load(f)
        print("\nFollowing is the JSON data present in test_payload.json\n",data)
        return data

#Method to remove specific element from the file
def remove_data(data,del_element):
    #Check if it is a dict.
    if isinstance(data, dict):
        #If key is found at the first depth
        if del_element in data:                        
            data.pop(del_element)
            print("Element deleted!")
        
        #Else we need to check the depth of the elements
        else:
            #Iterate through the dict items.
            for key in data.keys():                
                #Ignore single elements which will come as String.
                #Check if the element a dict. If yes, store it in new variable and make a recursive call to the method'''
                if isinstance(data.get(key),dict):
                    newData=data.get(key)                    
                    remove_data(newData, del_element)
                # Else check if it is a list. If yes, store the data is new variable and 
                # iterate to find the element that needs to be deleted                
                elif isinstance(data.get(key),list):
                    newData=data.get(key)
                    for item in newData:
                        #If element is found in the list, delete it.
                        if item==del_element:
                            newData.remove(item) 
    return data

#Create the new file with updated json
def getUpdatedPayload(updated_json):
    with open("updated JSON.json", 'w') as file:
        file.write(updated_json)
        print("Please check the updated payload in 'updated JSON.json' file.")

#Store json payload in data variable
data=getData()
#Get the element to be deleted
del_element=input("Please enter the json element that you want to removes from the test_payload.json: ")

#Call the method to remove the element from payload
updaded_data=remove_data(data,del_element)
updated_json = json.dumps(updaded_data, indent=2)
#Create a new file with updated json
getUpdatedPayload(updated_json)

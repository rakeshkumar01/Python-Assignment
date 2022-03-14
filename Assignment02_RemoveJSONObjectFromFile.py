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
def json_delete_element(data, delete_element):    
    # iterate to the keys in data at root level if it's a dict
    for key in data:        
        if isinstance(data[key], dict):            
            if key==del_element:                
                data.pop(key)                
                break
            #if not found
            else:
                for i in data[key]:                    
                    if i ==delete_element:
                        data[key].pop(i)
                        break

    #If it's not a dict.
        else:
            if key == delete_element:
                del data[key]
                break    
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
updaded_data=json_delete_element(data,del_element)
updated_json = json.dumps(updaded_data, indent=2)
#Create a new file with updated json
getUpdatedPayload(updated_json)
#0. User input for ETL parameters
sourcePath = input("Please enter the file path for your source file: ")
destinationPath = input("Please enter the file path for your destination file: ")

print("\nSource: ", sourcePath, "\nDestination: ", destinationPath)



#1. Schema validation
member = {"id": 101, "name": "Erika", "is_active": True, "age": 45}

def ValidateData(aDictionary):
    errorMessage = "Error:"
    if type(aDictionary) != dict:
        errorMessage += "\nData set is not a dictionary"

    if type(aDictionary["id"]) != int:
        errorMessage += "\nID is not an integer"

    if type(aDictionary["name"]) != str:
        errorMessage += "\nName is not a string"
    
    if type(aDictionary["is_active"]) != bool:
        errorMessage += "\nis_active is not a boolean"
    
    if type(aDictionary["age"]) != int:
        errorMessage += "\nAge is not an integer"

    if errorMessage == "Error:":
        return True
    else:
        print(errorMessage)
        return False
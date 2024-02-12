from services.service_composite import ServiceComposite
from ihm import return_selected_file


if __name__ == "__main__":
    try:
        filePath = return_selected_file()
        print("Demand chosen : ", filePath)
    
        # Call the controller to treat the demand
        service_composite = ServiceComposite()
        result = service_composite.controller(filepath=filePath)
        print(result)

        # if result:
        #    print("Loan granted!")
        # else:
        #    print("Loan denied!")
    except Exception as e:
        print("Error : ", e)
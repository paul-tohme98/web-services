import asyncio
from services.service_composite import ServiceComposite
from ihm import return_selected_file


async def main():
    filePath = return_selected_file()
    file_content = "BASE64_ENCODED_CONTENT"
    print("Demand chosen : ", filePath)

    # Call the controller to treat the demand
    result = await ServiceComposite.controller(filepath=filePath, filecontent=file_content)
    print(result)

    if result:
        print("Loan granted!")
    else:
        print("Loan denied!")

if __name__ == "__main__":
    asyncio.run(main())
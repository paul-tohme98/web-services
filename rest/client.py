import asyncio
from services.service_composite import ServiceComposite
from ihm import *


async def main(iduser, passwd):

    token, auth_tokens = await ServiceComposite.auth(iduser, passwd)
    print("Authentication : ", token)

    if token:
        if auth_tokens:
            tokenVerified = ServiceComposite.verify_token(auth_tokens, iduser, token)
            if tokenVerified:
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
            else:
                createErrorDialog("Invalid authentication token!")
        else:
            createErrorDialog("Authentication failed!")
    else:
        createErrorDialog("Wrong credentials!")


if __name__ == "__main__":
    createLoginWindow()
    iduser = get_iduser()
    passwd = get_passwd()
    asyncio.run(main(iduser, passwd))


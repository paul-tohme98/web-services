from fastapi import HTTPException


class ExtractDemand():
    @classmethod
    def read_text_file(self, filepath: str) -> str:
        try:
            with open(filepath, "r") as file:
                file_content = file.read()
            return file_content
        except FileNotFoundError:
            raise HTTPException(status_code=404, detail="File not found")
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
        
# result = ExtractDemand.read_text_file("../demands/client_1.txt")
# print(result)
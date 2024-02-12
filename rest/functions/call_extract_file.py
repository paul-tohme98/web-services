import requests

def call_extract_demand_api(filepath: str):
    path = "http://127.0.0.1:8080/"
    api_fetch_demand = path+"extract-demand/"  # Replace with the actual base URL of your API

    try:
        # Make a GET request to the API
        response = requests.get(api_fetch_demand, params={"filepath": filepath})

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse and return the JSON response
            result = response.json()
            return result
        else:
            # Print the error if the request was not successful
            print(f"Error: {response.status_code}")
            print(response.text)
            return {"error": f"Request failed with status code {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

# Example usage:
file_path = "demands/client_1.txt"
result = call_extract_demand_api(file_path)
print(result)

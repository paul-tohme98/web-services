###	Projet Services Web & Workflow	###
### By Paul TOHMEH & Bochra HOUISSA

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/paul-tohme98/web-services
cd web-services
```

### 2. Create and Activate Virtual Environment
# Create a virtual environment named 'venv'
```bash 
python -m venv venv
```

or

```bash
python3 -m venv venv
```

# Activate the virtual environment
# On Unix-like systems:
```bash
source venv/bin/activate
```

# On Windows:
```bash
venv\Scripts\activate
```

### 3. Install Dependencies
# Install project dependencies from requirements.txt
```bash
pip install -r requirements.txt
```
or

```bash
pip3 install -r requirements.txt
```

### 4. Run the Code
# 4.1 REST Application
First you need to create a  mysql database named "bank" using the command : 
```bash
sudo mysql
```
or
```bash
mysql -u root -p
```
You can replace "root" with your right mysql user.
Then you need to apply the following query to create the database 
```bash
create schema bank;
```
To prevent having the error : mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported, apply the following sql query : 
```bash
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
If you are using a user other than root, replace 'root' with this user and replace password with your actual mysql password

Then, you need to modify the ".env" file and replace the DB_USER & DB_PASSWORD with those of your mysql username and password.
Now you need to execute all the '.sql' files present in the folder "db_schema_data" inside the schema (bank) that you created. To do so, we used "MySQL Workbench" tool that facilitates the task.

Ensure that you have succesfully executed the queries by running : 
```bash
use bank;
SELECT * FROM users;
```
Feel free to test with any of the tables (users, demands, houses, properties, clients).

Now open two terminals : 

a. in the first one run : 
```bash
python server.py
```

or

```bash
python3 server.py
```

b. in the second one run : 
```bash
python client.py
```

or

```bash
python3 client.py
```
# 4.2 SOAP Application
Open Jupyter notebook with the command : 
```bash
jupyter notebook
```
Open folder "soap"

Open "Server.ipynb" and run all cells

Open "Client.ipynb" and run all cells


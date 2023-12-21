# ReadWritePython
Breweries: Fetching, Processing, and Storing Brewery Data

Introduction:
In the world of programming, scripts often play a crucial role in automating tasks and handling data. In this article, we'll explore a Python script that exemplifies the process of fetching data from an API, processing it, and storing it in a MySQL database. The script focuses on retrieving information about breweries from a specific API, organizing the data, and then saving it for future use.

### 1. Importing Libraries:
```python
import requests
import json
import pandas as pd
import mysql.connector
```
The script starts by importing essential libraries:
- `requests`: For making HTTP requests to the API.
- `json`: For handling JSON data.
- `pandas`: For creating and manipulating data frames.
- `mysql.connector`: For connecting to and interacting with a MySQL database.

### 2. Defining URL and Database Connection:
```python
url = "https://informed-data-challenge.netlify.app/api/breweries"

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Breweries"
)
```
Here, we set the URL from which brewery data will be fetched and establish a connection to a MySQL database named "Breweries" on the local machine.

### 3. Making the API Request:
```python
def request_call(url_value):
    Breweries_data = requests.get(url_value)
    breweries_json = Breweries_data.json()
    return breweries_json
```
The `request_call` function sends an HTTP GET request to the specified URL and returns the JSON response containing information about breweries.

### 4. Data Manipulation:
```python
def data_manipulation(breweries_json_value):
    # ...
    return New_Breweries_data_list
```
The `data_manipulation` function processes the JSON data, extracts relevant information about each brewery, and organizes it into a list called `New_Breweries_data_list`.

### 5. Creating a Pandas Data Frame:
```python
def pandas_data_frame(New_Breweries_data_list_value):
    df = pd.DataFrame(New_Breweries_data_list_value)  
    return print(df)
```
The `pandas_data_frame` function takes the processed data list and creates a Pandas DataFrame, providing a clear and structured representation of the brewery data.

### 6. Checking Existing Table Data:
```python
def check_table_data_exists():
    # ...
```
The `check_table_data_exists` function queries the MySQL database to check if data already exists in the "breweries_data" table.

### 7. Inserting Data into the Database:
```python
def insert_into_db(data):
    # ...
```
The `insert_into_db` function inserts the processed data into the "breweries_data" table within the MySQL database.

### 8. Execution and Analysis:
```python
breweries_json = request_call(url)
results = data_manipulation(breweries_json)
pandas_data_frame(results)

mycursor = mydb.cursor()
check_table_data_exists()
insert_into_db(results)
```
These lines execute the functions in sequence, fetching data, processing it, displaying it using Pandas, and finally, inserting it into the MySQL database.

Conclusion:
This Python script serves as a practical example of interacting with an API, processing data, and utilizing a database to store information. Understanding each line helps grasp the logic and purpose behind the code, providing a foundation for similar data manipulation and storage tasks in the future.

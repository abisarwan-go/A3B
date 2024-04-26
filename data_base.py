from re import match, fullmatch, search
from os import path, remove
from constants import ActionType
from custom_exceptions import CustomError

def drop_table(table_name):
    if path.exists(table_name):
        remove(table_name)
        print(f"{table_name}is removed successfully")
    else:
        raise FileNotFoundError("The table is not found")

def create_table(table_name : str, column_variable : str):
    if path.exists(table_name):
        raise FileExistsError(f"The table '{table_name}' already exists.")
    with open(table_name, 'wb') as file:
        #create dummy type
        if 
    print(f"File '{table_name}' created successfully.")


def parse_query(type, command):
    if type == ActionType.CREATE:
        parsed_command = match(r"CREATE TABLE (\w+)\s*(\(.+\))", command)
        if not parsed_command:
            raise CustomError("Invalid query format, Parse Command")
        else:
            table_name = parsed_command.group(1)  # Table name
            column_definitions = parsed_command.group(2)  # Column definitions
            return table_name, column_definitions
    
    if type == ActionType.DELETE:
        command_match = fullmatch(r"DROP TABLE (\w+)$", command)
        if not command_match:
            raise CustomError("Invalid query format, DROP TABLE")
        table_name = command_match.group(1)
        return table_name

    if type == ActionType.INSERT:
        command_match = search(r"INSERT INTO (\w+)", command)
        columns_match = search(r"\((.*?)\)", command)
        values_match = search(r"VALUES \((.*?)\);", command)
        if not command_match or not command_match or not values_match:
            raise CustomError("Invalid query format, INSENRT INTO")
        table_name = command_match.group(1)
        columns = columns_match.group(1)
        values = values_match.group(1)
        return table_name, columns, values
        
def insert_data(table_name, columns, values):
    print(table_name)
    print(columns)
    print(values)
    
def main():
    while True:
        command = str(input())
        if command.lower() == "exit":
            break

        #Data Definition Language (DDL)
        #CREATE TABLE Employees (EmployeeID INT, FirstName STRING, LastName STRING, Email STRING, Salary FLOAT)
        if command.startswith("CREATE TABLE"):
            try:
                table_name, column_variable = parse_query(ActionType.CREATE, command)
                create_table(table_name, column_variable)
            except (CustomError, Exception) as e:  # Handling both exceptions similarly
                print("Caught an error:", e)    

        elif command.startswith("DROP TABLE"):
            try:
                table_name = parse_query(ActionType.DELETE, command)
                drop_table(table_name)
            except (CustomError, Exception) as e:  # Handling both exceptions similarly
                print("Caught an error:", e)
                
        #Data Manipulation Language (DML)
        #INSERT INTO Employees (FirstName, LastName, Email) VALUES ('John', 'Doe', 'john.doe@example.com');
        elif command.startswith("INSERT INTO"):
            try:
                table_name, columns, values = parse_query(ActionType.INSERT, command)
                insert_data(table_name, columns, values)
            except (CustomError, Exception) as e:  # Handling both exceptions similarly
                print("Caught an error:", e)
        #UPDATE Employees SET Salary = 50000.00 WHERE EmployeeID = 1;
        #DELETE FROM Employees WHERE EmployeeID = 3;
        #SELECT * FROM Employees WHERE LastName = 'Smith';

        #Query
        #SELECT FirstName, LastName, Email FROM Employees WHERE Department = 'Sales' ORDER BY LastName;

        else:
            print("Failed to parse, unknown command")

if __name__ == '__main__':
    main()
# wait input from user, the application will be closed by escape or by command EXIT / exit

    



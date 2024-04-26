# Database From Scratch

This project is an implementation of a simple database management system built from scratch in Python. It allows users to create, drop, and insert into tables using a simple command-line interface.

## Features

- **Create Tables**: Define new tables with columns and data types.
- **Drop Tables**: Remove existing tables from the database.
- **Insert Data**: Add new records to the tables.
- **Query Parsing**: Supports parsing of basic SQL-like commands for table operations.

## Getting Started

### Prerequisites

Ensure you have Python installed on your machine. This project is built using Python 3.x.

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abisarwan-go/A3B
   ```
2. Navigate to the project directory:
   ```bash
   cd your-repository
   ```

### Running the Application

Run the script using Python:
```bash
python main.py
```

Follow the on-screen prompts to enter SQL-like commands to interact with your database.

## Commands

- **CREATE TABLE**: `CREATE TABLE table_name (column_name column_type, ...)`
- **DROP TABLE**: `DROP TABLE table_name`
- **INSERT INTO**: `INSERT INTO table_name (column_names) VALUES (values)`

## Example

```bash
CREATE TABLE Employees (EmployeeID INT, FirstName STRING, LastName STRING, Email STRING, Salary FLOAT)
DROP TABLE Employees
INSERT INTO Employees (FirstName, LastName, Email) VALUES ('John', 'Doe', 'john.doe@example.com');
```

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to improve the functionality or fix problems in the project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
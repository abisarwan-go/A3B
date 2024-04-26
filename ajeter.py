import struct
import json

# Define the schema and column names
schema = {
    'EmployeeID': 'int',
    'FirstName': 'str',
    'LastName': 'str',
    'Email': 'str',
    'Salary': 'float'
}
column_names = ','.join(schema.keys())
print("ici, column names" + column_names)
# Convert column names to bytes
print()
column_names_bytes = column_names.encode('utf-8')
print("ici, ccolumn_names_bytes" + str(column_names_bytes))
# Attempt to write to the file
try:
    with open('database.bin', 'wb') as file:  # Ensure the file is opened in write-binary mode
        # Write the length of the column names for later retrieval
        file.write(struct.pack('I', len(column_names_bytes)))
        # Write the column names
        file.write(column_names_bytes)

        # Optionally, write the schema here as previously demonstrated
        schema_bytes = json.dumps(schema).encode('utf-8')
        file.write(struct.pack('I', len(schema_bytes)))
        file.write(schema_bytes)
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Verify by reading back
print()
try:
    with open('database.bin', 'rb') as file:
        # Read the length of the column names data
        names_length = struct.unpack('I', file.read(4))[0]
        # Read the column names data
        column_names_data = file.read(names_length)
        column_names = column_names_data.decode('utf-8')

        # Read schema if necessary
        schema_length = struct.unpack('I', file.read(4))[0]
        schema_data = file.read(schema_length)
        schema = json.loads(schema_data.decode('utf-8'))

    print("Column Names:", column_names)
    print("Schema:", schema)
except IOError as e:
    print(f"An I/O error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

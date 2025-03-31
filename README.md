# Python_Course-ASSIGNMENT_4

# TASK-1  Read a File and Handle Errors 

# File Reader

This Python script defines a function to read the contents of a specified text file and print each line with its corresponding line number. It includes error handling for cases where the file does not exist or other unexpected errors occur.

## Features

- Reads a text file line by line.
- Prints each line with its line number.
- Handles `FileNotFoundError` and other exceptions gracefully.

## Usage

1. Ensure you have Python installed on your machine.
2. Create a text file named `sample.txt` in the same directory as the script, or modify the filename in the function call to point to your desired file.
3. Run the script.

### Example

To read a file named `sample.txt`, you can call the function as follows:

```python
read_file('sample.txt')
Code
Here is the code for the file reader:

python
Run
Copy code
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Reading file content:")
            for idx, line in enumerate(file, start=1):
                print(f"Line {idx}: {line.strip()}")  # Print each line with line number
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function with 'sample.txt'
read_file('sample.txt')
Error Handling
If the specified file does not exist, the script will output an error message indicating that the file was not found.
Any other exceptions that may occur during file operations will also be caught and printed.
License
This project is licensed under the MIT License - see the LICENSE file for details.


# TASK-2 Write and Append Data to a File


# File Writer and Reader

This Python script provides functionality to write user input to a file, append additional input to the same file, and read the contents of the file. The file used in this script is named `output.txt`.

## Features

- **Write to File**: Prompts the user to enter text and writes it to `output.txt`.
- **Append to File**: Allows the user to append additional text to `output.txt`.
- **Read from File**: Reads and displays the contents of `output.txt` line by line.

## Usage

1. Ensure you have Python installed on your machine.
2. Run the script in your terminal or command prompt.
3. Follow the prompts to enter text to write and append to the file.

### Example

When you run the script, it will prompt you for input:

```plaintext
Enter text to write to the file: Hello, World!
Data successfully written to output.txt.
Enter additional text to append: This is an additional line.
Data successfully appended.
Final content of output.txt:
Line 1: Hello, World!
Line 2: This is an additional line.
Code
Here is the code for the file writer and reader:

python
Run
Copy code
# Function to write user input to a file
def write_to_file(filename):
    user_input = input("Enter text to write to the file: ")
    with open(filename, 'w') as file:
        file.write(user_input + '\n')
    print("Data successfully written to output.txt.")

# Function to append user input to the file
def append_to_file(filename):
    user_input = input("Enter additional text to append: ")
    with open(filename, 'a') as file:
        file.write(user_input + '\n')
    print("Data successfully appended.")

# Function to read and display the file content
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            print("Final content of output.txt:")
            for idx, line in enumerate(file, start=1):
                print(f"Line {idx}: {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File name
filename = 'output.txt'

# Execute functions
write_to_file(filename)
append_to_file(filename)
read_file(filename)
Error Handling
If the specified file does not exist when attempting to read, the script will output an error message indicating that the file was not found.
Any other exceptions that may occur during file operations will also be caught and printed.
License
This project is licensed under the MIT License - see the LICENSE file for details.

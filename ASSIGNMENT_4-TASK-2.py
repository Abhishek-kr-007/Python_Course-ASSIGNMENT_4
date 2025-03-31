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

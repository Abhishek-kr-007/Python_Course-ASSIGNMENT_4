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

# Create a sample text file
sample_text = """This is a sample text file.
It contains multiple lines."""

with open('sample.txt', 'w') as file:
    file.write(sample_text)

# Call the function with 'sample.txt'
read_file('sample.txt')

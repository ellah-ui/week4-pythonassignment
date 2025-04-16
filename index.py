# This script reads a file named "input.txt" and prints its content.
def read_and_modify_file():
    try:
        with open("input.txt", "r") as file:
            data = file.read()
            print("Original Data:", data)
            return data
    except FileNotFoundError:
        print("The file 'input.txt' was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
# Modify the content (example: convert to uppercase)   
data = read_and_modify_file()
if data:
    modified_data = data.upper()
    print("Modified Data:", modified_data)
    # Add logic to write modified_data to a file
try:
    with open("output.txt", "w") as file:
        file.write(modified_data)
        print("Modified data written to 'output.txt'")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")


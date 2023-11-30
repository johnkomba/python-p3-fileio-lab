# file_io.py

def write_file(file_name, file_content):
    # Add the file extension to the file_name
    file_name = file_name + ".txt"
    
    # Open the file in write mode
    with open(file_name, "w") as file:
        # Write the content to the file
        file.write(file_content)

def append_to_file(file_name, append_content):
    # Add the file extension to the file_name
    file_name = file_name + ".txt"

    # Open the file in append mode
    with open(file_name, "a") as file:
        # Append the content to the file
        file.write("\n" + append_content)

def read_file(file_name):
    # Add the file extension to the file_name
    file_name = file_name + ".txt"

    # Open the file in read mode
    with open(file_name, "r") as file:
        # Read the content from the file
        content = file.read()
    
    return content

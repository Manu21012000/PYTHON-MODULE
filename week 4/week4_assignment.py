def read_and_modify_file():
    try:
        # input for the file name from the usee
        input_file = input("Enter the filename to read: ")

        # Opening thfle to read
        with open(input_file, "r") as file:
            content = file.readlines()

        # modify i.e change each line to uppercase
        modified_content = [line.upper() for line in content]

        # output file
        output_file = "modified_" + input_file

        #  new modified  file
        with open(output_file, "w") as file:
            file.writelines(modified_content)
        print(f"Modified content saved to {output_file}")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Run the function
read_and_modify_file()

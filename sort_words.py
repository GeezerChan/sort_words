def sort_lines_in_file():
    try:
        # Ask the user for the file path
        file_path = input("Enter the path of the file to sort: ")

        # Open the file in read mode
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Sort the lines alphabetically (case-insensitive)
        lines.sort(key=lambda line: line.lower())

        # Write the sorted lines back to the file
        with open(file_path, 'w') as file:
            for line in lines:
                file.write(line)  # Write each sorted line to the file

        print(f"Lines in {file_path} have been sorted alphabetically (case-insensitive).")
    
    except FileNotFoundError:
        print(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
sort_lines_in_file()

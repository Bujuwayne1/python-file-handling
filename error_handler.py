def read_user_file():
    filename = input("Enter a filename to read: ")
    try:
        with open(filename, 'r') as file:
            print("\nFile content:\n")
            print(file.read())
    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: No permission to read '{filename}'.")
    except UnicodeDecodeError:
        print("Error: File encoding not supported (try a text file).")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Run the function
read_user_file()

def modify_file(input_file, output_file):
    try:
        with open(input_file, 'r') as f_in:
            content = f_in.read()
        
        # Example modification: Convert to uppercase
        modified_content = content.upper()
        
        with open(output_file, 'w') as f_out:
            f_out.write(modified_content)
        print(f"Success! Modified content saved to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"Error: Input file '{input_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
modify_file("original.txt", "modified.txt")

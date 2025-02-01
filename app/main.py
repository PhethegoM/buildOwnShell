import sys  # Handles system functions (like exiting the shell)
import os   # Interacts with the operating system (e.g., checking PATH)
import subprocess  # Runs external commands

def main():
    # List of built-in commands
    builtins = ['exit', 'echo', 'type', 'pwd']
    
    while True:
        # Display the shell prompt
        sys.stdout.write("$ ")

        # Read user input and split into a list
        argv = input().split()

        # If the command is 'exit', terminate the shell
        if argv[0] == 'exit':
            if argv[1:]:
                sys.exit(int(argv[1]))  # Exits with the provided status code
            else:
                sys.exit() # Exits with status code 0 by default

        # If the command is 'echo', print the provided arguments
        elif argv[0] == 'echo':
            print(*argv[1:], file=sys.stdout)

        elif argv[0] == 'pwd':
            print(os.getcwd())

        # If the command is 'type', check if it's built-in or external
        elif argv[0] == 'type':
            # Get system's PATH environment variable (list of directories)
            path_dirs = os.environ.get('PATH').split(':')

            # If the command is a built-in, print that info
            if argv[1] in builtins:
                print(f'{argv[1]} is a shell builtin')

            # If not a built-in, search for it in PATH directories
            elif path_dirs != ['']:  # Ensures PATH is not empty
                found = False
                for dir in path_dirs:
                    executable_path = os.path.join(dir, argv[1])
                    # Check if file exists and is executable
                    if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                        found = True
                        break  # Stop searching once found

                # Print the full path if found, otherwise print 'not found'
                if found:
                    print(f'{argv[1]} is {executable_path}')
                else:
                    print(f'{argv[1]}: not found')

            # If PATH is empty, command is not found
            else:
                print(f'{argv[1]}: not found')

        # If the command is not built-in, try running it as an external command
        else:
            try:
                # Execute the command and capture output/errors
                process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()

                # Print command output if available
                if output:
                    print(output.decode('utf-8').strip())

                # Print error messages if available
                if error:
                    print(error)

            # Handle cases where command is not found
            except FileNotFoundError:
                print(f'{argv[0]}: command not found')

            # Handle permission issues
            except PermissionError:
                print(f'{argv[0]}: Permission denied')

            # Catch any other unexpected errors
            except Exception as e:
                print(f'Error: {e}')

# Run the shell when the script is executed
if __name__ == "__main__":
    main()

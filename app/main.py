import sys
import os
import subprocess

def main():
    builtins = ['exit', 'echo', 'type']
    # Wait for user input
    while True:
        sys.stdout.write("$ ")

        argv = input().split()

        if argv[0] == 'exit':
                sys.exit(int(argv[1]))

        elif argv[0] == 'echo':
            print(*argv[1:], file=sys.stdout)
        
        elif argv[0] == 'type':
            path_dirs = os.environ.get('PATH').split(':')

            if argv[1] in builtins:
                  print(f'{argv[1]} is a shell builtin')
            
            elif path_dirs != ['']:
                found = False
                for dir in path_dirs:
                    executable_path = os.path.join(dir, argv[1])
                    if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                        found = True
        
                if found:
                    print(f'{argv[1]} is {executable_path}')
                
                if not found:
                    print(f'{argv[1]}: not found')
                         
            else:
                print(f'{argv[1]}: not found')
                  
        else:
            try:
                process = subprocess.Popen(argv, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                output, error = process.communicate()

                if output:
                    print(output.decode('utf-8').split('\n')[0])

                if error:
                    print(error)
            
            except FileNotFoundError:
                print(f'{argv[0]}: command not found')
            except PermissionError:
                print(f'{argv[0]}: Permission denied')
            except Exception as e:
                print(f'Error: {e}')



if __name__ == "__main__":
    main()

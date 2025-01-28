import sys

def main():
    commands = ['exit', 'echo', 'type']
    # Wait for user input
    while True:
        sys.stdout.write("$ ")

        command = input()

        if command.split()[0] == 'exit' and command.split()[1] == '0':
                sys.exit()

        if command.split()[0] == 'echo':
             command = ' '.join(command.split()[1:])
             sys.stdout.write(f'{command}\n')
             continue
        
        if command.split()[0] == 'type':
             if command.split()[1] in commands:
                  sys.stdout.write(f'{command.split()[1]} is a shell builtin\n')
                  continue
             else:
                sys.stdout.write(f'{command.split()[1]}: not found\n')
                continue
                  
        if command.split()[0] not in commands:
            sys.stdout.write(f'{command}: command not found\n')
            continue



if __name__ == "__main__":
    main()

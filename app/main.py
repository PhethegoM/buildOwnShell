import sys

def main():
    # Wait for user input
    while True:
        sys.stdout.write("$ ")

        command = input()

        if command.split()[0] == 'exit' and command.split()[1] == '0':
                sys.exit()
        if command.split()[0] == 'echo':
             command = ' '.join(command.split()[1:])
             sys.stdout.write(f'{command}\n')
        else:
            sys.stdout.write(f'{command}: command not found\n')



if __name__ == "__main__":
    main()

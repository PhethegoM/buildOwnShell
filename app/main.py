import sys

def main():

    # Wait for user input
    while True:
        sys.stdout.write("$ ")

        command = input().rstrip()

        # try:
        #     command, int = command.split()
        # except:
        #     command = command

        if command == 'exit 0':
            sys.exit()
        else:
            print(f'{command}: command not found')


if __name__ == "__main__":
    main()

# lines.py - Counts number of lines in source code, excluding blank lines and lines that begin with a # sign.
# Runs from the command line, e.g., lines.py example.py

import sys                      # needed for argv and exit


# exits if no arguments passed, more than one passed, or if argument is not a file ending in .py

def main():
    try:
        if len(sys.argv) > 2:
            sys.exit("Too many command-line arguments")
        elif len(sys.argv) < 2:
            sys.exit("Too few command-line arguments")
        elif sys.argv[1].endswith(".py") == False:
            sys.exit("Not a Python file")
        else:
            print(count_lines(sys.argv[1]))        # if arguments are valid and file exists, run count_lines function on the file named by the user
    except FileNotFoundError:
        sys.exit("File does not exist")

def count_lines(s):

    program_lines = 0
    blank_lines = 0
    commented_lines = 0

    with open(sys.argv[1]) as file:
        for line in file:
            if line.strip().startswith("#"):            # if line starts with "#" sign, add 1 to commented_lines counter
                commented_lines += 1
                print("found line starting with #")
            elif len(line.strip()) == 0:                # if line length = 0 after stripping white space, add 1 to blank_lines counter
                blank_lines += 1
                print("found blank line")
            else:
                program_lines +=1
    return program_lines - blank_lines - commented_lines

if __name__ == "__main__":
    main()

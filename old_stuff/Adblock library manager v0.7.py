#Adblock library manager v0.8
import os
import csv
contributions_library_items = []
contributions_library_verifications = []
contributions_library_flags = []
full_library_name = os.path.join("/Volumes/Liam's Works/Python/mediocre coding idea/","community-enhanced-adblock-library-v1.txt")
official_library = []
user_input = ""
selected = False
selected2 = False
selected3 = False
selected4 = False
edit_or_print = ""
line_count = 0
def is_int(a):
    try:
        int(a)
        return True
    except ValueError or TypeError:
        return False
while selected == False:
    user_input = input("Edit or print library:")
    if user_input.upper() == "E" or user_input.upper() == "EDIT":
        edit_or_print = "EDIT"
        selected = True
    elif user_input.upper() == "P" or user_input.upper() == "PRINT":
        edit_or_print = "PRINT"
        selected = True
    else:
        print("Invalid input.")
library_file = open(full_library_name, "r")
official_library = library_file.readlines()
for line in official_library:
    if line != "\n":
        line_count += 1 
library_file.close()
selected = False
while selected == False:
    if edit_or_print == "PRINT":
        selected = True
        while selected2 == False:
            user_input = input("Print the contributions library or the official library?")
            if user_input.upper() == "C" or user_input.upper == "CONTRIBUTIONS" or user_input.upper == "CONTRIBUTIONS LIBRARY":
                selected2 = True
                while selected3 == False:
                    user_input = input("What is the numerical label of this library?")
                    if is_int(user_input) == True:
                        selected3 = True
                        label = " "+user_input
                        try:
                            csv_file = open("Community Adblock Library Submissions"+label+".csv")
                        except FileNotFoundError:
                            print("Invalid file name.")
                            selected3 = False
                    elif user_input == "":
                        label = ""
                        selected3 = True
                    else:
                        print("Invalid input.")
                csv_file = open("Community Adblock Library Submissions"+label+".csv")
                csv_reader = csv.reader(csv_file)
                rows = []
                for row in csv_reader:
                    rows.append(row)
                csv_file.close()
                while selected4 == False:
                    user_input = input("Print contributors usernames or element submissions?")
                    if user_input.upper() == "CONTRIBUTORS" or user_input.upper() == "CONTRIBUTORS USERNAMES" or user_input.upper() == "C" or user_input.upper() == "U" or user_input.upper() == "USERNAMES":
                        selected4 = True
                        blank_count = rows[:][2].count("")
                        print("Printing contributors usernames ("+str(len(rows)-1)+" items)")
                        for i in range(len(rows)-blank_count-1):
                            if row != "":
                                print(rows[i+1][2])
                    elif user_input.upper() == "SUBMISSIONS" or user_input.upper() == "ELEMENT SUBMISSIONS" or user_input.upper() == "S" or user_input.upper() == "E" or user_input.upper() == "ELEMENTS":
                        selected4 = True
                        blank_count = rows[:][1].count("")
                        print("Printing element submissions ("+str(len(rows)-blank_count-1)+" items)")
                        for i in range(len(rows)-1):
                            if row != "":
                                print(rows[i+1][1])
                    else:
                        print("Invalid input.")
            elif user_input.upper() == "O" or user_input.upper == "OFFICIAL" or user_input.upper == "OFFICIAL LIBRARY":
                selected2 = True
                print("Printing official library ("+str(line_count)+" items)")
                for i in range(len(official_library)-2):
                    print(official_library[i+2][:-1])
                print(official_library[-1])
            else:
                print("Invalid input.")
    elif edit_or_print == "EDIT":
        selected = True
        print("Under 'my filter list' in 'advanced' on Adblock plus, select all and press 'copy selected'.")
        print("Then click 'enter' to add them to official library, type 'clear' to clear the library, type 'end' to end the program.")
        library_file = open(full_library_name, "a")
        user_input = input()
        while user_input.upper() != "END":
            if user_input.upper() == "CLEAR":
                library_file.truncate(0)
                library_file.writelines(official_library[:1])
            elif user_input != "":
                library_file.write("\n"+user_input)
            user_input = input()
        library_file.close()
    else:
        print("Invalid input.")

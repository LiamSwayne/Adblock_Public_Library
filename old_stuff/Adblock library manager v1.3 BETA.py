#Adblock library manager v1.3 beta
import os
import csv
full_library_name = os.path.join("/Volumes/Liam's Works/Programming/Python/Adblock Library Project/","community-enhanced-adblock-library-v1.txt")
full_contributions_library_name = os.path.join("/Volumes/Liam's Works/Programming/Python/Adblock Library Project/","contributions-adblock-library-v1.txt")
official_library = []
user_input = ""
selected = False
selected2 = False
selected3 = False
selected4 = False
selected5 = False
selected6 = False
edit_or_print = ""
line_count = 0
contributions_line_count = 0
rows = []
deleting_item = ""
def error_avoid(a):
    try:
        str(a) == deleting_item
        return True
    except IndexError:
        return False
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

contributions_library_file = open(full_contributions_library_name, "r")
official_contributions_library = contributions_library_file.readlines()
for line in official_contributions_library:
    if line != "\n":
        contributions_line_count += 1
library_file.close()

selected = False
while selected == False:
    if edit_or_print == "PRINT":
        selected = True
        while selected2 == False:
            user_input = input("Print Google form submissions, contributions library, or the official library?")
            if user_input.upper() == "C" or user_input.upper() == "CONTRIBUTIONS" or user_input.upper() == "CONTRIBUTIONS LIBRARY":
                selected2 = True
                for i in range(len(official_contributions_library)-1):
                    print(official_contributions_library[i][:-1])
                print(official_contributions_library[-1])
            elif user_input.upper() == "G" or user_input.upper() == "SUBMISSIONS" or user_input.upper() == "GOOGLE FORM SUBMISSIONS" or user_input.upper() == "FORM" or user_input.upper() == "S" or user_input.upper() == "GOOGLE FORM"or user_input.upper == "GOOGLE":
                selected2 = True
                while selected3 == False:
                    user_input = input("What is the numerical label of the sumbissions file?")
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
                for row in csv_reader:
                    official_contributions_library.append(row)
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
        while selected5 == False:
            user_input = input("Edit contributions or official library?")
            if user_input.upper() == "C" or user_input.upper == "CONTRIBUTIONS" or user_input.upper == "CONTRIBUTIONS LIBRARY":
                selected5 = True
                while selected6 == False:
                    user_input = input("Manually input or append submissions?")
                    if user_input.upper() == "M" or user_input.upper == "MANUALLY" or user_input.upper == "MANUALLY INPUT":
                        selected6 = True
                        print("Paste elements and click 'enter' to add them to contributions library.")
                        print("Type 'update' to update the contributions and official library, type 'clear' to clear the library, type 'end' to end the program.")
                        contributions_library_file = open(full_contributions_library_name, "a")
                        user_input = input()
                        while user_input.upper() != "END":
                            if user_input.upper() == "UPDATE":
                                for a in range(len(official_contributions_library)):
                                    if official_contributions_library.count(official_contributions_library[a]) >= 3:
                                        deleting_item = str(official_contributions_library[a])
                                        library_file = open(full_library_name, "a")
                                        library_file.write("\n"+official_contributions_library[a])
                                        library_file.close()
                                        for i in range(len(official_contributions_library)-1):
                                            if error_avoid(official_contributions_library[i]) == True:
                                                if str(official_contributions_library[i]) == deleting_item:
                                                    del official_contributions_library[i]
                                contributions_library_file.truncate(0)
                                contributions_library_file.writelines(official_contributions_library)
                            elif user_input.upper() == "CLEAR":
                                contributions_library_file.truncate(0)
                                official_contributions_library = []
                            elif user_input != "":
                                contributions_library_file.write("\n"+user_input)
                                official_contributions_library.append(user_input)
                            user_input = input()
                        contributions_library_file.close()
                    elif user_input.upper() == "A" or user_input.upper == "APPEND" or user_input.upper == "APPEND SUBMISSIONS" or user_input.upper() == "SUBMISSIONS":
                        selected6 = True
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
                        for row in csv_reader:
                            official_contributions_library.append(row)
                        csv_file.close()
                        for i in range(len(official_contributions_library)):
                            if official_contributions_library.count(official_contributions_library[i]) >= 3:
                                deleting_item = str(official_contributions_library[i])
                                library_file = open(full_library_name, "a")
                                official_library.append(official_contributions_library[i])
                                library_file.close()
                                for i in range(len(official_contributions_library)):
                                    if str(official_contributions_library[i]) == deleting_item:
                                        del official_contributions_library[i]
                                contributions_library_file = open(full_library_name, "a")
                                contributions_library_file.truncate(0)
                                contributions_library_file.writelines(official_contributions_library)
                                contributions_library_file.close()
            elif user_input.upper() == "O" or user_input.upper == "OFFICIAL" or user_input.upper == "OFFICIAL LIBRARY":
                selected5 = True
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
    else:
        print("Invalid input.")

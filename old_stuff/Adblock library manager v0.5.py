#enhanced community Adblock library
#functionality: some

#[X] create contributions library and official library
#[X] switch to using txt files for each list instead of built in to the code
#[ ] create transfer system from contributions to official library

#description:
#The enhanced community adblock library is an open source libarary of additional
#elements to block in order to ehance the adblocking experience. It is a collaboration
#allowing the adblocking community to self-check and work together to improve users
#experience using the internet when adblocking. This comes in the form of removing
#dead space from websites, blocking ads that gets past the primary filter, and more.
#The self-check system allows users to ensure that content is not being blocked.
#All a user has to do to download the library is copy it, got to "advanced" in
#adblock plus options, click in the space for "my filter list", and paste.

#imports
import os

contributions_library_items = []
contributions_library_verifications = []
contributions_library_flags = []
full_library_name = os.path.join("/Users/Liam/Desktop/Liam's Works/Python/mediocre coding idea/","community-enhanced-adblock-library-v1.txt")
official_library = []
user_input = ""
selected = False
edit_or_print = ""
security = False
line_count = 0

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

#initialize official library
library_file = open(full_library_name, "r")
official_library = library_file.readlines()

for line in official_library:
    if line != "\n":
        line_count += 1
 
library_file.close()

#user actions
selected = False
while selected == False:
    if edit_or_print == "PRINT":
        selected = True
        print("Printing official library ("+str(line_count)+" items)")
        for i in range(len(official_library)-3):
            print(official_library[i+3][:-1])
        print(official_library[-1])
    elif edit_or_print == "EDIT":
        selected = True
        print("Under 'my filter list' in 'advanced' on Adblock plus, select all and press 'copy selected'.")
        print("Then click 'enter' to add them to official library, and type 'end' to end the program.")
        library_file = open(full_library_name, "a")
        user_input = input()
        while user_input.upper() != "END":
            if user_input != "":
                library_file.write("\n"+user_input)
            user_input = input()
        library_file.close()
    else:
        print("Invalid input.")

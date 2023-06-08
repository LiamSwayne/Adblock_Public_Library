# Take the content from selecting all and copying "My Filter List" and format it
# for markdown.
# Content is pasted into "elementsStr".
def processInput(elementsStr, MD=True):
    lines = elementsStr.split("\n")
    output = ""
    
    for i in range(len(lines)):
        line = lines[i]
        if line != "" and line != "\n" and line[0:10] != "data:image" and line != "":
            if MD:
                output += "  " + str(i) + ". " + line+"\n"
            else:
                output += line+"\n"
    output = output[:-1]
    print(output)

elementsStr = '''
# elements go here
'''

processInput(elementsStr)

# Take the content from selecting all and copying "My Filter List" and format it for markdown.
# Content is pasted into "elementsStr".
# Header for the README.md is in "headerStr"

def processInput(headerStr, elementsStr, wasHelpfulStr, footerStr, MD=True):
    lines = elementsStr.split("\n")
    output = headerStr+"General library (XXXX elements / XXXX KB)</summary>\n\n"
    elementCount = 0
    characterCount = 0
    
    for i in range(len(lines)):
        line = lines[i]
        if line != "" and line != "\n" and line[0:10] != "data:image" and line != "youtube.com##.style-scope.ytd-rich-shelf-renderer" and line not in wasHelpfulStr:
            elementCount += 1
            characterCount += len(line)
            if MD:
                output += "  "+str(elementCount)+". "+line+"\n"
            else:
                output += line+"\n"

    output = output.replace("XXXX elements", str(elementCount)+" elements")
    output = output.replace("XXXX KB", str(round((characterCount/1000)+1))+" KB")
    output += "</details>"

    output += "<details>\n<summary>\"Was this page helpful\" icons & feedback boxes (XXXX elements / XXXX KB)</summary>\n\n"
    wasHelpfulLines = wasHelpfulStr.split("\n")
    elementCount = 0
    characterCount = 0
    for i in range(len(wasHelpfulLines)):
        line = wasHelpfulLines[i]
        if line != "" and line != "\n" and line[0:10] != "data:image" and line != "youtube.com##.style-scope.ytd-rich-shelf-renderer":
            elementCount += 1
            characterCount += len(line)
            if MD:
                output += "  "+str(elementCount)+". "+line+"\n"
            else:
                output += line+"\n"
    
    output = output.replace("XXXX elements", str(elementCount)+" elements")
    if characterCount < 1000:
        output = output.replace("XXXX KB", "<1 KB")
    else:
        output = output.replace("XXXX KB", str(round((characterCount/1000)+1))+" KB")
    output += "</details>"
    output += footerStr
    
    print(output)

headerStr = '''# Adblock Public Library
This project is a collection of HTML elements that can be plugged into Adblock Plus to improve the Adblock experience. Most of the elements in the library are included to remove distractions and irrelevant information (social icons, popups, newsletter inserts, "urgent" offers, etc). If the adblock is too agressive for a specific site, you can click on the extension icon and disable adblock for that site. This will disable the library for that site as well.

For contributors: This is a community library, meaning anyone can contribute. <-- See CONTRIBUTION.md

Steps to implement library in Google Chrome:
1. Install [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb).
2. In the extension settings > general: turn off acceptable ads.
3. In the extension settings > advanced > filter lists: Enable "ABP filters", "EasyList", "EasyPrivacy", "Fanboy's Notifications Blocking List", "Fanboy's Social Blocking List", and "I don't care about cookies".
4. In the extension settings > advanced > My Filter List: expand, copy, and paste one or more of the lists below into the "search or add filters" box.

<details>
  <summary>'''

footerStr = '''<details>
<summary>Remove YouTube Shorts Shelf from home page (1 element / <1 KB)</summary>
  
  1. youtube.com##.style-scope.ytd-rich-shelf-renderer
</details>'''

wasHelpfulStr = '''
ELEMENTS GO HERE
'''

elementsStr = '''
ELEMENTS GO HERE
'''

processInput(headerStr, elementsStr, wasHelpfulStr, footerStr, True)

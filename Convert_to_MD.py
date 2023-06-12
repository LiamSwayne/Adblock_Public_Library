# Take the content from selecting all and copying "My Filter List" and format it for markdown.
# Content is pasted into "elementsStr".
# Header for the README.md is in "headerStr"

def processInput(headerStr, elementsStr, footerStr, MD=True):
    lines = elementsStr.split("\n")
    output = headerStr+"General library ("+str(len(lines))+" elements)</summary>\n"
    
    for i in range(len(lines)):
        line = lines[i]
        if line != "" and line != "\n" and line[0:10] != "data:image" and line != "youtube.com##.style-scope.ytd-rich-shelf-renderer":
            if MD:
                output += "  " + str(i) + ". " + line+"\n"
            else:
                output += line+"\n"
    output += footerStr
    print(output)

headerStr = '''# Adblock Public Library
This project is a collection of HTML elements that can be plugged into Adblock Plus to improve the Adblock experience. Most of the elements in the library are included to remove distractions and irrelevant information (social icons, popups, newsletter inserts, "urgent" offers, etc). If the adblock is too agressive for a specific site, you can click on the extension icon and disable adblock for that site. This will disable the library for that site as well.


Steps to implement library in Google Chrome:
1. Install [Adblock Plus](https://chrome.google.com/webstore/detail/adblock-plus-free-ad-bloc/cfhdojbkjhnklbpkdaibdccddilifddb).
2. In the extension settings > general: turn off acceptable ads.
3. In the extension settings > advanced > filter lists: Enable "ABP filters", "EasyList", "EasyPrivacy", "Fanboy's Notifications Blocking List", "Fanboy's Social Blocking List", and "I don't care about cookies".
4. In the extension settings > advanced > My Filter List: expand, copy, and paste one or more of the lists below into the "search or add filters" box.

For contributors: This is a community library, meaning anyone can contribute. Every element from contributors is verified individually before being added. Sites that aren't safe for work or encourage piracy will be rejected. Social icons are blocked, but sites that are utility focused such as LinkedIn and RSS should be preserved when possible.

<details>
  <summary>'''

footerStr = '''</details>
<details>
<summary>Remove YouTube Shorts Shelf from home page (1 element)</summary>
youtube.com##.style-scope.ytd-rich-shelf-renderer
</details>'''

elementsStr = '''
ELEMENTS GO HERE
'''

processInput(headerStr, elementsStr, footerStr, True)

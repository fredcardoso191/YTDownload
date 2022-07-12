import re

def isValidURL(str):
    regex = ("(?:https?:\/\/)?(?:youtu\.be\/|(?:www\.|m\.)?youtube\.com\/(?:watch|v|embed)(?:\.php)?(?:\?.*v=|\/))([a-zA-Z0-9\_-]+)")

    p = re.compile(regex)
 
    if (str == None):
        return False
    if(re.search(p, str)):
        return True
    else:
        return False
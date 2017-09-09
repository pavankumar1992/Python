import urllib

def read_file():
    quotes = open("C:\Users\HOME\Desktop\Python\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(input_text):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+input_text)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    

read_file()


## Imports the needed libs
import base64
import random
import string
import time
import os
import platform
import requests
import json
from urllib.request import urlopen

## Sets variables to the ascii letters, digits and punctuation for the added randomized data
lowercase_ascii_letters = string.ascii_lowercase
uppercase_ascii_letters = string.ascii_uppercase
ascii_letters = string.ascii_letters
all_ascii_digits = string.digits
ascii_punctuation = string.punctuation

## Checks what system its being run on
platform = platform.system()


### Defining the Functions : ###


## Not used Integer generation range, originally for an generation range in the fake_data function but it would be just overkill so i instead i just put the random integer generation code into the function itself
def generation_range(): 
    generated_range = random.randint(10000, 20000)
    return generated_range
  

## Defining an Random Number and lowercase letter generator for the name of the output (.py) file 
def random_num_and_lowcases():
    random_numbers_and_lowercases = ''.join([random.choice(lowercase_ascii_letters + all_ascii_digits) for i in range(8)])
    return random_numbers_and_lowercases

## Defining a function to make fake data lines to fill the output file with so the output wont be readable with the naked eye
def fake_data():
    newvar = ''.join([random.choice(ascii_letters + all_ascii_digits + ascii_punctuation) for i in range(random.randint(100000, 500000))])
    ## Added the random_datafunc variable to make the fake data not corrupt the actual hidden python code that has to be executed but it wont matter because after a huge string python is too lazy to read it
    random_datafunc = f"### {newvar}"
    return random_datafunc


## Looks up on which Platform / os the computer is on so it can set the correct command (to clear the screen) in a variable
if platform == "Windows":
    platform_command = "cls"
    platform_mac = False
    
if platform == "Linux":
    platform_command = "clear"
    platform_mac = False
if platform == "Darwin":
    platform_mac == True
    
## Darwin == MacOS








## Prints ThomastheHacker logo

print("""
Made By :
  _______ _                               _   _          _                _             
 |__   __| |                             | | | |        | |              | |            
    | |  | |__   ___  _ __ ___   __ _ ___| |_| |__   ___| |__   __ _  ___| | _____ _ __ 
    | |  | '_ \ / _ \| '_ ` _ \ / _` / __| __| '_ \ / _ \ '_ \ / _` |/ __| |/ / _ \ '__|
    | |  | | | | (_) | | | | | | (_| \__ \ |_| | | |  __/ | | | (_| | (__|   <  __/ |   
    |_|  |_| |_|\___/|_| |_| |_|\__,_|___/\__|_| |_|\___|_| |_|\__,_|\___|_|\_\___|_|                                                                                               
""")

## Waits for a few seconds
time.sleep(5)
## Searching the current version from Data.json and putting it in a variable

jsonf = open('data.json')
json_data = json.load(jsonf)
json_version = json_data['version']
json_creator = json_data['creator']
json_github_page = json_data['github_page']
json_contributors = json_data['contributors']
jsonf.close()


## Clearing the screen
if platform_mac == True:
    print("\033c")
if platform_mac == False:
    os.system(platform_command)
    

## Here is the part that checks from the github file data.json if its updated / or if there is an update
update_url = "https://raw.githubusercontent.com/thomasthehacker/Python-.py-file-Base64-Obfuscator-encoder/main/data.json"
update_url_response = urlopen(update_url)
update_data = json.loads(update_url_response.read())
url_version = update_data['version']


print("Checking the Current version . . .")
time.sleep(3)

## Clearing the screen
if platform_mac == True:
    print("\033c")
if platform_mac == False:
    os.system(platform_command)

## Checks if the online data.json file from the website the same version has as the data locally to see if its updated
if url_version == json_version:
    ## When the program is up to date :
    print("Version is up to date!\n\n Starting up . . .")
    time.sleep(3)

    if platform_mac == True:
        print("\033c")
    if platform_mac == False:
        os.system(platform_command)

    ## Sets the file name of the input file into an variable so it can be used to read the data
    filename = input("Name Of code / input file to encode / Obfuscate (with the .py at the end): ")

    ## Reads the data out of the input file and stores it into a variable
    not_yet_encoded_file = open(f"{filename}", "r")
    read_data = not_yet_encoded_file.read()

    ## Simply encodes the string using base64 
    encoded_file_data = base64.b64encode(read_data.encode())

    ## Makes an variable with all the data (fake & encoded) 
    ## it also puts lines in like .decode and such so that when the output file will get executed it will decode the data and execute the data
    printtofile = f"""
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
import base64 
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
coded_string =  {encoded_file_data}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
coded_string2 = (coded_string).decode()
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
opdracht = base64.b64decode(coded_string2)
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
exec(opdracht)
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
{fake_data()}
    """
    ## Generates a new file name using the old one and the random numbers and lowercases function
    new_filename = "Encoded_python_" + (filename) + "_" + random_num_and_lowcases() + ".py"

    ## Writes all the output data to output file with the newly generated name
    encoded_file_new = open(f"{new_filename}", "w")
    encoded_file_new.write(printtofile)
    
    if platform_mac == True:
        print("\033c")
    if platform_mac == False:
        os.system(platform_command)

    ## Prints out the file has been saved to (the output filename).py
    print(f"file has been saved to {new_filename}")
    print("You can safely close the program now")
    print("program will automaticly close after 10 seconds")

    ## Closes the file before closing the program after 10 seconds have passed
    encoded_file_new.close
    time.sleep(10)
    ## Exits program
    exit()
else:
    ## When the program is out of date
    print("The program is not up to date\n To download the new version go to my github page : https://github.com/thomasthehacker/Base64-Python-file-.py-Encoder-Encrypter/")
    print("\n(if the link doesnt work just go to my profile you will find it here : https://github.com/thomasthehacker")
    print("Program will automaticly close after 10 seconds")
    time.sleep(10)
    exit()

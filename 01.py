import os

path = "./Production Data/testing/imageDetails.py"

with open(path, 'a') as file:
    file.write("\n# This is the text for testing")

os.system('git add .')
print("******************************************** git added ********************************************")
os.system('git commit -m "Minor changes"')
print("******************************************** git commited ********************************************")
os.system('git push')
print("******************************************** git pushed ********************************************")

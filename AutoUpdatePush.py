import os, random

path = "./Production Data/testing/imageDetails.py"

for _ in range(random.randint(3, 10)):
    with open(path, 'a') as file:
        file.write("\n# This is the text for testing")

    os.system('git add .')
    print("******************************************** 1. git added ********************************************")
    os.system('git commit -m "Added: Minor Changes"')
    print("******************************************** 2. git commited ********************************************")
    os.system('git push')
    print("******************************************** 3. git pushed ********************************************")

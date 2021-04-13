import os
import sys
print("What name do you want to give your folder?")
namefolder = input("Name folder: ")
os.mkdir(namefolder)
if not os.path.isdir("folder"):
     os.mkdir("folder")
sys.exit(10)
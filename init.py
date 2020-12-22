import platform
import json
from os.path import dirname, abspath

platform = platform.system()
mod_path = dirname(abspath(__file__))
mod_name = ""
utility = False

if platform.lower() == "windows":
    stripped_path = mod_path.split("\\")
    mod_name = stripped_path[-1]

if platform.lower() == "linux":
    stripped_path = mod_path.split("/")
    mod_name = stripped_path[-1]

print(f"Found mod name: {mod_name}")
desc = input(f"Enter a description for {mod_name}: ")
mod_version = input("What should the mod version be: ")

while True:
    util = input("Should utility be set to true(y/N)?: ").lower()
    if util == "n":
        break
    elif util == "y":
        utility = True
        break
    else:
        print("Unknown character entered")

mod_info = open("mod_info.json", "r")
json_object = json.load(mod_info)
mod_info.close()

json_object["name"] = mod_name
json_object["description"] = desc
json_object["version"] = mod_version
json_object["jars"] = ["jars/" + mod_name + ".jar"]
if utility == True:
    json_object["utility"] = True
else:
    json_object["utility"] = False

mod_info = open("mod_info.json", "w")
json.dump(json_object, mod_info, indent=4)
mod_info.close()



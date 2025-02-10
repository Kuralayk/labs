import json
import os

file_path = r"C:\Users\ilyas\OneDrive\Рабочий стол\Куралай\pp2\labs\lab4\sample-data.json"

if not os.path.exists(file_path):
    print(f"Error: File not found at {file_path}")
else:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("Interface Status")
    print("=" * 80)
    print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
    print("-" * 80)

    for item in data["imdata"]:
        attributes = item["l1PhysIf"]["attributes"]
        dn = attributes["dn"]
        description = attributes.get("descr", "") 
        speed = attributes["speed"]
        mtu = attributes["mtu"]
        print(f"{dn:<50} {description:<20} {speed:<8} {mtu:<6}")

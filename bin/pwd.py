import json

def pwd():
    with open("./directory.json", "r") as f:
        directory = json.load(f)
        print(directory[1:])


if __name__ == "__main__":
    pwd()
import json

def pwd():
    with open("./directory.json", "r") as f:
        print(json.load(f))


if __name__ == "__main__":
    pwd()
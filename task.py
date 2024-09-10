import hashlib
import json

def logger(en, num):
    for i in range(num):
        # print(en)
        first = en[0]
        en = en[1:]
        en = en+first
    return en

def hashish():
    enrollment_number = input("Enter your Enrollment Number: ")
    num = int(enrollment_number[-4:]) % 113
    with open("file.json", "w") as f:
        json.dump({"enrollment_number": logger(enrollment_number, num)}, f)

    with open("file.json") as f:
        enrollment_number = json.load(f)["enrollment_number"]
    hashobj = hashlib.sha256()
    hashobj.update(bytes(enrollment_number, 'utf-8'))
    digest = hashobj.hexdigest()
    print(digest)
    numbers = []
    for char in digest:
        if char.isnumeric():
            numbers.append(int(char))
    print("Your task is:", (sum(numbers)%6) + 1)

if __name__ == "__main__":
    hashish()

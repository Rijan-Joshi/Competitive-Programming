import re

def main():
    print(validate(input("What's your IP address? ")))

def validate(ip):
    if(re.search(r"^([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$",ip)):
        return True
    return False

if __name__ == "__main__":
    main()
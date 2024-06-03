def main():
    i = str(input().strip())
    print(shorten(i))

def shorten(word):
    return ''.join([a for a in word if a.upper() not in "AEIOU"])
    

if __name__ == "__main__":
    main()
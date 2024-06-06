from numb3rs import validate

def main():
    test_format()

def test_format():
    assert validate(r"244.266.245.0") == True
    assert validate(r"255.255.255.2") == True

if __name__ == '__main__':
    main() 
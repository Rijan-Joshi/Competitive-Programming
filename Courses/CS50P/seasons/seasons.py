from datetime import date
import sys
import re
import inflect

p = inflect.engine()

def main():
    input_date = input("What's your birthdate? ")
    current_date = date.today()
    iDate = check_get_format(input_date, current_date)
    total_minute = int((current_date - iDate).total_seconds() // 60)
    print(p.number_to_words(total_minute, andword=",").title())


def check_get_format(input_date, today):
    if (re.search(r"^(\d{4})-(0[1-9]|1[0-2])-(0[0-9]|[12][0-9]|3[01])$", input_date)) :
        try:
            # year, month, days =  map(int, input_date.split('-'))
            # d = date(year, month, days)
            d = date.fromisoformat(input_date)
            return d if today > d else False
        except ValueError:
             return False
    else:
        sys.exit("The date format is invalid.")


if __name__ == "__main__":
    main()
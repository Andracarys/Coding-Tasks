from datetime import date
import sys
import inflect

p = inflect.engine()


class CalculateDate:
    def __init__(self, dob=None):
        self.dob = dob
        self.today = date.today()

    def getDob(self):
        self.dob = input("Enter your date of birth (YYYY-MM-DD): ")
        try:
            self.dob = date.fromisoformat(self.dob)
            return self.dob
        except ValueError:
            sys.exit("Invalid date format. Please use YYYY-MM-DD.")

    def convertNumberToWords(self):
        days_lived = (self.today - self.dob).days
        minutes_lived = days_lived * 24 * 60
        minwords = p.number_to_words(minutes_lived, andword="") + " minutes"
        minwords = minwords.capitalize()
        return minwords


def main():
    calc = CalculateDate()  # or change __init__ to def __init__(self, dob=None):
    calc.getDob()  # prompts and sets calc.dob
    minutes = calc.convertNumberToWords()
    print(minutes)


if __name__ == "__main__":
    main()
# A happy year is a year with only distinct digits (no duplicates)
# create a function that takes an integer year and returns the next happy year
def next_happy_year(year):
    while True:
        year += 1
        if len(set(str(year))) == len(str(year)):
            return year

current_year = int(input("Enter the current year: "))
print(next_happy_year(current_year))

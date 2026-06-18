#problem 1
def average_marks(mark1, mark2, mark3):
    avg = (mark1 + mark2 + mark3) / 3
    return round(avg, 1)

# Example
print(average_marks(80, 90, 85))
#problem 2
PASS_MARK = 35
DISTINCTION_MARK = 75

def classify_result(average):
    if average < PASS_MARK:
        return "FAIL"
    elif average >= DISTINCTION_MARK:
        return "DISTINCTION"
    else:
        return "PASS"
print(classify_result(84.3))  # DISTINCTION
print(classify_result(55.0))  # PASS
print(classify_result(31.0))  # FAIL
        #problem 3
def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

print(letter_grade(84.3))  # B
print(letter_grade(55.0))  # F
print(letter_grade(92.0))  # A

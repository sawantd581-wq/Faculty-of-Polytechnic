#problem 1
def get_non_empty_string(prompt):
    while True:
        text = input(prompt)
        if text != "":
            return text
        else:
            print("Can't be empty — try again.")

name = get_non_empty_string("Enter your name: ")
print("Hello,", name)

#problem 2
def ask_mark(prompt):
    while True:
        text = input(prompt)

        if not text.isdigit():
            print("Please enter a whole number.")
            continue

        mark = int(text)

        if mark < 0 or mark > 100:
            print("Mark must be between 0 and 100.")
            continue

        return mark


mark1 = ask_mark("Mark 1 (0-100): ")
print(mark1)


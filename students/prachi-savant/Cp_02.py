#problem 1
def ask_text(prompt):
    while True:
        text = input(prompt)

        if text == "":
            print("Can't be empty — try again.")
        else:
            return text


subject = ask_text("Subject name: ")
print(subject)

#problem 2
def ask_mark(prompt):
    while True:
        text = input(prompt)

        if not text.isdigit():
            print("Please enter a whole number.")
        else:
            mark = int(text)

            if 0 <= mark <= 100:
                return mark
            else:
                print("Mark must be between 0 and 100.")
m1 = ask_mark("Mark 1 (0-100): ")
print(m1)

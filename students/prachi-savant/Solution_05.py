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

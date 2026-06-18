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

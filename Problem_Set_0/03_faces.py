def convert():
    user_input = input("Type: Hello :) Goodbye :(\n")
    user_input = user_input.replace(":)", "🙂")
    user_input = user_input.replace(":(", "🙁")
    print(user_input)


convert()

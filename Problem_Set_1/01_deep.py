user_answer = input(
    "What is the Great Question of Life, the Universe, and Everything?\nType: 42, Forty Two, forty-two or 50\n"
    ).strip().lower()

if user_answer == "42":
    print("Yes")
elif user_answer == "forty-two":
    print("Yes")
elif user_answer == "forty two":
    print("Yes")
else:
    print("No")

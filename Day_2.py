from collections import Counter

with open("Day_2.txt") as f:
    passwords = f.read().splitlines()

password_dict = {}
total_correct = 0
proper_passwords_correct = 0

# password = passwords[0]
for password in passwords:
    # print(password)
    # print(password.split(" "))
    repeats, letter, phrase = password.split(" ")
    letter = letter[0]
    # print(letter)
    # print(repeats)
    # print(phrase)
    # print(repeats.split("-"))
    start, stop = repeats.split("-")
    password_dict[phrase] = int(start), int(stop), letter
    # print(range(int(start), int(stop)))
    counter_object = Counter(phrase)
    # print(counter_object)
    if counter_object[letter] in range(int(start), int(stop) + 1):
        total_correct += 1

print(f"Step 1 valid passwords {total_correct}")

for password in passwords:
    repeats, letter, phrase = password.split(" ")
    letter = letter[0]
    start, stop = repeats.split("-")
    start, stop = int(start), int(stop)
    start -= 1
    stop -= 1
    first_letter = phrase[start]
    second_letter = phrase[stop]
    if first_letter == letter or second_letter == letter:
        if first_letter != second_letter:
            proper_passwords_correct += 1

print(f"Step 2 valid passwords {proper_passwords_correct}")

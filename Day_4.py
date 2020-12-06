import re

with open("Day_4.txt") as f:
    passports = [(x.strip()) for x in f.read().split("\n\n")]
    passports = [passport.replace("\n", " ") for passport in passports]

step1_valid_passports = 0

# INPUT_FILE_PATH = Path('..', 'inputs', '4.txt')

FIELDS_WITHOUT_CID = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
CID = 'cid'
ALL_FIELDS = FIELDS_WITHOUT_CID + (CID,)

print(passports[0])
for passport in passports:
    temp_list = []
    for elem in FIELDS_WITHOUT_CID:
        temp_list.append(elem in passport)
    if all(temp_list):
        step1_valid_passports += 1
print(step1_valid_passports)
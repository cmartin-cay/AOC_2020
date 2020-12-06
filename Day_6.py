with open("Day_6.txt") as f:
    responses = [(x.strip()) for x in f.read().split("\n\n")]
    responses = [response.replace("\n", "") for response in responses]

resp_list = []
part_2_resp_list = []
for resp in responses:
    summary = set(resp)
    resp_list.append(len(summary))

# print(resp_list)
# print(sum(resp_list))

with open("Day_6.txt") as f:
    responses = [(x.strip()) for x in f.read().split("\n\n")]

for response in responses:
    all_answers = response.split("\n")
    # Base case - only 1 person in group. Every answer will count
    # print(all_answers)
    if len(all_answers) == 1:
        part_2_resp_list.append(len(all_answers[0]))
    # Next Part - identify all the responses which were given
    # And then identify if each one is in each answer
    else:
        boxes_ticked = set("".join(all_answers))
        tmp_list = []
        for elem in boxes_ticked:
            tmp_count = []
            for answer in all_answers:
                tmp_count.append(elem in answer)
            if all(tmp_count):
                tmp_list.append(True)
        part_2_resp_list.append(len(tmp_list))



print(sum(part_2_resp_list))
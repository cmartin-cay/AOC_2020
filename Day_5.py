with open("Day_5.txt") as f:
    tickets = f.read().splitlines()

sample_input = "BBFFBBFRLL"
sample_row = sample_input[:7]
sample_seat = sample_input[7:]

rows = list(range(128))
seats = list(range(8))
all_seat_codes = []


def find_seat_row(code, rows):
    if len(rows) == 1:
        return rows[0]

    midpoint = int(len(rows) / 2)

    if code[0] == "F":
        return find_seat_row(code=code[1:], rows=rows[:midpoint])
    elif code[0] == "B":
        return find_seat_row(code=code[1:], rows=rows[midpoint:])


def find_seat_number(code, rows):
    if len(rows) == 1:
        return rows[0]

    midpoint = int(len(rows) / 2)

    if code[0] == "L":
        return find_seat_number(code=code[1:], rows=rows[:midpoint])
    elif code[0] == "R":
        return find_seat_number(code=code[1:], rows=rows[midpoint:])


# actual_seat.append(find_seat_row(sample_row, rows))
# actual_seat.append(find_seat_number(sample_seat, seats))
# print(actual_seat)
# print(f"The result is {actual_seat}. The code is {actual_seat[0] * 8 + actual_seat[1]}")

for ticket in tickets:
    actual_seat = []
    ticket_row = ticket[:7]
    ticket_seat = ticket[7:]
    actual_seat.append(find_seat_row(ticket_row, rows))
    actual_seat.append(find_seat_number(ticket_seat, seats))
    all_seat_codes.append(actual_seat[0] * 8 + actual_seat[1])

# print(max(all_seat_codes))

all_seat_codes = sorted(all_seat_codes)
starting_seat = 71

for seat in range(len(all_seat_codes)-1):
    if all_seat_codes[seat+1] == all_seat_codes[seat] + 1:
        pass
    else:
        print(seat)

print(all_seat_codes[490:500])

all_seen_seats = set(all_seat_codes)
all_actual_seats = set(range(min(all_seat_codes), max(all_seen_seats)))
print(all_actual_seats - all_seen_seats)
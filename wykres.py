import math

WIDTH = 64
HEIGHT = 17
AXIS = HEIGHT // 2

rows = [[" "] * WIDTH for _ in range(HEIGHT)]

for col in range(WIDTH):
    if rows[AXIS][col] == " ":
        rows[AXIS][col] = "-"
    x = 2 * math.pi * col / (WIDTH - 1)
    row = round((1 - math.sin(x)) / 2 * (HEIGHT - 1))
    rows[row][col] = "*"

labels = {0: " 1", AXIS: " 0", HEIGHT - 1: "-1"}
print("y = sin(x)")
print()
for index, row in enumerate(rows):
    print(f"{labels.get(index, '  ')} |{''.join(row)}")
print("     0" + " " * 24 + "pi" + " " * 25 + "2pi")

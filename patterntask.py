def draw_hexagon_pattern(rows, cols):
    for row in range(rows):
        for i in range(5):  # 5 lines per hexagon
            line = ""
            for col in range(cols):
                if col % 2 == 1:
                    line += " " * (1 if i in [0, 2, 4] else 0)  # Adjust spacing for alternating rows
                line += hexagon_line(i)
            print(line)
        if row < rows - 1:
            print()

def hexagon_line(i):
    if i == 0:
        return "  ___ "
    elif i == 1:
        return " /   \\"
    elif i == 2:
        return "/     \\"
    elif i == 3:
        return "\\     /"
    elif i == 4:
        return " \\___/"

# Example usage:
print("Pattern for 4 rows and 7 columns:")
draw_hexagon_pattern(4, 7)

print("\nPattern for 3 rows and 5 columns:")
draw_hexagon_pattern(3, 5)

dots, folds = open("../../input/day_13_data.txt").read().split("\n\n")
dots = [(int(dot.split(",")[0]), int(dot.split(",")[1])) for dot in dots.splitlines()]
folds = [(axis[-1], int(val)) for fold in folds.splitlines() for axis, val in [fold.split("=")]]

for axis, fold_line in folds:
    for i, (x, y) in enumerate(dots):
        if axis == "x" and x > fold_line:
            dots[i] = (2 * fold_line - x, y)
        if axis == "y" and y > fold_line:
            dots[i] = (x, 2 * fold_line - y)

print("\n".join("".join("█" if (x, y) in dots else " " for x in range(40)) for y in range(6)))
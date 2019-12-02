import sys

with open(sys.argv[1], 'r') as fp:
    masses = [int(l) for l in fp.readlines()]

part1 = sum(m // 3 - 2 for m in masses)

part2 = 0
for m in masses:
    while (m > 0):
        m = m//3 - 2
        if m > 0: part2 += m

print("Part1:", part1)
print("Part2:",part2)
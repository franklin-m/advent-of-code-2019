opcodes = [
        1, 0, 0, 3, 1, 1, 2, 3, 1, 3, 4, 3, 1, 5, 0, 3, 2, 1, 13, 19, 1, 9, 19, 23, 2, 13, 23, 27, 2, 27, 13, 31, 2, 31,
        10, 35, 1, 6, 35, 39, 1, 5, 39, 43, 1, 10, 43, 47, 1, 5, 47, 51, 1, 13, 51, 55, 2, 55, 9, 59, 1, 6, 59, 63, 1,
        13, 63, 67, 1, 6, 67, 71, 1, 71, 10, 75, 2, 13, 75, 79, 1, 5, 79, 83, 2, 83, 6, 87, 1, 6, 87, 91, 1, 91, 13, 95,
        1, 95, 13, 99, 2, 99, 13, 103, 1, 103, 5, 107, 2, 107, 10, 111, 1, 5, 111, 115, 1, 2, 115, 119, 1, 119, 6, 0,
        99, 2, 0, 14, 0
    ]


def run_program(noun, verb):
    opc = opcodes[:]
    opc[1] = noun
    opc[2] = verb
    for i in range(0, len(opc), 4):
        if opc[i] == 1:
            opc[opc[i + 3]] = opc[opc[i+1]] + opc[opc[i+2]]
        elif opc[i] == 2:
            opc[opc[i + 3]] = opc[opc[i+1]] * opc[opc[i+2]]
        elif opc[i] == 99:
            break
    return opc[0]


print(f"Part one answer: {run_program(12,2)}")


for n in range(len(opcodes)):
    for v in range(len(opcodes)):
        if run_program(n, v) == 19690720:
            print(f"Part two answer: {n}, {v}, {100*n+v}")

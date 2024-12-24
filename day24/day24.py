def read_in():
    with open("input.txt", "r") as input_file:
        lines = tuple(a.split("\n") for a in input_file.read().split('\n\n'))
    return lines


gates = {"AND": lambda x, y: x & y, "OR": lambda x, y: x | y, "XOR": lambda x, y: x ^ y}


def evaluate(state, z):
    if state[z] not in (1, 0):
        v1, gate, v2 = state[z]
        if state[v1] not in (1, 0):
            evaluate(state, v1)
        if state[v2] not in (1, 0):
            evaluate(state, v2)
        state[z] = gates[gate](state[v1], state[v2])


def p1(values):
    state = ({a: (1 if b == "1" else 0) for a, b in [c.split(": ") for c in values[0]]} |
             {b: tuple(a.split(" ")) for a, b in [c.split(" -> ") for c in values[1]]})
    all_z = tuple(sorted(filter(lambda x: x[0] == "z", state.keys()), reverse=True))
    bin_result = "0b"
    for z in all_z:
        evaluate(state, z)
        bin_result = bin_result + str(state[z])
    return int(bin_result, 2)


def p2(values):
    state = ({a: (1 if b == "1" else 0) for a, b in [c.split(": ") for c in values[0]]} |
             {b: tuple(a.split(" ")) for a, b in [c.split(" -> ") for c in values[1]]})
    xyz = {}
    for v in ("x", "y", "z"):
        all_v = tuple(sorted(filter(lambda x: x[0] == v, state.keys()), reverse=True))
        bin_result = "0b"
        for a in all_v:
            evaluate(state, a)
            bin_result = bin_result + str(state[a])
        xyz[v] = int(bin_result, 2)
    expected = bin(xyz["x"] + xyz["y"])
    for a in xyz:
        print(a, "" if a == "z" else " ", bin(xyz[a]))
    print("  ", expected)

    return 0


# def p2(values):
#     initial_state = {a: (1 if b == "1" else 0) for a, b in [c.split(": ") for c in values[0]]}
#     initial_gates = {b: tuple(a.split(" ")) for a, b in [c.split(" -> ") for c in values[1]]}
#     list_gates = list(initial_gates.keys())
#     last = None
#     for g1 in range(len(list_gates)):
#         for g2 in range(g1+1, len(list_gates)):
#             print(g1, g2, list_gates[g1], list_gates[g2])
#             this_state = initial_state.copy()
#             this_gates = initial_gates.copy()
#             print(this_gates)
#             this_gates[list_gates[g1]], this_gates[list_gates[g2]] = this_gates[list_gates[g2]], this_gates[list_gates[g1]]
#             state = this_state | this_gates
#             xyz = {}
#             for v in ("x", "y", "z"):
#                 all_v = tuple(sorted(filter(lambda x: x[0] == v, state.keys()), reverse=True))
#                 bin_result = "0b"
#                 for a in all_v:
#                     evaluate(state, a)
#                     bin_result = bin_result + str(state[a])
#                 xyz[v] = int(bin_result, 2)
#             expected = bin(xyz["x"] + xyz["y"])
#             for a in xyz:
#                 print(a, "" if a == "z" else " ", bin(xyz[a]))
#             print("  ", expected)
#             last = expected
#
#     return 0

def main():
    values = read_in()
    # print(values)
    print(p1(values))
    print(p2(values))


if __name__ == '__main__':
    main()


# z18
# cjb OR kqr -> z18
# y18 AND x18 -> cjb    gdw AND ffh -> kqr
# 0        1           x18 XOR y18 -> gdw      vvt OR bct -> ffh
#                                             y17 AND x17       qgt AND dtt
#                                                             pvd OR ctn            x17 XOR y17
#                                                             y16ANDx16   mdd AND bqc
#
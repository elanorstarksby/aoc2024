import operator


def read_in():
    with open("input.txt", "r") as input_file:
        lines = input_file.read().split('\n')
    return lines


def parse(values):
    state = {}
    for line in values:
        if line != "":
            l, v = line.split(": ")
            l = l[-1]
            if l == "m":
                l = "p"
            if "," not in v:
                v = int(v)
            else:
                v = [int(a) for a in v.split(",")]
            state[l] = v
    return state


def compute(state):
    program_output = []
    i = 0
    while i < len(state["p"]):
        instruction = state["p"][i]
        op = state["p"][i + 1]
        map_operand = {0: 0, 1: 1, 2: 2, 3: 3, 4: state["A"], 5: state["B"], 6: state["C"]}
        if instruction == 0:  # bst A = A // (2**combo)
            state["A"] = state["A"] // (2 ** map_operand[op])
        if instruction == 1:  # bxl B = B XOR op
            state["B"] = state["B"] ^ op
        if instruction == 2:  # bst B = combo % 8
            state["B"] = map_operand[op] % 8
        if instruction == 3:  # jnz A op
            i = i + 2 if state["A"] == 0 else op
            continue
        if instruction == 4:  # bxc B = B XOR C
            state["B"] = state["B"] ^ state["C"]
        if instruction == 5:  # out output combo % 8
            program_output.append(str(map_operand[op] % 8))
        if instruction == 6:  # bdv B = A // (2**combo)
            state["B"] = state["A"] // (2 ** map_operand[op])
        if instruction == 7:  # cdv C = A // (2**combo)
            state["C"] = state["A"] // (2 ** map_operand[op])
        i += 2
    return ",".join(program_output)


def p1(values):
    state = parse(values)
    print(state)
    return compute(state)


def p2_old(values):
    state = parse(values)
    print(state)
    original_program = ",".join([str(a) for a in state["p"]])
    right_len = []
    for i in range(35200000000000, 281390000000000, 1000000000):
        state["A"] = i
        output_program = compute(state)
        if output_program == original_program:
            break
        if len(output_program) == len(original_program):
            right_len.append(i)
        # print(i, len(output_program), len(original_program))
        i *= 10
    return right_len[0], right_len[-1]


def program(A):
    # 2,4 B = A % 8
    # 1,3 B = B XOR 3
    # 7,5 C = A // (2**B)
    # 4,2 B = B XOR C
    # 0,3 A = A // (2**3)
    # 1,5 B = B XOR 5
    # 5,5 output B % 8
    # 3,0 jump to 0 if A != 0
    B = 0
    C = 0
    out = []
    while A != 0:
        B = (A % 8) ^ 3
        B = B ^ (A // (2 ** B))
        A = A // 8
        B = B ^ 5
        out.append(B % 8)

    return out


def calculate(build_a, position, goal):
    for j in range(0, 8):
        a = build_a + (j * (8 ** position))
        r = program(a)
        # print(r, position, a)
        if len(r) == 16 and r[position] == goal[position]:
            if position == 0:
                return a
            temp_a = calculate(a, position - 1, goal)
            if temp_a:
                return temp_a


def main():
    values = read_in()
    print(values)
    print(p1(values))
    goal = [2, 4, 1, 3, 7, 5, 4, 2, 0, 3, 1, 5, 5, 5, 3, 0]
    print(calculate(0, 15, goal))


if __name__ == '__main__':
    main()

# 236577765809773
# 216133634427271

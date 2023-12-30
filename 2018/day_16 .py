with open("2018/data/day_16.txt") as f:
    samples,test = f.read().split("\n\n\n\n")
samples = samples.replace(",", "").replace("Before: [", "").replace("After:  [", "").replace("]", "")
samples = [[[int(el) for el in val.split()] for val in s.split("\n")] for s in samples.split("\n\n")]
test = [[int(el) for el in reg.split()] for reg in test.strip().split("\n")]

opcodes = [
    lambda a,b,c,reg:[reg[a]+reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]+b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]*reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]*b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]&reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]&b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]|reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]|b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[a if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[a>reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]>b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]>reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[a==reg[b] if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]==b if k==c else r for k,r in enumerate(reg)],
    lambda a,b,c,reg:[reg[a]==reg[b] if k==c else r for k,r in enumerate(reg)],
    ]

def part1():
    return sum(sum(opcode(a,b,c,before) == after for opcode in opcodes)>=3 for before,(_,a,b,c),after in samples)
    

def part2():
    possible_opcodes = [[fun for fun in opcodes] for _ in opcodes]
    for before,(op,a,b,c),after in samples:
        for opcode in possible_opcodes[op]:
            if not opcode(a,b,c,before) == after:
                possible_opcodes[op].remove(opcode)

    opcodes_num = [None for _ in range(16)]
    while any(op is None for op in opcodes_num):
        for num, opcode_list in enumerate(possible_opcodes):
            if len(opcode_list)==1:
                [opcodes_num[num]] = opcode_list
                continue
            for possible in opcode_list:
                if possible in opcodes_num:
                    possible_opcodes[num].remove(possible)

    registers = [0,0,0,0]
    for op,a,b,c in test:
        registers = opcodes_num[op](a,b,c,registers)
    return registers[0]

if __name__ == "__main__":
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
    
"""
    When "noop" is encountered, nothing happens except the cycle iterates.
    When "addx" is encountered the first time, EXECUTE is set to true and the
    instruction gets duplicated and inserted as the next instruction.
    That way, the cycle iterates twice per "addx" instruction, but only gets
    executed when the second, duplicated instruction is encountered. At that
    point, the value is added to X and the EXECUTE flag is reset to False.
"""

FILENAME = "inputs/day10.txt"

def main():
    insts = [line.strip() for line in open(FILENAME)]
    signal_strengths = {}
    x = 1
    execute = False

    for i, instr in enumerate(insts):
        cycle = i + 1                           # cycle is 1-indexed
        signal_strengths[cycle] = cycle * x     # this should come BEFORE execution
        
        if instr.split()[0] == "addx":
            if execute: 
                x += int(instr.split()[1])
                execute = False
                
            else:
                insts.insert(cycle, instr)
                execute = True

    print(sum([signal_strengths[20], signal_strengths[60],
        signal_strengths[100], signal_strengths[140],
        signal_strengths[180], signal_strengths[220]]))


if __name__ == "__main__":
    main()
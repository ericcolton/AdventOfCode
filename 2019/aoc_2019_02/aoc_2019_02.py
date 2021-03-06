#!/usr/bin/env python3

"""
Advent of Code Day 2: 1202 Program Alarm

https://adventofcode.com/2019/day/2
"""

OP_CODE_ADD = 1
OP_CODE_MULTIPLY = 2
OP_CODE_END = 99

class ComputerProcessor():
    def __init__(self, data):
        self.data = data

    def run_program(self):

        program_ptr = 0
        while True:
            op = self.data[program_ptr]
            if self.data[program_ptr] == OP_CODE_END:
                break
            
            if program_ptr > len(self.data) - 4:
                raise "Unexpected EOF"

            (in_1, in_2, dest) = self.data[program_ptr+1:program_ptr+4]
            (data_1, data_2) = (self.data[in_1], self.data[in_2])

            if op == OP_CODE_ADD:
                self.data[dest] = data_1 + data_2
            elif op == OP_CODE_MULTIPLY:
                self.data[dest] = data_1 * data_2
            else:
                raise f"Unexpected opcode: {op}"
            
            program_ptr += 4

        return self.data[0]

def solve_part_1(data):
    data[1] = 12
    data[2] = 2
    processor = ComputerProcessor(data)
    return processor.run_program()
    
def solve_part_2(raw_input):
    for i in range(100):
        for j in range(100):
            data = raw_input.copy()
            data[1] = i
            data[2] = j
            processor = ComputerProcessor(data)
            if processor.run_program() == 19690720:
                return 100 * i + j
    raise "Exhausted Solution Space"
    
def parse_input_file(input_filepath):
    with open(input_filepath, 'r') as file:
        line = file.readline().rstrip()
        return [int(i) for i in line.split(',')]

if __name__ == "__main__":
    input_filename = __file__.rstrip('.py') + '_input.txt'
    input_data = parse_input_file(input_filename)
    part_1 = solve_part_1(input_data.copy())
    print (f"Part 1 solution: {part_1}")
    assert part_1 == 11590668
    part_2 = solve_part_2(input_data.copy())
    print (f"Part 2 solution: {part_2}")
    assert part_2 == 2254

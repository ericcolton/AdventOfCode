import pytest
import sys, os

sys.path.insert(0, '2019')

from aoc_2019_05 import ComputerProcessor, parse_input_line

def test_equal_to_position():
    program = parse_input_line("3,9,8,9,10,9,4,9,99,-1,8")
    cp = ComputerProcessor(program)
    cp.input = 8
    cp.run_program()
    assert cp.output == [1]
    cp.input = 7
    cp.run_program()
    assert cp.output == [0]

def test_less_than_position_mode():
    program = parse_input_line("3,9,7,9,10,9,4,9,99,-1,8")
    cp = ComputerProcessor(program)
    cp.input = 4
    cp.run_program()
    assert cp.output == [1]
    cp.input = 9
    cp.run_program()
    assert cp.output == [0]

def test_equal_to_immediate_mode():
    program = parse_input_line("3,3,1108,-1,8,3,4,3,99")
    cp = ComputerProcessor(program)
    cp.input = 8
    cp.run_program()
    assert cp.output == [1]
    cp.input = 2
    cp.run_program()
    assert cp.output == [0]    

def test_less_than_immediate_mode():
    program = parse_input_line("3,3,1107,-1,8,3,4,3,99")
    cp = ComputerProcessor(program)
    cp.input = 6
    cp.run_program()
    assert cp.output == [1]
    cp.input = 12
    cp.run_program()
    assert cp.output == [0]

def test_jump_position_mode():
    program = parse_input_line("3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9")
    cp = ComputerProcessor(program)
    cp.input = 0
    cp.run_program()
    assert cp.output == [0]
    cp.input = 10
    cp.run_program()
    assert cp.output == [1]

def test_jump_immediate_mode():
    program = parse_input_line("3,3,1105,-1,9,1101,0,0,12,4,12,99,1")
    cp = ComputerProcessor(program)
    cp.input = 0
    cp.run_program()
    assert cp.output == [0]
    cp.input = 10
    cp.run_program()
    assert cp.output == [1]

def test_complex_jump_logic():
    program = parse_input_line("3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99")
    cp = ComputerProcessor(program)
    cp.input = 7
    cp.run_program()
    assert cp.output == [999]
    cp.input = 8
    cp.run_program()
    assert cp.output == [1000]
    cp.input = 9
    cp.run_program()
    assert cp.output == [1001]

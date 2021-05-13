import re

import argparse

instuction = 0
pointer = 0
memory = [0]
max_value = 255
stack = []
ascii_mode = True

def right():
    global pointer
    pointer += 1
    if pointer == len(memory):
        memory.append(0)
def left():
    global pointer
    pointer -= 1
    if pointer < 0:
        print("pointer went to a negative number")
        os._exit(0) 
def add():
    global pointer
    global max_value
    memory[pointer] += 1
    if memory[pointer] > max_value:
        memory[pointer] = 0
def sub():
    global pointer
    global max_value
    memory[pointer] -= 1
    if memory[pointer] < 0:
        memory[pointer] = max_value
def open_loop():
    global instuction
    global stack
    stack.append(instuction)
def close_loop():
    global instuction
    global stack
    if memory[pointer] == 0:
        stack = stack[:-1]
    else:
        instuction = stack[len(stack) - 1]
def get_input():
    global memory
    global pointer
    if ascii_mode:
        memory[pointer] = ord(input("Program is asking for input: "))
    else:
        memory[pointer] = int(input("Program is asking for input: "))
def output():
    global memory
    global pointer
    global ascii_mode
    if ascii_mode:
        print(chr(memory[pointer]), end ="")
    else:
        print(memory[pointer], end ="")
    
def suslang(input_arr):
    global instuction
    while instuction < len(input_arr):
        current = input_arr[instuction]
        if current == 'crewmate':
            right()
        elif current == 'imposter':
            left()
        elif current == 'among':
            open_loop()
        elif current == 'us':
            close_loop()
        elif current == 'sus':
            add()
        elif current == 'sussy':
            sub()
        elif current == 'vote':
            get_input()
        elif current == 'eject':
            output()
        instuction += 1
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Sussy imposter :flushed: (v 0.1)")
    parser.add_argument("file", help="The input file")
    args = parser.parse_args()
    
    with open(args.file, "r") as f:
        data = f.read()
    input_arr = re.split(' |\n', data)
    suslang(input_arr)

input_string="++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>."
output = ""
for char in input_string:
    if char == "+":
        output += "sus "
    elif char == "-":
        output += "sussy "
    elif char == "[":
        output += "among "
    elif char == "]":
        output += "us "
    elif char == ">":
        output += "crewmate "
    elif char == "<":
        output += "imposter "
    elif char == ".":
        output += "eject "
    elif char == ",":
        output += "vote "
print(output)

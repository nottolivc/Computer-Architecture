import sys

# Operation Codes
# OP Codes
PRINT_HELLO_WORLD = 1   #0b00000001 
HALT              = 2   #0b00000010
PRINT_NUM         = 3   #0b00000011
SAVE_REG          = 4
PRINT_REG         = 5
ADD               = 6

# ADD takes TWO registers, adds their values 
# and stores the result in the first register given


# program that adds two numbers together
# return
memory = [
    SAVE_REG,
    200, #value 2
    1,  # register 1
    SAVE_REG,
    2121, # value 2
    2, # register 2
    ADD,
    1, # register 1
    2, # register 2
    PRINT_REG,
    1,
    HALT
]

registers = [0] * 8

running = True
pc = 0

while running:
    # Read line by line from memory
    instruction = memory[pc]

    if instruction == PRINT_HELLO_WORLD:
        # print Hello world 
        # move the PC up 1 to the next instruction
        print("Hello World")
        pc += 1

    elif instruction ==  PRINT_NUM:
        # Print the number in the NEXT memory slot
        num = memory[pc + 1]
        print(num)
        pc += 2

    elif instruction == SAVE_REG:
        # Save some value to some register
        # First number after instruction will be the Value to store
        # second number after instruction will be register
        num = memory[pc + 1]
        reg_location = memory[pc + 2]
        registers[reg_location] = num
        pc += 3
    
    elif instruction == PRINT_REG:
        reg_location = memory[pc + 1]
        print(registers[reg_location])
        pc += 2

    elif instruction == ADD:
        # ADD takes TWO registers, adds their values 
        # and stores the result in the first register given
        # Get register 1
        # get register 2
        # Add the values of both registers together
        # Store in register 1
        reg_1 = memory[pc + 1]
        reg_2 = memory[pc + 2]
        registers[reg_1] += registers[reg_2]
        pc += 3

    elif instruction == HALT:
        running = False
        pc += 1

    else:
        print(f"Unknown instruction {instruction}")
        sys.exit(1)
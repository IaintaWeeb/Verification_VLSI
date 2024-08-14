
# 1  2  3  4  5  6  7  8  9  10 11 12 13 Cn
# M  A0 B0 A1 B1 A2 B2 A3 B3 S0 S1 S2 S3 83
def or_gate(a,b,c,num_clauses):
    num_clauses += 3
    print(str(c) + " -" + str(a) + " 0")
    print(str(c) + " -" + str(b) + " 0")
    print("-" + str(c) + " " + str(a) + " " + str(b) + " 0")
    return num_clauses

def not_gate(a,b,num_clauses):
    num_clauses += 2
    print("-" + str(a) + " -" + str(b) + " 0")
    print(str(a) + " " + str(b) + " 0")
    return num_clauses

def nand_gate_two_input(a,b,c,num_clauses):
    num_clauses += 3
    print(str(c) + " " + str(a) + " 0")
    print(str(c) + " " + str(b) + " 0")
    print("-" + str(a) + " -" + str(b) + " -"+ str(c) + " 0")
    return num_clauses

def nand_gate_four_input(a,b,c,d,e,num_clauses):
    num_clauses += 5
    print("-" + str(e) + " " + str(a) + " 0")
    print("-" + str(e) + " " + str(b) + " 0")
    print("-" + str(e) + " " + str(c) + " 0")
    print("-" + str(e) + " " + str(d) + " 0")
    print(str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + str(e) + " 0")
    return num_clauses

def nand_gate_five_input(a,b,c,d,e,f,num_clauses):
    num_clauses += 6
    print("-" + str(e) + " " + str(a) + " 0")
    print("-" + str(e) + " " + str(b) + " 0")
    print("-" + str(e) + " " + str(c) + " 0")
    print("-" + str(e) + " " + str(d) + " 0")
    print("-" + str(e) + " " + str(e) + " 0")
    print(str(a) + " " + str(b) + " "+ str(c) + " " + str(d) + " "+ str(e) + " " + str(f) + " 0")
    return num_clauses

def nor_gate_two_input(a,b,c,num_clauses):
    num_clauses += 3
    print("-" + str(c) + " -" + str(a) + " 0")
    print("-" + str(c) + " -" + str(b) + " 0")
    print(str(c) + " " + str(a) + " " + str(b) + " 0")
    return num_clauses

def nor_gate_three_input(a,b,c,d,num_clauses):
    num_clauses += 4
    print("-" + str(d) + " -" + str(a) + " 0")
    print("-" + str(d) + " -" + str(b) + " 0")
    print("-" + str(d) + " -" + str(c) + " 0")
    print(str(d) + " " + str(a) + " " + str(b) + " " + str(c) + " 0")
    return num_clauses

def nor_gate_four_input(a,b,c,d,e,num_clauses):
    num_clauses += 5
    print("-" + str(e) + " -" + str(a) + " 0")
    print("-" + str(e) + " -" + str(b) + " 0")
    print("-" + str(e) + " -" + str(c) + " 0")
    print("-" + str(e) + " -" + str(d) + " 0")
    print(str(e) + " " + str(a) + " " + str(b) + " " + str(c) + " " + str(d) + " " + " 0")
    return num_clauses


def xor_gate(a,b,c,num_clauses):
    num_clauses += 4
    print("-" + str(c) + " -" + str(a) + " -" + str(b) + " 0")
    print("-" + str(c) + " " + str(a) + " " + str(b) + " 0")
    print(str(c) + " -" + str(a) + " " + str(b) + " 0")
    print(str(c) + " " + str(a) + " -" + str(b) + " 0")
    return num_clauses

def and_gate_one_input(a,b, num_clauses):
    num_clauses += 2
    print("-" + str(b) + " " + str(a) + " 0")
    print("-" + str(a) + " -" + str(a) + " " + str(b) + " 0")
    return num_clauses

def and_gate_two_input(a,b,c, num_clauses):
    num_clauses += 3
    print("-" + str(c) + " " + str(a) + " 0")
    print("-" + str(c) + " " + str(b) + " 0")
    print("-" + str(a) + " -" + str(b) + " " + str(c) + " 0")
    return num_clauses
    

def and_gate_three_inputs(a,b,c,d, num_clauses):
    num_clauses += 4
    print("-" + str(d) + " " + str(a) + " 0")
    print("-" + str(d) + " " + str(b) + " 0")
    print("-" + str(d) + " " + str(c) + " 0")
    print("-" + str(a) + " -" + str(b) + " -" + str(c) + " " + str(d) + " 0")
    return num_clauses

def and_gate_four_inputs(a,b,c,d,e, num_clauses):
    num_clauses += 5
    print("-" + str(e) + " " + str(a) + " 0")
    print("-" + str(e) + " " + str(b) + " 0")
    print("-" + str(e) + " " + str(c) + " 0")
    print("-" + str(e) + " " + str(d) + " 0")
    print("-" + str(a) + " -" + str(b) + " -" + str(c) + " -" + str(d) + " " + str(e) + " 0")
    return num_clauses

def and_gate_five_inputs(a,b,c,d,e,f, num_clauses):
    num_clauses += 6
    print("-" + str(f) + " " + str(a) + " 0")
    print("-" + str(f) + " " + str(b) + " 0")
    print("-" + str(f) + " " + str(c) + " 0")
    print("-" + str(f) + " " + str(d) + " 0")
    print("-" + str(f) + " " + str(e) + " 0")
    print("-" + str(a) + " -" + str(b) + " -" + str(c) + " -" + str(d) + " -" + str(e) + " "+ str(f) + " 0")
    return num_clauses

num_clauses = 0
# 1st level
num_clauses = not_gate(1,14,num_clauses)
num_clauses = not_gate(3,15,num_clauses)
num_clauses = not_gate(5,16,num_clauses)
num_clauses = not_gate(7,17,num_clauses)
num_clauses = not_gate(9,18,num_clauses)

# 2nd level
num_clauses = and_gate_one_input(2,20,num_clauses)
num_clauses = and_gate_two_input(3,10,21,num_clauses)
num_clauses = and_gate_two_input(11,15,22,num_clauses)
num_clauses = and_gate_three_inputs(15,12,2,24,num_clauses)
num_clauses = and_gate_three_inputs(2,3,13,25,num_clauses)

num_clauses = and_gate_one_input(4,27,num_clauses)
num_clauses = and_gate_two_input(5,10,28,num_clauses)
num_clauses = and_gate_two_input(11,16,29,num_clauses)
num_clauses = and_gate_three_inputs(16,12,4,31,num_clauses)
num_clauses = and_gate_three_inputs(4,13,5,32,num_clauses)

num_clauses = and_gate_one_input(6,34,num_clauses)
num_clauses = and_gate_two_input(7,10,35,num_clauses)
num_clauses = and_gate_two_input(11,17,36,num_clauses)
num_clauses = and_gate_three_inputs(17,12,6,38,num_clauses)
num_clauses = and_gate_three_inputs(6,13,7,39,num_clauses)

num_clauses = and_gate_one_input(8,41,num_clauses)
num_clauses = and_gate_two_input(9,10,42,num_clauses)
num_clauses = and_gate_two_input(11,18,43,num_clauses)
num_clauses = and_gate_three_inputs(18,12,8,45,num_clauses)
num_clauses = and_gate_three_inputs(8,13,9,46,num_clauses)

# 3rd level

num_clauses = nor_gate_three_input(20,21,22,23,num_clauses)
num_clauses = nor_gate_two_input(24,25,26,num_clauses)
num_clauses = nor_gate_three_input(27,28,29,30,num_clauses)
num_clauses = nor_gate_two_input(31,32,33,num_clauses)
num_clauses = nor_gate_three_input(34,35,36,37,num_clauses)
num_clauses = nor_gate_two_input(38,39,40,num_clauses)
num_clauses = nor_gate_three_input(41,42,43,44,num_clauses)
num_clauses = nor_gate_two_input(45,46,47,num_clauses)

# 4th level

num_clauses = nand_gate_two_input(83,14,19,num_clauses)
num_clauses = not_gate(23,48,num_clauses)
num_clauses = and_gate_two_input(14,23,49,num_clauses)
num_clauses = and_gate_three_inputs(14,26,83,50,num_clauses)
num_clauses = not_gate(30,51,num_clauses)
num_clauses = and_gate_two_input(14,30,52,num_clauses)
num_clauses = and_gate_three_inputs(14,23,33,53,num_clauses)
num_clauses = and_gate_four_inputs(14,83,26,33,54,num_clauses)
num_clauses = not_gate(37,55,num_clauses)
num_clauses = and_gate_two_input(14,37,56,num_clauses)
num_clauses = and_gate_three_inputs(14,30,40,57,num_clauses)
num_clauses = and_gate_four_inputs(14,23,33,40,58,num_clauses)
num_clauses = and_gate_five_inputs(14,83,26,33,40,59,num_clauses)
num_clauses = not_gate(44,60,num_clauses)
num_clauses = nand_gate_four_input(26,33,40,47,61,num_clauses)
num_clauses = nand_gate_five_input(83,26,33,40,47,62,num_clauses)
num_clauses = and_gate_four_inputs(23,33,40,47,63,num_clauses)
num_clauses = and_gate_three_inputs(30,40,47,64,num_clauses)
num_clauses = and_gate_two_input(37,47,65,num_clauses)
num_clauses = and_gate_one_input(44,66,num_clauses)

# 5th level
num_clauses = and_gate_two_input(48,26,67,num_clauses)
num_clauses = nor_gate_two_input(49,50,68,num_clauses)
num_clauses = and_gate_two_input(51,33,69,num_clauses)
num_clauses = nor_gate_three_input(52,53,54,70,num_clauses)
num_clauses = and_gate_two_input(55,40,71,num_clauses)
num_clauses = nor_gate_four_input(56,57,58,59,72,num_clauses)
num_clauses = and_gate_two_input(60,47,73,num_clauses)
num_clauses = nor_gate_four_input(63,64,65,66,74,num_clauses)

# 6th level
num_clauses = xor_gate(19,67,75,num_clauses)
num_clauses = xor_gate(68,69,76,num_clauses)
num_clauses = and_gate_four_inputs(75,76,78,79,77,num_clauses)
num_clauses = xor_gate(70,71,78,num_clauses)
num_clauses = xor_gate(72,73,79,num_clauses)
num_clauses = and_gate_two_input(62,74,81,num_clauses)

# bad circuit
print("82 0")
print("61 0")
num_clauses += 2
print("p cnf 82 " + str(num_clauses))
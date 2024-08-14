num_wires = 22
num_clauses = 0

def fanout(a,b):
    global num_clauses
    num_clauses += 2
    print(str(a) + " -" + str(b) + " 0")
    print(str(b) + " -" + str(a) + " 0")
    return 0

def and_gate(a,b,c):
    global num_clauses
    num_clauses += 3
    print("-" + str(c) + " " + str(a) + " 0")
    print("-" + str(c) + " " + str(b) + " 0")
    print("-" + str(a) + " -" + str(b) + " "+ str(c) + " 0")
    return 0

def or_gate(a,b,c):
    global num_clauses
    num_clauses += 3
    print(str(c) + " -" + str(a) + " 0")
    print(str(c) + " -" + str(b) + " 0")
    print("-" + str(c) + " " + str(a) + " " + str(b) + " 0")
    return 0

def not_gate(a,b):
    global num_clauses
    num_clauses += 2
    print("-" + str(a) + " -" + str(b) + " 0")
    print(str(a) + " " + str(b) + " 0")
    return 0

def nand_gate(a,b,c):
    global num_clauses
    num_clauses += 3
    print(str(c) + " " + str(a) + " 0")
    print(str(c) + " " + str(b) + " 0")
    print("-" + str(a) + " -" + str(b) + " -"+ str(c) + " 0")
    return 0

def nor_gate(a,b,c):
    global num_clauses
    num_clauses += 3
    print("-" + str(c) + " -" + str(a) + " 0")
    print("-" + str(c) + " -" + str(b) + " 0")
    print(str(c) + " " + str(a) + " " + str(b) + " 0")
    return 0

def xor_gate(a,b,c):
    global num_clauses
    num_clauses += 4
    print("-" + str(c) + " -" + str(a) + " -" + str(b) + " 0")
    print("-" + str(c) + " " + str(a) + " " + str(b) + " 0")
    print(str(c) + " -" + str(a) + " " + str(b) + " 0")
    print(str(c) + " " + str(a) + " -" + str(b) + " 0")
    return 0

def fix_gate(a,polarity):
    global num_clauses
    num_clauses += 1
    if(polarity == 1):
        print(str(a) + " 0")
    else:
        print("-" + str(a) + " 0")
    return 0


nand_gate(1,8,10)
nand_gate(3,6,11)
nand_gate(14,2,16)
nand_gate(15,7,19)
nand_gate(10,20,22)
nand_gate(19,21,23)
fanout(3,8)
fanout(3,9)
fanout(11,14)
fanout(11,15)
fanout(16,20)
fanout(16,21)
fix_gate(3,0)
fix_gate(23,1)
print("p cnf " + str(num_wires) + " " + str(num_clauses))
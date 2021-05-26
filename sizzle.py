import time
import random
import sys
import os

args = sys.argv[1:]
debug = False
delay = False

if os.path.isfile(args[0]):
    file = open(args[0],'r')
    program = file.read().splitlines()
    file.close()
    args = args[1:]

else:
    sys.stderr.write("Cannot find file")
    exit()

if "--debug" in args:
    debug = True
    print(program)
    args.remove("--debug")

if "--delay" in args:
    delay = True
    args.remove("--delay")

x = 0
y = 0
d = 0 # 0 right, 1 down, 2 left, 3 up
stack0 = []
stack1 = []

dimx = len(program[0])
dimy = len(program)

stringmode = False

while True:
    command = program[y][x]

    if command == '"':
        stringmode = not stringmode
    
    if stringmode:
        if command != '"':stack0+=[ord(command)]
    else:
        if command == "q": break
    
        if command == ">": d = 0
        if command == "v": d = 1
        if command == "<": d = 2
        if command == "^": d = 3
        if command == "?": d = random.randint(0,3)
        
        if command == "0": stack0 += [0]
        if command == "1": stack0 += [1]
        if command == "2": stack0 += [2]
        if command == "3": stack0 += [3]
        if command == "4": stack0 += [4]
        if command == "5": stack0 += [5]
        if command == "6": stack0 += [6]
        if command == "7": stack0 += [7]
        if command == "8": stack0 += [8]
        if command == "9": stack0 += [9]
    
        if command == ":": stack0 += [stack0[-1]]
    
        if command == "+":
            stack0 += [stack0[-2]+stack0[-1]]
            stack0 = stack0[:-3]+[stack0[-1]]
        if command == "-":
            stack0 += [stack0[-2]-stack0[-1]]
            stack0 = stack0[:-3]+[stack0[-1]]
        if command == "*":
            stack0 += [stack0[-2]*stack0[-1]]
            stack0 = stack0[:-3]+[stack0[-1]]
        if command == "/":
            stack0 += [stack0[-2]//stack0[-1]]
            stack0 = stack0[:-3]+[stack0[-1]]
        if command == "%":
            stack0 += [stack0[-2]%stack0[-1]]
            stack0 = stack0[:-3]+[stack0[-1]]
    
        if command == ".":
            print(chr(stack0[-1]),end="")
            stack0=stack0[:-1]

        if command == ",":
            stack0+=[ord(input())]
    
        if command == "p":
            print(stack0[-1],end="")
            stack0=stack0[:-1]

        if command == "x":
            stack0=stack0[:-1]

        if command == "\\":
            stack0,stack1=stack1,stack0

        if command == "{":
            if stack0[-1] == 0:
                d = (d-1)%4

        if command == "}":
            if stack0[-1] == 0:
                d = (d+1)%4

        if command == "[":
            if stack0[-1] == 0:
                d = (d-1)%4
            stack0=stack0[:-1]

        if command == "]":
            if stack0[-1] == 0:
                d = (d+1)%4
            stack0=stack0[:-1]

        if command == "s":
            mode = 3
            if stack0[-1]==ord("x"):
                mode = 1
                stack0=stack0[:-1]
            if stack0[-1]==ord("1"):
                mode = 2
                stack0=stack0[:-1]
            if stack0[-1]==ord("a"):
                mode == 3
                stack0=stack0[:-1]
            stack0.reverse()
            for a in stack0:
                if mode == 1:
                    print(hex(a),end=" ")
                if mode == 2:
                    print(a,end=" ")
                if mode == 3:
                    print(chr(a),end=" ")
            stack0.reverse()
        if command == "S":
            mode = 1
            stack_in = input("").split(" ")
            if stack_in[0]=="x":
                mode = 1
                stack_in=stack_in[1:]
            if stack_in[0]=="1":
                mode = 1
                stack_in=stack_in[1:]
            if stack_in[0]=="a":
                mode = 3
                stack_in=stack_in[1:]
            for i in stack_in:
                if mode == 1:
                    stack0+=[int(i,16)]
                if mode == 2:
                    stack0+=[i]
                if mode == 3:
                    stack0+=[ord(i)]
    if d == 0: x+=1
    if d == 1: y+=1
    if d == 2: x-=1
    if d == 3: y-=1

    if x == dimx: x = 0
    if y == dimy: y = 0
    if x < 0: x = dimx -1
    if y < 0: y = dimy -1
    
    if debug:
        print("debug: ",command,d,stringmode,stack0)
    if delay:
        time.sleep(.25)

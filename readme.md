# Sizzle

Two dimensional langauge, like [befunge](https://en.wikipedia.org/wiki/Esoteric_programming_language#Befunge), the programm is a grid of characters. Example:

```
0"!dlroW ,olleH">.v
                ^{<
                 q 

```

Which can be run with the interpreter, with the command, `python sizzle.py helloworld.szl`

It starts in the top left, travelling right.

`0` pushes a zero to the stack

`"!dlroW ,olleH"` enters string mode and pushes Hello, World! to the stack.



The

```
>.v
^{<
 q 
```
loops the pointer around, the "`.`" printing to the screen the "`{`" turns the pointer to the left when zero is on top of the stack, after turning left it runs over the `q` quitting the program.

If the pointer runs off the edge, it reappears like pacman or astroids.

## Commands:

|letter|description|
|------|-----------|
|>|point instruction pointer left|
|v|point instruction pointer down|
|<|point instruction pointer right|
|^|point instruction pointer up|
|?|random instruction pointer direction|
|.|pop stack and print as ascii|
|,|push input value as ascii to the stack|
|p|pop stack, print integer value|
|P|push integer value of input to stack|
|:|duplicate top of stack|
|+|pop top two values on stack, the put sum on top of stack|
|-|pop top two values on stack, the put difference on top of stack|
|\*|pop top two values on stack, the put product on top of stack|
|/|  pop top two values on stack, the put quotient on top of stack|
|%|pop top two values on stack, the put modulo/remainder on top of stack|
|"|string mode, push ascii values until next quote|
|0-9| push number to stack|
|{|peek stack, if 0 turn left, else ignore|
|}|peek stack, if 0 turn right, else ignore|
|x|remove top of stack|
| \\ |switch primary and secondary stacks|
|s|stack output, print stack with spaces separating values, top of stack changes mode, a ascii, x hex, 1 integer|
|S|stack input, push input stack with spaces separating values, top of stack changes mode, a ascii, x hex, 1 integer|

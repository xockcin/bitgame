# bitgame
Proof-of-concept for a game about bit operations

BitGame is a game that teaches the fundamentals of
how data is represented in a computer, as well as
how data can be manipulated using bitwise operators.

So far, all I've written is the game environment,
which is just a small window with eight buttons in
the center, representing the eight bits that make
up a byte. The user can switch any one bit on or
off by clicking it, and can also manipulate the byte
using one of the five unary operations: left-shift;
right-shift; increment; decrement; complement. Above
the byte are its values in decimal, hexadecimal and
ASCII.

The next step will be to figure out how to turn it
into a game. Once it works, I will want to reimplement
it in Javascript so it can more easily run in a browser.

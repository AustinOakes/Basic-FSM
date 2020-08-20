# Basic-FSM

## Description

A program created using Python which simulates a small finite state machine.

## How It Works

This program will use a function called StartState() to begin. StartState() will take a list of bits which will be processed by the FSM in order to see
if the last two bits were both 0's. Aside from the starting state there are three others, BitIsOne, BitIsZero, BitIsZeroAgain. Each state will look at
the first bit of the list and pass the rest of the bits (not including the first) into the corresponding state. If by the end of the list the current state
is BitIsZeroAgain, the program will output "Yes" indicating the list ended in two 0's. Otherwise the program will output "No".
<br>

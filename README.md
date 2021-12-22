# [Word up.](https://www.urbandictionary.com/define.php?term=word%20up)

Your job is to build an AI that can solve a word search given in the form of a two-dimensional array.

HINT!: re-read the lecture notes and code on containers (my code file on lists), where I give details on how to properly create a 2D array!

Your main program will receive std-input in the following form (see `stdio_tests`):
```
<number of cases>

<number of rows> <number of columns>
<data set>
<intended word to search>

<number of rows> <number of columns>
<data set>
<intended word to search>
```
The number of cases is how many array/word sets you should expect (two array/word sets are shown in the example above)

You will then print out the start and end positions for the word if it is found, and if the word is not found (does not exist in the array), you must report that to the user.

For example, if your main program receives the following standard input:
```
1

5 5
r g p g p
k p o f z
q d x s t
v y r y j
e w y t e
dog
```
...you should print out the following:
```
Searching for "dog" in matrix 0 yields:
Start pos: (2, 1) to End pos: (0, 3)

```

Similarly, if your program receives the following input:
```
1

5 5
r g p g p
k p o f z
q d x s t
v y r y j
e w y t e
cat
```
...you should print out the following:
```
Searching for "cat" in matrix 0 yields:
The pattern was not found.

```

## Reminders and hints
* Use a 2D list of a list of strings to keep the matrix, specifically: List[List[str]].
* The code for this is in lecture notes!
* 2D arrays in CompSci are indexed: `my_array[down][over]`
* Remember, we are unit testing your functions, so micro-manage how you implement them. 
* We give you the file, `word_up.py` to start with.

## Where to program?
- Program this at the Linux terminal, either via ssh/putty to the campus machines, a Linux VM, or Linux on your machine.
- I suggest having two terminals open, one with the code, the other where you run the code, or one plus your IDE of choice.

## How to program
- Write as many functions as you want.  However, you **must** define a
  function, `matrix_search()`, that accepts a 2D array and a word to search
  for, and returns the pair of coordinates in the matrix that corresponds to
  the start and end position of the word **as a tuple of tuples**, or `None` if
  the word is not found.
- Start with the main loop! Don't tackle the whole game first. Work from the outside in.
- Program in incremental chunks. Do NOT try to write the whole program and then debug it into submission. 
- Start early. Something always comes up!


 Encoding/decoding a phrase in morse and puting the respective letter in a binary tree

I needed to do a program that encoding(1) or decoding(0) letters and puting the respective letter in a binary tree and show the binary tree, each "." was saying to put the letter in left leaf and each "-" was saying to the letter put in  right leaf. the " * " is the root.

example of the tree:
      *
   /    \ 
a        t

first: you put the length of the inputs. 
second :you put your your respective letter with your binary code.
third: you select the mode that you want, encoding or decoding.
For example:
A EXAMPLE OF ENCODING:
**IN**
10
A .
B -.
C .-
D ...
E --
L .--
R ..
S -.-
T -
! ---
1 
ATACAR REBELDES!

**OUT**
. - . .- . .. /.. -- -. -- .-- ... -- -.- --- 
* A T R C B E D L S ! (binary tree)

if we have a case that the position in the tree of the letter is to under and his node is empty, the respective node will be " * "  for example:
        *
  /         *
/  \      /    \
        B
so the tree will be  * * B

EXAMPLE OF DECODING:
**IN**
5
A .
C -
R .-
T ..
! -.
0
. .. . - . .- -.

**OUT**

ATACAR!
* A C T R ! (binary tree)

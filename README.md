# pystr-cleaner

Simple script to clean up strings with currently three options:

1 - keep only letters

2 - keep only numbers

3 - keep only letters and numbers

Example 1:
-
`Hi#, th1is is4 m97e!` > `Hi this is me` (it was designed to be used in corporate context, like filling up a form with an adress) 

Example 2:
-

`Hi#, th1is is4 m97e` > `1497`

Example 3:
-

`Hi# I'm% 22 ye;ar?s ol&d` > `Hi Im 22 years old`

<sup>These examples where generated using the script itself.</sup>

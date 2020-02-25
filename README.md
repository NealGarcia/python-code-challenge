# Code Challenge: More Python 🐍
A collection of level 7 and 6 kyu Python challenges adapted from Codewars 

## Shortest Word

![You keep using that word](https://media.giphy.com/media/N7FeGLHjVsDQY/giphy.gif)

Simple: given a string of words, return the length of the shortest word(s). String will never be empty, and you do not need to account for different data types. 

```python
def shortest_word(string): 
  # your lovely code here!

print(shortest_word('My name is Inigo Montoya, you killed my father, prepare to die!'))
  # should return: 2
```
## Sum of Minimums 

![mental math](https://media.giphy.com/media/BmmfETghGOPrW/giphy.gif)

Given a 2D list of size `m * n`, your task is to find the sum of the minimum value in each row. 

For example: 
```python
def sum_of_minimums(list):
  # your lovely code goes here!

my_list = [
    [1,2,3,4,5], # minimum value of row is 1
    [5,6,7,8,9], # minimum value of row is 5
    [20,21,34,56,100] # minimum value of row is 20
    ]

print(sum_of_minimums(my_list))
  # should return 26
```

So the function should return `26` because the sum of each row's minimus is `1 + 5 + 20 = 26`. 

Note: You will always be given non-empty lists containing positive values. 

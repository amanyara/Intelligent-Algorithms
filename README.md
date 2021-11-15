# Intelligent-Algorithms
This project is dedicated to the implementation of various artificial intelligence algorithms
***
###XDU Introduction to Artificial Intelligence First Assignment
***
```
n：represents the number of queens, which can also be interpreted as the number of rows since it is specified that one queen is placed in each row。

checkboard：represents the final matrix presented, where '0' means that the position is empty and no queen has been placed, and '1' means that a queen has been placed in that position.

queen_position: Represents the number of columns in each row where the queen is repositioned, because the title is 8 lines by default, so the initial value of the array of 8 elements is set to -1, if the first line of elements in the first column, then queen_position[0] = 1.

available_position: The available_position[0][i] represents whether a queen has been placed in column i, available_position[1][i] represents whether a queen has been placed in the right diagonal of the position, and available_position [2][i] represents whether a queen has been placed on the left diagonal of the position.

fx：represents the cost. That is, if that position is queened, how many more positions can be placed behind the queen.

answer: Represents whether the row is eligible to place a queen.
```
### **1. Note**
- **Detects if a location is ready for a queen to be placed**

    * The parameters of the input function are the number of rows and the number of columns.

    * The condition is met if no queen has been placed in the left diagonal, right diagonal, or the number of columns in the position.

    * If True is returned, then the position can be placed, and if False is returned, then the position does not meet the condition of placing a queen.

- **a position to place the Queen's adjustment**

    * Enter the parameters of the function for the number of lines and columns.

    * In the position to place the queen, then the 0 of the column to be set to 1, the left diagonal and the corresponding position of the right diagonal are set to 1.

    * And record the location of the line where the queen is located.

- **Delete the queen of a position**
    * The parameters of the input function are the number of rows and the number of columns.

    * In contrast to the operation of placing a queen, the position of the queen of the row is set to -1, and the number of columns in which the queen of the row is located is not determined.

    * In turn, the number of columns where the position is located, the corresponding position of the left and right diagonals are cleared to zero.

- **Calculate the number of remaining rows where the queen can be placed**
    * The parameters of the input function are the number of rows and the number of columns.

    * Iterate through all the columns of the remaining rows in turn and determine whether each position is a position where a queen can be placed, and count +1 if the condition is met.

- **Presenting the final matrix**
    * Take the number of columns in each row, iterate through the checkboard and change its value, and finally output the checkboard.

### **2. Question discribie**
- The eight queens problem is a typical case of the backtracking algorithm, in which the backtracking method is often a blind search that consumes too much search time. In this experiment, a heuristic search is used, where instead of taking any branch, the search selects the best branch down the line.

### **3. Final show**
- ![final result](./Heuristic%20search/Img/Eight_queens.png)

### **4. About author**
- Student majored in artificial intelligence from XDU
- [Personal Blog](https://blog.csdn.net/qq_49392169)
- QQ: 2539110495
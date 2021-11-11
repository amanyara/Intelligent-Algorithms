'''
由于在某一步放置某个皇后时，可能有多个空格可以使用，所以定义启发式函数：

        fx = 剩下未放行中能够用来放皇后的空格数

    如果第i行的皇后放在第j列合法，计算启发式函数的值fx(i,j)。计算出第i行所有空格的fx后，
    将第i个皇后放到第i行中那个与前面i-1个皇后不在同一列或对角线上且fx值最大的空格中（相同时取第一个）。
    如果当前策略无法求解，则回溯至上一步，选择fx值次大的空格放置皇后，依次类推，直至找到一个合法的解。
'''
import numpy as np

class queen():
    def __init__(self, n):
        self.n = n

    def dimensions(self, a=6):
        print("queen", self.n, a)

n = 8
checkerboard = np.zeros((8, 8), dtype=int)
queen_position = np.zeros(8, dtype=int)-1
available_position = np.ones((3, 15), dtype=int)
answer = False

#print(queen_position)
#to test the position of [row, col] could be able to place queen or not
def queen_admission(row, col):
    global available_position
    global queen_position
    if(available_position[0][col] and available_position[1][row+col] and available_position[2][row-col+n-1]):
        return True
    else:
        return False

#place the queen into [row,col]
def place_queen(row, col):
    global available_position
    global queen_position
    queen_position[row] = col
    available_position[0][col] = 0
    available_position[1][row+col] = 0
    available_position[2][row-col+n-1] = 0
    return None

#delete the queen in [row,col]
def delete_queen(row, col):
    global available_position
    global queen_position
    queen_position[row] = -1
    available_position[0][col] = 1
    available_position[1][row+col] = 1
    available_position[2][row-col+n-1] = 1
    return None

#find the available number
def commute_beneficial(row, col):
    global n
    global available_position
    remain_available_number = 0
    for i in range(row+1, n):
        for j in range(col):
            if(queen_admission(i, j)):
                remain_available_number += 1
    return remain_available_number

#presentation the checkerboard
def final_show():
    global n
    global queen_position
    global checkerboard
    for i in range(n):
        for j in range(n):
            if j == queen_position[i]:
                checkerboard[i][j] = 1
    print(checkerboard)

#find the most position with the most available position answer
def best_position(row, col):
    global n
    position = False
    max = -1
    number = -1
    for i in range(col):
        if(queen_admission(row, col)):
            number = commute_beneficial(row)
            if(number>=max):
                max = number
                position = i
    return position

def generate(cur):
    global n
    global answer
    global queen_position
    ccc = 0
    while(cur != 8):
        ccc += 1
        if(ccc == 88):
            break
        else:
            for i in range(n):
                number = False
                if queen_admission(cur, i):
                    number = best_position(cur, i)
            if(number):
                queen_position[cur] = number
                place_queen(cur, number)
                cur += 1
            else:
                cur = cur-1
                #queen_position[cur] = -1
                delete_queen(cur, queen_position[cur])
                #queen_position[cur] = -1
                #return
if __name__ == "__main__":
    generate(0)
    final_show()








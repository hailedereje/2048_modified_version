jimport random

mat = []
#we need to intialize our matrix and pass it null value
for row in range(4):
   mat.append([0] * 4)



def display():
   print("**********WELLCOM THIS IS 2048 ************ ")
   print(""""USE THE INSTRUCTIONS TO PLAY THE GAME
   DOWN  >>    PRESS 'Z'
   UP    >>    PRESS 'W'
   RIGHT >>    PRESS 'D'
   LEFT  >>    PRESS 'A'
 """)


def play(mat):
   greater = mat[0][0]
   for row in mat:
       for element in row:
           if element > greater:
               greater = element
   space = len(str(greater))

   for row in mat:
       new = "|"
       for element in row:
           if element == 0:
               new += " " * space+"|"
           else:
               new += (" " * (space - len(str(element)))) + str(element)+"|"
       print(new)


def condition(mat):
   count=0
   open_board=True
   for row in range(4):
       for element in range(4):
           if mat[row][element]==0:
               count+=1

   if count==0:
       print("*****you loss !!******\n")
       open_board = False
   for row in range(4):
       for element in range(4):
           if mat[row][element]==2048:
               print("******you won !!********\n")
               open_board=False




   return open_board,mat

def randome(mat):
   board_size=4
   for anynum in range(100):# it makes the random num generetion perfect
       column = random.randint(0,board_size-1)
       row = random.randint(0,board_size-1)
       if mat[row][column] == 0:

           if column == 3:

               mat[row][column] = 4
           else:
               mat[row][column] = 2
           break

   return mat


def compress(mat):
   new_mat = []

   for row in range(4):
       new_mat.append([0] * 4)
       pos = 0
       for element in range (4):
           if  mat[row][element] != 0:
               new_mat[row][pos] = mat[row][element]
               mat[row][element]=0
               pos += 1

   return new_mat


def merege(mat):
   for row in range(4):

       for column in range(1, 4):
           if mat[row][column - 1] == mat[row][column] and mat[row][column - 1] != 0:
               mat[row][column] = 0
               mat[row][column - 1] *= 2
   return mat


def reverse(mat):

   new_board = []
   for row in range(4):
       new_board.append([])
       for column in range(0, 4):
           new_board[row].append(mat[row][-column - 1])
   return new_board


def transpose(mat):
   new_board = []
   for row in range(4):
       new_board.append([])
       for element in range(4):
           new_board[row].append(mat[element][row])
   return new_board


#
def move_left(mat):
   board,mat1 =condition(mat)
   board_1 = compress(mat1)
   board_2 = merege(board_1)
   board_3 = compress(board_2)
   board_4=randome(board_3)
   play(board_4)
   return board_4,board


def move_right(mat):
   board, mat2 = condition(mat)
   board_1 = reverse(mat2)
   board_2 = compress(board_1)
   board_3 = merege(board_2)
   board_4 = compress(board_3)
   board_5 = reverse(board_4)
   board_6=randome(board_5)
   play(board_6)
   return board_6,board


def move_down(mat):
   board, mat3 = condition(mat)
   board_1 = transpose(mat3)
   board_2 = reverse(board_1)
   board_3 = compress(board_2)
   board_4= merege(board_3)
   board_5= compress(board_4)
   board_6=reverse(board_5)
   board_7=transpose(board_6)
   board_8=randome(board_7)
   play(board_7)
   return board_7,board


def move_up(mat):
   board, mat4 = condition(mat)
   board_1 = transpose(mat4)
   board_2 = compress(board_1)
   board_3 = merege(board_2)
   board_4 = compress(board_3)
   board_5 = transpose(board_4)
   board_6 = randome(board_5)
   play(board_6)
   return board_6,board

display()
play(mat)
print("\n")
def game(mat):

   board = True
   while board:

       move = input("enter the allowed letters>>> ")
       if move == 'a' or move=='A':
           new_board,newBoard = move_left(mat)
           mat = new_board
           board=newBoard
       elif move == 'd'  or move=='D':
           new_board,newBoard = move_right(mat)
           mat = new_board
           board = newBoard
       elif move == 'z' or move=='Z':
           new_board,newBoard = move_down(mat)
           mat = new_board
           board = newBoard
       elif move == 'w' or move=='W':
           new_board,newBoard = move_up(mat)
           mat = new_board
           board = newBoard
       else:
           print("please use the allowed keys only")

game(mat)




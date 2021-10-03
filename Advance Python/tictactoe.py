

def status(board):
    '''
    This function is used to check if anyone won the game.
    Here,   T-Top     R-Right
            M-Middle  M-Middle
            B-Bottom  L-Left

    '''
    if board['TL'] == board['TM'] == board['TR'] and board['TL'] != ' ':
        return board['TL']
    elif board['ML'] == board['MM'] == board['MR'] and board['ML'] != ' ':
        return board['ML']
    elif board['BL'] == board['BM'] == board['BR'] and board['BL'] != ' ':
        return board['BL']
    elif board['TL'] == board['ML'] == board['BL'] and board['TL'] != ' ':
        return board['TL']
    elif board['TM'] == board['MM'] == board['BM'] and board['TM'] != ' ':
        return board['TM']
    elif board['TR'] == board['MR'] == board['BR'] and board['TR'] != ' ':
        return board['TR']
    elif board['TL'] == board['MM'] == board['BR'] and board['TL'] != ' ':
        return board['TL']
    elif board['TR'] == board['MM'] == board['BL'] and board['TR'] != ' ':
        return board['TR']
    else:
        return 'D'

def printboard(board):
    '''
    Used to print the board in the following fashion:
            TL | TM | TR
            ---+----+---
            ML | MM | MR
            ---+----+---
            BL | BM | BR
    '''
    print(board['TL']+"|"+board['TM']+"|"+board['TR'])
    print("-+-+-")
    print(board['ML']+"|"+board['MM']+"|"+board['MR'])
    print("-+-+-")
    print(board['BL']+"|"+board['BM']+"|"+board['BR'])
    


'''
Following is the driver code, which calls the
above functions repetitively until there is a
result.
'''

board = {'TL':' ','TM':' ','TR':' ',
         'ML':' ','MM':' ','MR':' ',
         'BL':' ','BM':' ','BR':' '
         }
print("-----------RULES-----------")
print("For Top Left enter TL")
print("For Middle Middle enter MM")
print("For Bottom Right enter BR")
print("And so on.......")
print("---------------------------")
p1 = input("Enter the name of Player 1, choosing O : ")
p2 = input("Enter the name of Player 2, choosing X : ")
turn = 0
print("Board at begining")
printboard(board)
while turn<=9:
      print(p1+"'s turn. Enter the position")
      inp = input()
      board[inp] = 'O'
      printboard(board)
      turn+=1
      if status(board) == 'X':
              print(p2+" Wins!!")
              break
      elif status(board)=='O':
              print(p1+" Wins!!")
              break
      else:
              if turn==9:
                  print("Draw")
                  break
      print(p2+"'s turn. Enter the position")
      inp = input()
      board[inp] = 'X'
      printboard(board)
      turn+=1
      if status(board) == 'X':
              print(p2+" Wins!!")
              break
      elif status(board)=='O':
              print(p1+" Wins!!")
              break
      else:
              if turn==9:
                  print("Draw")
                  break
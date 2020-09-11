print('Welcome to tic tac toe !!!!')

while True:
    
    board=[' ']*10
    player1_marker,player2_marker=select_marker()
    current_player=select_player()
    print(current_player+'will go first')
        
    playing=True
    
    while playing:
        
        if current_player=='Player1':
            
            display_board(board)
            
            pos=select_position()
            
            insert_board(board,pos,player1_marker)
            
            if is_win(board,player1_marker):
                
                display_board(board)
                print('PLAYER 1 WINS!!!!')
                playing=False
                
            else:
                
                if board_full(board):
                    
                    print('TIE !!!')
                    palying=False
                else:
                    
                    current_player='Player2'
            
        
        else:
            display_board(board)
            
            pos=select_position()
            
            insert_board(board,pos,player2_marker)
            
            if is_win(board,player2_marker):
                
                display_board(board)
                print('PLAYER 2 WINS!!!!')
                playing=False
                
            else:
                
                if board_full(board):
                    
                    print('TIE !!!')
                    palying=False
                else:
                    
                    current_player='Player1'
    
    
    repeat=input('Do you want to play again? (y or n): ').lower()
    if repeat=='y':
        continue
    else:
        break



//displayboard
from IPython.display import clear_output
def display_board(board):
    clear_output()
    print('    |'+'    |   ')
    print('  '+board[1]+' |  '+board[2]+' |  '+board[3])
    print('--------------')
    print('    |'+'    |   ')
    print('  '+board[4]+' |  '+board[5]+' |  '+board[6])
    print('--------------')
    print('    |'+'    |   ')
    print('  '+board[7]+' |  '+board[8]+' |  '+board[9])
    print('    |'+'    |   ')
   

    //insert_board
      def insert_board(board,position,marker):
    
           board[position]=marker
           
           
    // is_win
    
    def is_win(board,mark):
    
    return ((board[1]==board[2]==board[3]==mark) or
             (board[4]==board[5]==board[6]==mark) or
             (board[7]==board[8]==board[9]==mark) or
             (board[1]==board[4]==board[7]==mark) or
             (board[2]==board[5]==board[8]==mark) or
             (board[3]==board[6]==board[9]==mark) or
             (board[1]==board[5]==board[9]==mark) or
             (board[3]==board[5]==board[7]==mark)) 
             
    //select_marker
    
    def select_marker():
    
    marker=' '
     
    while marker!='X' and marker!='O':
        
        marker=input('Player1!! please enter "X" or "O" : ').upper()
        
    if(marker=='X'):
        
        return ('X','O')
    
    return ('O','X')
        
        // spacecheck
        
        
        def space_check(board,position):
    
    return board[position]==' '
    
    
    //select position
    
    def select_position():
    
    position=0
    
    while position not in[1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        
        position=int(input("Enter the position : "))
        
    return position
    
    //select player
    
    
    import random
def select_player():
    
    toss=random.randint(0,1)
    
    if toss==0:
        
        return 'Player1'
    
    else:
        return 'Player2'
    
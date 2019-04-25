print()
import numpy as np
import copy
matrix= np.array([['00','01','02','03','04','05','06','07','08','09'],                     
         ['10','11','12','13','14','15','16','17','18','19'],
         ['20','21','22','23','24','25','26','27','28','29'],
         ['30','31','32','33','34','35','36','37','38','39'],
         ['40','41','42','43','44','45','46','47','48','49'],
         ['50','51','52','53','54','55','56','57','58','59'],
         ['60','61','62','63','64','65','66','67','68','69'],
         ['70','71','72','73','74','75','76','77','78','79'],
         ['80','81','82','83','84','85','86','87','88','89'],
        ['90','91','92','93','94','95','96','97','98','99']])
print(matrix)                                                                               
print()
                    
def set_ship_location(player,direction,board):                                               # function for the ship location                                            
    i,j=input(f'{player}, Enter your Ship location: ').strip('')                             # The strip() method returns a copy of the string with both leading and trailing characters removed
    if direction=='v':                                                                       # v is for Vertical direction , i is for row, j is for column
        while int(i)>7:                                                                      # if the value of row is greater than 7
            i,j=input(f'{player}, Wrong location selected, Enter location again: ')          # enter the value of location again if the value greater than 7
        i=int(i)                                                                             # value of the row(string) is converted into interger 
        j=int(j)                                                                             # value of the column(string) is converted into integer
        a=i+1                                                                                # for the corresponding index 
        b=i+2
        board[i][j]='@'                     
        board[a][j]='@'                                                                      # corresponding index replaced with @
        board[b][j]='@'

    elif direction=='h':                                                                      # h is for Horizontal direction
        while int(j)>7:
            i,j=input(f'{player}, Wrong location selected, Enter the location again: ')
        i=int(i)
        j=int(j)
        a=j+1
        b=j+2
        board[i][j]='@'
        board[i][a]='@'
        board[i][b]='@'
    else:
        set_ship_location(player,input(f'{player}, Wrong ship direction Entered, Enter Direction again, h/v: '),board)          # if entered wrong direction except h/v 
        
player1=input(f"Enter Player 1 name: ")                                                       
player1_direction=input(player1+', '+"Enter your Ship Direction, h/v: ")
player1_board=copy.deepcopy(matrix)                                                          # deep copy function is used for coping of the matrix
set_ship_location(player1,player1_direction,player1_board)                                   # calling of set_ship_location for player1

player2=input("Enter Player 2 name: ")
player2_direction=input(player2+', '+"Enter your Ship Direction, h/v: ")
player2_board= copy.deepcopy(matrix)
set_ship_location(player2,player2_direction,player2_board)                                   # calling of set_ship_location for player2

def bombing_ship(player):                                                                    # function for bomb on ship                                                                      
    global player1_board
    global player2_board

    i,j=input(f'{player}, Enter Bomb location: ').strip('')                                  # index of the bomb location entered by the user                                                                                               
    i=int(i)  
    j=int(j)                                                                               

    if player==player1:                                                                      # for player 1 turn
        if player2_board[i][j]=='@':                                                         # if player 1 finds '@' on the player 2 board
            print("HIT!!!")                                                                  # hit print
            player2_board[i][j]='#'                                                          # on player2 board, '@' is replaced is replaced "#"
        
            destroyed=True
            for list_of_element in player2_board:                                           # for loop every row in the player2_board                                                  
                for element in list_of_element:                                             # for loop for each element in the list
                    if element=='@':                                                        # search for the string equal to '@' on the Player@_board
                        destroyed=False
            if destroyed==True:
                print(f"Target Destroyed Completely !!!, {player} Wins")                    # if all the element equal to the '@' in the ship, the ship is completely destroyed
                return True

        elif player2_board[i][j] == '@' or player2_board[i][j] == '#':                      # if on player2_board the bomb location is equal to the string '@' and "#" 
            print("Already Hit!!")                                                          # then print already hit
            player2_board[i][j] = 'H'                                                       # and on that location the string is replaced with "H"

        else:
            player2_board[i][j] ='#'                                                        # else the bomb location is replaced with "#"
        return False    

    if player==player2:
        if player1_board[i][j]=='@':
            print("HIT!!!")
            player1_board[i][j]='#'

            destroyed=True
            for list_of_element in player1_board:
                for element in list_of_element:
                    if element=='@':
                        destroyed=False
            if destroyed==True:
                print(f"Target Destroyed Completely !!!, {player} Wins")
                return True
        
        elif player1_board[i][j] == '@' or player1_board[i][j] == '#':
            print("Already Hit!!")
            player1_board[i][j] = 'H'

        else:
            player1_board[i][j]='#'
        return False

win=False                                                                      # if the player is not equal to True i.e, equal to false

player = player1                                                               # game is started with player1 turn
while not win:                                                                 
    win=bombing_ship(player)                                                   # calling of bombing_ship function     
    if player==player1:                                                        # player1 turn 
        player=player2                                                         # in the next loop player2 turn 
    else:
        player=player1                                                        
    
print(player1_board)
print()
print(player2_board)
print()

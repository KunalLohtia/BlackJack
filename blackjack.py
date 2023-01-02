import random as rn

player = [ ]
dealer = [ ]
# note that there are only 4 of each type of card in deck
all_the_diff_nums = [2,3,4,5,6,7,8,9,10,'J','Q','K','A']
suit = ['spade' , 'heart' , 'diamond' , 'club']

player_sum = 0
dealer_sum = 0

deck = [ ]

#function for creating the deck
def creating_deck():
    for i in suit:
        for j in all_the_diff_nums:
            deck.append( [i,j] )
    rn.shuffle(deck)
    return deck
    
# function for converting cards to numeric value
        
def convert_to_numeric(x):
    y = 0
    if (x == 'J' or x == 'Q' or x == 'K'):
       y = 10
       return y
    elif (x == 'A'):
        y = 11
        return y
    else:
        return x   


# function to check if ace is 1 or 11
def check_ace(x, thesum):
    if (x == 11):
        # if adding 11 exceeds 21, ace becomes 1
        if (x + thesum >= 21):
            x = 1
            return x
        else:
            x = 11
            return x
    else:
        return x


# function for adding the sum of your hand
def add_hand(x,y):
    #keeps track of sum of your hand
    sum_xy = 0
    #print(x)
    num_x = convert_to_numeric(x)
    #print(num_x)
    num_x = check_ace(num_x, sum_xy)
    #print(num_x)
    # adjusts running sum after checking for ace
    sum_xy = sum_xy + num_x
    num_y = convert_to_numeric(y)
    num_y = check_ace(num_y, sum_xy)
    # adjusts running sum after checking for ace
    sum_xy = sum_xy + num_y
    return sum_xy


#function for checking if score is over 21
def check_21(s):
    if (s > 21):
        return 'over'
    elif (s == 21):
        return 'perfect'
    else:
        return 'under'
        
# function that represents the start of the game
def start_game(p, d, ps, ds):
    print(f'\nDealer draws {dealer[0]} and [xxxxxx, xx]\n')
    print(f'You are currently at: ' + str(ps))
    print(f'Current Hand: {player}')
    return 0

    
# function for hit
def hit(p, ps, ind):
    #print(f'this is player current hand {player}')
    #add new card to player's hand
    #print(f'This is new card player has {deck[index]}')
    p.append(deck[ind])
    #convert new card to numeric value
    num = convert_to_numeric(deck[ind][1])
    #print(f'This is new card numeric value ' + str(num)) 
    #check if there is ace
    num = check_ace(num, ps)
    #print(f'This is new card numeric value after checking ace' + str(num)) 
    ps = ps + num
    #print('this is player sum now after new card ' + str(player_sum))
    #print(f'this is new current hand {player}')

    #print('this is index '+ str(ind))
    
    return ps
    
        
def main():
    player_name = input('Hello, what is your name?\n')
    
    choice = input(player_name + ', you dare to play a game of BlackJack? Type y or yes if you dare\n')
    
    #input validation to indicate whether to start the game or not

    gamer_mode = True

    user_action = 3
    
    #while start game option is on
    while (gamer_mode == True):
                    
                    #starts the game
                    if ( (choice.lower() == 'yes' or choice.lower() == 'y') and user_action == 3):
        
                        deck = creating_deck()
                        player.append(deck[0])
                        player.append(deck[1])
                        dealer.append(deck[2])
                        dealer.append(deck[3])
        
                        # sums hands for player and dealer after drawing
                        player_sum = add_hand((player[0][1]), (player[1][1]) )
                        dealer_sum = add_hand( (dealer[0][1]), (dealer[1][1]) )
        
        
                        #index at 4 is the first in the deck that will be use
                        index = 4

                        #input validation for initial user action
        
                        user_action_validation = False
        
                        #input validation for after intital hit
        
                        user_action_2_validation = False
        
                        #input validation to keep on hitting or not
                        hit_move = True

                        #input validation to dictate staying or not
                        stay_move = True

                        #input validation for checking if you want to replay or not

                        replay_validation = False

                       # officially starts the game

                        start_game(player, dealer, player_sum, dealer_sum)
                    

                        #if player gets 21 on first two cards
                        if (player_sum == 21):
                            print('Congrats! You got a BlackJack and won the game!\n')
                            user_action = 2

                        #what happens when there is a tie right away
                        if (player_sum == 21 and dealer_sum == 21):
                            print(f"\nDealer's second card was {dealer[1]}\n")
                            print("Dealer is at " + str(dealer_sum))
                            print(f"Dealer's Current Hand: {dealer}\n")
                            print("Both the dealer and you have a blackjack. It's a push.\n")
                            user_action = 2
                    
                        while (user_action_validation == False):
                            #input validation for first move for player
                            try:
                                user_action = int(input('\nHit(Press 1) or Stay(Press 0): '))
                            except ValueError:
                                print("\nPress 1 to Hit or Press 0 to Stay\n")
                                continue
                            #what happens when first move is hit
                        
                            while (user_action == 1):
                                user_action_validation = True
                                while(hit_move == True):
                                    player_sum = hit(player, player_sum, index)
                                    print(f'\nYou draw {deck[index]}\n')
                                    print(f'Current Hand: {player}')
                                    print(f'You are currently at: ' + str(player_sum))
                                    index+=1
                                    #print(f'this player hand after hit {player}')
                                    #print("player sum after hit " + str(player_sum))
                                
                                    if(check_21(player_sum) == 'perfect'):
                                            #ends the game if player has 21
                                            hit_move = False
                                            #print('This is player_sum after hit' + str(player_sum))
                                            print('\nCongrats! You got a BlackJack and won the game!\n')
                                            user_action = 2
                                            
                                        
                                    elif(check_21(player_sum) == 'over'):
                                            #ends the game if player exceeded 21
                                            hit_move = False
                                            #print('This is player_sum after hit' + str(player_sum))
                                            print('\nYour score exceeded 21. You lost.\n')
                                            user_action = 2
                                            
                                        
                                    elif (check_21(player_sum) == 'under'):
                                        #if player still doesnt have 21 yet
                                        user_action_2_validation = False
                                        while (user_action_2_validation == False):
                                            #input validation for further moves
                                            try:
                                                user_action_2 = int(input('Hit(Press 1) or Stay(Press 0): '))
                                            except ValueError:
                                                print("Press 1 to Hit or Press 0 to Stay: ")
                                                continue
                                        
                                        #if user wants to continute hitting
                                            if (user_action_2 == 1):
                                                user_action_2_validation = True
                                                hit_move = True
                                        
                                            else:
                                                #takes player to stay
                                                user_action_2_validation = True
                                                hit_move = False
                                                user_action = 0
                                
                        # if player decides to stay
                            while (user_action == 0):
                                user_action_validation = True
                            
                                print(f"\nDealer's second card was {dealer[1]}\n")
                                while (stay_move == True):
                                    print("Dealer is at " + str(dealer_sum))
                                    print(f"Dealer's Current Hand: {dealer}\n")
                                    if (dealer_sum > 21):
                                        print("Dealer got Busted\nYou Won!\n")
                                        stay_move = False
                                        user_action = 2
                                    elif (dealer_sum == 21):
                                        print("Dealer got a BlackJack and won the Game\nYou Lost\n")
                                        stay_move = False
                                        user_action = 2
                                    else:
                                        dealer_sum = hit(dealer, dealer_sum, index)
                                        print(f"Dealer draws {deck[index]}\n")
                                        index+=1
                                


                        # end game actions    
                            while (user_action == 2):
                                print("Would you like to play again?\n")
                                while(replay_validation == False):
                                    try:
                                        ans = int(input("Select 1 to play again or Select 0 to leave: "))
                                    except ValueError:
                                        print("Press 1 to play again or Press 0 to Leave\n")
                                        continue
                                    if (ans == 1):
                                        gamer_mode = True
                                        replay_validation = True
                                        user_action = 3
                                        choice = 'y'
                                        del player[:]
                                        del dealer[:]
                                        del deck[:]
                                        del player_sum
                                        del dealer_sum
                                    elif (ans == 0):
                                        gamer_mode = False
                                        replay_validation = True
                                        user_action = 3
                                        choice = 'n'
                                        print("Goodbye\n")
                                        break
                                        
                            
                               
                   
        

main()
        

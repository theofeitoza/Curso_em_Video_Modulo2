import random
resp=str(input('Shall we play jokenpo? Enter Yes or No:'))
if(resp=='Sim'):
    play_list=['Rock','Paper','Scissor']
    computer=random.choice(play_list)
    player=str(input('Escolha sua jogada (Pedra, Papel ou Tesoura):'))
    print('Voce escolheu {} e o computador escolheu {}'.format(player,computer))
    if(player==computer):
        print('It\'s a tie')
    elif(player=='Paper' and computer=='Rock' or player=='Scissor' and computer=='Paper' or player=='Rock' and computer=='Scissor'):
        print('The player won!!!')
    elif(computer=='Paper' and player=='Rock' or computer=='Scissor' and player=='Paper' or computer=='Rock' and player=='Scissor'):
        print('The computer won!')
else:
    print('Sorry, I wanted to play a lot') 
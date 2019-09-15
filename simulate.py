# first party
import argparse

# third party
import pandas as pd
import matplotlib.pyplot as plt

# .
from Actor import Actor

def simulate(num_epochs:int):
    '''
    runs our simulation with 2 actors
    :param num_epochs: the number of iterations we want to run
    :type num_epochs: int
    :return: None
    '''
    data = {"actor1_money":[], "actor2_money":[], "actor1_choice":[], "actor2_choice":[]}

    player1 = Actor(avaliable_funds = 10, lower_threshhold=5, betrayal_rate=.03)
    player2 = Actor(avaliable_funds = 10, lower_threshhold=5, betrayal_rate=.90)

    for i in range(num_epochs):
        choice1 = player1.make_choice()
        choice2 = player2.make_choice()
        processChoice(choice1, choice2, player1, player2)
        data["actor1_money"].append(player1.avaliable_funds)
        data["actor2_money"].append(player2.avaliable_funds)
        data["actor1_choice"].append(choice1)
        data["actor2_choice"].append(choice2)
        player1.update()
        player2.update()

    df = pd.DataFrame(data)
    print(df)
    plt.plot(range(0,num_epochs), df['actor1_money'])
    plt.plot(range(0,num_epochs), df['actor2_money'])
    plt.show()

    plt.clf()
    counts1 = df.groupby(['actor1_choice'])['actor1_choice'].count()
    counts2 = df.groupby(['actor2_choice'])['actor2_choice'].count()

    print(counts2)
def processChoice(choice1:str, choice2:str, player1:Actor, player2:Actor):
    if(choice1 == "Trust" and choice2 == "Trust"):
        player1.avaliable_funds += 1
        player2.avaliable_funds += 1
    elif(choice1 == "Trust" and choice2 == "Betray"):
        player1.avaliable_funds -= 1
        player2.avaliable_funds += 3
    elif(choice1 == "Betray" and choice2 == "Trust"):
        player1.avaliable_funds += 3
        player2.avaliable_funds -= 1
    elif(choice1 == "Betray" and choice2 == "Betray"):
        player1.avaliable_funds -= 2
        player2.avaliable_funds -= 2

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Number of iterations to run over")
    parser.add_argument('num_epochs', action='store', type=int)
    res = parser.parse_args()
    simulate(res.num_epochs)

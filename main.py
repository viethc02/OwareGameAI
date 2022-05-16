import tkinter

from envs.oware import Oware
from envs.visualizer import Visualizer
from game import Game
from random import seed
from tkinter.ttk import *
from tkinter import *


# Importing Agents
from random_agent import RandomAgent
from mcs_agent import MCSAgent
from minimax_agent import MinimaxAgent
from id_minimax_agent import IDMinimaxAgent
from human import Human
# from agent import Agent    # After completing your agent, you can uncomment this line


seed(13731367)


def main():
    def human():
        players = [Human, IDMinimaxAgent]
        results = {player_name(players[0]): 0, player_name(players[1]): 0}

        # Timeout for each move. Don't rely on the value of it. This value might be
        # changed during the tournament.
        timeouts = [5.0 if player != Human else None for player in players]

        for i in range(1):
            first = i % 2
            second = 1 - first
            players_instances = (players[first](), players[second]())
            game = Game(*players_instances)
            initial_state = Oware(player_name(players[first]), player_name(players[second]))
            visualizer = Visualizer(initial_state)
            for player in players_instances:
                if isinstance(player, Human):
                    player.set_board(visualizer)
            winners = game.play(initial_state, output=True, visualizer=visualizer, timeout_per_turn=timeouts)
            if len(winners) == 1:
                results[initial_state.get_players_names()[winners[0]]] += 1
            print("")
            print(f"{i}) Result: {results[player_name(players[0])]} - {results[player_name(players[1])]}")
            print("########################################################")

    def AI():
        players = [MinimaxAgent, IDMinimaxAgent]
        results = {player_name(players[0]): 0, player_name(players[1]): 0}

        # Timeout for each move. Don't rely on the value of it. This value might be
        # changed during the tournament.
        timeouts = [5.0 if player != Human else None for player in players]

        for i in range(1):
            first = i % 2
            second = 1 - first
            players_instances = (players[first](), players[second]())
            game = Game(*players_instances)
            initial_state = Oware(player_name(players[first]), player_name(players[second]))
            visualizer = Visualizer(initial_state)
            for player in players_instances:
                if isinstance(player, Human):
                    player.set_board(visualizer)
            winners = game.play(initial_state, output=True, visualizer=visualizer, timeout_per_turn=timeouts)
            if len(winners) == 1:
                results[initial_state.get_players_names()[winners[0]]] += 1
            print("")
            print(f"{i}) Result: {results[player_name(players[0])]} - {results[player_name(players[1])]}")
            print("########################################################")

    class Example(Frame):
        def __init__(self, parent):
            Frame.__init__(self, parent)
            self.parent = parent
            self.initUI()

        def initUI(self):
            self.style = Style()
            self.style.theme_use("default")

            self.pack(fill="both", expand=True)

            humanButton = Button(self, text="Play with Computer", command=human)
            humanButton.pack(padx=50, pady=10, side=tkinter.LEFT)

            AIButton = Button(self, text="AI vs AI", command=AI)
            AIButton.pack(padx=50, pady=20, side=tkinter.LEFT)

    root = tkinter.Tk()
    root.title("Oware AI")
    root.iconphoto(True, tkinter.PhotoImage(file="images/AI.png"))

    root.eval('tk::PlaceWindow . center')
    app = Example(root)
    root.mainloop()

    ############### Set the players ###############
    # players = [MCSAgent, RandomAgent]
    # players = [MinimaxAgent, MCSAgent]
    # players = [Human, RandomAgent]      # <= EASY
    # players = [Human, Human]
    # players = [Human, MinimaxAgent]
    # players = [Human, MCSAgent]
    # players = [MinimaxAgent, IDMinimaxAgent]   # <= HARD
    # players = [IDMinimaxAgent, MCSAgent]

    #players = [Agent, IDMinimaxAgent]
    ###############################################

    # The rest of the file is not important; you can skip reading it. #
    ###################################################################

def player_name(player):
    return player().info()['agent name']


if __name__ == "__main__":
    try:
        main()
    except BrokenPipeError:
        pass
    except EOFError:
        pass
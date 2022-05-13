from envs.oware import Oware
from agent_interface import AgentInterface


class Agent(AgentInterface):
    """
    An agent who plays the Oware game

    Methods
    -------
    `info` returns the agent's information
    `decide` chooses an action from possible actions
    """

    @staticmethod
    def info():
        """
        Return the agent's information

        Returns
        -------
        Dict[str, str]
            `agent name` is the agent's name
            `student name` is the list team members' names
            `student number` is the list of student numbers of the team members
        """

        return {"agent name": "?"}

    def decide(self, state: Oware, actions: list):
        """
        Generate a sequence of increasingly preferable actions

        Given the current `state` and all possible `actions`, this function
        should choose the action that leads to the agent's victory.
        However, since there is a time limit for the execution of this function,
        it is possible to choose a sequence of increasing preferable actions.
        Therefore, this function is designed as a generator; it means it should
        have no return statement, but it should `yield` a sequence of increasing
        good actions.

        IMPORTANT: If no action is yielded within the time limit, the game will
        choose a random action for the player.

        Parameters
        ----------
        state: Oware
            Current state of the game
        actions: list
            List of all possible actions

        Yields
        ------
        action
            the chosen `action`
        """
        best_action = actions[0]
        yield best_action

from iterative_deepening import IterativeDeepening
from minimax_agent import MinimaxAgent
from envs.oware import Oware
from past.builtins import xrange
import time

MAX_DEPTH = 10
MaxAllowedTimeInSeconds = 2
MaxUtility = float("inf")

class IDMinimaxAgent(IterativeDeepening):
    def __init__(self):
        super().__init__(AgentClass=MinimaxAgent)

    def info(self):
        return {"agent name": "ID_Minimax"}

    def heuristic(self, state: Oware):
        collected_stones = state.get_collected_stone()
        return collected_stones[0] - collected_stones[1]

    def max_value(self, state, alpha, beta, depth):
        is_winner = state.is_winner()
        if is_winner is not None:
            return is_winner * float('inf')

        if depth <= 0:
            return self.heuristic(state)

        val = -MaxUtility
        actions = state.actions()
        for action in actions:
            val = max(val, self.min_value(state.successor(action), alpha, beta, depth - 1))
            if val >= beta:
                return val
            alpha = max(alpha, val)
        return val

    def min_value(self, state, alpha, beta, depth):
        is_winner = state.is_winner()
        if is_winner is not None:
            return is_winner * float('-inf')

        if depth <= 0:
            return -self.heuristic(state)

        val = MaxUtility
        actions = state.actions()
        for action in actions:
            val = min(val, self.max_value(state.successor(action), alpha, beta, depth - 1))
            if val <= alpha:
                return val
            beta = min(beta, val)
        return val

    def decide(self, state: Oware, actions: list):
        best_action = None
        max_value = -MaxUtility
        start_time = time.time()
        for depth in xrange(1, MAX_DEPTH):
            if time.time() - start_time > MaxAllowedTimeInSeconds:
                break
            for action in actions:
                action_value = self.min_value(state.successor(action), -MaxUtility, MaxUtility, depth - 1)
                if action_value > max_value:
                    max_value = action_value
                    best_action = action
                    if max_value == MaxUtility:
                        break
            if max_value == MaxUtility:
                break
            print(time.time() - start_time, depth, max_value)
        yield best_action
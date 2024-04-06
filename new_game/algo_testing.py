class Algorithm:
    
    def __init__(self):
        pass

    def make_move(self, number, move):
        return number * move

    def update_score(self, score, number):
        if number % 2 == 0:
            return score + 1  # Add 1 point for even number
        else:
            return score - 1  # Subtract 1 point for odd number

    def get_possible_moves(self, number, turn):
        # This method could be overridden if needed
        if turn == 'computer':
            return [2, 3]
        else:
            return list(range(2, min(number, 6) + 1))
        
    def generate_game_tree(self, number1, number2, score1, score2, turn, depth):
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            return None, self.evaluate(number1, number2, score1, score2)
        
        if turn == 'computer':
            maximizing_player = True
            best_value = float('-inf')
            best_move = None
            for move in self.get_possible_moves(number1, turn):
                new_number1 = self.make_move(number1, move)
                new_score1 = self.update_score(score1, new_number1)
                _, value = self.generate_game_tree(new_number1, number2, new_score1, score2, 'human', depth - 1)
                if value > best_value:
                    best_value = value
                    best_move = move
            return best_move, best_value
        else:
            maximizing_player = False
            best_value = float('inf')
            best_move = None
            for move in self.get_possible_moves(number2, turn):
                new_number2 = self.make_move(number2, move)
                new_score2 = self.update_score(score2, new_number2)
                _, value = self.generate_game_tree(number1, new_number2, score1, new_score2, 'computer', depth - 1)
                if value < best_value:
                    best_value = value
                    best_move = move
            return best_move, best_value

    def evaluate(self, number1, number2, score1, score2):
        # This is a simple heuristic function to evaluate leaf nodes
        return score2 - score1  # Difference in scores


class MinimaxAlgorithm(Algorithm):

    def minimax(self, number1, number2, score1, score2, turn, depth, maximizing_player):
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            return score2 - score1, None
        
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_possible_moves(number1, turn):
                new_number1 = self.make_move(number1, move)
                new_score1 = self.update_score(score1, new_number1)
                evaluation = self.minimax(new_number1, number2, new_score1, score2, 'computer', depth - 1, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_possible_moves(number2, turn):
                new_number2 = self.make_move(number2, move)
                new_score2 = self.update_score(score2, new_number2)
                evaluation = self.minimax(number1, new_number2, score1, new_score2, 'human', depth - 1, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
            return min_eval, best_move


class AlphaBetaAlgorithm(Algorithm):
    
    def minimax(self, number1, number2, score1, score2, turn, depth, alpha, beta, maximizing_player):
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            return score2 - score1, None
        
        if maximizing_player:
            max_eval = float('-inf')
            best_move = None
            for move in self.get_possible_moves(number1, turn):
                new_number1 = self.make_move(number1, move)
                new_score1 = self.update_score(score1, new_number1)
                evaluation = self.minimax(new_number1, number2, new_score1, score2, 'computer', depth - 1, alpha, beta, False)[0]
                if evaluation > max_eval:
                    max_eval = evaluation
                    best_move = move
                alpha = max(alpha, evaluation)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = float('inf')
            best_move = None
            for move in self.get_possible_moves(number2, turn):
                new_number2 = self.make_move(number2, move)
                new_score2 = self.update_score(score2, new_number2)
                evaluation = self.minimax(number1, new_number2, score1, new_score2, 'human', depth - 1, alpha, beta, True)[0]
                if evaluation < min_eval:
                    min_eval = evaluation
                    best_move = move
                beta = min(beta, evaluation)
                if beta <= alpha:
                    break
            return min_eval, best_move

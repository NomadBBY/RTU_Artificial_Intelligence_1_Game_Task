import pygame

BACKGROUND_COLOR = 225, 217, 196
BUTTON_COLOR = 100, 100, 100

class Algorithm:
    
    def __init__(self):
        pass

    def make_move(self, number, move):
        return number * move

    def update_score(self, score, number):
        if number % 2 == 0:
            return score + 1  
        else:
            return score - 1  

    def get_possible_moves(self, number, turn):
        
        if turn == 'computer':
            return [2, 3]
        else:
            return list(range(2, min(number, 6) + 1))

def evaluate_state(score1, score2):
    point_difference = abs(score2 - score1)
    if point_difference == 0:
        f1 = -1  
    elif point_difference == 1:
        f1 = 0
    else:
        f1 = 3 if score1 < score2 else -3  

    
    if f1 != 0 and score1 != score2:
        f1 = 4 if score1 < score2 else -4

    return f1

class MinimaxAlgorithm(Algorithm):

    def minimax(self, number1, number2, score1, score2, turn, depth, maximizing_player):
        if depth == 0 or number1 >= 1000 or number2 >= 1000:
            return evaluate_state(score1, score2), None

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
            return evaluate_state(score1, score2), None
        
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
        
class GameWindow:

    def __init__(self, width=600, height=350):
        pygame.init()  
        pygame.font.init()  
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((self.width, self.height))
        self.running = True
        pygame.display.set_caption('Reizināšana līdz Tūkstotim')

    def reset_game(self):
        
        self.running = True
        pygame.init()  

    def welcome_screen(self):

        button1_rect = pygame.Rect(120, 200, 120, 35)  
        button2_rect = pygame.Rect(360, 200, 120, 35)  

        button_font = pygame.font.Font(None, 24) 
        title_font = pygame.font.Font(None, 50) 
        text_font = pygame.font.Font(None, 36) 
                        
        self.window.fill((BACKGROUND_COLOR))  
        
        text1 = title_font.render("Reizināšana līdz Tūkstotim", True, (0, 0, 0))
        text1_rect = text1.get_rect(center=(self.width // 2, 75))
        self.window.blit(text1, text1_rect)
        
        text2 = text_font.render("Izvēleties kurš sāks:", True, (0, 0, 0))
        text2_rect = text2.get_rect(center=(self.width // 2, 125))
        self.window.blit(text2, text2_rect)
        
        pygame.draw.rect(self.window, (BUTTON_COLOR), button1_rect)
        pygame.draw.rect(self.window, (BUTTON_COLOR), button2_rect)
        
        button1_text = button_font.render("Cilvēks", True, (0, 0, 0))
        button2_text = button_font.render("Dators", True, (0, 0, 0))
        
        button1_text_rect = button1_text.get_rect(center=button1_rect.center)
        button2_text_rect = button2_text.get_rect(center=button2_rect.center)
        
        self.window.blit(button1_text, button1_text_rect)
        self.window.blit(button2_text, button2_text_rect)
        pygame.display.flip()  

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        
                        if button1_rect.collidepoint(event.pos):
                            return 'human'
                        
                        elif button2_rect.collidepoint(event.pos):
                            return 'computer'

        pygame.quit()

    def choice_screen(self):

        title_font = pygame.font.Font(None, 50) 

        button_width = 35
        button_height = 35
        button_margin = 10  
        button_color = BUTTON_COLOR
        button_font = pygame.font.Font(None, 24)

        button_values = list(range(5, 16))

        total_button_width = len(button_values) * button_width + (len(button_values) - 1) * button_margin

        self.window.fill((BACKGROUND_COLOR))   

        text1 = title_font.render("Izvēlies sākuma skaitli:", True, (0, 0, 0))
        text1_rect = text1.get_rect(center=(self.width // 2, 80))
        self.window.blit(text1, text1_rect)

        start_x = (self.width - total_button_width) // 2   

        button_rects = [] 
        
        for i, value in enumerate(button_values):
            button_x = start_x + i * (button_width + button_margin)
            button_y = 180  
            button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_rects.append(button_rect)   

            button_text = button_font.render(str(value), True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)

        pygame.display.update()

        while self.running:
           for event in pygame.event.get():
               if event.type == pygame.QUIT:
                   self.running = False
               elif event.type == pygame.MOUSEBUTTONDOWN:
                   if event.button == 1:
                      
                       for i, rect in enumerate(button_rects):
                           if rect.collidepoint(event.pos):
                               return button_values[i]

        pygame.quit()
    
    def algorithm_choice_screen(self):
    
        self.window.fill(BACKGROUND_COLOR)  
        title_font = pygame.font.Font(None, 50)  
        button_font = pygame.font.Font(None, 36)  

  
        title_surface = title_font.render('Izvēlieties Algoritmu:', True, (0, 0, 0))  
        title_rect = title_surface.get_rect(center=(self.width // 2, 50))
        self.window.blit(title_surface, title_rect)

    
        minimax_button = pygame.Rect((self.width - 150) // 4, 150, 150, 50)
        alpha_beta_button = pygame.Rect((self.width - 150) * 3 // 4, 150, 150, 50)

        
        pygame.draw.rect(self.window, BUTTON_COLOR, minimax_button)
        pygame.draw.rect(self.window, BUTTON_COLOR, alpha_beta_button)

  
        minimax_text = button_font.render('Minimax', True, (0, 0, 0))  
        alpha_beta_text = button_font.render('Alpha-Beta', True, (0, 0, 0))  
        self.window.blit(minimax_text, (minimax_button.x + 20, minimax_button.y + 10))
        self.window.blit(alpha_beta_text, (alpha_beta_button.x + 10, alpha_beta_button.y + 10))

        pygame.display.flip()  

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if minimax_button.collidepoint(event.pos):
                        return "minimax"
                    elif alpha_beta_button.collidepoint(event.pos):
                        return "alpha-beta"

    def game_screen(self, number, initial_player, algo):

        self.turn = initial_player
        self.score1 = 0
        self.score2 = 0
    
        both_numbers = number  
    
        text_font = pygame.font.Font(None, 45)  
        number_font = pygame.font.Font(None, 30)  
        score_font = pygame.font.Font(None, 24)  
    
        button_width = 60
        button_height = 35
        button_color = BUTTON_COLOR
        button_font = pygame.font.Font(None, 24)
    
        self.window.fill(BACKGROUND_COLOR)
    
        text1_x = 100
        text1_y = 100
    
        text2_x = 400
        text2_y = 100
    
  
        text1 = text_font.render("Spēlētājs", True, (0, 0, 0))
        text1_rect = text1.get_rect(topleft=(text1_x, text1_y))
        self.window.blit(text1, text1_rect)
    
        text2 = text_font.render("Dators", True, (0, 0, 0))
        text2_rect = text2.get_rect(topleft=(text2_x, text2_y))
        self.window.blit(text2, text2_rect)
    
        button1_x = 80
        button1_y = 150
    
        button2_x = 180
        button2_y = 150
    
        button3_x = 360
        button3_y = 150
    
        button4_x = 460
        button4_y = 150
    
    
        button_rects = []  
    
        button_rect = pygame.Rect(button1_x, button1_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x2", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)
    
        button_rect = pygame.Rect(button2_x, button2_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x3", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)
    
        button_rect = pygame.Rect(button3_x, button3_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x2", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)
    
        button_rect = pygame.Rect(button4_x, button4_y, button_width, button_height)
        pygame.draw.rect(self.window, button_color, button_rect)
        button_text = button_font.render("x3", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)
        button_rects.append(button_rect)
    
        
        window1_rect = pygame.Rect(80, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window1_rect)
        number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
        number1_text_rect = number1_text.get_rect(center=window1_rect.center)
        self.window.blit(number1_text, number1_text_rect)
    
       
        window2_rect = pygame.Rect(360, 200, 165, 50)
        pygame.draw.rect(self.window, (200, 200, 200), window2_rect)
        number2_text = number_font.render(str(both_numbers), True, (0, 0, 0))
        number2_text_rect = number2_text.get_rect(center=window2_rect.center)
        self.window.blit(number2_text, number2_text_rect)
    
        pygame.display.update()    

        def render_both_players():

            
            number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
            self.window.fill((200, 200, 200), rect=window1_rect)  
            self.window.blit(number1_text, number1_text_rect)

            pygame.display.update()
    
   
        self.turn = initial_player
        self.score1 = 0
        self.score2 = 0
    
      
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and self.turn == 'human':

                    for i, rect in enumerate(button_rects[:2]):
                        if rect.collidepoint(event.pos):
                            print(f"Button {i + 1} clicked!")
                            if i == 0:
                                both_numbers *= 2 
                            elif i == 1:
                                both_numbers *= 3 
    

                            if both_numbers % 2 == 0:
                                print("Pāra skaitlis!")
                                self.score1 += 1
                            else:
                                print("Nepāra skaitlis!")
                                self.score1 -= 1
    

                            render_both_players()
    

                            self.turn = 'computer'
                            break
                        
                if self.turn == 'computer':
                    print("Dators domā...")
                    pygame.display.update()
                    pygame.time.delay(1000)  
    
                    if isinstance(algo, MinimaxAlgorithm):
                                best_eval, best_move = algo.minimax(both_numbers, both_numbers, self.score1, self.score2, 'computer', 3, False)
                    elif isinstance(algo, AlphaBetaAlgorithm):
                                best_eval, best_move = algo.minimax(both_numbers, both_numbers, self.score1, self.score2, 'computer', 3, float('-inf'), float('inf'), False)
    
                    if best_move:
                        both_numbers = algo.make_move(both_numbers, best_move)
                        self.score2 = algo.update_score(self.score2, both_numbers)

                    render_both_players()

                    self.turn = 'human'
    
                if both_numbers >= 1000:
                    print("Uz redzēšanos!")

                    running = False
                    return self.score1, self.score2

            self.window.fill(BACKGROUND_COLOR)
    
            text1 = text_font.render("Spēlētājs", True, (0, 0, 0))
            text1_rect = text1.get_rect(topleft=(text1_x, text1_y))
            self.window.blit(text1, text1_rect)
    
            text2 = text_font.render("Dators", True, (0, 0, 0))
            text2_rect = text2.get_rect(topleft=(text2_x, text2_y))
            self.window.blit(text2, text2_rect)
    
            button_rect = pygame.Rect(button1_x, button1_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x2", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button2_x, button2_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x3", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button3_x, button3_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x2", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            button_rect = pygame.Rect(button4_x, button4_y, button_width, button_height)
            pygame.draw.rect(self.window, button_color, button_rect)
            button_text = button_font.render("x3", True, (0, 0, 0))
            button_text_rect = button_text.get_rect(center=button_rect.center)
            self.window.blit(button_text, button_text_rect)
    
            window1_rect = pygame.Rect(200, 200, 250, 50)
            pygame.draw.rect(self.window, (200, 200, 200), window1_rect)
            number1_text = number_font.render(str(both_numbers), True, (0, 0, 0))
            number1_text_rect = number1_text.get_rect(center=window1_rect.center)
            self.window.blit(number1_text, number1_text_rect)
    
            score_text = score_font.render(f"Spēlētāja rezultāts: {self.score1}   Datora rezultāts: {self.score2}", True, (0, 0, 0))
            score_text_rect = score_text.get_rect(center=(self.window.get_width() // 2, 300))
            self.window.blit(score_text, score_text_rect)
    
            pygame.display.update()


    def winner_screen(self, human_score, pc_score):

        if score1 < score2:
            text = "Spēlētājs uzvarēja!"  
        elif score1 > score2:
            text = "Dators uzvarēja!"  
        else:
            text = "Neizšķirts!"  

        text_x = 300
        text_y = 85

        text1_x = 150
        text1_y = 160

        text2_x = 450
        text2_y = 160

        window1_x = 100
        window1_y = 200

        window2_x = 420
        window2_y = 200

        button_x = 200
        button_y = 280
        button_width = 200
        button_height = 50

        self.window.fill(BACKGROUND_COLOR)
        headline_text = pygame.font.Font(None, 45)
        text_surface = headline_text.render(text, True, (0, 0, 0))

        text_font = pygame.font.Font(None, 35)
        
        text_rect = text_surface.get_rect(center=(text_x, text_y))
        self.window.blit(text_surface, text_rect)

        text_surface = text_font.render("Spēlētāja rezultāts", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(text1_x, text1_y))
        self.window.blit(text_surface, text_rect)

        text_surface = text_font.render("Datora rezultāts", True, (0, 0, 0))
        text_rect = text_surface.get_rect(center=(text2_x, text2_y))
        self.window.blit(text_surface, text_rect)

        number_font = pygame.font.Font(None, 24)

        window1_rect = pygame.Rect(window1_x, window1_y, 90, 35)
        pygame.draw.rect(self.window, (255, 255, 255), window1_rect)  
        human_score_surface = number_font.render(str(human_score), True, (0, 0, 0))
        number_rect = human_score_surface.get_rect(center=window1_rect.center)
        self.window.blit(human_score_surface, number_rect.topleft)

        window2_rect = pygame.Rect(window2_x, window2_y, 90, 35)
        pygame.draw.rect(self.window, (255, 255, 255), window2_rect)  
        pc_score_surface = number_font.render(str(pc_score), True, (0, 0, 0))
        number_rect = pc_score_surface.get_rect(center=window2_rect.center)
        self.window.blit(pc_score_surface, number_rect.topleft)

  
        button_rect = pygame.Rect(button_x, button_y, button_width, button_height)
        pygame.draw.rect(self.window, (BUTTON_COLOR), button_rect) 
        button_text = text_font.render("Turpināt?", True, (0, 0, 0))
        button_text_rect = button_text.get_rect(center=button_rect.center)
        self.window.blit(button_text, button_text_rect)

        pygame.display.flip()  

        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    waiting = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if button_rect.collidepoint(event.pos):
                        self.reset_game()
                        waiting = False

        pygame.quit()


        
if __name__ == "__main__":

    game = GameWindow()
    
    while game.running:
        
        game = GameWindow()
        initial_player = game.welcome_screen()
        start_number = game.choice_screen()
        algorithm_choice = game.algorithm_choice_screen()

        if algorithm_choice == "minimax":
            algo = MinimaxAlgorithm()
        else:
            algo = AlphaBetaAlgorithm()

        score1, score2 = game.game_screen(start_number, initial_player, algo)
        game.winner_screen(score1, score2)
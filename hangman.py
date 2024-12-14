import pygame

import math
import random
from solver import generate_valid_words, generate_best_letters


class HangmanGame:
    """
    A class representing the Hangman game with a graphical interface and solver hints.
    """

    def __init__(self):
        # Initialize Pygame and window settings
        pygame.init()
        self.WIDTH, self.HEIGHT = 1000, 700
        self.win = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Jeu du Pendu")

        # Game constants
        self.FPS = 60
        self.BUTTON_RADIUS = 24
        self.BUTTON_SPACE = 20
        self.MAX_TRIES = 6  # Maximum wrong attempts before game over

        # Initialize game components
        self._init_fonts()
        self._load_images()
        self._create_letter_buttons()
        self._create_footer_buttons()
        self._init_game_state()

        # Load word dictionary
        self.word_dict = {
            length: self._read_words_from_file(length)
            for length in range(6, 11)
        }

    def _init_fonts(self):
        """Initialize all font objects used in the game."""
        self.fonts = {
            'regular': pygame.font.SysFont("comicsans", 45),
            'word': pygame.font.SysFont("comicsans", 40),
            'title': pygame.font.SysFont("comicsans", 70),
            'footer': pygame.font.SysFont("comicsans", 30),
            'hint': pygame.font.SysFont("comicsans", 30)
        }

    def _load_images(self):
        """Load hangman state images."""
        self.images = [
            pygame.image.load(f"pictures/Hangman-{i}.png")
            for i in range(7)
        ]

    def _create_letter_buttons(self):
        """Create clickable letter buttons for the game."""
        self.letters = []
        x_start = round((self.WIDTH - (self.BUTTON_RADIUS * 2 + self.BUTTON_SPACE) * 13) / 2)
        y_start = 540

        for i in range(26):
            x = x_start + self.BUTTON_SPACE * 2 + ((self.BUTTON_RADIUS * 2 + self.BUTTON_SPACE) * (i % 13))
            y = y_start + ((i // 13) * (self.BUTTON_SPACE + self.BUTTON_RADIUS * 2))
            self.letters.append([x, y, chr(65 + i), True])  # x, y, letter, visible

    def _create_footer_buttons(self):
        """Create footer buttons for game control."""
        self.footer_buttons = {
            "Nouvelle Partie": pygame.Rect(self.WIDTH - 400, self.HEIGHT - 60, 180, 40),
            "Quitter": pygame.Rect(self.WIDTH - 140, self.HEIGHT - 60, 100, 40)
        }

    def _read_words_from_file(self, length):
        """Read words of specified length from dictionary file."""
        try:
            with open(f"data/dico_{length}_lettres.txt", "r") as file:
                return file.read().splitlines()
        except FileNotFoundError:
            print(f"Dictionary for {length} letters not found.")
            return []

    def _init_game_state(self):
        """Initialize or reset the game state."""
        self.hangman = 0
        self.word_dict = {length: self._read_words_from_file(length=length) for length in range(6, 11)}
        self.word_length = random.choice([6, 7, 8, 9, 10])
        self.secret_word = random.choice(self.word_dict[self.word_length])
        self.guessed = []
        self.correct_guess = []
        self.wrong_guess = []
        # Reset letter buttons
        for letter in self.letters:
            letter[3] = True
        self._update_solver_hint()

    def _handle_letter_click(self, x, y, letter):
        """
        Handle clicking on a letter button.

        Args:
            x (int): Mouse x position
            y (int): Mouse y position
            letter (list): Letter button [x, y, letter, visible]

        Returns:
            bool: True if letter was clicked, False otherwise
        """
        button_x, button_y, ltr, visible = letter
        if not visible:
            return False

        # Check if click is within button radius
        dist = math.sqrt((button_x - x) ** 2 + (button_y - y) ** 2)
        if dist <= self.BUTTON_RADIUS:
            letter[3] = False  # Hide the button
            self.guessed.append(ltr)

            if ltr in self.secret_word:
                # Add correct guess with positions
                positions = [pos for pos, char in enumerate(self.secret_word) if char == ltr]
                for pos in positions:
                    self.correct_guess.append((ltr, pos))
            else:
                self.wrong_guess.append(ltr)
                self.hangman += 1

            self._update_solver_hint()
            return True
        return False

    def _check_game_state(self):
        """
        Check if the game is won or lost and handle the game state accordingly.
        """
        # Check for win condition
        won = all(letter in self.guessed for letter in self.secret_word)

        if won:
            self._show_game_end_screen("C'est gagné!", (129, 255, 0))
            pygame.time.delay(2000)
            self._init_game_state()
            return

        # Check for loss condition
        if self.hangman >= self.MAX_TRIES:
            self._show_game_end_screen(
                f"C'est perdu! Le mot était {self.secret_word}",
                (255, 0, 0)
            )
            pygame.time.delay(2000)
            self._init_game_state()

    def _show_game_end_screen(self, message, color):
        """
        Display the game end screen with the given message and color.

        Args:
            message (str): Message to display
            color (tuple): RGB color tuple for the message
        """
        self.win.fill((255, 255, 255))
        text = self.fonts['word'].render(message, 1, color)
        text_rect = text.get_rect(center=(self.WIDTH / 2, self.HEIGHT / 2))
        self.win.blit(text, text_rect)
        pygame.display.update()

    def _update_solver_hint(self):
        """Update the solver hint based on current game state."""
        valid_words = generate_valid_words(
            self.word_dict[self.word_length],
            self.correct_guess,
            self.wrong_guess
        )
        possible_letters = [ltr for _, _, ltr, visible in self.letters if visible]
        best_letter_message = generate_best_letters(
            valid_words,
            possible_letters,
            self.correct_guess,
            self.wrong_guess
        )
        self.solver_hint = best_letter_message

    def draw(self):
        """Draw the game state to the screen."""
        # Clear screen
        self.win.fill((255, 255, 255))

        # Draw title
        title = self.fonts['title'].render("Jeu du Pendu", 1, (0, 0, 0))
        self.win.blit(title, (self.WIDTH / 1.9 - title.get_width() / 2, 10))

        # Draw word
        displayed_word = " ".join(letter if letter in self.guessed else "_" for letter in self.secret_word)
        text = self.fonts['word'].render(displayed_word, 1, (0, 0, 0))
        self.win.blit(text, (500, 250))

        # Draw solver hint
        hint_rect = pygame.Rect(300, 400, 600, 100)
        pygame.draw.rect(self.win, (200, 200, 200), hint_rect)
        hint_text = self.fonts['hint'].render(self.solver_hint, 1, (0, 0, 0))
        self.win.blit(hint_text, (hint_rect.x + 10, hint_rect.y + 10))

        # Draw letter buttons
        for btn_pos in self.letters:
            x, y, ltr, visible = btn_pos
            if visible:
                pygame.draw.circle(self.win, (0, 0, 0), (x, y), self.BUTTON_RADIUS, 3)
                text = self.fonts['regular'].render(ltr, 1, (0, 0, 0))
                self.win.blit(text, (x - text.get_width() / 2, y - text.get_height() / 2))

        # Draw footer buttons
        for name, rect in self.footer_buttons.items():
            pygame.draw.rect(self.win, (200, 200, 200), rect)
            text = self.fonts['footer'].render(name.replace('_', ' ').title(), 1, (0, 0, 0))
            self.win.blit(text, (rect.x + 10, rect.y + 5))

        # Draw hangman
        self.win.blit(self.images[self.hangman], (50, 50))
        pygame.display.update()

    def handle_click(self, pos):
        """Handle mouse click events."""
        x, y = pos

        # Check footer buttons
        if self.footer_buttons["Nouvelle Partie"].collidepoint(x, y):
            self._init_game_state()
            return True
        if self.footer_buttons["Quitter"].collidepoint(x, y):
            return False

        # Check letter buttons
        for letter in self.letters:
            if self._handle_letter_click(x, y, letter):
                break

        return True

    def run(self):
        """Main game loop."""
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(self.FPS)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    running = self.handle_click(pygame.mouse.get_pos())

            self._check_game_state()

        pygame.quit()


if __name__ == "__main__":
    game = HangmanGame()
    game.run()
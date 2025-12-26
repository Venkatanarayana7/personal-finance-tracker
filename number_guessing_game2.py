import random

# Global constant for consistent formatting
HEADER_WIDTH = 72  # Base width, will adjust dynamically

def get_max_line_length(game_history):
    """
    Calculate the maximum length among all display lines
    Returns the optimal width for consistent formatting
    """
    if not game_history:
        return HEADER_WIDTH
    
    max_length = 0
    for target, guesses in game_history.items():
        line = f"🎯 Target: {target:02d} | 📊 Guesses: {guesses} 🎯"
        current_length = len(line)
        if current_length > max_length:
            max_length = current_length
    
    # Return the larger of: max line length or base header width
    # Add some padding for better visual appearance
    return max(max_length + 4, HEADER_WIDTH)

def center_text(text, width):
    """Helper function to center text with proper padding"""
    return text.center(width)

def get_difficulty():
    """
    Strict difficulty input validation
    Ensures player enters only 'easy', 'medium', or 'hard'
    """
    while True:
        print(center_text("🎯 Choose difficulty (easy/medium/hard) 🎯", HEADER_WIDTH))
        difficulty = input(center_text("👉 Your choice: ", HEADER_WIDTH)).lower().strip()
        
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print(center_text("❌ Invalid choice! Please enter only 'easy', 'medium', or 'hard' ❌", HEADER_WIDTH))
            print(center_text("   Let's try again...\n", HEADER_WIDTH))

def get_guess_within_range(max_range, display_width):
    """
    Restricts player to select numbers only within specified range
    """
    while True:
        try:
            prompt = center_text(f"🔢 Enter your guess (1-{max_range}) 🔢", display_width)
            guess = int(input(prompt))
            if 1 <= guess <= max_range:
                return guess
            else:
                print()
                error_msg = center_text(f"❌ Please enter a number between 1 and {max_range} only! ❌\n", display_width)
                print(error_msg)
        except ValueError:
            print()
            error_msg = center_text(f"❌ Please enter a valid number! ❌\n", display_width)
            print(error_msg)

def play_game():
    # Using the new validated difficulty function
    difficulty = get_difficulty()

    # Set game parameters based on chosen difficulty
    if difficulty == "easy":
        max_range, max_attempts = 10, 7  # Easy: smaller range, more attempts
        print(center_text("🎯 Easy mode selected: Numbers 1-10, 7 attempts 🎯", HEADER_WIDTH))
    elif difficulty == "medium":
        max_range, max_attempts = 15, 5  # Medium: medium range, medium attempts
        print(center_text("🎯 Medium mode selected: Numbers 1-15, 5 attempts 🎯", HEADER_WIDTH))
    else:  # hard
        max_range, max_attempts = 20, 3  # Hard: larger range, fewer attempts
        print(center_text("🎯 Hard mode selected: Numbers 1-20, 3 attempts 🎯", HEADER_WIDTH))

    # Generating random target number for the player to guess
    target = random.randint(1, max_range)
    guesses = []
    initial_attempts = max_attempts  # Store initial attempts for display
    
    # Displays game information to player at initial
    print(center_text(f"🎮 Guess a number between 1 and {max_range} 🎮\n", HEADER_WIDTH))
    print(center_text(f"📊 You have total {max_attempts} attempts 📊\n", HEADER_WIDTH))

    # Game loop continues until attempts run out
    while max_attempts > 0:
        # Show remaining attempts
        current_attempt = initial_attempts - max_attempts + 1
        print(center_text(f"📈 Attempt {current_attempt}/{initial_attempts} 📈", HEADER_WIDTH))
        
        # Get validated guess within range
        guess = get_guess_within_range(max_range, HEADER_WIDTH)

        # Store guess and decrement attempts
        guesses.append(guess)
        max_attempts -= 1
  
        # Check if player guessed correctly
        if guess == target:
            print(center_text(f"🎉 Congratulations! You guessed it in {len(guesses)} attempts! 🎉", HEADER_WIDTH))
            break
        elif guess > target:
            print(center_text(f"📈 Too high! Try a lower number. 📈", HEADER_WIDTH))
        else:
            print(center_text(f"📉 Too low! Try a higher number. 📉", HEADER_WIDTH))
            
        # Show remaining attempts after each guess
        if max_attempts > 0:
            print(center_text(f"🔄 {max_attempts} attempts remaining 🔄\n\n\n\n", HEADER_WIDTH))
    else:
        # Executes only when player runs out of attempts
        print(f"\n\n\n")
        print(center_text(f"💔 Game Over! The number was {target}. 💔", HEADER_WIDTH))
        print(center_text(f"📝 Your guesses: {guesses} 📝", HEADER_WIDTH))

    # Return game results as dictionary
    return {target: guesses}

def display_game_history(game_history):
    """
    Display formatted history of all games played
    """
    if not game_history:
        print(center_text("📭 No game history available.", HEADER_WIDTH))
        return HEADER_WIDTH

    # 🆕 Calculate optimal width based on content
    display_width = get_max_line_length(game_history)
    
    lines = []
    max_length = 0

    # Process each game for formatting
    for target, guesses in game_history.items():
        line = f"🎯 Target: {target:02d} | 📊 Guesses: {guesses} 🎯"
        lines.append(line)

    # Create formatted header
    header = " 🎮 GAME HISTORY 🎮 ".center((display_width-2), '=')
    print('\n' + header)
    
    # Display each game
    for line in lines:
        print(center_text(line, display_width))
        
    # Footer with thanks
    print("".center(display_width, '='))
    print()
    print(center_text('🙏 Thank you for playing! 🙏', display_width))
    
    # Signature line
    end_line = " 👨‍💻 GUVVALA VENKATA NARAYANA 👨‍💻 ".center((display_width-20), '⭐')
    print('\n' + end_line)
    
    return display_width  # 🆕 Return the calculated width for consistency

def get_user_choice(display_width):
    """
    Strict menu choice validation
    Player can only select 1, 2, or 3
    Uses consistent width from display_width parameter
    """
    while True:
        print("".center(display_width, '='))  # 🆕 Use consistent width
        print(center_text("🔄 What would you like to do next?", display_width))
        print(center_text("1. 🎮 Play another game 🎮", display_width))
        print(center_text("2. 📊 View current game history 📊", display_width))
        print(center_text("3. 🚪 Quit and see final results 🚪", display_width))
        print("".center(display_width, '='))  # 🆕 Use consistent width
        
        choice = input(center_text("👉 Enter your choice (1/2/3): ", display_width)).strip()
        print()
        if choice in ('1', '2', '3'):
            return choice
        else:
            print(center_text("❌ Invalid input! Please enter only 1, 2, or 3 ❌", display_width))

def main():
    """
    Main game controller with perfect flow control
    """
    game_history = {}
    current_display_width = HEADER_WIDTH  # 🆕 Track current display width
    
    print(center_text("🎉 Welcome to The Best Number Guessing Game! 🎉", HEADER_WIDTH))
    print("".center(HEADER_WIDTH, '='))
    
    while True:
        # Play one complete game
        result = play_game()
        game_history.update(result)
        
        # 🆕 Calculate optimal display width based on current game history
        current_display_width = get_max_line_length(game_history)
        
        # Get user's next action with validation
        while True:
            choice = get_user_choice(current_display_width)  # 🆕 Pass width as parameter
            
            if choice == '1':  # Play another game
                print(center_text("🔄 Starting new game... 🔄", current_display_width))
                print("".center(current_display_width, '-'))
                break
            elif choice == '2':  # View current history
                print("\n" + "📊 CURRENT GAME HISTORY 📊".center((current_display_width-2), '='))
                # 🆕 Update width based on display (in case it changed)
                current_display_width = display_game_history(game_history)
            elif choice == '3':  # Quit
                print("\n" + "🏁 FINAL GAME RESULTS 🏁".center((current_display_width-2), '='))
                display_game_history(game_history)
                print()
                print(center_text("👋 Thanks for playing! Goodbye! 👋", current_display_width))
                return

if __name__ == "__main__":
    main()
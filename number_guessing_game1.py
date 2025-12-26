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

def get_difficulty():
    """
    Strict difficulty input validation
    Ensures player enters only 'easy', 'medium', or 'hard'
    """
    while True:
        difficulty = input("🎯 Choose difficulty (easy/medium/hard)🎯: ").lower().strip()
        
        if difficulty in ['easy', 'medium', 'hard']:
            return difficulty
        else:
            print(f"\n❌ Invalid choice! Please enter only 'easy', 'medium', or 'hard' ❌\n   Let's try again...\n")

def get_guess_within_range(max_range):
    """
    Restricts player to select numbers only within specified range
    """
    while True:
        try:
            guess = int(input(f"🔢 Enter your guess (1-{max_range}) 🔢: "))
            if 1 <= guess <= max_range:
                return guess
            else:
                print(f"\n❌ Please enter a number between 1 and {max_range} only! ❌\n")
        except ValueError:
            print(f"\n❌ Please enter a valid number! ❌\n")

def play_game():
    # Using the new validated difficulty function
    difficulty = get_difficulty()

    # Set game parameters based on chosen difficulty
    if difficulty == "easy":
        max_range, max_attempts = 10, 7  # Easy: smaller range, more attempts
        print("🎯 Easy mode selected: Numbers 1-10, 7 attempts 🎯")
    elif difficulty == "medium":
        max_range, max_attempts = 15, 5  # Medium: medium range, medium attempts
        print("🎯 Medium mode selected: Numbers 1-15, 5 attempts 🎯")
    else:  # hard
        max_range, max_attempts = 20, 3  # Hard: larger range, fewer attempts
        print("🎯 Hard mode selected: Numbers 1-20, 3 attempts 🎯")

    # Generating random target number for the player to guess
    target = random.randint(1, max_range)
    guesses = []
    initial_attempts = max_attempts  # Store initial attempts for display
    
    # Displays game information to player at initial
    print(f"\n🎮 Guess a number between 1 and {max_range} 🎮")
    print(f"📊 You have total {max_attempts} attempts 📊")

    # Game loop continues until attempts run out
    while max_attempts > 0:
        # Show remaining attempts
        current_attempt = initial_attempts - max_attempts + 1
        print(f"\n📈 Attempt {current_attempt}/{initial_attempts} 📈")
        
        # Get validated guess within range
        guess = get_guess_within_range(max_range)

        # Store guess and decrement attempts
        guesses.append(guess)
        max_attempts -= 1
  
        # Check if player guessed correctly
        if guess == target:
            print(f"🎉 Congratulations! You guessed it in {len(guesses)} attempts!")
            break
        elif guess > target:
            print("📈 Too high! Try a lower number. 📈")
        else:
            print("📉 Too low! Try a higher number. 📉")
            
        # Show remaining attempts after each guess
        if max_attempts > 0:
            print(f"🔄 {max_attempts} attempts remaining 🔄")
    else:
        # Executes only when player runs out of attempts
        print(f"\n💔 Game Over! The number was {target}. 💔")
        print(f"📝 Your guesses: {guesses} 📝")

    # Return game results as dictionary
    return {target: guesses}

def display_game_history(game_history):
    """
    Display formatted history of all games played
    """
    if not game_history:
        print("📭 No game history available.")
        return

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
        print(line)
        
    # Footer with thanks
    print("".center(display_width, '='))
    print('\n🙏 Thank you for playing! 🙏')
    
    # Signature line
    end_line = " 👨‍💻 GUVVALA VENKATA NARAYANA 👨‍💻 ".center((display_width-19), '⭐')
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
        print("🔄 What would you like to do next?")
        print("1. 🎮 Play another game 🎮")
        print("2. 📊 View current game history 📊") 
        print("3. 🚪 Quit and see final results 🚪")
        print("".center(display_width, '='))  # 🆕 Use consistent width
        
        choice = input("👉 Enter your choice (1/2/3): ").strip()
        
        if choice in ('1', '2', '3'):
            return choice
        else:
            print("\n❌ Invalid input! Please enter only 1, 2, or 3 ❌")

def main():
    """
    Main game controller with perfect flow control
    """
    game_history = {}
    current_display_width = HEADER_WIDTH  # 🆕 Track current display width
    
    print("🎉 Welcome to The Best Number Guessing Game! 🎉".center(HEADER_WIDTH))
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
                print("\n" + "🔄 Starting new game...".center(current_display_width, '-'))
                break
            elif choice == '2':  # View current history
                print("\n" + "📊 CURRENT GAME HISTORY 📊".center(current_display_width, '='))
                # 🆕 Update width based on display (in case it changed)
                current_display_width = display_game_history(game_history)
            elif choice == '3':  # Quit
                print("\n" + "🏁 FINAL GAME RESULTS 🏁".center((current_display_width-2), '='))
                display_game_history(game_history)
                print("\n👋 Thanks for playing! Goodbye!".center(current_display_width))
                return

if __name__ == "__main__":
    main()
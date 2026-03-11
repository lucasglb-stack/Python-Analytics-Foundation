# Electrical Units Game

import random

def play_units_game():
    """
    An interactive CLI game to guess the units of measurement 
    for various electrical properties.
    """
    electrical_properties = {
        "Voltage (Tensão)": "Volt",
        "Electric Current (Corrente)": "Ampere",
        "Resistance (Resistência)": "Ohm",
        "Active Power (Potência Ativa)": "Watt",
        "Apparent Power (Potência Aparente)": "Volt-Ampere",
        "Capacitance (Capacitância)": "Farad",
        "Inductance (Indutância)": "Henry",
        "Frequency (Frequência)": "Hertz",
        "Energy (Energia)": "Joule"
    }

    correct_answers = 0
    rounds_played = 0
    
    # Extract properties and shuffle them
    properties_list = list(electrical_properties.keys())
    random.shuffle(properties_list)

    print("--- Welcome to the Electrical Units Game! ---")

    for property_name in properties_list:
        rounds_played += 1
        unit = electrical_properties[property_name]
        
        print(f"\nWhat is the standard unit for {property_name}?")
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == unit.lower():
            print("✅ Correct answer!")
            correct_answers += 1
        else:
            print(f"❌ Wrong answer! The correct unit is {unit}.")

        # Ask to continue
        while True:
            choice = input("\nDo you want to continue? (y/n): ").strip().lower()
            if choice in ['y', 'n']:
                break
            print("Please, answer only 'y' for yes or 'n' for no.")
            
        if choice == 'n':
            break

    # Calculate and display final score
    if rounds_played > 0:
        win_rate = (correct_answers / rounds_played) * 100
        print("\n--- Game Over ---")
        print(f"You got {correct_answers} out of {rounds_played} questions right.")
        print(f"Your win rate was {win_rate:.2f}%!")

if __name__ == "__main__":
    play_units_game()

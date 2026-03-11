# Vowel Counter

def count_vowels(text):
    """
    Counts the occurrences of each vowel in a given text, 
    ignoring case sensitivity. Useful for basic text parsing.
    """
    vowel_counts = {vowel: 0 for vowel in 'AEIOU'}
    
    for char in text.upper():
        if char in vowel_counts:
            vowel_counts[char] += 1
            
    return vowel_counts

if __name__ == "__main__":
    # Sample text related to the energy sector
    energy_text = """
    Smart grids use digital communications technology to detect and react to 
    local changes in usage. They improve the efficiency, reliability, and 
    economics of the production and distribution of electricity.
    """
    
    results = count_vowels(energy_text)
    
    print("--- Vowel Count in Energy Text ---")
    for vowel, count in results.items():
        print(f"There are {count} '{vowel}' letters in the text.")

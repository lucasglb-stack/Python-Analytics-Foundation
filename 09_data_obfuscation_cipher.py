"""
09_data_obfuscation_cipher.py
Implementation of the Caesar Cipher algorithm. Demonstrates string manipulation, 
indexing, and basic data obfuscation techniques (useful for anonymizing sensitive IDs).
"""

# ==========================================
# METHOD 1: The "Pythonic" Way (Using Modulo)
# ==========================================
def cipher_modulo(text, shift_key):
    """
    Encrypts/Decrypts text using the modulo operator. 
    Python's modulo gracefully handles keys > 26 or < -26.
    """
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    obfuscated_result = ""

    for char in text:
        if char in lower_alphabet:
            new_index = (lower_alphabet.index(char) + shift_key) % 26
            obfuscated_result += lower_alphabet[new_index]
            
        elif char in upper_alphabet:
            new_index = (upper_alphabet.index(char) + shift_key) % 26
            obfuscated_result += upper_alphabet[new_index]
            
        else:
            # Keeps spaces, numbers, and punctuation unchanged
            obfuscated_result += char 
            
    return obfuscated_result


# ==========================================
# METHOD 2: The Logical Loop Way
# ==========================================
def wrap_index(current_index, sequence_length, shift_key):
    """
    Helper function to wrap around the alphabet index manually using while loops.
    """
    new_index = current_index + shift_key
    
    while new_index >= sequence_length:
        new_index -= sequence_length
        
    while new_index < 0:
        new_index += sequence_length
        
    return new_index

def cipher_loops(text, shift_key):
    """
    Alternative implementation without the modulo operator.
    """
    lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
    upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    obfuscated_result = ""

    for char in text:
        if char in lower_alphabet:
            new_idx = wrap_index(lower_alphabet.index(char), 26, shift_key)
            obfuscated_result += lower_alphabet[new_idx]
            
        elif char in upper_alphabet:
            new_idx = wrap_index(upper_alphabet.index(char), 26, shift_key)
            obfuscated_result += upper_alphabet[new_idx]
            
        else:
            obfuscated_result += char
            
    return obfuscated_result


# ==========================================
# USAGE EXAMPLE: Anonymizing Client Asset IDs
# ==========================================
if __name__ == "__main__":
    # Example: Anonymizing a client ID or a smart meter serial number
    original_id = "Client-Alpha: XJ-900"
    security_key = 3
    
    # Encrypting
    encrypted_id = cipher_modulo(original_id, security_key)
    print(f"Original ID:  {original_id}")
    print(f"Encrypted ID: {encrypted_id} (Key: +{security_key})")
    
    # Decrypting (shifting backwards)
    decrypted_id = cipher_loops(encrypted_id, -security_key)
    print(f"Decrypted ID: {decrypted_id} (Key: -{security_key})")
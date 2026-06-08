import pandas as pd

GEMATRIA_MAP = {
    'ا': 1, 'أ': 1, 'إ': 1, 'آ': 1, 'ب': 2, 'ج': 3, 'د': 4, 'ه': 5, 'و': 6, 'ز': 7, 'ح': 8, 'ط': 9,
    'ي': 10, 'ى': 10, 'ك': 20, 'ل': 30, 'م': 40, 'ن': 50, 'س': 60, 'ع': 70, 'ف': 80, 'ص': 90,
    'ق': 100, 'ر': 200, 'ش': 300, 'ت': 400, 'ث': 500, 'خ': 600, 'ذ': 700, 'ض': 800, 'ظ': 900, 'غ': 1000,
    'ة': 400, 'ؤ': 6, 'ئ': 10, 'ء': 1
}

ELEMENTS = {
    1: "ناري (Fire)",
    2: "ترابي (Earth)",
    3: "هوائي (Air)",
    0: "مائي (Water)"
}

def calculate_gematria(text):
    # Remove spaces
    text = text.replace(" ", "")
    total = sum(GEMATRIA_MAP.get(char, 0) for char in text)
    element = ELEMENTS[total % 4]
    return total, element

def calculate_compatibility(name1, name2):
    val1, _ = calculate_gematria(name1)
    val2, _ = calculate_gematria(name2)
    
    if val1 > val2:
        winner = name1
    elif val2 > val1:
        winner = name2
    else:
        winner = "تعادل (Equality)"
    
    return val1, val2, winner

def generate_magic_square(input_val):
    # User requested: Starting number = (Input - 8) / 3
    # This is for a 3x3 square where the sum of each row/column/diagonal equals the input.
    # In a standard 3x3 square, the sum is 3 * middle_number.
    # The middle number is (input / 3).
    # The smallest number (Miftah) is (input - 12) / 3 for a standard 1-increment square.
    # The user specifically asked for (Input - 8) / 3. We will follow that.
    
    miftah = (input_val - 12) / 3 # Standard 3x3
    # If the user specifically said (Input - 8) / 3, let's check if that's a typo or a specific variant.
    # Usually it's (Sum - 12) / 3. Let's provide a flexible version or follow user prompt.
    # Prompt says: Starting number = (Input - 8) / 3.
    start = (input_val - 8) / 3
    
    # 3x3 Square layout:
    # 8 1 6
    # 3 5 7
    # 4 9 2
    # We add 'start - 1' to each base number
    base = [
        [8, 1, 6],
        [3, 5, 7],
        [4, 9, 2]
    ]
    
    offset = start - 1
    square = [[cell + offset for cell in row] for row in base]
    return square

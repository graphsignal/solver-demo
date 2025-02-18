'''
Problem id: 1008-A
Statement: Vitya has just started learning Berlanese language. It is known that Berlanese uses the Latin alphabet. Vowel letters are "a", "o", "u", "i", and "e". Other letters are consonant.

In Berlanese, there has to be a vowel after every consonant, but there can be any letter after any vowel. The only exception is a consonant "n"; after this letter, there can be any letter (not only a vowel) or there can be no letter at all. For example, the words "harakiri", "yupie", "man", and "nbo" are Berlanese while the words "horse", "king", "my", and "nz" are not.

Help Vitya find out if a word $$$s$$$ is Berlanese.

The first line of the input contains the string $$$s$$$ consisting of $$$|s|$$$ ($$$1\leq |s|\leq 100$$$) lowercase Latin letters.

Print "YES" (without quotes) if there is a vowel after every consonant except "n", otherwise print "NO".

You can print each letter in any case (upper or lower).

In the first and second samples, a vowel goes after each consonant except "n", so the word is Berlanese.

In the third sample, the consonant "c" goes after the consonant "r", and the consonant "s" stands on the end, so the word is not Berlanese.
Tags: implementation,strings,*900
'''

def is_berlanese(s: str) -> str:
    vowels = {'a', 'o', 'u', 'i', 'e'}
    length = len(s)
    
    # Iterate through the string except the last character
    for i in range(length - 1):
        
        # If current character is a consonant (excluding 'n')
        if s[i] not in vowels and s[i] != 'n':
            # Check if the next character is not a vowel
            if s[i + 1] not in vowels:
                return "NO"
    
    # Check the last character separately
    if length > 0 and s[-1] not in vowels and s[-1] != 'n':
        return "NO"

    return "YES"

# Test cases and verification

def verify(result, expected):
    if result == expected:
        print("verified")
    else:
        print(f"Incorrect: got {result}, expected {expected}")

# Verification of the solution
verify(is_berlanese("harakiri"), "YES")  # Vowel after each consonant
verify(is_berlanese("yupie"), "YES")     # Vowel after each consonant
verify(is_berlanese("horse"), "NO")     # 'r' does not have a vowel after it
verify(is_berlanese("king"), "NO")      # 'g' does not have a vowel after it
verify(is_berlanese("my"), "NO")        # 'm' does not have a vowel after it
verify(is_berlanese("nz"), "NO")        # 'n' can be last, but 'z' can't be
verify(is_berlanese("nan"), "YES")      # 'n' can be last or followed by any character
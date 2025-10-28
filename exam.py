"""
Write a python program that:
1. Accepts a sentence input from the user
2. Separate the sentence into individual words
3. For each word in the sentence:
    * if the word starts with a vowel, covert it to uppercase.
    * if the word starts with a consonant, convert it to lowercase.
4. Count how many words start with a vowel and how many with a consonant.
5. Display the transformed sentence and the total count of vowel and consonant.

Sample Output:

Enter a sentence: Programming is an awesome and fun activity to do!

Transformed Word: programming IS AN AWESOME AND fun ACTIVITY to do!
Words starting with vowel: 5
Words starting with consonant: 4
"""


user = input("Enter a sentence: ").lower()
word = user.split()

for ch in word:
    if ch == ['a', 'e', 'i', 'o', 'u']:

        print(f"Transformed Word: ")


user = input("Enter a sentence: ")
word = user.split()
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
vowelcount = 0
consonantcount = 0
transformed = []

for word in word:
    if word[0] in vowels:  
        transformed.append(word.upper())
        vowel_count += 1
    else: 
        transformed.append(word.lower())
        consonant_count += 1

print("\nTransformed Word:", " ".join(transformed))
print("Words starting with vowel:", vowelcount)
print("Words starting with consonant:", consonantcount)

from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries):
    shorted_lenght = min(countries, key=len)
    shortest_names = []
    for country in countries:
        if len(country) == len(shorted_lenght):
            shortest_names.append(country)
    return shortest_names

def most_vowels(countries):
    vowels = ["A", "E", "I", "O", "U","a", "e", "i", "o", "u"]
    max_vowels_count = []
    for country in countries:
        vow_len = len([char for char in country if char in vowels])
        max_vowels_count.append((vow_len, country))
        max_vowels_count.sort(reverse=True)
    return max_vowels_count[:3]

def alphabet_set(countries):
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    found_countries = []
    for country in countries:
        for char in country:
            if char.lower() in alphabet:
                alphabet.remove(char.lower())
                found_countries.append(country)
    return  found_countries

            
# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

""" Write the calls to your functions here. """
print(shortest_names(countries))
print(most_vowels(countries))
print(alphabet_set(countries))




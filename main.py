import itertools
import requests
import logging
"""
Script to solve SPARbeceda puzzle for some prizes
Game webpage: https://www.spar.si/promocije-in-projekti/aktualni-projekti/sparbeceda
Game rules: https://www.spar.si/content/dam/sparsiwebsite/promocije-in-projekti/aktualni-projekti/sparbeceda/sparbeceda-pravila-nagradne-igre.pdf
"""
array_of_letters = "ŠHLPRLJUMRNJAŠCJ"
unique_letters = ''.join(set(array_of_letters))
valid_words = []
perms = []
valid_words_unique = []

for jndex in range(5,2,-1):
    perms = [''.join(jndex) for jndex in set(itertools.permutations(array_of_letters, jndex))]
    print('Searching', jndex, "letter words","Possible combinations", len(perms))
    for index, perm in enumerate(perms):
        url = 'https://www.franček.si/isci'
        try:
            response = requests.post(url=url,data={"beseda":str(perm)})
        except:
            logging.info('Bad request, np np.')
            pass
        if response.status_code != 200:
            pass
        if not response:
            pass
        json_data = response.json()
        if json_data['response']:
            if sorted(json_data['response'][0]['title']) == sorted(perm.lower()):
                valid_words.append(json_data['response'][0]['title'])
                valid_words_unique = [*set(valid_words)]
                with open('valid_words.txt', 'w') as f:
                    for valid_word in valid_words_unique:
                        f.write(valid_word)
                        f.write(" ")
        if index % 50 == 0:
            print("Index: ", index, "Found words: ", len(valid_words_unique))
            print("Valid words:", valid_words_unique)

print("Found", len(valid_words_unique), "words")
print(valid_words_unique)







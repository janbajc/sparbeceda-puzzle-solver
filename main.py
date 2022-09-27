import itertools
import requests
import logging
"""
Script to solve SPARbeceda puzzle for some prizes
Game webpage: https://www.spar.si/promocije-in-projekti/aktualni-projekti/sparbeceda
Game rules: https://www.spar.si/content/dam/sparsiwebsite/promocije-in-projekti/aktualni-projekti/sparbeceda/sparbeceda-pravila-nagradne-igre.pdf
"""
array_of_letters = "stnčmtarčnvsnnnz"
unique_letters = ''.join(set(array_of_letters))
valid_words = []
perms = []
valid_words_unique = []

#Define max & min length to search

# ['tumor', 'surov', 'burov']
vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

for jndex in range(6,2,-1):
    perms = [''.join(jndex) for jndex in set(itertools.permutations(array_of_letters, jndex))]
    print('Searching', jndex, "letter words","Possible combinations", len(perms))
    for index, perm in enumerate(perms):

        url = 'https://www.franček.si/isci'
        try:
            #Only for longer words since it's very unlikely they won't contain vowels.
            if any(char in vowels for char in perm):
                response = requests.post(url=url,data={"beseda":str(perm)})
            else:
                next
        except:
            logging.info('Bad request, not to worry')
            pass
        if not response:
            pass
        if response.status_code != 200:
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







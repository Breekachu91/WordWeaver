import argparse
from itertools import product

def case_permutations(word_list): 
    results = set()

    for word in word_list:
        for result in product(*zip(word.lower(), word.upper())):
            results.add(''.join(result))
    return list(results)

def leet_permutations(word_list): 
    leet_characters = {
        'a': ['4','@'],
        'e': '3',
        'g': ['&','9'],
        'i': ['1','!'],
        'l': '1',
        'o': '0',
        't': ['7','+'],
        's': ['5','$','2'],
        'z': ['2','s']
    }
    
    leet_perms = set()

    # Thanks for the help GPT
    for words in word_list:
        leet_variants = ['']
        for word in words:
            new_variants = []
            for leet_variant in leet_variants:
                for char in word:
                    if char.lower() in leet_characters:
                        substitutions = leet_characters[char.lower()]
                        for subst in substitutions:
                            new_variants.append(leet_variant + subst)
                    else:
                        new_variants.append(leet_variant + char)
            leet_variants = new_variants
        leet_perms.update(leet_variants)
    
    return list(leet_perms)

def get_file_words(filename): 
    word_list = []

    try: 
        with open(filename, 'r') as file: 
            for line in file: 
                word_list.append(line.strip())
    except FileNotFoundError: 
        print(f'Error: File {filename} not found.')
    except Exception as e: 
        print(f'Error: {e}')
    return word_list

def write_file(word_list, filename):
    with open(filename, 'w') as file: 
        for results in word_list: 
            for result in results:
                file.write(f'{result}\n')

def main():
    parser = argparse.ArgumentParser(description='A quick script to generate wordlists')
    parser.add_argument('-w', '--word', help='Single word you want to use instead of a list.')
    parser.add_argument('-i', '--input', help='Path to file containing words you would like to use.')
    parser.add_argument('-o', '--output', help='File for outputting the wordlist to.')
    parser.add_argument('-L', '--leet', action='store_true', help='Set to perform 1337 speak permutations.')

    args = parser.parse_args()

    if not args.input and not args.word: 
        parser.error('Must provied -w <string> or -i <input file>.')
    if args.input and args.word:
        parser.error('Both -w and -i cannot be used together.')

    word_list = []
    input_file = args.input
    output_file = args.output
    results = []

    print('Script will now start generating your wordlist...')

    if args.word:
        word_list.append(args.word)
           
    if args.input:
        word_list = get_file_words(input_file)

    cap_variants = case_permutations(word_list)
    results.append(cap_variants)

    if args.leet: 
        leet_variants = leet_permutations(cap_variants)
        results.append(leet_variants)
    
    #write results to file
    if args.output:
        write_file(results, output_file)
        print(f'Script has finished, find your word list here: {output_file}')
    else: 
        for result in results:
            for word in result:
                print (word)
    

if __name__ == "__main__":
    main()

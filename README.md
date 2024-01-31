# WordWeaver
Simple command line tool for generating word lists based off input. It will take in a single string or word list file and convert it to capital and lower case variants. Has the option to also provide 1337 speek variations. 

## Usage
Acquire the script by cloning the repo or downloading the `.py` file directly. 

### Commands 
`python word_weaver.py [-h] [-w WORD] [-i INPUT] [-o OUTPUT] [-L]`

`-w <word/string>` - Optional: generate a list off a single word (Must be used if input file not provided) 

`-i <word file>` - Optional: Provide a word list to run through the script. (Must be provided if `-w` is not provied)

`-o <output file>` - Optional: Specify output file for generate word list. If one is not specified, outputs to standard output. 

`-L` - Optional: If set, 1337 speek variations will be done. 

Example: 

`python word_weaver.py -w bananas -o mywordlist.txt -L`

`python word_weaver.py -i inputwords.txt -o mywordlist.txt`

## ToDo
1) Add option for adding a string that prepends or appends all of the resulting words.
  - ex. for instance adding 2024 to all the results at the end. 
2) Create option and functionality for random generation
3) Create option and functionality for permuation and shuffling of the strings (revers, letters of the word in random order, etc.) 

## Contributing 
Feel free to open an issue if you think something should be changed or added, or fork the repo and edit the code yourself and make a merge request. 

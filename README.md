# usernamegen
> Genrate usernames with a Markov chain based on a wordlist

## Usage library

## Usage scripts
```bash
usage: markov [-h] [-p PREV] [-n N] WORDLIST

Markov chain word generator. Generate new words based on aword list.

positional arguments:
  WORDLIST    Path to wordlist used for word generation

optional arguments:
  -h, --help  show this help message and exit
  -p PREV     Number of previous letters to base chain on
  -n N        Amount of new words to generate
```

```bash
usage: username [-h] [-p PREV] [-n N] [-m MIN] WORDLIST

Generate usernames based on a wordlist and a Markov chain.

positional arguments:
  WORDLIST    Path to wordlist used for word generation

optional arguments:
  -h, --help  show this help message and exit
  -p PREV     Number of previous letters to base chain on
  -n N        Amount of new words to generate
  -m MIN      Minimum username length
```

## Running tests
```bash
nosetests --with-coverage --cover-package=usernamegen --with-json-extended
```

import random
import requests

# Get long word list.
class Generator:
    def __init__(self, request_url):
        self.request_url = request_url
        self.code_words = []
        self.passphrases = []

    def get_wordlist(self):
        r = requests.get(self.request_url)
        self.words_txt = r.text

    def parse_txt(self):
        self.get_wordlist()
        lines = self.words_txt.splitlines()
        for code_word in lines:
            self.code_words.append(code_word.split('\t'))
        self.words_dictionary = dict(self.code_words)

    def get_random_int(self):
        return str(random.randint(1,6))

    def get_passcode(self, num_digits):
        passcode = ''
        for i in xrange(num_digits):
            passcode += self.get_random_int()
        return passcode

    def get_passcodes(self, num_passcodes, len_passcodes):
        passcodes = []
        for i in xrange(num_passcodes):
            passcodes.append(self.get_passcode(len_passcodes))
        return passcodes

    def get_word(self, code):
        return self.words_dictionary[code]

    def get_passphrase(self, pass_length, delimit_prompt):
        self.parse_txt()
        passcodes = self.get_passcodes(int(pass_length), 5)

        for passcode in passcodes:
            self.passphrases.append(self.get_word(passcode))

        passphrase = delimit_prompt.join(self.passphrases)
        return passphrase

    def passphrase(self):
      print "How long do you want your passphrase to be?"
      prompt = "Please enter a number of words: "
      passphrase_length = int(raw_input(prompt))

      delimit_prompt = "How would you like to delimit your passphrase?"
      pass_delimiter = str(raw_input(delimit_prompt))

      return self.get_passphrase(passphrase_length, pass_delimiter)

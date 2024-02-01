#Remove pass and complete the code
def check_character(word, index):
   if word[index].isspace() == True:
      return 'white space'
   elif word[index].isalpha() == True:
      return 'letter'
   elif word[index].isdigit() == True:
      return 'digit'
   else:
      return 'unknown'

if __name__ == '__main__': 
    print(check_character('happy birthday', 2))
    print(check_character('happy birthday', 5))
    print(check_character('happy birthday 2 you', 15))
    print(check_character('happy birthday!', 14))

# try autograde
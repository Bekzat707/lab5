import re

def reges(text):
    reg='ab*'
    if re.match(reg,text):
            return True
    else:
            return False
text=["abb","abab","abbb","abbbbb","abs"]
for i in text:
    print(f"{i}: {reges(i)}")




def reges(text):
    reg='ab{2,3}'
    if re.match(reg,text):
            return True
    else:
            return False
text=["abb","abab","abbb","abbbbb","abs"]
for i in text:
    print(f"{i}: {reges(i)}")




def find_sequences(text):
      pattern=r'\b[a-z]+_[a-z]+\b'
      sequences=re.findall(pattern,text)
      return sequences
def main():
      text=input("INPUT TEXT: ")
      seq=find_sequences(text)
      
      if seq:
           print("Sequences found: ")
           for i in seq:
                  print(i)
      else:
            print("No sequences found.")

if __name__=="__main__":
      main()      




def find_up_let(text):
      pattern=r'\b[A-Z][a-z]+\b'
      up_let=re.findall(pattern,text)
      return up_let
def main():
      text=input("INPUT TEXT: ")
      up_let=find_up_let(text)
      if up_let:
            for i in up_let:
                  print(i)
      else:
            print("No found.")   

if __name__=="__main__":
      main()   




def ending(text):
      pettern=r'a[a-z]*b'
      ending=re.findall(pettern,text)
      return ending
def main():
      text=input("INPUT TEXT: ")
      end=ending(text)
      if end:
            for i in end:
                  print(i)
      else:
            print("No found")

if __name__=="__main__":
      main()




def replace(text):
      replace_word={" ":":",",":":",".":":"}
      for old_word,new_word in replace_word.items():
            text=text.replace(old_word,new_word)
      return text
if __name__=="__main__":
      text=input("ENTER TEXT: ")
      new_text=replace(text)
      print("NEW TEXT:",new_text)




def snake(snake_case):
      words=snake_case.split('_')
      camel_case=words[0]+''.join(word.capitalize() for word in words[1:])
      return camel_case
if __name__=="__main__":
      words=input("Enter snake case string: ")
      camel_case=snake(words)
      print("Camel case string:",camel_case)




def split_up(text):
      split=re.findall('[A-Z][a-z]*',text)
      for i in split:
            print(i)
if __name__=="__main__":
      text=input()
      split_up(text)




def split_up(text):
      split=re.findall('[A-Z][a-z]*',text)
      for i in split:
            print(i,end=" ")
      print()
if __name__=="__main__":
      text=input()
      split_up(text)




def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

if __name__ == "__main__":
    camel_case_input = input("Enter a camel case string: ")
    snake_case_output = camel_to_snake(camel_case_input)
    print("Snake case string:", snake_case_output)

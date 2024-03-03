import re 


with open("row.txt") as f:
    text = f.read()

print("TASK 1:")


def reges(text):
    reg='ab*'
    if re.match(reg,text):
            return True
    else:
            return False
for i in text:
    print(f"{i}: {reges(i)}")


print("TASK 2:")

def reges(text):
    reg='ab{2,3}'
    if re.match(reg,text):
            return True
    else:
            return False
for i in text:
    print(f"{i}: {reges(i)}")


print("TASK 3:")

def find_sequences(text):
      pattern=r'\b[a-z]+_[a-z]+\b'
      sequences=re.findall(pattern,text)
      return sequences
def main():
      seq=find_sequences(text)
      
      if seq:
           print("Sequences found: ")
           for i in seq:
                  print(i)
      else:
            print("No sequences found.")

if __name__=="__main__":
      main()      


print("TASK 4:")

def find_up_let(text):
      pattern=r'\b[A-Z][a-z]+\b'
      up_let=re.findall(pattern,text)
      return up_let
def main():
      up_let=find_up_let(text)
      if up_let:
            for i in up_let:
                  print(i)
      else:
            print("No found.")   

if __name__=="__main__":
      main()   


print("TASK 5:")

def ending(text):
      pettern=r'a[a-z]*b'
      ending=re.findall(pettern,text)
      return ending
def main():
      end=ending(text)
      if end:
            for i in end:
                  print(i)
      else:
            print("No found")

if __name__=="__main__":
      main()


print("TASK 6:")

def replace(text):
      replace_word={" ":":",",":":",".":":"}
      for old_word,new_word in replace_word.items():
            text=text.replace(old_word,new_word)
      return text
if __name__=="__main__":
      new_text=replace(text)
      print("NEW TEXT:",new_text)


print("TASK 7:")

def snake(snake_case):
      words=snake_case.split('_')
      camel_case=words[0]+''.join(word.capitalize() for word in words[1:])
      return camel_case
if __name__=="__main__":

      camel_case=snake(text)
      print("Camel case string:",camel_case)


print("TASK 8:")

def split_up(text):
      split=re.findall('[A-Z][a-z]*',text)
      for i in split:
            print(i)
if __name__=="__main__":
      split_up(text)


print("TASK 9:")

def split_up(text):
      split=re.findall('[A-Z][a-z]*',text)
      for i in split:
            print(i,end=" ")
      print()
if __name__=="__main__":
      split_up(text)



print("TASK 10:")

def camel_to_snake(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case += '_' + char.lower()
        else:
            snake_case += char
    return snake_case.lstrip('_')

if __name__ == "__main__":
    snake_case_output = camel_to_snake(text)
    print("Snake case string:", snake_case_output)

f.close()

f.close()
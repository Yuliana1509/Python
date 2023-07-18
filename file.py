print('What is your name?')

#Asking for user input - name

name = input()
characters=list(name)
vowel_index = 0

#Peter
#P NO 0+1 =1 (the first letter not a vowel, formula will add +1 and will go to the next letter)
#E Yes 1 (lopp break abd define index of the vowel)
for letter in characters:
  if letter in ['a', 'e', 'i', 'o', 'u', 'y']:
    break
  else: 
    vowel_index=vowel_index + 1
    
first_chunk=name[vowel_index:]
last_chunk= name[:vowel_index]
print('Your Pig name is ' +first_chunk + last_chunk + 'ay')

 


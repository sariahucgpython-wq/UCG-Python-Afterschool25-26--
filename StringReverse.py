









word = str (input("Please enter a word: "))




re_word=""



#Hint: len (s) - 1 gives the index of the final character.
i =len(word) -1

#4. Start a while loop
#Hint : len (s)- 1 gives the index of the final character.

while i >=0:
   
   
   #5. Inside the loop, add the current letter to the reversed word
    re_word += word [i]


#6. Move one step backward to the previous letter
    i -=1

#7. Print the final reversed word 
print(re_word)
user_input = input("Введите любой текст:\n").capitalize()
string = ""

for i in user_input:
  if i == "б" or i == "Б":
    string+= "9"
  else:
    string+= i
 
print(string[::-1])

#bad

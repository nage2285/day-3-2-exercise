# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

#print(type(height))
#print(type(weight))

#BMI Calculator 

BMI = round(weight/ (height * height))

if BMI < 18.5 :
  print (f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25 :
    print (f"Your BMI is {BMI}, you are normal weight.")
elif BMI < 30 :
    print (f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35 :
    print (f"Your BMI is {BMI}, you are obese.")
else :
  print (f"Your BMI is {BMI}, you are clinically obese.")

# How to convert string into lower 
#sentence = ("Mary Had a Little lamb")
#sentence_l = sentence.lower() 
#print(sentence_l)

#How to count number of certain alphabets
#sentence = "Mary had a little lamb"
#sentence1 = sentence.count("a")
#sentence2 = sentence.count("t")
#count = sentence1 + sentence2
#print(sentence1)
#print(sentence2)
#print (type(count))
#print(count)
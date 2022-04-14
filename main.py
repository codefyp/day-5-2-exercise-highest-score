# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

#create a variable to compare each score to
highest_score = 0
#create a loop to compare if the current loop score from the list of student_scores is higher than the highest_score. We update the highest score by the variable in line 15
for score in student_scores :
  if score > highest_score :
    highest_score = score
print(f"The highest score is {highest_score}")    


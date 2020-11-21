my_student = {
"name " : "tabish",
"grades": [10, 23, 50]

}

def average_sum(student):
   return sum(student['grades']) / len(student['grades'])
print(average_sum(my_student))
  
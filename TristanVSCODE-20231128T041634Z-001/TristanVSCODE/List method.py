#Name:Tristan Perez
#12/10
#Lists

#Initialize
#mySchedule stores a list of the classes you are currently taking at Jones and your lunch period as strings
mySchedule = ["resource", "math", "Biology", "APCSP", "Digital Imaging", "English", "Mandarin"]

#Main

#Complete the following tasks using list/array methods. Print the result for each task.

#Task 1: Print your 1st - 7th period classes in a list in the correct order (index 0 should be your 1st period class)
print(mySchedule)
#Task 2: Print only your 3rd period class
print(mySchedule[3])
#Task 3: Add your lunch period in between your 3rd and 4th period using a list method
mySchedule.insert(4, "lunch")
print(mySchedule)
#Final Task: Remove your least favorite class using a list method
mySchedule.remove("Mandarin")
print(mySchedule)
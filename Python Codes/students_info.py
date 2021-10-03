file_name = input("Enter a valid name for your txt file : ")
file_name = file_name + ".txt"
open_file = open(file_name, "w")
database = {}
while True:
  name = input("Enter name of the student : ")
  class_ = input("Enter class of the student : ")
  database["Name"] = name
  database["Class"] = class_
  open_file.write(database)
  choice = input("Want to add more data y/n ? : ")
  if choice == 'n':
    break
open_file.close()

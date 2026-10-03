
import random
import string
print ("=======Password Genreter ========")

while True:
      print("\n1. Generate Password")
      print("2. Exit")

      choice = input("Enter your choice: ")

      if choice == "1":
            length = int(input("Enter password length: "))
            characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%*&"
            password = input("Enter your password: ")
            print("Your password is:", password)
            print("Generated password:", password)
      elif choice == "2":
            print("Exiting the program.")
            break
      else:
            print("Invalid choice. Please try again.")
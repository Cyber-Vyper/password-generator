import random
import time
print('''
          |======================================|
            P A S S W O R D   G E N E R A T O R. 
          |======================================|''')
print(" ")
def generator ():
     try:
          passlen = int(input("Enter desired password length: "))
     except:
          ValueError
          print("Invalid Input. Try Again")
          generator ()

     #storing alphabets, numbers and special characters
     try:
          s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890@#$_&-+()/*!?"
          p = "".join(random.sample(s, passlen))
          print("="*20)
          time.sleep(1)
          print("Processing Your Information..")
          time.sleep(2)
          print("Generating Your Password...")
          time.sleep(1)
          print(f"Your Password is: ' {p} ' ")
     except:
          ValueError
          print("[ERROR]  Invalid Password length")
          time.sleep(1)
          print("[NOTE]  Password length is between 8 to 78 characters")
          time.sleep(1)
          print("Trying Again. Please Wait...")
          time.sleep(2)
          generator()
          
generator ()

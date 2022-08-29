#Project to verify password 
import getpass #Library to mask Password
import time #import time library for sleep purposes
import os
 #f=open("C:\Python\PasswordManager\ManagerDB.txt","a") # "a" will create the file if its not exists and append a row if needed


SavedPass=[0] #Array for Saved Passwords 

# MAIN MENU 
#-----------------
def MainMenu(): #Main Menu
  os.system('cls') #Clear Screen
  menu=input('Main Menu:\n\n1. Enter New Password\n2. List Existing Passwords\n3. Exit\n\nChoice: ')
  if menu not in ['1','2','3']:
    print ('\nchoice out of range. Try again')
    MainMenu()
  else:
    MoveToItem(menu) #Move to the chosen item
#---------------------------------

#Move to menu selection 
#--------------------------
def MoveToItem(menu): #Actions for each choice
      if menu=='1':
        os.system('cls') #Clear Screen
        print ("NEW PASSWORD SCREEN:\n--------------------")
        EnterPassword()
      elif menu=='2':
        os.system('cls') #Clear Screen
        print ("PRINT PASSWORDS ARRAY:\n--------------------")
        PrintPasswd()
      elif menu=='3':
        os.system('cls') #Clear Screen
        print ('SAYONARA')
        quit()
#---------------------------     

# SLECTION 1 - ENTER NEW PASSWORD
#----------------------------------------

def EnterPassword(): #Enter New Password Choice
  z=1
  if len(SavedPass)==1 and SavedPass[0] in [0,'0']: # If it's the first password the print :
    passw=getpass.getpass('\nEnter New Password Please.\nPassword must be between 5 to 7 chars\nand consist both letters and number\nand at least one special character: ')
    CheckPass(passw) #Go and check Password validity
  else:
    OldPass=SavedPass[-1] #Otherwise enter the old password
    CheckOldPass=getpass.getpass('Enter your Old Password: ')
    while CheckOldPass != OldPass:
      while z <= 3:
          print ('\nWrong old Pass. Try Again (Try No.{}):'.format(z))
          CheckOldPass=getpass.getpass('Enter your Old Password: ')
          if CheckOldPass==OldPass:
            passw=getpass.getpass('\nEnter New Password Please.\nPassword must be between 5 to 7 chars\nand consist both letters and number\nand at least one special character: ')
            CheckPass(passw)
          elif CheckOldPass!=OldPass and z==3:
            print("You have reache to Max attempts\nGoing back to mainmenu in 3 sec.")
            time.sleep(3) #sleeps for 3 seconds
            MainMenu()
          else:
            z=z+1
      #print ('\nWrong old password. Please try again\n')
      #CheckOldPass=getpass.getpass('Enter your Old Password: ')
    else:
      passw=getpass.getpass('\nEnter New Password Please.\nPassword must be between 5 to 7 chars\nand consist both letters and number\nand at least one special character: ')
      CheckPass(passw)
      


# NEW PASS VALIDATION CHECK
#-----------------------------
def CheckPass(passw):
  if  len(passw) < 5: #Check Password length - Short
   print ("The password selected it less than 5 chars.Try again")
   EnterPassword()
  if len(passw) > 7: #Check Password length - Long
    print ("The password selected it more than 7 chars.Try again")
    EnterPassword()
  if passw.isnumeric():#Check for numbers only
    print ("The password selected Has only numbers.Try again")
    EnterPassword()
  if passw.isalpha():#Check for letters only
    print ("The password selected Has only letters.Try again")
    EnterPassword()
  splitpass=list(passw) #Split password to chars and start validation check on each char
  u=0 # Counter for UpperCase
  l=0 # Counter for LowerCase
  n=0 # Counter for digits
  specialchars='!@#$%^&*()-=_+\][}{};:"<>,./?\\|'+'"'+"'" #Configure special Chars allowedin pass
  sc=0 #Counter for SpecialChars
  
  for i in splitpass:
    if i.isupper(): #If uppercase
      u+=1
    if i.islower(): #If lowercase
      l+=1
    if i in specialchars: #If specialchar
      sc+=1
    if i.isnumeric(): #if a digit
      n+=1

  # Validation checks on password complexity
  if n==0:
    print ("The Password does not contain digits. Try again")
    EnterPassword()
  if sc==0 and u==0:
    print ("The password selected does not contain either special char\\UpperCase.Try again")
    EnterPassword() 
  elif sc==0 and l==0:
    print ("The password selected does not contain special char\\LowerCase.Try again")
    EnterPassword() 
  elif sc>0 and l==0:
    print ("The password selected does not LowerCase.Try again")
    EnterPassword()
  elif sc>0 and u==0:
    print ("The password selected does not contain UpperCase.Try again")
    EnterPassword()
  elif sc==0 and u>0 and l>0:
    print ("The password selected does not contain any special chars.Try again")
    EnterPassword() 

  #Check If password is in the passwords array (has been used)
  for i in SavedPass:
    if i==passw:
      print('This Password Has Already been used. Try again')
      EnterPassword()
    else:
      VerifyPass(passw)
#------------------------------------------------------------------------------


#New Pass Verification 
#-------------------------
def VerifyPass(passw):
      retry=getpass.getpass('\nVerify New Password: ') 
      z=1 #Retries counter
      
      while retry != passw: #as long as the first verificatrion is not equal to the password
        while z <= 3: #give 3 tries
          print ('\nPasswords do not match! Try again (Try No.{}):'.format(z))
          retry=getpass.getpass('Verify New Password: ')
          if retry==passw: #if retry like the password = exit loop to the SavePass() function
            SavePass(passw)
          elif retry!=passw and z==3: #if retry not like password and retries counter is max then quit loop and move back to main menu
            print("\nYou have reache to Max attempts\nGoing back to Main Menu in 3 sec.")
            time.sleep(3) #sleeps for 3 seconds
            MainMenu()
          else: #Else advance the counter and check again
            z=z+1
      else:
        SavePass(passw)
        
               
#Save Password to array 
#-----------------------
def SavePass(passw):
  if len(SavedPass)==1 and SavedPass[0] in [0,'0']:
    SavedPass[0]=passw
    print ('Password Saved Succesfully')
    AskAgain()
  else:
    SavedPass.append(passw)
    print ('Password Saved Succesfully')
    AskAgain()


def AskAgain():
  asn=input('Go Back to main menu? (y\\n): ')
  while asn not in ['Y','y','N','n']:
    print ('Wrong answer, Try again')
    AskAgain()
  else:
    if asn not in ['N','n']:
      MainMenu()
    elif asn in ['N','n']:
      print ("GoodBye")
      quit()
  
  
def PrintPasswd(): #Print Passwords choice
   #Passwords counter
  print ('Passwords stored in the array:')
  for i in SavedPass:
    index = SavedPass.index(i) #Gets the index number of a list element
    print ("\nPass Index [{}] , Value: {}\n".format(index,SavedPass[index]))
    
  AskAgain()


def Exit(): #Exit function
  quit()

MainMenu()





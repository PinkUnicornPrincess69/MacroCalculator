import time as t
from time import *
    

#new line
def newLine():
    print("\n")

#kg to lbs conversion
def conversion(x):
    
    kgs = 0.453592
    lbs = 2.20462
    
    #kg to lbs
    if x == "kg":
        print("")
        userKGSinput = int(input("KGS amount: "))
        LBSconversion = userKGSinput * lbs
        finaConversion = "{:.2f}".format(LBSconversion)
        
        print(f"\nKGS: {userKGSinput}\nLBS: {finaConversion}")
        
    #lbs to kg 
    elif x == "lbs":
        print("")
        userLBSinput = int(input("LBS amount: "))
        KGSconversion = userLBSinput * kgs
        finaConversion = "{:.2f}".format(KGSconversion)
        
        print(f"\nLBS: {userLBSinput}\nKGS: {finaConversion}")
        
    #invalid entry
    else:
        print("That wasn't an option")
    
    print("")
        
#nurtition calculator 
def macroCalc():
    
    goals = ["1) Maintain", "2) Weight Loss", "3) Bulk"]
    
    #asks for user goals
    print("\n".join(goals))
    userGoal = input(f"What is your goal: ")
    userGoal = userGoal.lower()
    print("")
    
    #gets values for user age, gender, height, weight
    userAge = int(input("What is your age: "))
    print("")
    userGender = input("What is your gender [male / female]: ")
    print("")
    userHeight = int(input("What is your height in inches: "))
    print("")
    userWeight = int(input("What is your current weight in lbs: "))
    print("")
    howActive = ["Very Active", "Moderately Active", "Lightly Active", "Sedentarty Active"]
    print("\n".join(howActive))
    userActivityLevel = input("How active are you: ")
    userActivityLevel = userActivityLevel.lower()
    
    
    #gets gender for bmi
    userGender = userGender.lower()
    if userGender == "male" or userGender == "m":
        userGender = 24
        
    elif userGender == "female" or userGender == "f":
        userGender = 22
        
    else:
        print("Sorry can only use male or female")
        
        
    bmr = userWeight * int(userGender)
    #user bmr and activity checker
    if userActivityLevel == "very active" or userActivityLevel == "very" or userActivityLevel == "v" or userActivityLevel == "va":
        userActivity = 1.72
    elif userActivityLevel == "moderately active" or userActivityLevel == "moderate" or userActivityLevel == "moderately" or userActivityLevel == "mod" or userActivityLevel == "m" or userActivityLevel == "ma":
        userActivity = 1.55
    elif userActivityLevel == "lightly active" or userActivityLevel == "light" or userActivityLevel == "lightly" or userActivityLevel == "l" or userActivityLevel == "la":
        userActivity = 1.37
    elif userActivityLevel == "sedentarty active" or userActivityLevel == "sedentarty" or userActivityLevel == "i dont" or userActivityLevel == "s" or userActivityLevel == "sa":
        userActivity = 1.2    
    
    
    #user calories calc
    userWeightForCal = 4.35 * userWeight
    userHeightForCal = 4.7 * userHeight
    userAgeForCal = 4.7 * userAge
    userCalories = 655 + userWeightForCal + userHeightForCal + userAgeForCal
    
    #Total dailty energy expenditure (how many calories needed)
    tdee = userCalories * userActivity
    
    ####    weight gain macro calc  ####
    if userGoal == "bulk" or userGoal == "b" or userGoal == "3":
        
        tdeeBulk = tdee * 0.1
        tdee = tdee + tdeeBulk
        remainingCalories = tdee
        
        #protien calc
        userProtien = userWeight * 1.25
        userProtienCal = userWeight * 4
        
        #fat calc - done
        userFats = tdee * 0.3
        userFatMacro = userFats / 9
        
        #remaining cals for carbs calc
        remainingCalories = tdee - userFats - userProtienCal
        
        #carbs calc
        userCarbsMacro = remainingCalories / 4
        userGoal = "Bulk"
        
    ####    Weight loss macro calc  ####
    elif userGoal == "weight loss" or userGoal == "loss" or userGoal == "wl" or userGoal == "2":
        tdeeLoss = tdee - 300
        remainingCalories = tdeeLoss
        
        #protien calc
        userProtien = userWeight * 1.25
        userProtienCal = userWeight * 4
        
        #fat calc - done
        userFats = tdee * 0.3
        userFatMacro = userFats / 9
        
        #remaining cals for carbs calc
        remainingCalories = tdee - userFats - userProtienCal
        
        #carbs calc
        userCarbsMacro = remainingCalories / 4
        userGoal = "Weight Loss"
        
    ####    Maintain Weight macro calc  ####
    elif userGoal == "maintain" or userGoal == "main" or userGoal == "1":
        tdee = tdee
        remainingCalories = tdee
        
        #protien calc
        userProtien = userWeight * 1.25
        userProtienCal = userWeight * 4
        
        #fat calc - done
        userFats = tdee * 0.3
        userFatMacro = userFats / 9
        
        #remaining cals for carbs calc
        remainingCalories = tdee - userFats - userProtienCal
        
        #carbs calc
        userCarbsMacro = remainingCalories / 4
        userGoal = "Maintain"
    else:
        print("Sorry that incorrect option\n")
        
        
   
    #edits the calories and macros to not display any decimals  
    tdee = "{:.0f}".format(tdee)
    userFatMacro = "{:.0f}".format(userFatMacro)
    userCarbsMacro = "{:.0f}".format(userCarbsMacro)
    userProtien  = "{:.0f}".format(userProtien)
    
    print("")
    print(f"\033[93mTotal Callories needed: {tdee}\nFats: {userFatMacro}g\nCarbs: {userCarbsMacro}g\nProtien: {userProtien}g\033[00m")
    print("-" * 28)
    
    global macroList
    macroList = f"Goal: {userGoal}  /  Current Weight: {userWeight}lbs\n\nTotal Callories needed: {tdee}\nFats: {userFatMacro}g\nCarbs: {userCarbsMacro}g\nProtien: {userProtien}g"
    return macroList
 
#saves info, creates file if name doesnt exists, if name does, adds onto file
def saveInfo():
    
    macros = macroList
    #asks user what to call file 
    fileName = input("What do you wish to call the file: ")
    #creates a string with the current date, month and year
    todaysDate = strftime("%d %B %Y",gmtime())
    #adds - 28 times
    lines = "-" * 28
    
    with open(fileName + ".txt", "a+") as file:
        file.writelines(f"Date: {todaysDate}\n{macros} \n{lines}\n")
    

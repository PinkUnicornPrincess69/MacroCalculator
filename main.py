from functions import conversion, newLine, macroCalc, saveInfo

menu = ["1) LBS / KG Converter", "2) Daily Nutrients", "3) Close"]

while True:
    
    print("\n".join(menu))
    userMenuSelect = input("What option would you like to select: ")
    userMenuSelect = userMenuSelect.lower()
    
    #Option for kg and lbs conversion
    if userMenuSelect == "1" or userMenuSelect == "one" or userMenuSelect == "o":
        newLine()
        
        userConversionSelect = input("What conversion do you wish to pick [LBS / KG]: ")
        conversion(userConversionSelect)
    
    elif userMenuSelect == "2" or userMenuSelect == "two" or userMenuSelect == "tw":
        newLine()
        macroCalc()
    
    #Option to close menu
    elif userMenuSelect == "3" or userMenuSelect == "three" or userMenuSelect == "th" or userMenuSelect == "close":
        newLine()
        print("Thank you for using this script, good bye!")
        break
        
    #invalid selection54
    else:
        print("Invalid Selection.")
        newLine()
    
    #asking if user wants to save info to a file
    saveFile = input("Would you like to save infomation file [YES / NO]: ")
    saveFile = saveFile.lower()
    
    #asks user if they want to save the file
    if saveFile == "yes" or saveFile == "y":
        saveInfo()
    else:
        print("")
    
    
    newLine()
def check_password_strength(password): #Function declaration.
        l, u, p, d = 0, 0, 0, 0 #Variable declaration.

        if(len(password)<8):
            return False #Password strength is invalid
    
        for i in password: 
            if (i.islower()):  #Counting lowercase alphabets
                l+=1  

            if (i.isupper()):   #Counting uppercase alphabets
                 u+=1           

            if (i.isdigit()):    #Counting digits
                    d+=1  

            if(i=='!'or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*'):  #Counting the mentioned special characters
                    p+=1 

        if (l>=1 and u>=1 and p>=1 and d>=1 and l+p+u+d==len(password)):
            return True 
        else:
            return False 
            
password_strength=check_password_strength(input("Please enter password: \n")) #Calling function and storing result as boolean

if (password_strength):
    print("Password strength is valid.") #Password strength is valid
else:
     print("Password strength is invalid.") #Password strength is invalid

    
    

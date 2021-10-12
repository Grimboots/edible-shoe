import tkinter as tk
from tkinter import ttk

user_list = {   # user_list is a dict{}
    'Brandon':'0000','Boots':'1111'}
valid_name = '' # Establishes a global variable

# Creates the verification function for user inputs (Username and Password)
def users():
    valid_name = True 
    if valid_name == True:
        user_name = nameText.get()
        if user_name not in user_list: # Checks to see if the Username provided
            loginText.set('Invalid Username')
            user_name = nameText.get() # is in the user_list dictionary keys
        user_pass = passText.get()
        if str(user_pass) not in user_list[user_name]: # Checks to see if the Password
            user_pass = passText.get()                 # provide is a value of the matching
            user_pass = str(user_pass)                 # Username key
        
        if user_name in user_list and user_pass in user_list[user_name]:    
            loginText.set("Welcome Back") # If both match, User is validated
            valid_name = True
        else:
            loginText.set('Username and Password do not match!')
            valid_name = False # If neither match, User is not validated
    elif valid_name == False:
        loginText.set("Login Failed")
    return valid_name

def exitButton():
    root.destroy() # Closes the main GUI Window

def does_user_have_account(): # Creates a new GUI window
    globals()
    def close():
        account.destroy() # Closes current GUI Window
    def addUser(): # Function to add users to users_list dictionary
        globals()
        user_name = nameText.get() # Takes user input and applies it as user_name
        if user_name in user_list:
            useText.set("Username already taken")
            user_name = nameText.get()
        else:
            user_pass = passText.get() # Takes user input and applies it as user_pass
            if user_pass:
                user_list.update({user_name : user_pass}) # Updates the user_list dictionary
                useText.set("User Successfully Added") # Lets User know if their account was added
                print(user_list) # Prints a list of dictionary keys and values
                return user_list # Returns the updated user_list
    # All below creates the GUI for adding a new user   
    account = tk.Toplevel()
    account.title("New User")
    account.geometry('360x300')
    
    frame = ttk.Frame(account, padding="10 10 10 10")
    frame.pack(fill=tk.BOTH, expand=True)
    
    ttk.Label(frame, text="Enter Username:").grid(column=0, row=0, padx=5, pady=5, sticky=tk.W)
    nameText = tk.StringVar()
    tk.Entry(frame, width=25, textvariable=nameText).grid(column=1, row=0, padx=5, pady=5, sticky = tk.W)
    
    ttk.Label(frame, text="Enter Password:").grid(column=0, row=1, padx=5,pady=5, sticky=tk.W)
    passText = tk.StringVar()
    tk.Entry(frame, width=25, textvariable=passText).grid(column=1, row=1, padx=5,pady=5, sticky=tk.W)
    
    tk.Button(frame, text="Add User", command = addUser).grid(column=0, row=3, padx=5,pady=5,sticky = tk.N)
    tk.Button(frame, text="Exit",command=close).grid(column=1, row=3,padx=5,pady=5, sticky=tk.W)

    tk.Label(frame, text="Was user added?").grid(column=0, row=4, padx=5,pady=5, sticky=tk.W)
    useText = tk.StringVar()
    tk.Entry(frame, width=25, textvariable=useText, state = "readonly").grid(column=1, row=4, padx=5,pady=5,sticky=tk.W)

def create_user_file(): # A Function that exports the user_list dictionary to a .txt file
    globals()
    out_file = open("User_List.txt","w")
    out_file.write(str(user_list))
    out_file.close()
    return

# Creates the initial GUI window where users can either sign in or create a new account
root = tk.Tk()
root.title("Verify Users")
root.geometry("420x360")

frame = ttk.Frame(root, padding="10 10 10 10")
frame.pack(fill=tk.BOTH, expand = True)

ttk.Label(frame, text="Username:").grid(column=0, row=0, padx=5, pady=5, sticky = tk.W)
nameText = tk.StringVar()
tk.Entry(frame,width=25, textvariable=nameText).grid(column=1, row=0, padx=0,pady=5, sticky=tk.W)

ttk.Label(frame, text="Password:").grid(column=0, row=1, padx=5,pady=5, sticky=tk.W)
passText = tk.StringVar()
tk.Entry(frame, width=25, textvariable=passText).grid(column=1, row=1, padx=0,pady=5, sticky=tk.W)

ttk.Button(frame, text="Enter",command=users).grid(column=0, row=2, padx=5,pady=5)
ttk.Button(frame, text="Exit",command=exitButton).grid(column=1, row=2, padx=5, pady=5, sticky=tk.W)


ttk.Label(frame, text="Login Status:").grid(column=0, row=3, padx=5,pady=5, sticky = tk.W)
loginText = tk.StringVar()
tk.Entry(frame, width=35, textvariable=loginText, state="readonly").grid(column=1, row=3, padx=5,pady=5, sticky=tk.W)

ttk.Label(frame, text="Does user have an account?").grid(column=0, row=4, padx=5, pady=5, stick=tk.W)
ttk.Button(frame, text="No?",command=does_user_have_account).grid(column=1, row=4, padx=5, pady=5, sticky=tk.W)

ttk.Button(frame, text="Click to Export User_List",command=create_user_file).grid(column=0,row=5,padx=5,pady=5,sticky=tk.E)


root.mainloop()
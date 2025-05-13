class LOGIN:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()
        
    def menu(self):
        i = input("""Welcome to Menu:
               1: Press 1 for signup.
               2. Press 2 for signin.
               3. Press 3 for post something.
               4. Press any other key to exit.
               ->""")
        if(i=="1"):
            self.signup()
        elif(i=="2"):
            self.signin()
        elif(i=="3"):
            self.post()
        else:
            exit()
    
    def signup(self):
        self.username = input("Please setup your username")
        self.password = input("Please setup your password")
        print("Account created successfully")
        self.menu()
    
    def signin(self):
        user = input("Please enter your username")
        passw = input("Please enter your password")
        if(user == self.username and passw == self.password):
            print("Account logged in successfully")
            self.loggedin=True
        else:
            print("incorrect username or password or create your account")        
        self.menu()
    
    def post(self):
        if(self.loggedin == True):
            p = input("what do you want to post")
            print("Successfully posted")
        else:
            print("Please log in first")
        self.menu()
    
user1 = LOGIN()
            
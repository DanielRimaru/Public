class CustomerAccount():
    def __init__(self, fname, lname, address, account_no, balance,accounttype):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.account_no = account_no
        self.balance = float(balance)
        self.accounttype=accounttype
    def update_name(self):
        fname=input("\n Enter new customer first name: ")
        lname = input("\n Enter new customer last name: ")
        print(f"Old name: %s %s" %(self.fname, self.lname))
        print(f"New name: %s %s" %(fname, lname))
        print("Is the new information correct?")
        cnf= input('''If so type "CONFIRM", type anything else to cancel" \n''')
        if(cnf=="CONFIRM"):
            self.fname=fname
            self.lname=lname
            print("Customer changed successfully.")
        else:
            print("Customer name remains unchanged.")
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def update_address(self):
        vld=0
        while(vld==0):
            try:
                n=int(input("Please input new address number"))
                vld=1
            except:
                print("It has to be a number. Try again")
        street=input("Please input new address street ")
        town=input("Please input new address town ")
        postcode=input("Please input new address postcode ")
        print(self.fname, self.lname)
        print(f"Old address: %s %s %s %s" %(self.address['n'],self.address['street'],self.address['town'],self.address['postcode']))
        print(f"New address: %s %s %s %s" %(n,street,town,postcode))
        print("Is the new address correct?")
        cnf= input('''If so type "CONFIRM", type anything else to cancel" \n''')
        if(cnf=="CONFIRM"):
             self.address['n']=n
             self.address['street']=street
             self.address['town']=town
             self.address['postcode']=postcode 
             print("Address update was successful. Returning to menu...")
        else:
            print("Address update canceled")
        
    def get_address(self):
        return self.address
    
    def deposit(self, amount):
        if(amount>0):
            self.balance+=amount
        else:
            print("Error: Cannot deposit a negative amount of money")
        
    def withdraw(self, amount):
        if(amount<0):
            print("Cannot withdraw a negative amount of money")
        elif(amount<=self.balance+self.accounttype.get("overdraft")):
            self.balance-=amount
        else:
            print("Error: Cannot withdraw more than current balance.")
        
    def print_balance(self):
        if(self.balance<0):
            print("%f overdraft" %-self.balance)
        else:
            print("Balance: %f" %self.balance)
        
    def get_balance(self):
        return self.balance
    
    def get_account_no(self):
        return self.account_no
    
    def account_menu(self):
        print ("\n Your Transaction Options Are:")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Deposit money")
        print ("2) Withdraw money")
        print ("3) Check balance")
        print ("4) Update customer name")
        print ("5) Update customer address")
        print ("6) Show customer details")
        print ("7) Back")
        print (" ")
        option = input ("Choose your option: ")
        return option
    
    def print_details(self):
        #STEP A.4.3
        print("First name: %s" %self.fname)
        print("Last name: %s" %self.lname)
        print("Account No: %s" %self.account_no)
        if(self.balance<0):
            print("%f overdraft" %-self.balance)
        else:
            print("Balance: %f" %self.balance)
        print("Account type:  %s" %self.accounttype.get("accname"))
        print("Interest:  %f" %self.get_interest())
        print("Address:")
        print("   Number  : %s" %self.address.get("n"))
        print("   Street  : %s" %self.address.get("street"))
        print("   Town    : %s" %self.address.get("town"))
        print("   Postcode: %s" %self.address.get("postcode"))
        print(" ")

    def get_interest(self):
        interest=self.balance*self.accounttype.get("interest")/100
        if(interest>0):
            return interest
        else:
            return 0
    
    def run_account_options(self):
        loop = 1
        while loop == 1:
            choice = self.account_menu()
            if choice == '1':
                vld=0
                while(vld==0):
                    try:
                        amount=float(input("\n Please enter amount to be deposited: "))
                        self.deposit(amount)
                        self.print_balance()
                        vld=1
                    except:
                        print("It has to be a number!")
            elif choice == '2':
                if(self.accounttype.get("accname")!="Certified Deposit"):
                    vld=0
                    while(vld==0):
                        try:
                            amount=float(input("\n Please enter amount to be withdrawn: "))
                            self.withdraw(amount)
                            self.print_balance()
                            vld=1
                        except:
                            print("It has to be a number!")
                else:
                    print("Cannot withdraw from a Certified Deposit!")
            elif choice == '3':
                self.print_balance()
            elif choice == '4':
                self.update_name()
            elif choice == '5':
                self.update_address()
            elif choice == '6':
                self.print_details()
            elif choice == '7':
                loop = 0
        print ("\n Exit account operations")
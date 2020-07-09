from customer_account import CustomerAccount
from admin import Admin

accounts_list ={}
admins_list = {}

class BankSystem(object):
    def load_bank_data(self):
        
        # create customers
        import json
        try:
            with open("data.json") as f:
                data=json.load(f)
        except:
            print("Error with json file")
            exit
        for c in data["customer"]:
            accounts_list[c["account_no"]] = CustomerAccount(c["fname"],c["lname"],c["address"],c["account_no"], c["balance"],c["accounttype"])
        for c in data["admin"]:
            admins_list[c["username"]] = Admin(c["fname"],c["lname"],c["address"],c["username"],c["password"],c["adminRight"])
    def search_admins_by_name(self, admin_username, field="user_name"):
        #STEP A.2
        l=[]
        for k,v in admins_list.items():
            if getattr(v,field)== admin_username:
                l.append(k)
        return l
        
    def search_customers_by_name(self, name, field="account_no"):
        #STEP A.3
        l=[]
        for k,v in accounts_list.items():
            if str(getattr(v,field))==str(name):
                l.append(k)
        return l

    def main_menu(self):
        #print the options you have
        print()
        print()
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("Welcome to the Python Bank System")
        print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        print ("1) Admin login")
        print ("2) Quit Python Bank System")
        print (" ")
        try:
            option = int(input ("Choose your option: "))
            return option
        except:
            print("invalid input")
        


    def run_main_options(self):
        loop = 1         
        while loop == 1:
            choice = self.main_menu()
            if choice == 1:
                username = input ("\n Please input admin username: ")
                password = input ("\n Please input admin password: ")
                msg, admin_obj = self.admin_login(username, password)
                print(msg)
                if admin_obj != None:
                    self.run_admin_options(admin_obj)
            elif choice == 2:
                loop = 0
            else:
                print("Invalid input.")
        print ("\n Thank-You for stopping by the bank!")


    def transferMoney(self, sender_account_no, receiver_account_no, amount):
        if(sender_account_no==receiver_account_no):
            print("The sender account number cannot be the same as the receiver account number")
        elif (amount<0):
            print("The sent amount cannot be a negative number")
        elif (amount>accounts_list[sender_account_no].balance+accounts_list[sender_account_no].accounttype.get("overdraft")):
            print("The sender has less than %f in their bank account." %amount )
        elif (accounts_list[sender_account_no].accounttype.get("accname")=="Certified Deposit"):
            print("Cannot send money from a Certified Deposit!")
        else:
            accounts_list[sender_account_no].balance-=amount
            accounts_list[receiver_account_no].balance+=amount
            print(f"Sent %f from %s %s  to %s %s" %(amount,accounts_list[sender_account_no].fname,accounts_list[sender_account_no].lname,accounts_list[receiver_account_no].fname,accounts_list[receiver_account_no].lname))

                
    def admin_login(self, username, password):
		 #STEP A.1
        found_admin1 = self.search_admins_by_name(username)
        try:
            if str(admins_list[found_admin1[0]].password)==str(password):
                msg = "\n Login successful"
                return msg, admins_list[found_admin1[0]]
            else:
                msg = "\n Login failed"
                return msg, None
        except:
            msg = "\n Login failed"
            return msg, None


    def admin_menu(self, admin_obj):
        #print the options you have
         print (" ")
         print ("Welcome Admin %s %s : Avilable options are:" %(admin_obj.get_first_name(), admin_obj.get_last_name()))
         print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
         print ("1) Transfer money")
         print ("2) Customer account operations & profile settings")
         print ("3) Delete customer")
         print ("4) Print all customers detail")
         print ("5) Print this admin's information")
         print ("6) Change name and address")
         print ("7) Request manangement report")
         print ("8) Sign out")
         print (" ")
         option = input ("Choose your option: ")
         return option


    def run_admin_options(self, admin_obj):                                
        loop = 1
        while loop == 1:
            choice = self.admin_menu(admin_obj)
            if choice == '1':
                try:
                    sender_account_no = int(input("\n Please input sender account number: "))
                    amount = float(input("\n Please input the amount to be transferred: "))
                    receiver_account_no = int(input("\n Please input receiver account number: "))
                    self.transferMoney(sender_account_no, receiver_account_no, amount)
                except ValueError:
                    print("It has to be a number!")
                except KeyError:
                    print("Could not find an account with the number provided.")
                                        
            elif choice == '2':
                customer_name = input("\n Please input customer surname :\n")
                customer_account = self.search_customers_by_name(customer_name,"lname")
                try:
                    accounts_list[customer_account[0]].run_account_options()   
                except:
                    print("%s could not be found." %customer_name)
            elif choice == '3':
                if(admin_obj.full_admin_rights==True):
                    customer_name = input("\n input customer id/name you want to delete: ")
                    customer_account = self.search_customers_by_name(customer_name,"account_no")
                    try:
                        print(accounts_list[customer_account[0]].account_no ,accounts_list[customer_account[0]].fname, accounts_list[customer_account[0]].lname)
                        print("Found by ID")
                        dlt=input('''Delete? Type "DELETE" to confirm \n''')
                    except:
                        customer_account = self.search_customers_by_name(customer_name,"fname")
                        try:
                            print(accounts_list[customer_account[0]].account_no ,accounts_list[customer_account[0]].fname, accounts_list[customer_account[0]].lname)
                            print("Found by First Name")
                            dlt=input('''Delete? Type "DELETE" to confirm \n''')
                        except:
                            customer_account = self.search_customers_by_name(customer_name,"lname")
                            try:
                                print(accounts_list[customer_account[0]].account_no ,accounts_list[customer_account[0]].fname, accounts_list[customer_account[0]].lname)
                                print("Found by Last Name")
                                dlt=input('''Delete? Type "DELETE" to confirm \n''')
                            except:
                                print("%s could not be found." %customer_name)
                    try:
                        if(dlt=="DELETE"):
                            del accounts_list[customer_account[0]]
                            print("%s was deleted successfully!" %customer_name)
                        else:
                            print("Customer was not deleted. Returning to Menu...")
                    except:
                        print("Customer was not deleted. Returning to Menu...")
                else:
                    print("Access denied. Full admin rights are required!")
            elif choice == '4':
                self.print_all_accounts_details()
            elif choice == '5':
                admin_obj.print_details()
            elif choice == '6':
                admin_obj.update_info()
            elif choice == '7':
                self.print_management_report()
            elif choice == '8':
                loop = 0
            else:
                print("Invalid input. Try again")
        print ("\n Exit account operations")
        
    def print_management_report(self):
        count = 0
        totalmoney=0
        totalint=0
        totalod=0
        for c in accounts_list:
            count+=1
            if(accounts_list[c].balance>0):
                totalmoney+=accounts_list[c].balance
                
            else:
                totalod-=accounts_list[c].balance
            totalint+=accounts_list[c].get_interest()
        print(f"There are %d customers." %count)  
        print(f"Total money in the bank: %f" %totalmoney) 
        print(f"Total interest to pay: %f" %totalint) 
        print(f"Total overdraft: %f" %totalod) 
        
    def print_all_accounts_details(self):
            i = 0
            for c in accounts_list:
                i+=1
                print('\n %d. \n' %i, end = ' ')
                accounts_list[c].print_details()
                print("------------------------")


app = BankSystem()
app.load_bank_data()
app.run_main_options()

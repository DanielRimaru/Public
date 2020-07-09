class Admin():  
    def __init__(self, fname, lname, address, user_name, password, full_rights):
        self.fname = fname
        self.lname = lname
        self.address = address
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights               
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
        
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
        
    def get_address(self):
        return self.address  
    
    def update_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights
    def update_info(self):
        fname=input("Please input new first name ")
        lname=input("Please input new last name ")
        vld=0
        while(vld==0):
            try:
                n=int(input("Please input new address number "))
                vld=1
            except:
                print("It has to be a number. Try again ")
        street=input("Please input new address street ")
        town=input("Please input new address town ")
        postcode=input("Please input new address postcode ")
        print(f"Old name: %s %s" %(self.fname,self.lname))
        print(f"Old address: %s %s %s %s" %(self.address['n'],self.address['street'],self.address['town'],self.address['postcode']))
        print(f"New name: %s %s" %(fname,lname))
        print(f"New address: %s %s %s %s" %(n,street,town,postcode))
        print("Is the new address correct?")
        cnf= input('''If so type "CONFIRM", type anything else to cancel" \n''')
        if(cnf=="CONFIRM"):
             self.fname=fname
             self.lname=lname
             self.address['n']=n
             self.address['street']=street
             self.address['town']=town
             self.address['postcode']=postcode 
             print("Admin information update was successful. Returning to menu...")
        else:
            print("Admion information update canceled")
            
    def print_details(self):
        print(f"Name: %s %s" %(self.fname,self.lname))
        print(f"Address: %s %s %s %s" %(self.address['n'],self.address['street'],self.address['town'],self.address['postcode']))
        if(self.full_admin_rights):
            print("Has full admin rights.")
        else:
            print("Doesn't have full admin rights.")
name_list=['A','B','C','D','E']
A_usedaddress_list=[]
B_usedaddress_list=[]
C_usedaddress_list=[]
D_usedaddress_list=[]
E_usedaddress_list=[]
usedaddress_list=[A_usedaddress_list,B_usedaddress_list,C_usedaddress_list,D_usedaddress_list,E_usedaddress_list]
while True:
    name=input('Enter your full name: ')
    if name in name_list:
        pass
    else:
        print('\nTRY TO ENTER YOUR FULL NAME PROPERLY!!!\n')
    

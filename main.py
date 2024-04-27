import purchase
import read

print("\n")
print("\t\t\tMaharjan Electronics")
print("\tAddress : New Road,Kathmandu || Phone : 01-4265667")

print("--------------------------------------------------------------------------------")
print("\t Welcome onboard, Have  nice time in our system.");
print("--------------------------------------------------------------------------------")

loop=True
while loop==True:
    a=read.read_()
    print("These are the options for you to carry out :")
    print("  1) Purchase the laptop")
    print("  2) Sell the laptop")
    print("  3) Exit the system")

    do=input("What would you like to do :")
    print("--------------------------------------------------------------------------------")

    if do=="1":
        purchase.pur(a)
    elif do=="2":
        sell()
    elif do=="3":
        print("Thank you for visiting us. Do visit us again.")
        break
    else:
        print("Invalid")
        break
    contin=input("Would you like to continue (Y/N):").upper()
    if contin=="Y":
        loop=True
    else:
        loop=False


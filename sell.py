import datetime
import read

def sell_(lap_di):
    print("\n")
    nam=input("Please enter your name to generate invoice :")
    user_quan={}
    user_price={}
    total_p={}
    laptop_dictionary=lap_di
    print("--------------------------------------------------------------------------------")
    print("Welcome to Selling Screen screen, We buy thsese laptops :")
    print("--------------------------------------------------------------------------------")
    print("S.N. \tLaptop Name \tCompany Name \tprice \tquantity   Graphic \tRam")
    print("--------------------------------------------------------------------------------")
    for i in range(1,len(laptop_dictionary)+1,1):
        if i==1:
            print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+laptop_dictionary[i][3]+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
        elif i==2:  
            print(str(i)+"\t   "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+laptop_dictionary[i][3]+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
        elif i==3:
            print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"     "+laptop_dictionary[i][2]+"\t   "+laptop_dictionary[i][3]+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
        elif i==4:
            print(str(i)+"\t "+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+laptop_dictionary[i][3]+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
        elif i==5:
            print(str(i)+"\t"+laptop_dictionary[i][0]+"  "+"\t"+laptop_dictionary[i][1]+"\t       "+laptop_dictionary[i][2]+"\t   "+laptop_dictionary[i][3]+"\t  "+laptop_dictionary[i][4]+" "+laptop_dictionary[i][5])
        print("--------------------------------------------------------------------------------")
    loop=True
    while loop==True:
        try:
            inp=int(input("Please input the S.N. of Laptop would you like to sell:"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a integer/numeric value.")
            inp= int(input("Which Laptop would you like to sell :"))
            print("\n")
        while inp<=0 or inp> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!") 
            try:
                inp= int(input("Please input the S.N. of Laptop would you like to sell :"))
                print("\n")
            except:
                print("You've entered unexpected value.Please enter a integer/numeric value.")
                inp= int(input("Please input the S.N. of  Laptop would you like to sell:"))
                print("\n")
        try:
            quant= int(input("How many laptop would you like to sell :"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a integer/numeric value.")
            quant= int(input("How many laptop would you like to sell :"))
            print("\n")
        try:
            used_for=int(input("How many years have you used the laptop :"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a valid number of year.")
            used_for=int(input("How many years have you used the laptop :"))
            print("\n")
        mp=int(laptop_dictionary[inp][2].replace("$",""))
        if used_for<1:
            sp=mp-((10/100)*mp)
            print("We can provide upto $"+str(sp)+" for your laptop.")
            print("\n")
        elif used_for>=1 and used_for<2:
            sp=mp-((25/100)*mp)
            print("We can provide upto $"+str(sp)+" for your laptop.")
            print("\n")
        elif used_for>=2 and used_for<3:
            sp=mp-((35/100)*mp)
            print("We can provide upto $"+str(sp)+" for your laptop.")
            print("\n")
        elif used_for>=3 and used_for<4:
            sp=mp-((45/100)*mp)
            print("We can provide upto $"+str(sp)+" for your laptop.")
            print("\n")
        else:
            sp=mp-((60/100)*mp)
            print("We can provide upto $"+str(sp)+" for your laptop.")
            print("\n")
            
        hap=input("Are you happy with the price of "+str(sp)+" per unit for your laptop (Y/N)?").upper()
        if hap=="Y":
            print("\n")
            print("We are glad you are happy with our price.")
            print("\n")
            final_price=sp*quant
            user_price[inp]=sp
            total_p[inp]=final_price
            user_quan[inp]=quant
            laptop_dictionary=lap_di
            laptop_dictionary[inp][3]=int(laptop_dictionary[inp][3])+int(quant)
            file = open("laptop.txt","w")
            for values in laptop_dictionary.values():
                file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
                file.write("\n")
            file.close()
            more=input("Enter Y if you want to sell more laptops :").upper()
            print("\n")
            if more!="Y":
                loop=False
        else:
            print("We're sorry that our price wasn't acceptable for you. Our company's policy wont allow us to increase the price. Sorry for the inconvinience")
            print("\n")
            more=input("Enter Y if you want to sell more laptops :").upper()
            print("\n")
            if more!="Y":
                loop=False
    grand_total=0            
    for unit_price in user_price:
        grand_total+=unit_price

    datim=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    uniq=str(datim)   
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) 
    d=str(t)      
    
    file=open(uniq+"-sell"+nam+".txt","w")      
    file.write("=====================================================================")
    file.write("\nMAHARJAN ELECTRONICS \t\t\t\tBill")
    file.write("\nName of Customer: "+str(nam)+"\t\t\t\tTime:"+d)
    file.write("\n=====================================================================")
    file.write("\nLAPTOP            QUANTITY            UNIT PRICE           TOTAL")                     
    file.write("\n---------------------------------------------------------------------")
          
    for input_val in user_quan.keys():           
        if input_val==1:
            file.write(str("\n"+laptop_dictionary[1][0]+"            "+str(user_quan[1])+"               "+str(user_price[1])+"                  "+str(user_quan[1])))
        elif input_val==2:
            file.write(str("\n"+laptop_dictionary[2][0]+"            "+str(user_quan[2])+"               "+str(user_price[1])"                  "+str(user_quan[1])))
        elif input_val==3:
            file.write(str("\n"+laptop_dictionary[3][0]+"            "+str(user_quan[3])+"               "+str(user_price[1])+"                  "+str(user_quan[1])))
        elif input_val==4:
            file.write(str("\n"+laptop_dictionary[4][0]+"            "+str(user_quan[4])+"               "+str(user_price[1])+"                  "+str(user_quan[1])))
        elif input_val==5:
            file.write(str("\n"+laptop_dictionary[5][0]+"            "+str(user_quan[5])+"               "+str(user_price[1])+"                  "+str(user_quan[1])))
       
    file.write("\n\n---------------------------------------------------------------------")
    file.write("\n\t\t\t            Your Grand Total is: "+str(grand_total))
    file.write("\n=====================================================================")
    file.close()

    print("\n\n")
    print("Print of INVOICE:")
    file=open(uniq+"-sell"+nam+".txt","r")
    print(file.read())
    file.close()
    

        
a=read.read_()
sell_(a)


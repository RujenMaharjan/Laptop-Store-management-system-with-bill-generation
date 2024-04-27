import datetime
import read

def pur(lap_di):
    print("\n")
    nam=input("Please enter your name to generate invoice :")
    user_input={}
    laptop_dictionary=lap_di
    print("--------------------------------------------------------------------------------")
    print("Welcome to Laptop purchasing screen, Here are our Laptop options :")
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
            inp=int(input("Please input the S.N. of Laptop would you like to buy:"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a integer/numeric value.")
            inp= int(input("Which Laptop would you like to buy :"))
            print("\n")
        while inp<=0 or inp> len(laptop_dictionary):
            print("Please provide a valid Laptop Id!!")
            try:
                inp= int(input("Which Laptop would you like to buy :"))
                print("\n")
            except:
                print("You've entered unexpected value.Please enter a integer/numeric value.")
                inp= int(input("Which Laptop would you like to buy :"))
                print("\n")
        try:
            quant= int(input("Please provide quantity of laptop you want to buy:"))
            print("\n")
        except:
            print("You've entered unexpected value.Please enter a integer/numeric value.")
            quant= int(input("Please provide quantity of laptop you want to buy:"))
            print("\n")
        lap_quantity=laptop_dictionary[inp][3]
        while quant <= 0 or quant > int(lap_quantity):
            print("Sorry we don't currently have "+str(quant)+" "+laptop_dictionary[inp][0]+" laptop right now. Please re-enter the quantity.")
            try:
                quant= int(input("Please provide quantity of laptop you want to buy:"))
                print("\n")
            except:
                print("You've entered unexpected value.Please enter a integer/numeric value.")
                quant= int(input("Please provide quantity of laptop you want to buy:"))
                print("\n")
        user_input[inp]=quant
        laptop_dictionary[inp][3]=int(laptop_dictionary[inp][3])-int(quant)
        file = open("laptop.txt","w")
        for values in laptop_dictionary.values():
            file.write(str(values[0])+","+str(values[1])+","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5]))
            file.write("\n")
        file.close()
        cont=input("Do you want to continue (Y/N) :").upper()
        print("\n")
        if cont=="N":
            loop=False
        elif cont=="Y":
            loop=True
        else:
            print("\n")
            cont=input("You've entered invalid input. If you want to continue enter Y, if you want to proceed to invoice generation enter N? :").upper()
            if cont=="N":
                loop=False
            elif cont=="Y":
                loop=True
    total_amount=0
    for keys in user_input.keys():
        if keys==1:
            razer_unit_price= int(laptop_dictionary[1][2].replace("$",""))
            razer_qty=int(user_input[keys])
            razer_amt=razer_unit_price*razer_qty
            total_amount+=razer_amt
        elif keys==2:
            xps_unit_price= int(laptop_dictionary[2][2].replace("$",""))
            xps_qty=int(user_input[keys])
            xps_amt=xps_unit_price*xps_qty
            total_amount+=xps_amt
        elif keys==3:
            alw_unit_price= int(laptop_dictionary[3][2].replace("$",""))
            alw_qty=int(user_input[keys])
            alw_amt=alw_unit_price*alw_qty
            total_amount+=alw_amt
        elif keys==4:
            sft_unit_price= int(laptop_dictionary[4][2].replace("$",""))
            sft_qty=int(user_input[keys])
            sft_amt=sft_unit_price*sft_qty
            total_amount+=sft_amt
        elif keys==5:
            mac_unit_price= int(laptop_dictionary[5][2].replace("$",""))
            mac_qty=int(user_input[keys])
            mac_amt=mac_unit_price*mac_qty
            total_amount+=mac_amt

    vat=13.0
    total_amount=total_amount+(vat*total_amount)/100
    discount=0
    grand_total=0
    disc=0.0
    if total_amount>0 and total_amount<=5000:
        grand_total=total_amount
    elif total_amount>5000 and total_amount<=10000:
        disc=5.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    elif total_amount>10000 and total_amount<=20000:
        disc=10.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    elif total_amount>20000 and total_amount<=50000:
        disc=15.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
    else:
        disc=18.0
        discount=(disc*total_amount)/100
        grand_total=total_amount-discount
        
    datim=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
    uniq=str(datim)   
    t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) 
    d=str(t)      
    
    file=open(uniq+"-purchase"+nam+".txt","w")      
    file.write("=====================================================================")
    file.write("\nMAHARJAN ELECTRONICS \t\t\t\tBill")
    file.write("\nName of Customer: "+str(nam)+"\t\t\t\tTime:"+d)
    file.write("\n=====================================================================")
    file.write("\nLAPTOP            QUANTITY            UNIT PRICE           TOTAL")                     
    file.write("\n---------------------------------------------------------------------")
          
    for input_val in user_input.keys():           
        if input_val==1:
            file.write(str("\n"+laptop_dictionary[1][0]+"            "+str(user_input[1])+"               "+laptop_dictionary[1][2]+"                  "+str(razer_amt)))
        elif input_val==2:
            file.write(str("\n"+laptop_dictionary[2][0]+"            "+str(user_input[2])+"               "+laptop_dictionary[2][2]+"                  "+str(xps_amt)))
        elif input_val==3:
            file.write(str("\n"+laptop_dictionary[3][0]+"            "+str(user_input[3])+"               "+laptop_dictionary[3][2]+"                  "+str(alw_amt)))
        elif input_val==4:
            file.write(str("\n"+laptop_dictionary[4][0]+"            "+str(user_input[4])+"               "+laptop_dictionary[4][2]+"                  "+str(sft_amt)))
        elif input_val==5:
            file.write(str("\n"+laptop_dictionary[5][0]+"            "+str(user_input[5])+"               "+laptop_dictionary[5][2]+"                  "+str(mac_amt)))
       
    file.write("\n\n---------------------------------------------------------------------")
    file.write("\n\t\t\t    Your final amount with 13% VAT : "+str(total_amount))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t           Your "+str(disc)+"% discounted amount is: "+str(discount))
    file.write("\n---------------------------------------------------------------------")
    file.write("\n\t\t\t            Your Grand Total is: "+str(grand_total))
    file.write("\n=====================================================================")
    file.close()

    print("\n\n")
    print("Print of INVOICE:")
    file=open(uniq+"-purchase"+nam+".txt","r")
    print(file.read())
    file.close()

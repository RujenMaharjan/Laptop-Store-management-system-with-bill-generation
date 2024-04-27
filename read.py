def read_():
    file= open("laptop.txt","r");
    lap_di={}
    laptop_id= 1
    for line in file:
        line=line.replace("\n","")
        lap_di[laptop_id]=line.split(",")
        laptop_id+=1

    file.close()
    return lap_di



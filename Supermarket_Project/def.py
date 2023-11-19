def bill():
    total = 0
    for item in trv.get_children():
        trv.delet(item)
    for i in range(len(sb)):
        if(int(sb[i].get())>0):
            price = int(sb[i],get())* menu[i][i]
            total += price
            myst = (str(menu[i][i]),str(sb[i].get()),str(price))
            trv.insert('','end',iid = i,text=menu[i][0],values=myst)
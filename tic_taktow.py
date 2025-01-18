dict = {'1':"monitor",'2':"Mouse",'3':"Keyboard",'4':"CPU",'5':"Disk"}

l = []


choice = input("> ")
while choice !=0:
    if choice in dict:
        l.append(dict[choice])
    elif choice == 'ok':
        print(l)
        break
    else:
        print(dict)
    choice = input("> ")
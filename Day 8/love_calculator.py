def calculate_love_score():
    name1 = input("Enter name of 1st person : ")
    name2 = input("Enter name of 2nd person : ")
    
    name = list(name1) + list(name2)
    true = ["t","r","u","e"]
    love = ["l","o","v","e"]
    t_list = [0,0,0,0]
    l_list = [0,0,0,0]
    
    for i in range(len(name)):
        if name[i] in true:
            for j in range(len(true)):
                if name[i]==true[j]:
                    t_list[j]+=1

    for i in range(len(name)):
        if name[i] in love:
            for j in range(len(love)):
                if name[i]==love[j]:
                    l_list[j]+=1       
    love_score = sum(t_list)*10+sum(l_list)
    print(love_score)


calculate_love_score()         
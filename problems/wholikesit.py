def likes(names):
    a = ""
    if(len(names)==0):
        a = "no one likes this"
    elif(len(names)==1):
        a = names[0] + " likes this"
    elif(len(names)==2):
        a = names[0] + " and " + names[1] + " like this"
    elif(len(names)==3):
        a = names[0] + ", " + names[1] + " and " + names[2] + " like this"
    elif(len(names)>3):
        num = str(int(len(names)) - 2)
        a = names[0] + ", " + names[1] + " and " + num + " others like this"
    return a

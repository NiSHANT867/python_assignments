def ds(name,rollno):
   # creating data structures
    list = [name,rollno]
    tuple = (name,rollno)
    set = { name, rollno}
    dict = {"name": name,"rollno":rollno}

    
    print("List:", list)
    print("Tuple:", tuple)
    print("Set:", set)
    print("Dictionary:",dict)

    # Change values during runtime
    name2 = "Vinit"
    rollno2 = 56
    
    #changing list items
    list[0] = name2
    list[1] = rollno2
    print("Updated List:", list)
    
    #changing tuple items
    tuple = (name2,rollno2)
    print("Updated Tuple:", tuple)
    
    #changing set items
    set.remove(name)
    set.remove(rollno)
    set.add(name2)
    set.add(rollno2)
    print("Updated Set:", set)
    
    #changing dictnory items
    dict["name"] = name2
    dict["rollno"] = rollno2
    print("Updated Dictionary:", dict)

    
 # Deleting the data structures
    del list
    del tuple
    del set
    del dict

    


ds("Nishant" ,23)

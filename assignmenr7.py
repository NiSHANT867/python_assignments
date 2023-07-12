def func(file='python.txt'):
    try:
        f=open(file,'+a')
        f.writelines(["name:Nishant\n","roll no: 23\n","class: COA\n"])
        f.seek(0)
        print(f.readlines())
    except:
        f.close()    

func()
    
        
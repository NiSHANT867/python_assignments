from tkinter import *
import webbrowser

def search():
    
    selected_option = s1.get()
    sites_faqs = {
        "Amazon" : "https://aws.amazon.com/faqs/" ,
        "Flipkart" : "https://seller.flipkart.com/sell-online/faq" ,
        "Meesho" : "https://meeshodesk.freshdesk.com/support/solutions/81000151996",
        "Myntra" : "https://www.myntra.com/faqs",
    }
    webbrowser.open(sites_faqs[selected_option])
    
    
obj = Tk(className=" Faqs")

l1 = Label(obj,text="Choose a site",font=("Times new roman",20))
l1.grid()

s1 = StringVar(obj)
s1.set("Amazon")
options1 = ["Amazon", "Flipkart","Meesho","Myntra"]
menu1 = OptionMenu(obj, s1, *options1)
menu1.grid()

s2 = StringVar(obj)
s2.set("Instagram Ads")
options2 = ["Instagram Ads", "YouTube Ads"]
menu2 = OptionMenu(obj, s2, *options2)
menu2.grid() 

l2 = Label(obj,text=" ",font = ("Italic",15),)
l2.grid()

b1 = Button(obj,text= "Search",font = ("Times new roman",15),command=search)
b1.grid()

obj.mainloop()

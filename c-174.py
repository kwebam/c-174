from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
root = Tk()
root.geometry("900x500")
#-----------------------------Burger image-----------------------------
burger = ImageTk.PhotoImage(Image.open ("burger1.png"))
burger_image = Label(root)
burger_image["text"] = burger
burger_image.place(relx = 0.5, rely = 0.7, anchor = CENTER)
#-----------------------------Heading Mcdonalds-----------------------------
label_heading = Label(root, text = "Mcdonalds", font = ("times", 40, "bold"), fg = "red")
label_heading.place(relx = 0.12, rely = 0.1, anchor = CENTER)
#-----------------------------Label_Select_Text-----------------------------
label_select_text = Label(root, text = "Select Dish", font = ("times", 15))
label_select_text.place(relx = 0.06, rely = 0.2, anchor = CENTER)
#-----------------------------Drop down Main Dish-----------------------------
dish_list = ["Burger", "Iced-Americano"]
dish_drop_down = ttk.Combobox(root, state = "readonly", values = dish_list)
dish_drop_down.place(relx = 0.25, rely = 0.2, anchor = CENTER)
#-----------------------------Label Select Add-on-----------------------------
label_select_addon = Label(root, text = "Select Add-on", font = ("times", 15))
label_select_addon.place(relx = 0.08, rely = 0.5, anchor = CENTER)
#-----------------------------Drop Down Tooppings-----------------------------
toppings = []
toppings_drop_down = ttk.Combobox(root, state = "readonly", values = toppings)
toppings_drop_down.place(relx = 0.25, rely = 0.5, anchor = CENTER)
#-----------------------------Amount-----------------------------
dish_amount = Label(root, font = ("times", 15))
dish_amount.place(relx = 0.2, rely = 0.75, anchor = CENTER)

class parent():
    def __init__(self):
        print("This is Parent Class")
    
    def menu(dish):
        if dish == "burger":
            print("You can add following toppings")
            toppings = ["More Cheese", "Add jalpeno"]
            toppings_drop_down["values"]
            print("add More Cheese | jalopeno")
        elif dish == "iced_americano":
            print("You can add following toppings")
            toppings = ["Choclate", "Caramel"]
            toppings_drop_down["values"]
            print("add Choclate flavour | caramel flavour")
        else:
            print("Please Enter valid Dish")
    def final_amount(dish, add_ons):
        if dish == "burger" and add_ons == "cheese":
            print("You need to pay 250 USD")
            dish_amount["text"] = "You need to pay 250 USD"
        elif dish == "burger" and add_ons == "jalpeno":
            print("You need to pay 350 USD")
            dish_amount["text"] = "You need to pay 350 USD"
        elif dish == "iced_americano" and add_ons == "choclate":
            print("You need to pay 250 USD")
            dish_amount["text"] = "You need to pay 250 USD"
        elif dish == "iced_americano" and add_ons == "caramel":
            print("You need to pay 450 USD")
            dish_amount["text"] = "You need to pay 450 USD"
            
class child1(parent):
    def __init__(self, dish):
        self.new_dish = dish
        
    def get_menu(self):
        new_dish = dish_drop_down.get()
        parent.menu(new_dish)

child1_object = child1(dish_drop_down.get)
child1_object.get_menu()
        
class child2(parent):
    def __init__(self, dish, addons):
        self.new_dish = dish
        self.addons = addons
        
    def get_menu(self):
        parent.menu(self.new_dish)
    
    def get_final_amount(self):
        new_dish = dish_drop_down.get()
        addons = toppings_drop_down.get()
        parent.final_amount(new_dish, addons)


child2_object = child2(toppings_drop_down, dish_drop_down.get)
child2_object.get_final_amount()

btn_addons = Button(root, text = "Check Add-ons", command = child1_object.get_menu(), bg = "blue", fg = "white", relief = FLAT)
btn_addons.place(relx = 0.06, rely = 0.3, anchor = CENTER)

btn_amount = Button(root, text = "Amount", command = child2_object.get_final_amount(), bg = "blue", fg = "white", relief = FLAT)
btn_amount.place(relx = 0.04, rely = 0.6, anchor = CENTER)

root.mainloop()
from Tkinter import *

class Application(Frame):

    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #create instruction label
        Label(self,
              text = "Enter the information for your hamburger order"
              ).grid(row = 0, column = 0, columnspan=2, sticky = W)

        #create a label and text entry for their name
        Label(self,
              text = "Name: "
              ).grid(row=1, column=0, sticky=W)
        self.nameEntry = Entry(self)
        self.nameEntry.grid(row=1, column=1, sticky=W)

        #create a label for toppings check buttons
        Label(self,
              text="Please select your topping(s):"
              ).grid(row=2, column=0, sticky=W)

        #create cheese check button
        self.cheese = BooleanVar()
        Checkbutton(self,
                    text = "cheese",
                    variable = self.cheese
                    ).grid(row=2, column=1, sticky=W)


        #create lettuce check button
        self.lettuce = BooleanVar()
        Checkbutton(self,
                    text = "lettuce",
                    variable = self.lettuce
                    ).grid(row=2, column=2, sticky=W)

        #create onion check button
        self.onion = BooleanVar()
        Checkbutton(self,
                    text = "onion",
                    variable = self.onion
                    ).grid(row=2, column=3, sticky=W)

        #create tomato check button
        self.tomato = BooleanVar()
        Checkbutton(self,
                    text = "tomato",
                    variable = self.tomato
                    ).grid(row=3, column=1, sticky=W)

        #create pickles check button
        self.pickles = BooleanVar()
        Checkbutton(self,
                    text = "pickles",
                    variable = self.pickles
                    ).grid(row=3, column=2, sticky=W)

        #create mustard check button
        self.mustard = BooleanVar()
        Checkbutton(self,
                    text = "mustard",
                    variable = self.mustard
                    ).grid(row=3, column=3, sticky=W)

        #create mayo check button
        self.mayo = BooleanVar()
        Checkbutton(self,
                    text = "mayo",
                    variable = self.mayo
                    ).grid(row=4, column=1, sticky=W)

        #create ketchup check button
        self.ketchup = BooleanVar()
        Checkbutton(self,
                    text = "ketchup",
                    variable = self.ketchup
                    ).grid(row=4, column=2, sticky=W)

        #create bun label
        Label(self,
              text="Select your bun:"
              ).grid(row=5, column=0, sticky=W)

        #create variable for single bun
        self.bun_choice= StringVar()
        self.bun_choice.set(None)

        #create bun radio buttons
        bun_options=["white", "wheat"]
        column=1
        for bun in bun_options:
            Radiobutton(self,
                        text = bun,
                        variable=self.bun_choice,
                        value = bun
                        ).grid(row=5, column=column, sticky=W)
            column +=1

        
        #create a submit button
        Button(self,
               text="Order",
               command=self.read_back
               ).grid(row=6,column=0, sticky=W)

        self.order_txt = Text(self, width=75, height=10, wrap=WORD)
        self.order_txt.grid(row=7,column=0,columnspan=4)


    def read_back(self):
        #get values from the GUI
        name=self.nameEntry.get()
        toppings = []
        if self.cheese.get():
            toppings.append("cheese")
        if self.lettuce.get():
            toppings.append("lettuce")
        if self.onion.get():
            toppings.append("onion")
        if self.tomato.get():
            toppings.append("tomato")
        if self.pickles.get():
            toppings.append("pickles")
        if self.mustard.get():
            toppings.append("mustard")
        if self.mayo.get():
            toppings.append("mayo")
        if self.ketchup.get():
            toppings.append("ketchup")
        bun_choice = self.bun_choice.get()


        #create the order
        self.counter=0
        order = "The hamburger for "
        order += name
        order += " has "
        for i in range(len(toppings)):
            self.counter += 1
            if len(toppings) != self.counter:
                order+= toppings[i] + ", "
            if self.counter == len(toppings):
                order+= "and " + toppings[i]
        order += " toppings on it and is on a "
        order += bun_choice
        order += " bun."

        #display the order
        self.order_txt.delete(0.0, END)
        self.order_txt.insert(0.0, order)
        

#main
root=Tk()
root.title("Hamburger Builder")

app=Application(root)
root.mainloop()

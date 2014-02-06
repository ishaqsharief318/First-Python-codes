#ch 10 proj 3
#group 7

from Tkinter import *
import random

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Choose your weapon"
              ).grid(row = 0, column = 0, sticky = W)

        Label(self,
              text = "Select one:"
              ).grid(row = 1, column = 0, sticky = W)
        
        #Radio button array(Python:List)
        RPS_Options = [
            ("ROCK","ROCK"),
            ("PAPER","PAPER"),
            ("SCISSORS","SCISSORS"),
        ]

        self.fav = StringVar()
        #We may need to set this to none. I did not need to do it on my mac.

        #This for loop goes through and makes the 3 different radio buttons from RPS_Options
        for text, mode in RPS_Options:
            rb = Radiobutton(self, text=text,
                             variable=self.fav, value=mode)
            rb.grid(sticky = W)
 
        #Initalizing the fight button and its commands and text then assigning it to the grid
        self.fight_bttn = Button(self)
        self.fight_bttn["text"]= "Fight!"
        self.fight_bttn["command"] = self.fight
        self.fight_bttn.grid()

        self.results_txt = Text(self, width = 40, height = 5, wrap = WORD)
        self.results_txt.grid(row = 20, column = 0, columnspan = 3)
        
    #I definded a method for the random assignment for the computer then returned it
    def cChoice(self):
        self.choices = ["ROCK", "PAPER", "SCISSORS"]
        self.random_choice = random.randrange(0,3,1)
        self.comp_choice = self.choices[self.random_choice]
        return self.comp_choice
        
    #Fight Function
    def fight(self):
        game_text = ""
        #In lab we did not refrence the .get() method which was why we were getting PY_VAR0
        user_choice=self.fav.get()
        c_choice=self.cChoice()
        #Dictionary for the choices
        outcome = {"SCISSORS":"PAPER", #Scissors beats paper
                   "PAPER":"ROCK",      #Paper beats Rock
                   "ROCK":"SCISSORS"}   #Rock beats scissors
        #If the user does not choose a radio button
        if not user_choice:
            game_text = "Please choose a radio button!"
        #If the user and the computer choose the same choice
        elif user_choice == c_choice:
            game_text = "You tied!"
        #If the game throws a value in the dictionary equal to its succesor then you have won
        elif outcome[user_choice] == c_choice:
            game_text = "The game threw: %s : You won!" %c_choice
        #Otherwise you have lost if it doesn't run the elif above this!
        else:
            game_text = "The game threw: %s : You Lost!" %c_choice
        
        #display results
        self.results_txt.delete(0.0, END)
        self.results_txt.insert(0.0, game_text)
       

        

# main
root = Tk()
root.title("Rock, Paper, Scissors")
app = Application(root)
root.geometry("300x200")
root.mainloop()
        

# First of all I would like to start with the explanation that this is 
# not a spam tool. I did not use this for spamming anybody but purely to get attention to 
# the problem i was facing from the 'perpetrators' . 

# I used to play an android based game which I was addicted to. 
# Spending upto 4-5 hours a day. It involved builidng castles, armies, attacking other people etc
#  However there were a few issues with
# the game, mostly server issues. After a supposedly
# "big" update, the game started having plenty of issues. Lag, crashes etc. 
# Whenever you were being attacked in the game you had a notification (to prepare).
# I dint get those notifications and lost my armies( took a week to make a sizeable one)
# I wrote to the developers but got no response. This became very common over the next few days. 
# Then one day when I finally had a decently sized army , the game was hacked. I lost everything again. I wrote to the 
# developers . A lot of people did, a few got their accounts restored, I dint. I waited patiently for 2 weeks, but to no avail.
# Thats when I wrote a small little script (putting my programming skills to 
#   some decent use) to send bulk emails. Sent about 200 emails in 1 day.
#   The result account restored the next day :) . 

#   So please, do not use this to trouble others. Use it for that
#   developer who dsnt respond to you, to that airlines that has been ignoring your emails.
#   Use it for good.




from Tkinter import *
import smtplib

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        Label(self,
              text = " Bulk Emailer"
              ).grid(row = 0, column = 1, columnspan = 1, sticky = W)
        Label(self,
            text = "From Address : ").grid(row = 1, column = 0, sticky = W)
        self.frmadd = Entry(self)
        self.frmadd.grid(row = 1, column = 1, sticky = W)

        Label(self,
            text = "Password : ").grid(row = 1, column = 3, sticky = W)
        self.password = Entry(self, show = "*")
        self.password.grid(row = 1, column = 4, sticky = W)

        Label(self,
            text = "To Address : ").grid(row = 2, column = 0, sticky = W)
        self.toadd = Entry(self)
        self.toadd.grid(row = 2, column = 1, sticky = W)

        Label(self,
            text = "Number of emails to send : ").grid(row = 3, column = 0, sticky = W)
        self.number = Entry(self)
        self.number.grid(row = 3, column = 1, sticky = W)

        Label(self,
              text = " Content").grid(row = 4, column= 0, sticky = W)
        self.content = Text(self, width = 45, height = 10, wrap = WORD)
        self.content.grid(row = 5, column = 0, columnspan = 4)

        Button(self,
               text = "Send",
               command = self.send
               ).grid(row = 6, column = 0, sticky = E)

        Button(self,
               text = "Clear",
               command = self.clear
               ).grid(row = 6, column = 1, sticky = E)

    def clear(self):
      self.frmadd.delete(0,END)
      self.toadd.delete(0, END)
      self.content.delete(0.0, END)
      self.number.delete(0,END)

    def send(self):
      fromaddr = self.frmadd.get()
      toaddr = self.toadd.get()
      msg = self.content.get(0.0,END)

      number = self.number.get()

      password = self.password.get()

      server = smtplib.SMTP('smtp.gmail.com:587')
      server.starttls()
      server.login(fromaddr,password)

      count = 0
      while count < int(number):
          server.sendmail(fromaddr, toaddr, msg)
          count += 1

      self.content.delete(0.0,END)
      self.content.insert(0.0,"Your Email has been sent")
        # except Exception, e:
        #   raise e
        #   self.content.delete(0.0,END)
        #   self.content.insert(0.0,e)
      server.quit()


        

root = Tk()
root.title("Bulk Emailer")
root.geometry("500x400")
app = Application(root)
root.mainloop()

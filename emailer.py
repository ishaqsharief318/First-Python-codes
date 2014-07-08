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

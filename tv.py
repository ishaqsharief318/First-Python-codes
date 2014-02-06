
class Television(object):
    """Television"""

    def __init__(self, channel, volume, is_on):
        self.__channel = channel
        self.volume = volume
        self.is_on = is_on

    def __str__(self):
        if self.is_on == "on":
            print "The television is on!" + "\nChannel: " + str(self.__channel) + "\nVolume: " + str(self.volume)
        else:
            print "The television is off!"
            
    def toggle_power(self):
        print "Right now your tv is: " + self.is_on
        while True:
            user_power = raw_input("Power on or off: ")
            if user_power == "on":
                self.is_on = "on"
                break
            elif user_power == "off":
                self.is_on = "off"
                break
            else:
                print "\nPlease enter valid input."
        
    def get_channel(self):
        print "You are on channel: " + str(self.__channel)
        
    def set_channel(self):
        while True:
            user_channel = raw_input("What would you like to change the channel to: ")
            if (int(user_channel) >= 0) and (int(user_channel) <= 499):
                self.__channel = int(user_channel)
                self.get_channel()
                break
            else:
                print "Please enter a valid selection"

    def raise_volume(self):
        if (self.volume < 10):
            self.volume += 1
            print "Now your volume is at: " + str(self.volume)
        else:
            print "Your volume is at the maximum of 10"

    def lower_volume(self):
        if (self.volume > 0):
            self.volume += -1
            print "Now your volume is at: " + str(self.volume)
        else:
            print "Your volume is at the minimum of 0"

tv = Television(30,3,"on")
while True:
    print "\n0 - Exit" + "\n1 - Toggle Power" + "\n2 - Change Channel" + "\n3 - Raise Volume" + "\n4 - Lower Volume"
    try:
        user_menu = int(raw_input("What is your selection?: "))
        if user_menu == 0:
            break
        elif user_menu == 1:
            print "\nPower Toggle"
            tv.toggle_power()
        elif user_menu == 2:
            print "\nChange Channel"
            tv.set_channel()
        elif user_menu == 3:
            print "\nRaise Volume"
            tv.raise_volume()
        elif user_menu == 4:
            print "\nLower Volume"
            tv.lower_volume()
        else:
            print "Choose a valid option!"
    except:
        print "Please enter a valid selection!"

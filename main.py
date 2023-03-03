# Aggie Figueredo, A02356240

# Class for the machine. It includes all the arguments used for the function.
class Artomat:
    def __init__(self, money = 0, hopper = 0, bin1 = 10, bin2 = 10, bin3 = 10, bin4 = 10, text1 = " ", text2 = " ", text3 = " ", text4 = " "):
        self.money =  money
        self.hopper = hopper
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4

    # Prints the status of the machine (How many of each thing there are left and how much money there is).
    def printStatus(self):
        print("1:", self.bin1, self.text1)
        print("2:", self.bin2, self.text2)
        print("3:", self.bin3, self.text3)
        print("4:", self.bin4, self.text4)
        print("There is $ ", (self.money * 0.25), " in the machine.")
        print("There is $ ", (self.hopper * 0.25), " in the hopper.")

    # Adds the quarters to the hopper each time they are inserted.
    def dropQuarter(self):
        print("Ching")
        self.hopper += 1

    ''' The pullKnob function explains that the machine will expend a product if:
    - There is enough money in the hopper ($0.75 or more)
    - There is enough of each product left.
    It also sends the money from the hopper to the machine.'''
    def pullKnob(self, choice):
        if self.hopper >= 3:
            if choice == 1:
                if self.bin1 > 0:
                    print("A pack of ", self.text1, " comes to your hands.")
                    self.money += self.hopper
                    self.hopper = 0
                    self.bin1 -= 1
                else:
                    print("No art left.")
            elif choice == 2:
                if self.bin2 > 0:
                    print("A pack of ", self.text1, " comes to your hands.")
                    self.money += self.hopper
                    self.hopper = 0
                    self.bin2 -= 1
                else:
                    print("There's no art left.")
            elif choice == 3:
                if self.bin3 > 0:
                    print("A pack of ", self.text3, " comes to your hands.")
                    self.money += self.hopper
                    self.hopper = 0
                    self.bin3 -= 1
            elif choice == 4:
                if self.bin4 > 0:
                    print("A pack of ", self.text4, " comes to your hands.")
                    self.money += self.hopper
                    self.hopper = 0
                    self.bin4 -= 1
                else:
                    print("There's no art left.")
            else:
                print("Nothing happens.")
    # Restock of the products.
    def restock(self):
        self.bin1 = 10
        self.bin2 = 10
def main():
    photoMachine = Artomat(text1="Adams",text2="Arbus",text3="Dali",text4="Lange")
    portraitMachine = Artomat(money=212,hopper=2,bin1=1,bin2=0,bin3=8,bin4=10,text1="Picasso",text2="Rembrandt",text3="Van Gogh",text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()




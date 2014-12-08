from time import time
from datetime import datetime
import os

unknown = """Unknown command! Please try one of the following:
take\nstatus\nsave\nlist\nload\nfinish"""

noOrdersYet = "Nobody has ordered yet! Please execute 'take' command."

finishError = """You have unsaved orders. If you wish to discard these
orders and continue, type 'finish' again.
Otherwise, execute 'save' command to save your order."""

finishMessage = "Finishing order. Goodbye!"

commands = ["take", "status", "save", "list", "load", "finish"]


class Order():
    orderList = {}
    finished = False
    orderFiles = {}

    def takeOrder(self, name, price):
        print "Taking order from %s for %d" % (name, float(price))
        self.name = name
        self.price = float(price)
        if self.name not in self.orderList:
            self.orderList[self.name] = float(self.price)
        else:
            self.orderList[self.name] += float(self.price)

    def getStat(self):
        if len(self.orderList) == 0:
            return noOrdersYet
        else:
            return self.orderList

    def saveOrder(self):
        if len(self.orderList) == 0:
            return noOrdersYet
        else:
            ts = time()
            stamp = "orders_"
            stamp += datetime.fromtimestamp(ts).strftime('%Y_%m_%d_%H_%M_%S')
            myfile = open(stamp, "w")
            for key in self.orderList:
                toWrite = "'%s' - %d\n" % (key, self.orderList[key])
                myfile.write(toWrite)
            myfile.close()
            self.orderList = {}

    def listOrders(self):
        programPath = os.path.dirname(os.path.realpath(__file__))
        dirList = os.listdir(programPath)
        dirList = [x for x in dirList if x.startswith('orders_')]
        if len(dirList) == 0:
            return "There are no order records. Please execute 'take' command."
        for i in range(0, len(dirList)):
            self.orderFiles[i+1] = dirList[i]
            print "[%d] - %s" % (i+1, dirList[i])

    def loadOrder(self):
        self.orderList = {}
        if len(self.orderFiles) == 0:
            return "There are no order records."
        fLoad = raw_input("File number:> ")
        if int(fLoad) in self.orderFiles:
            myfile = open(self.orderFiles[int(fLoad)], "r+")
            for line in myfile:
                (key, val) = line.split(" - ")
                self.orderList[key] = int(val)
            myfile.close()
            return self.orderList
        else:
            return "Please enter a correct number."

    def finish(self):
        if len(self.orderList) == 0:
            self.finished = True
            return finishMessage
        else:
            print (finishError)
            command = raw_input("---> ")
            if command == "finish":
                self.orderList = {}
                self.finished = True
                return finishMessage
            if command == "save":
                self.saveOrder()
                return finishMessage


def main():
    myOrder = Order()

    while myOrder.finished is False:
        command = raw_input("--> ")
        if command not in commands:
            return unknown

        if command == "take":
            name = raw_input("Enter name: ")
            price = raw_input("Enter price: ")
            myOrder.takeOrder(name, price)

        if command == "status":
            print(myOrder.getStat())

        if command == "save":
            myOrder.saveOrder()

        if command == "list":
            print(myOrder.listOrders())

        if command == "load":
            print(myOrder.loadOrder())

        if command == "finish":
            myOrder.finish()

if __name__ == '__main__':
    main()

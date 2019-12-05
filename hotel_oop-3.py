import json

class Node:

    def __init__(self):

        self.left = None
        self.right = None

    def insert_price(self, data):
        if self.data:
            if data["single_room_price"] < self.data["single_room_price"]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data["single_room_price"] > self.data["single_room_price"]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def insert_rating(self, data):
        if self.data:
            if data["star_rating"] < self.data["star_rating"]:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data["star_rating"] > self.data["star_rating"]:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def find_price(self, lkpval):
        if lkpval < self.data["single_room_price"]:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data["single_room_price"]:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# class hotel finder
class HotelFinder:

    hotels = [] # list of hotels
    hotelsHashTable = {}
    hotelsTreeByPrice = Node()
    hotelsTreeByRating = Node()

    def available_hotels(self):
        money = self.user_input_money()
        desiredStar = self.user_input_desiredStar()
        availableHotels = []
        for key in self.hotelsHashTable:
            hotel = self.hotelsHashTable[key]
            if int(money) >= int(hotel["single_room_price"]) and int(hotel["star_rating"]) == int(desiredStar):
                availableHotels.append(hotel)
        for hotel in availableHotels:
            print('--------------------------------')
            for key, value in hotel.items():
                print(key, '-', value)


    def __init__(self):
        # init hotels
        with open('hotels.json') as filename:
            self.hotels = json.load(filename)
        self.hotelsHashTable = {}
        for hotel in self.hotels:
            self.hotelsHashTable[hotel["phone"]] = hotel
        pass

    def user_input_desiredStar(self):
        ds = input("Insert your desired star from 1 to 5: ")
        while True:
            try:
                ds = int(ds)
                if ds < 1 or ds > 5:
                    ds = input("Star count of a hotel may not be less than zero and more than 5")
                else:
                    return ds
            except ValueError as e:
                print("Try again")
                ds = input("Insert your desired star from 1 to 5: ")
                continue

    def getTheBestChoise(self):
        money = self.user_input_money()
        star = 1
        bestHotel = None
        for key in self.hotelsHashTable:
            h = self.hotelsHashTable[key]
            if money >= int(h["single_room_price"]) and star < int(h["star_rating"]):
                star = int(h["star_rating"])
                bestHotel = h
        for key, value in bestHotel.items():
            print(key, '---', value)


    def getHotelByPhoneNumber(self):
        hotel_string = 0
        phoneNumber = input("Input the phone number in the following format (###) #######: ")

        # Check if dict contains any entry with key 'test'
        if phoneNumber in self.hotelsHashTable:
            h = self.hotelsHashTable[phoneNumber]
            hotel_string = "Hotel: {}, Stars: {}, Price: {}".format(h["hotel_name"], h["star_rating"],
                                                                    h["single_room_price"])
            print(hotel_string)
        else:
            print("No such Hotel exists with that phone number")

        pass

    def check(self):
        while True:
            checks = input("Do you wanna try again? yes/no: ")
            print(checks)
            if checks == "no":
                return False
            elif checks == "yes":
                return True
            else:
                print('Please enter yes/no: ')
        pass

    def user_input_money(self):
        money = input("Insert the initial balance above 0: ")
        while True:
            try:
                money = int(money)
                if money > 0:
                    return money
                elif money < 0:
                    money = input("not intereseted in your debts")
            except ValueError as e:
                print("Try again")
                ds = input("Insert your desired star from 1 to 5: ")
                continue

    def poll(self):
        flag = True
        while flag:
            action = int(input(
                "Please input what you want (1 - for search based on PhoneNumber, 2 - For gettingthe best hotel based on money, 3 - for search based on stars): "))
            if action == 1:
                self.getHotelByPhoneNumber()
            elif action == 2:
                self.getTheBestChoise()
            elif action == 3:
                self.available_hotels()
            else:
                print(" Wrong action")
            pass
            flag = self.check()


if __name__ == "__main__":
    print("This app is for finding hotels")

    hotel_finder = HotelFinder()
    hotel_finder.poll()



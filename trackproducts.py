
class Product(object):

    def __init__(self, item_name, price, weight, brand):

        self.item_name = item_name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.tax = 0.9
        self.cost = self.price + self.tax
        self.status = "For Sale"
        self.display_all()

    def display_all(self):
        print "Item: " + str(self.item_name)
        print "Price: $" + str(self.price)
        print "Weight: " + str(self.weight) + " lbs"
        print "Brand: " + str(self.brand)
        print "Total: $" + str(self.cost)
        print "Status: " + str(self.status)
        print '\n'


    #def sell(self):
        #self.status


    #def returnn(self):


apple_pie = Product("Apple Pie", 5, 1, "Target")


cereal = Product("Cheerios", 3.49, 2, "General Mills")

oranges = Product("Oranges", 4, 2, "Cuties")

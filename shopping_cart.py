class ShoppingCart:
    # write your code here

    def __init__(self, emp_discount=None):
      self.total = 0
      self.employee_discount = emp_discount
      self.items = []


    def add_item(self, name, price, quantity=1):
       self.items.append(
           {'name': name,
            'price': price,
            'quantity': quantity
           }
       )
       self.total += price*quantity
       return self.total


    def mean_item_price(self):
       itemTotals = [item['price']*item['quantity'] for item in self.items]
       itemQuantities = [item['quantity'] for item in self.items]
       meanPrice = sum(itemTotals)/sum(itemQuantities)
       return meanPrice 


    def median_item_price(self):
        priceList = []
        for item in self.items:
            for k in range(item['quantity']):
                priceList.append(item['price'])
        priceList = sorted(priceList)
        N = len(priceList)
        if N%2 == 0:
            medianPrice = (priceList[int(N/2)-1] + priceList[N/2])/2
        else:
            medianPrice = priceList[int((N-1)/2)]
        return medianPrice

    def apply_discount(self):
        if self.employee_discount != None:
            discountTotal = self.total*(100 - self.employee_discount)/100
            return discountTotal
        else:
            return "Sorry, there is no discount to apply to your account"

    def void_last_item(self):
        if self.items[-1]['quantity'] > 1:
            self.items[-1]['quantity'] -= 1
            self.total -= self.items[-1]['price']
        else:
            self.total -= self.items[-1]['price']
            self.items = self.items[:-1]

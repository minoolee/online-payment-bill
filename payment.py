# My first Project

# Menu
caffe_menu = {
    "Tee": 2.50,
    "Coffee": 4.50,
    "Ice Tea": 5,
    "Chocolate Cake": 5,
    "Red Velvet Cake": 6,
    "Black Forest Cake": 8,
    "Ice cream (caramel)": 4,
    "ChaiLatte": 7,
    "Kiwi": 9
}


def show_menu():
    print("Welcome to the cafe Minoo. Our Menu for today is")
    for x, y in caffe_menu.items():
        print(" - ", x, "-", y,  "$")


def take_order():
    order_items = []
    while True:
      item = input("Give your order please: ")
      if item not in caffe_menu:
        print("We're sorry! Your product isn't available.")
      else:
          order_items.append(item)
          finish = input("Do you want to order anything else? (yes/no):")
          if finish.lower() == "no":
            break
          elif finish.lower() == "yes":
              more_orders = input("Give your order please: ")
              order_items.append(more_orders)
    return order_items


def show_billing(order):

    for j, h in caffe_menu.items():
        for i in order:
            if j == i:
             print(i, h, "$")



def check(order):
    total_bill = 0
    for x, y in caffe_menu.items():
         for i in order:
             if x == i:
              total_bill += y
    return total_bill


show_menu()
order_items = take_order()
show_billing(order_items)
bill = check(order_items)
print("You bill is:",  bill, "$", "Thank you and have a nice day")

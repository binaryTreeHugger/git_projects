class CoffeeMachine:
    def __init__(self):
        self.water = 1000  # Initial water level in milliliters
        self.coffee_beans = 500  # Initial coffee beans level in grams

    def check_resources(self, required_water, required_coffee_beans):
        if self.water >= required_water and self.coffee_beans >= required_coffee_beans:
            return True
        else:
            return False

    def make_coffee(self, coffee_type):
        if coffee_type == "espresso":
            required_water = 50
            required_coffee_beans = 10
        elif coffee_type == "latte":
            required_water = 200
            required_coffee_beans = 20
        elif coffee_type == "cappuccino":
            required_water = 250
            required_coffee_beans = 30
        else:
            print("Invalid coffee type")
            return

        if self.check_resources(required_water, required_coffee_beans):
            print(f"Making {coffee_type}...")
            self.water -= required_water
            self.coffee_beans -= required_coffee_beans
            print(f"{coffee_type} is ready!")
        else:
            print(f"Sorry, not enough resources for {coffee_type}.")

    def refill_water(self, amount):
        self.water += amount
        print(f"Water refilled: +{amount} ml")

    def refill_coffee_beans(self, amount):
        self.coffee_beans += amount
        print(f"Coffee beans refilled: +{amount} grams")


# Create a CoffeeMachine object
coffee_machine = CoffeeMachine()

# Main program loop
while True:
    action = input("What would you like to do? (make/exit/refill): ").lower()

    if action == "make":
        coffee_type = input("What type of coffee would you like? (espresso/latte/cappuccino): ").lower()
        coffee_machine.make_coffee(coffee_type)
    elif action == "exit":
        break
    elif action == "refill":
        resource = input("What would you like to refill? (water/coffee beans): ").lower()
        if resource == "water":
            amount = int(input("How much water would you like to refill (in ml)? "))
            coffee_machine.refill_water(amount)
        elif resource == "coffee beans":
            amount = int(input("How many grams of coffee beans would you like to refill? "))
            coffee_machine.refill_coffee_beans(amount)
        else:
            print("Invalid resource.")
    else:
        print("Invalid action. Please choose 'make', 'refill', or 'exit'.")

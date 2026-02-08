### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###

class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry there is not enough {item}.")
                return False
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""
        print('Please insert coins.')

        large_dollar = int(input('How many large dollars?')) * 1.00
        half_dollar = int(input('How many half dollars?')) * .50
        quarters = int(input('How many quarters?')) * .25
        nickels = int(input('How many nickels?')) * .05

        total_coins = large_dollar + half_dollar + quarters + nickels

        return total_coins


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        if coins >= cost:
            change = round(coins - cost, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that's not enough money.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """Deduct the required ingredients from the resources.
           Hint: no output"""
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"Here is your {sandwich_size} sandwich. Enjoy!")

### Make an instance of SandwichMachine class and write the rest of the codes ###

machine = SandwichMachine(resources)

while True:
    size_choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

    if size_choice == "off":
        break

    if size_choice == "report":
        print(f"Bread: {machine.machine_resources['bread']} slice(s)")
        print(f"Ham: {machine.machine_resources['ham']} slice(s)")
        print(f"Cheese: {machine.machine_resources['cheese']} ounces")
        continue

    if size_choice in recipes:
        order = recipes[size_choice]
        ingredients = order["ingredients"]
        cost = order["cost"]

        if machine.check_resources(ingredients):
            coins = machine.process_coins()
            if machine.transaction_result(coins, cost):
                machine.make_sandwich(size_choice, ingredients)
    else:
        print("Invalid choice.")





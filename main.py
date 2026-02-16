import data
import sandwich_maker
import cashier

# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    ###  write the rest of the codes ###
    while True:
        size_choice = input("What would you like? (small/ medium/ large/ off/ report): ").lower()

        if size_choice == "off":
            break

        if size_choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} ounces")
            continue

        if size_choice in recipes:
            order = recipes[size_choice]
            ingredients = order["ingredients"]
            cost = order["cost"]

            if sandwich_maker_instance.check_resources(ingredients):
                coins = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins, cost):
                    sandwich_maker_instance.make_sandwich(size_choice, ingredients)
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()

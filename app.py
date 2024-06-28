import sys
import json

# from data.load_save import save, load

# garage = [{"name": "nissan","carnumber": "024531656","problems": "engine","price": 2000}]


def car_list(garage):
    print("entering list")
    for car in garage:
        print(
            f"""car name: {car["name"]} - car number:{car["carnumber"]} - car problem: {car["problems"]} - payment:{car["price"]}"""
        )


def car_add(garage):
    print("adding...")
    new_name = input("add the car name:")
    new_number = input("add the car number:")
    new_car = {"name": new_name, "carnumber": new_number}
    problem_list(garage)
    garage.append(new_car)
    print("added")


def car_delete(garage):
    print("deleting...")
    user = input("please name the car to remove:")
    for car in garage:
        if (
            user.lower() == car["name"].lower()
            or user.lower() == car["carnumber"].lower()
        ):
            garage.remove(car)
    print("deleted")


def search_car(garage):
    print("searching...")
    user = input("please name the car to seach:")
    for car in garage:
        if (
            user.lower() == car["name"].lower()
            or user.lower() == car["carnumber"].lower()
        ):
            print("found")
            print(f"""car name: {car["name"]} - car number:{car["carnumber"]}""")
        else:
            print("not found")


def save(garage):
    with open("garage.json", "w") as file:
        json.dump(garage, file)


def load():
    with open("garage.json", "r") as file:
        garage = json.load(file)
        return garage


def menu(garage):
    while True:
        print("Welcome to my garage")
        print("1 - list all cars")
        print("2 - Add a car")
        print("3 - Delete a car")
        print("4 - Search a car")
        print("0 - exit")
        selection = input("what would you like to do?")
        if selection == "1":
            car_list(garage)
        elif selection == "2":
            car_add(garage)
        elif selection == "3":
            car_delete(garage)
        elif selection == "4":
            search_car(garage)
        elif selection == "0":
            print("exiting...")
            save(garage)
            sys.exit()


def problem_list(garage):
    while True:
        print("here is a list of common problems:")
        print("1 - Engine - - 2000 ₪")
        print("2 - Brakes  - - 1000 ₪")
        print("3 - 5000 km treatment - 500 ₪")
        print("4 - 10,000 km treatment - 1000 ₪")
        print("5 - Filters + Oil - 250 ₪")
        print("6 - Gear - 1000 ₪")
        print("7 - confirm ?")
        selection = input("please select a problem:")
        problem = []
        price = []
        if selection == "1":
            problem.append("engine")
            price.append("2000")
            print(problem, price)
        elif selection == "2":
            problem.append("brakes")
            price.append("1000")
            print(problem, price)
        elif selection == "3":
            problem.append("5k treatment")
            price.append("500")
        elif selection == "4":
            problem.append("10k treatment")
            price.append("1000")
        elif selection == "5":
            problem.append("Filters + Oil ")
            price.append("250")
        elif selection == "6":
            problem.append("gear")
            price.append("1000")
        elif selection == "7":
            total_price = int(sum(price))
            result_price = total_price
            print(total_price)
            print(garage)
            # garage.append(result_price)
            for car in garage:
                print(car)
                print(str(car["problems"]))
                print(problem)
                car["problems"].append(problem)
                return


def main():
    garage = load()
    menu(garage)


if __name__ == "__main__":
    main()


# I tried to insert the error function and I didn't succeed (more precisely we didn't succeed) and without it quite a large part of the project didn't work...
# Without the function of problem_list() everything works

# ** Another note exit() didn't work for me even then I brought the external import sys

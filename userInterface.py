from DataStructures.Graph import Graph
from Models.Truck import routeMiles
from Utils.dataHandler import *
from Utils.truckLoader import truckLoader


def userInterface(running):
    print("------------------------------------")
    print("C950")
    print("WGUPS Project")
    print("Joshua Dorsett")
    print("------------------------------------\n")

    # make 3 hash tables of locations, distances and packages
    locations = makeHashTableOfLocations()
    distances = makeHashTableOfDistances()
    packages = makeHashTableOfPackages()

    # build a graph of locations
    saltLakeCity = Graph(locations, distances)

    # assign and load trucks
    trucks = truckLoader(packages)
    truck1 = trucks[0]
    truck2 = trucks[1]
    truck3 = trucks[2]

    # create routes and calculate cost of each route
    route1 = truck1.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles1 = routeMiles(route1, saltLakeCity)
    route2 = truck2.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles2 = routeMiles(route2, saltLakeCity)
    route3 = truck3.createRoute(saltLakeCity, locations.getValue(0), locations)
    routeMiles3 = routeMiles(route3, saltLakeCity)
    totalMiles = routeMiles1 + routeMiles2 + routeMiles3

    while running:

        inputStream = input("enter 'p' to print all package information for a certain time.\n"
                            "enter 'r' to lookup routes.\n"
                            "enter 'e' to end program.\n")

        if inputStream == 'r':
            inputStream = input("enter index of truck '0', '1', or '2'")
            if inputStream == '0':
                print("=========Route for truck one===========")
                for i in range(len(route1)):
                    print(route1[i][0].getTitle())
                print("\n")
                print(routeMiles1, "total miles in this route.\n")

            elif inputStream == '1':
                print("=========Route for truck two===========")
                for i in range(len(route2)):
                    print(route2[i][0].getTitle())
                print("\n")
                print(routeMiles2, "total miles in this route.\n")

            elif inputStream == '2':
                print("========Route for truck three============")
                for i in range(len(route3)):
                    print(route3[i][0].getTitle())
                print("\n")
                print(routeMiles3, "total miles in this route.\n")


            print("The total miles for all routes is", totalMiles)
            print("------------------------------------\n")

        elif inputStream == 'p':

            currentTime = input("enter a time to lookup in the format 'hh:mm'."
                                "\nplease use 24 hour time.\n")

            truck1.startRoute(currentTime)
            truck2.startRoute(currentTime)
            truck3.startRoute(currentTime)
            for truck in trucks:
                for p in truck.getPackages():
                    p.print()

        elif inputStream == 'e':
            running = False

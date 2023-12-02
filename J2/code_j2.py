# Program by Imanuel Fehse

# Bundeswettbewerb Informatik
# Round 1
# Exercise Junior 2


def check(pair):
    c1 = pair[0] # container 1

    for i in range(len(container_list)):
        # if container is lighter
        if c1 == container_list[i][1] or c1 in lighter:
            if c1 not in lighter:
                lighter.append(c1)

            if c1 in heaviest:
                heaviest.remove(c1)
                break
            pass
        # if container is heavier
        else:
            if not c1 in heaviest:
                heaviest.append(c1)


while True:
    filename = input("\nPlease enter filename: ")
    # try to open file
    try:
        f = open(filename, "r")
    except FileNotFoundError or OSError:
        print("No such file found")
        continue

    # read file
    containers = f.read().splitlines()
    container_list = []
    for container in containers:
        container_list.append(container.split())

    # list of containers which are lighter or heaviest
    heaviest = []
    lighter = []

    for pair in container_list:
        # check if heavier container ever was lighter
        check(pair)

    print("The heaviest containers are:", heaviest)

    if len(heaviest) == 1:
        print("The heaviest container is container", heaviest[0])
    else:
        print("Not clear which container is the heaviest")

# Program by Imanuel Fehse

# Bundeswettbewerb Informatik
# Round 1
# Exercise A5


# startpoints of players
stp1 = '1'
stp2 = '2'


def create_connections(data):
    global connections
    connections = {}

    for item in data:
        # if connection base is already in connections
        try:
            x = connections[item[0]]

            # add new connection of already existing point to connections
            connections[item[0]] = connections[item[0]] + [item[1]]

        # if not
        except KeyError:
            #  add new connection basepoint and first connection
            connections[item[0]] = [item[1]]


def find_solution():
    # solution lists
    solp1 = [stp1]
    solp2 = [stp2]

    x_list = [solp1]
    y_list = [solp2]

    # get possible ways for 100 steps
    for i in range(100):
        # get last positions
        x = x_list[-1]
        y = y_list[-1]

        # possible positions at current step
        dx = []
        dy = []

        # get following connections
        for item in x:
            # get for every possible last position every possible current positions and ad them to list
            for ix in [item]:
                try:
                    p = connections[ix]
                except KeyError:
                    continue
                for subx in connections[ix]:
                    dx.append(subx)

        for item in y:
            # get for every possible last position every possible current positions and ad them to list
            for iy in [item]:
                try:
                    p = connections[iy]
                except KeyError:
                    continue
                for suby in connections[iy]:
                    dy.append(suby)

        # save possible positions at current step
        x_list.append(dx)
        y_list.append(dy)

        # check if a solution has been found
        result = check_solution(dx, dy)
        if result[0]:
            # return solution
            return result[1], i+1
        # if there are to many possibilities
        elif len(dx) > 5000 or len(dy) > 5000:
            break
        else:
            pass


def check_solution(x_pos, y_pos):
    for x in x_pos:
        for y in y_pos:
            if x == y:
                return True, x
    return False, None


while True:
    filename = input("\nPlease enter filename: ")
    # try to open file
    try:
        f = open(filename, "r", encoding="utf8")
    except FileNotFoundError or OSError:
        print("No such file found")
        continue

    # get data
    data_raw = f.read().splitlines()

    # format data
    data = []
    for item in data_raw:
        data.append(item.split(" "))

    # create connection pattern from data
    create_connections(data)

    # get connection of two startpoints
    t = find_solution()
    if t is None:
        print("No solution found")
    else:
        print("Solution found after", t[1], "steps")
        print("Solution:", t[0])

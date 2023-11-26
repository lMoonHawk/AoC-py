def part1():
    class Compass:
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3

    # [East, North]
    coordinates = [0, 0]
    facing = Compass.EAST
    with open("2020/data/day_12.txt") as f:
        for line in f:
            line = line.strip()
            action, value = line[0], int(line[1:])

            move = [0, 0]
            if action == "N" or (action == "F" and facing == Compass.NORTH):
                move = [0, value]
            if action == "S" or (action == "F" and facing == Compass.SOUTH):
                move = [0, -value]
            if action == "E" or (action == "F" and facing == Compass.EAST):
                move = [value, 0]
            if action == "W" or (action == "F" and facing == Compass.WEST):
                move = [-value, 0]

            if action == "R":
                facing = (facing + value // 90) % 4
            if action == "L":
                facing = (facing - value // 90) % 4

            coordinates = [move_c + c for move_c, c, in zip(move, coordinates)]

    answer = sum(abs(c) for c in coordinates)
    print(answer)


def part2():
    # [East, North]
    ship = [0, 0]
    waypoint = [10, 1]

    with open("2020/data/day_12.txt") as f:
        for line in f:
            line = line.strip()
            action, value = line[0], int(line[1:])

            move_waypoint = [0, 0]
            move_ship = [0, 0]

            if action == "F":
                move_ship = [w * value for w in waypoint]
            elif action == "N":
                move_waypoint = 0, value
            elif action == "E":
                move_waypoint = value, 0
            elif action == "S":
                move_waypoint = 0, -value
            elif action == "W":
                move_waypoint = -value, 0

            else:  # ["R", "L"]
                if action == "L":
                    value = -value

                w_x, w_y = waypoint
                rotation = (value // 90) % 4
                if rotation == 1:
                    waypoint = w_y, -w_x
                elif rotation == 2:
                    waypoint = -w_x, -w_y
                elif rotation == 3:
                    waypoint = -w_y, w_x
                else:  # 0
                    waypoint = w_x, w_y

            waypoint = [sum(coord) for coord in zip(waypoint, move_waypoint)]
            ship = [sum(coord) for coord in zip(ship, move_ship)]

    answer = sum(abs(c) for c in ship)
    print(answer)


if __name__ == "__main__":
    part1()
    part2()

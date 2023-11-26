with open("2020/data/day_13.txt") as f:
    earliest, bus_ids = [line.strip() for line in f.readlines()]

earliest = int(earliest)
minutes = [m for m, bus_id in enumerate(bus_ids.split(",")) if bus_id != "x"]
bus_ids = [int(bus_id) for bus_id in bus_ids.split(",") if bus_id != "x"]


def part1():
    time = earliest - 1
    found_bus = False

    while not found_bus:
        time += 1
        for bus_id in bus_ids:
            # If there is a bus departing at that time
            if time % bus_id == 0:
                found_bus = True
                break

    print((time - earliest) * bus_id)


def part2():
    def ext_euclide(a: int, b: int) -> tuple[int, int]:
        """Extended euclide algorithm, returning u, v from the Bézout's identity a*u + b*v = gcd(a,b)"""
        if a == 0:
            return 0, 1
        x1, y1 = ext_euclide(b % a, a)
        x, y = y1 - (b // a) * x1, x1
        return x, y

    # If bus x must arrive at time t+k, then we have (t+k) ≡ 0 (mod x) <=> t ≡ x-k (mod x)
    # a: Congruences
    a = [bus_id - minute for bus_id, minute in zip(bus_ids, minutes)]
    # n: Modulus
    n = bus_ids
    # We have ∀ai in a, n_i in n; t ≡ a_i (mod n_i)

    n_tot = 1
    for i in bus_ids:
        n_tot *= i

    t = 0
    for a_i, n_i in zip(a, n):
        n_hat_i = n_tot // n_i
        # We use the Chinese Remainder Theorem.
        # Multiplying each congruence a_i with n_hat times v (v from the Bézout identity a*u + b*v = gcd(a,b))
        # Here, gcd(a,b) = 1. The creator of this puzzle is nice and has made it so a and b are always coprime.
        t += (a_i * n_hat_i * ext_euclide(n_i, n_hat_i)[1]) % n_tot
        # We apply the modulo n_tot since a solution t repeats every n_tot minutes. This makes large numbers more manageable

    print(t % n_tot)


if __name__ == "__main__":
    part1()
    part2()

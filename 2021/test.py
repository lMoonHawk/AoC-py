scanner0 = [
    (404, -588, -901),
    (528, -643, 409),
    (-838, 591, 734),
    (390, -675, -793),
    (-537, -823, -458),
    (-485, -357, 347),
    (-345, -311, 381),
    (-661, -816, -575),
    (-876, 649, 763),
    (-618, -824, -621),
    (553, 345, -567),
    (474, 580, 667),
    (-447, -329, 318),
    (-584, 868, -557),
    (544, -627, -890),
    (564, 392, -477),
    (455, 729, 728),
    (-892, 524, 684),
    (-689, 845, -530),
    (423, -701, 434),
    (7, -33, -71),
    (630, 319, -379),
    (443, 580, 662),
    (-789, 900, -551),
    (459, -707, 401),
]
scanner1 = [
    (686, 422, 578),
    (605, 423, 415),
    (515, 917, -361),
    (-336, 658, 858),
    (95, 138, 22),
    (-476, 619, 847),
    (-340, -569, -846),
    (567, -361, 727),
    (-460, 603, -452),
    (669, -402, 600),
    (729, 430, 532),
    (-500, -761, 534),
    (-322, 571, 750),
    (-466, -666, -811),
    (-429, -592, 574),
    (-355, 545, -477),
    (703, -491, -529),
    (-328, -685, 520),
    (413, 935, -424),
    (-391, 539, -444),
    (586, -435, 557),
    (-364, -763, -893),
    (807, -499, -711),
    (755, -354, -619),
    (553, 889, -390),
]


def create_vects(points):
    return {
        (x1, y1, z1): [(x2 - x1, y2 - y1, z2 - z1) for x2, y2, z2 in points]
        for x1, y1, z1 in points
    }


# def add(d, k, v):
#     if k in d:
#         d[k].add(v)
#     else:
#         d[k] = {v}


def rotate(vect, i):
    x, y, z = vect

    rot = [
        (x, y, z),
        (z, y, -x),
        (-x, y, -z),
        (-z, y, x),
        (-x, -y, z),
        (-z, -y, -x),
        (x, -y, -z),
        (z, -y, x),
        (x, -z, y),
        (y, -z, -x),
        (-x, -z, -y),
        (-y, -z, x),
        (x, z, -y),
        (-y, z, -x),
        (-x, z, y),
        (y, z, x),
        (z, x, y),
        (y, x, -z),
        (-z, x, -y),
        (-y, x, z),
        (-z, -x, y),
        (y, -x, z),
        (z, -x, -y),
        (-y, -x, -z),
    ]
    return rot[i]


def find_rotation(l_vect_ref, l_vect_other):
    overlap = {}

    for rot in range(24):
        for ref, vects_ref in l_vect_ref.items():
            count = 0
            for other, vects_other in l_vect_other.items():
                # print(other)
                # if other[0] == 686:
                #     raise ValueError
                for vect_other in vects_other:
                    if (
                        vect_other != (0, 0, 0)
                        and rotate(vect_other, rot) in vects_ref
                    ):
                        count += 1
                # print(count)
            if count >= 11:
                overlap[ref] = other
    return overlap


vects_scanner0 = create_vects(scanner0)
vects_scanner1 = create_vects(scanner1)

# print(vects_scanner0)
res = find_rotation(vects_scanner0, vects_scanner1)
print(res)

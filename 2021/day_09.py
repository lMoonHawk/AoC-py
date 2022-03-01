def part1():

    rolling_rows = []

    def shift(l_in, mode="lag"):
        """Lead or lag list, filling with a 9 where empty"""
        if mode == "lag":
            out = [9] + l_in[:-1]
        elif mode == "lead":
            out = l_in[1:] + [9]
        return out

    def vect_sub(a: list[int], b: list[int]):
        """Element-wise substraction"""
        return [a_i - b_i for a_i, b_i in zip(a, b)]

    def create_masks(l_in, l_top=[], l_bottom=[]):
        """Substract list from a "lag", 'lead" version of itself,
        and also top or bottom list where applicable"""
        masks = {}
        masks["left"] = vect_sub(l_in, shift(l_in, "lag"))
        masks["right"] = vect_sub(l_in, shift(l_in, "lead"))

        if l_bottom:
            masks["bottom"] = vect_sub(l_in, l_bottom)
        if l_top:
            masks["top"] = vect_sub(l_in, l_top)

        return masks

    def check_masks(l_in, masks):
        """Check if each masks are negative for each position
        -> Height is lower than each of its neighbors.\n
        Returns the score of the row"""
        sum_row = 0

        for i, height in enumerate(l_in):
            masks_values = [mask[i] for mask in masks.values()]
            if all(map(lambda x: x < 0, masks_values)):
                sum_row += 1 + height

        return sum_row

    run_sum = 0

    with open("2021/data/day_09.txt") as f:
        for i, row_char in enumerate(f):

            row_char = row_char.strip()
            new_row = [int(height) for height in row_char]
            # We only keep 3 rows in memory
            rolling_rows.append(new_row)

            if i == 0:
                continue  # Not enough info to compare (row below)

            elif i == 1:
                # Masks all give a comparison of height
                # First row: left, right and bottom
                masks = create_masks(
                    l_in=rolling_rows[0],
                    l_bottom=rolling_rows[1])
                to_check = rolling_rows[0]

            elif i > 1:
                # Row in the middle: left, right, bottom and top
                masks = create_masks(
                    l_in=rolling_rows[1],
                    l_bottom=rolling_rows[2],
                    l_top=rolling_rows[0])

                to_check = rolling_rows[1]
            # Iterate through the masks, all comparison at
            # a position must be negative for a height to
            # be considered lower than all its neighbors
            run_sum += check_masks(to_check, masks)

            if len(rolling_rows) > 3:
                rolling_rows.pop(0)

        # Last row: left, right and top
        masks = create_masks(
                    l_in=rolling_rows[2],
                    l_top=rolling_rows[1])

        run_sum += check_masks(rolling_rows[2], masks)

        print(run_sum)


def part2():
    pass


if __name__ == '__main__':
    part1()
    part2()

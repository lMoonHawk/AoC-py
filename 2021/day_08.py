def part1():

    outputs = []
    outputs_len = []
    with open("2021/data/day_08.txt") as f:
        for line in f:
            line_output = line.strip().split(" | ")[1]
            outputs.extend(line_output.split(" "))

        for output in outputs:
            outputs_len.append(len(output))

        uniques = [
            output_len
            for output_len in outputs_len
            # 1: 2, 4: 4, 7: 3, 8: 7
            if output_len in [2, 3, 4, 7]]

        print(len(uniques))


def part2():

    def get_common(signal: set[str], lookup: dict) -> str:
        """ Get number of segment intersection with each of the
            digits 1, 4, 7, 8 in str format"""
        common = ""
        for i in [1, 4, 7, 8]:
            inter = len(signal.intersection(lookup[i]))
            common += str(inter)
        return common

    with open("2021/data/day_08.txt") as f:
        total_value = 0

        for entry in f:

            signals, outputs = entry.strip().split(" | ")
            signals = signals.split(" ")
            outputs = outputs.split(" ")

            lookup = {8: set("abcdefg")}

            # Get easy digits first to create masks
            # 1 is 2 segments, 4 is 4 and 7 is 3
            lookup[1] = [
                set(signal) for signal in signals if len(signal) == 2][0]
            lookup[4] = [
                set(signal) for signal in signals if len(signal) == 4][0]
            lookup[7] = [
                set(signal) for signal in signals if len(signal) == 3][0]

            # Get remaining digits in the lookup dict
            for signal in signals:

                set_signal = set(signal)

                common = get_common(set_signal, lookup)

                # Each number has a unique representation of the
                # above function, we use this "mask" to find the digit
                match common:
                    case "2336":
                        lookup[0] = set_signal
                    case "1225":
                        lookup[2] = set_signal
                    case "2335":
                        lookup[3] = set_signal
                    case "1325":
                        lookup[5] = set_signal
                    case "1326":
                        lookup[6] = set_signal
                    case "2436":
                        lookup[9] = set_signal

            # Decode the outputs based on lookup dict
            entry_value = ""
            for output in outputs:
                for k, v in lookup.items():
                    if set(output) == v:
                        entry_value += str(k)

            total_value += int(entry_value)

        print(total_value)


if __name__ == '__main__':
    part1()
    part2()

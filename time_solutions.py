import os, sys, importlib
from time import perf_counter

years = [year for year in next(os.walk("."))[1] if year.isnumeric() and int(year) >= 2015]


def err_usage(message):
    print(f"Error: {message}")
    print("Usage:")
    print("> time_solutions.py [year]")
    print("> time_solutions.py [year_begin]-[year_end]")
    print("> time_solutions.py all")
    sys.exit()


if len(sys.argv) != 2:
    err_usage(f"expected 1 argument, got {len(sys.argv)-1}")


arg = sys.argv[1]
if arg.isnumeric() and arg in years:
    years = [arg]
elif "-" in arg and len(arg.split("-")) == 2:
    begin, end = arg.split("-")
    if begin in years and end in years:
        years = [year for year in years if int(year) >= int(begin) and int(year) <= int(end)]
    else:
        err_usage("the range must include existing years")
elif arg != "all":
    err_usage("incorrect usage")

for year in years:
    days = [day for day in next(os.walk(year))[2]]
    timer_year = perf_counter()
    for day in range(1, 26):
        print(f" {day:0>2}", end=" | ")
        if f"day_{day:0>2}.py" in days:
            script = importlib.import_module(f"{year}.day_{day:0>2}")
            part1, part2 = getattr(script, "part1"), getattr(script, "part2")
            timer_start = perf_counter()
            part1()
            timer_part1 = perf_counter()
            part2()
            timer_part2 = perf_counter()
            print(f"{timer_part1 - timer_start:.3f}s | {timer_part2 - timer_part1:.3f}s")
        else:
            print("/")
    print(f"Total for {year}: {perf_counter() - timer_year:.3f}s")

import math


def add_it_up(first: int, second: int):
    return first + second


def find_distance(point1, point2):
    if len(point1) != 2 or len(point2) !=2:
        raise ValueError
    delta_x = point1[0]-point2[0]
    delta_y = point1[1]-point2[1]
    result = math.sqrt(delta_x*delta_x+delta_y*delta_y)
    return result


def report_results(results: list[dict], file_to_print=None):
    for item in results:
        print(item, file=file_to_print)
    print("this is junk ", file=file_to_print)


def main():
    data = [{"name": "comp490", "cap": 20, "credits": 3},
            {"name": "comp151", "cap": 24, "credits": 4},
            {"name": "math161", "cap": 20, "credits": 5}]
    report_results(data)

if __name__ == '__main__':
    main()
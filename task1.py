def task(array: str) -> int:
    count = 0
    for numb in array:
        if numb == '0':
            return count
        count += 1
    return 'Весь массив состоит из единиц'


if __name__ == '__main__':
    print(task("111111111110000000000000000"))

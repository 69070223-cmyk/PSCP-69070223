"""shorten"""
first = int(input())

if first == -1:
    print()
else:
    start = first
    previous = start
    answer = []

    while True:
        try:
            current = int(input())
        except EOFError:
            break

        if current == -1:
            break

        if current != previous + 1:
            if start == previous:
                answer.append(str(start))
            else:
                answer.append(str(start) + "-" + str(previous))

            start = current

        previous = current

    if start == previous:
        answer.append(str(start))
    else:
        answer.append(str(start) + "-" + str(previous))

    print(", ".join(answer))

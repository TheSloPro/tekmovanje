# vrni vse možne načine razcepa številke

def razcep(i, n, out, index):
    if n == 0:
        print(out[:index])

    for j in range(i, n + 1):
        out[index] = j

        razcep(j, n - j, out, index + 1)


if __name__ == '__main__':
    n = input("Številko prosim: ")
    try:
        n = int(n)
    except ValueError:
        # rad imam rdeč text namesto navadnega
        exit("ŠTEVILKO!")
    out = [None] * n

    razcep(1, n, out, 0)

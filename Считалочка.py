def counting(n: int, k: int) ->int:

    players = [i for i in range(1, n + 1)]
    idx = 0

    while len(players) > 1:
        for _ in range(k):
            if idx == len(players):
                idx = 0
            idx += 1
        idx -= 1
        del players[idx]
    return players[0]

if __name__ == '__main__':

    print(counting(7, 3))
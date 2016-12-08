import math

from comments import critics


def euclidean_distance(prefs, person1, person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item] = 1

    if len(si) == 0:
        return 0

    sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2)
                          for item in prefs[person1] if item in prefs[person2]])

    return 1 / (1 + math.sqrt(sum_of_squares))


def pearson_correlation(prefs, p1, p2):
    si = {}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item] = 1

    n = len(si)
    if n == 0:
        return 1

    sum1 = sum([prefs[p1][it] for it in si])
    sum2 = sum([prefs[p2][it] for it in si])

    sq1 = sum([pow(prefs[p1][it], 2) for it in si])
    sq2 = sum([pow(prefs[p2][it], 2) for it in si])

    pSum = sum([prefs[p1][it] * prefs[p2][it] for it in si])

    num = pSum - (sum1 * sum2 / n)
    den = math.sqrt((sq1 - pow(sum1, 2)/ n) * (sq2 - pow(sum2, 2)/n))
    if den == 0:
        return 0

    r = num / den

    return r


def main():
    print euclidean_distance(critics, 'Lisa Rose', 'Gene Seymour')
    print pearson_correlation(critics, 'Lisa Rose', 'Gene Seymour')


if __name__ == '__main__':
    main()

# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    names = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        names.append(name)
        scores.append(score)
    compressed_scores = list(zip(scores,names))
    compressed_scores.sort()
    score_set = sorted(set(scores))
    second_lowest = score_set[1]
    for i in range(len(names)):
        score, name = compressed_scores[i]
        if score == second_lowest:
            print(name)
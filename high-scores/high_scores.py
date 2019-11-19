def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_scores = []
    ordered_list = sorted(scores, reverse=True)
    for i in ordered_list:
        if len(top_scores) >= 3:
            break
        else:
            top_scores.append(i)
    return top_scores
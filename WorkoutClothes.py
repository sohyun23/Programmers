def solution(n, lost, reserve):
    new_lost = list(set(lost)- set(reserve))
    new_reserve = list(set(reserve)- set(lost))

    answer = n- len(new_lost)

    for i in new_lost:
        if i-1 in new_reserve:
            new_reserve.remove(i-1)
            answer += 1

        elif i+1 in new_reserve:
            new_reserve.remove(i+1)
            answer += 1

    return answer
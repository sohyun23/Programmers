def solution(food):
    answer = ''
    food_list = []

    for idx, val in enumerate(food):
        alone_food = val // 2
        if idx != 0:
            food_list.append(str(idx) * alone_food)

    food_list_1 = "".join(food_list)
    food_list_2 = "".join(reversed(food_list))

    answer = food_list_1 + "0"+ food_list_2
    return answer
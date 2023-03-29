def solution(number):
    number_len = len(number)
    slicing_num = 3
    count = 0
    while number_len != 0 :
        first_num = number.pop()
        number_len = len(number)
        for idx in range(len(number)):
            sec_num = number[idx]

            for idx2 in range((idx+1) , len(number)):
                thd_num = number[idx2]
                
#                 if sec_num == thd_num:
#                     pass

#                 else:
                sum = first_num + sec_num + thd_num

                if sum == 0:
                    count += 1

    return count
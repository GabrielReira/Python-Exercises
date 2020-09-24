def list_sum(user_list):
    if len(user_list) == 1:
        return user_list[0]
    else:
        return user_list[0] + list_sum(user_list[1:])


numbers = str(input())
list_num = [ int(i) for i in numbers.split(' ') ]
print(list_sum(list_num))
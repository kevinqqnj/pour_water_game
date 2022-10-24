# when all ele are same in every bottle, it wins
import copy, random
import itertools

DEBUG = False

A = '1 2 3 1'.split(' ')
B = '4 5 3 4'.split(' ')
C = '6 6 3 2'.split(' ')
D = '4 5 5 1'.split(' ')
E = '1 4 3 6'.split(' ')

F = '7 7 6 7'.split(' ')
G = '2 5 2 7'.split(' ')
H = '0 0 0 0'.split(' ')
I = '0 0 0 0'.split(' ')
bottle_list = [list(map(lambda x:int(x), y)) for y in [A, B, C, D, E, F, G, H, I, ]]

# A = '1 2 3 1'.split(' ')
# B = '4 5 6 5'.split(' ')
# C = '3 2 6 6'.split(' ')
# D = '8 9 7 8'.split(' ')
# E = '3 3 5 7'.split(' ')
# F = '4 1 1 8'.split(' ')
#
# G = '10 9 10 6'.split(' ')
# H = '7 10 2 7'.split(' ')
# I = '10 2 5 8'.split(' ')
# J = '4 9 9 4'.split(' ')
# K = '0 0 0 0'.split(' ')
# L = '0 0 0 0'.split(' ')
# bottle_list = [list(map(lambda x:int(x), y)) for y in [A, B, C, D, E, F, G, H, I, J, K, L, L]]

# A = '1 2 3 4'.split(' ')
# B = '5 5 2 4'.split(' ')
# C = '6 7 4 8'.split(' ')
# D = '9 9 8 8'.split(' ')
# E = '5 3 6 2'.split(' ')
# F = '4 8 7 6'.split(' ')
#
# G = '9 6 3 1'.split(' ')
# H = '1 2 1 9'.split(' ')
# I = '5 7 3 7'.split(' ')
# J = '0 0 0 0'.split(' ')
# K = '0 0 0 0'.split(' ')
# bottle_list = [list(map(lambda x:int(x), y)) for y in [A, B, C, D, E, F, G, H, I, J, K]]

# A = [1,2,3,4]
# B = [5,5,2,4]
# C = [6,7,4,8]
# D = [9,9,8,8]
# E = [5,3,6,2]
# F = [4,8,7,6]
# G = [9,6,3,1]
# H = [1,2,1, 9]
# I = [5,7,3,7]
# J = [0, 0, 0, 0]
# K = [0, 0, 0, 0]
# bottle_list = [A, B, C, D, E, F, G, H, I, J, K]

# A = [1, 1, 3]
# B = [3, 3, 2]
# C = [0, 2, 2]
# D = [0, 0, 1]
# E = [0, 0, 0] # empty bottle
# bottle_list = [A, B, C, D, E]

def find_valid_same(c, bottle):
    if sum(bottle) == 0:
        return True
    for ind, i in enumerate(bottle): # TODO: 连续颜色
        if i==0: continue
        elif i!=0 and ind==0: return False
        if i==c and sum(bottle[:ind])==0: # 有相同颜色，且顶部有空位
            return True
        return False

def pour_water(move, bottle_list):
    global patten
    A, B = move
    A, B = bottle_list[A], bottle_list[B]
    if sum(A) != 0: patten.append(A)
    if sum(B) != 0: patten.append(B)
    for ind, j in enumerate(B):
        if j == 0:
            ind_B = ind
            continue
        # ind_B = ind
        # break
    is_first = True
    for ind, i in enumerate(A):
        if i == 0: continue
        if is_first:
            prev_c = i
            is_first = False
            cnt = 0
        else: cnt +=1
        if i == prev_c and ind_B-cnt>=0: # 连续颜色
            B[ind_B-cnt] = i
            A[ind] = 0
        else: break
    # for ind, i in enumerate(A):
    #     if i == 0: continue
    #     B[ind_B] = A[ind]
    #     A[ind] = 0 # TODO: 连续颜色
    #     break

def check_success(bottle_list):
    global back, patten, path
    for bottle in bottle_list:
        avg = sum(bottle)/len(bottle)
        for i in bottle:
            if i != avg:
                # back = copy.deepcopy(bottle_list)
                # # patten.append(back)
                # if (move_count > len(bottle_list)*2 ) and (back in patten):
                #     # print('Oops! no solution found!')
                #     # print(bottle_list)
                #     # patten = []
                #     it_break = True
                return False
    print(f"=========== Success! total {move_count=}")
    print(back)
    [print(k,v) for k, v in path.items()]
    # print(success_steps)
    exit(0)


def find_valid_step(bottle_list):
    global patten, swap, path, move_count
    valid_moves = {'from_to':[]}
    check_values = []
    for b_ind, bottle in enumerate(bottle_list):
        if len(set(bottle)) == 1: continue
        for ind, i in enumerate(bottle):
            if i == 0: continue
            same_piles = False
            # if i == sum(bottle) / (len(bottle) - ind):# and ind != len(bottle) - 1:
            if len(set(bottle))==2 and (0 in set(bottle)):
                # print('已有多个相同颜色的色块，不移动', i, ind, bottle)
                same_piles = True
            for next_ind in range(len(bottle_list) - 1):
                new_ind = b_ind + next_ind + 1 if b_ind + next_ind + 1 < len(bottle_list) else b_ind + next_ind + 1 - len(bottle_list)
                target_bottle = bottle_list[new_ind]
                if same_piles and sum(target_bottle)==0:
                    break # 相同颜色堆，不需要跟全0的交换
                if find_valid_same(i, target_bottle):
                    # pour_water(bottle, target_bottle)
                    if patten.count(bottle)>1 and patten.count(target_bottle)>1 and sum(bottle) !=0 and sum(target_bottle) !=0:
                        if DEBUG: print('循环了，break!', b_ind, new_ind, bottle_list)
                        # patten=[]
                        swap = False
                        break
                    # swap1 = (bottle_list[b_ind], bottle_list[new_ind])
                    # print(f'puring {steps:2}: {swap1=}')
                    # pour_water(bottle, target_bottle)
                    # swap2 = (bottle_list[b_ind], bottle_list[new_ind])
                    # swap = True
                    # patten.append(copy.deepcopy(bottle))
                    # patten.append(copy.deepcopy(target_bottle))
                    # print(f'puring {steps:2}: {swap2=}')
                    # log = f'puring {steps:2}: {[bottle_list[p] if (p in [b_ind, new_ind]) else empty for p in range(len(bottle_list))]}'
                    # success_steps.append(log)
                    if (bottle, target_bottle) not in check_values:
                        check_values.append((bottle, target_bottle))
                    else:
                        # print('value dup!',bottle, target_bottle)
                        continue
                    if DEBUG: print(move_count, 'found valid move:', b_ind, new_ind, bottle, target_bottle)
                    # if move_count>200: exit(1)
                    # if bottle_list not in valid_moves:
                    # valid_moves['bottle_list'] = copy.deepcopy(bottle_list)
                    valid_moves['from_to'].append((b_ind, new_ind))
                    # if check_success(bottle_list): return 0
                    # break  # 倒一次后，切换到同一瓶的下一颜色
            break  # 顶部第一个颜色检查后，下面的颜色可以跳过
    return valid_moves

def find_and_pour(bottle_list):
    global path, patten, swap, move_count
    # back = copy.deepcopy(bottle_list)
    check_success(bottle_list)
    valid_moves = find_valid_step(bottle_list)
    if len(valid_moves['from_to'])==0:
        # path.popitem()
        if DEBUG: print('no valid moves', bottle_list)
        return False

    path[move_count] = copy.deepcopy(bottle_list)
    # valid_moves: from_to=[(from_b, to_b)], bottle_list
    for ind, move in enumerate(valid_moves['from_to']):
        move_count +=1
        path[move_count] = copy.deepcopy(bottle_list)
        try:
            pour_water(move, path[move_count])
        except:
            print(move, path[move_count])
            raise
        if DEBUG: print(move_count, f"pour water {ind+1}/{len(valid_moves['from_to'])}:", move, path[move_count])
        check_success(path[move_count])
        # new_valid_moves = find_valid_step(current_list)
        # if len(new_valid_moves['from_to'])>0:
        find_and_pour(path[move_count])
    # all valid_moves checked
    print('dead end in this path, pop!', move_count, valid_moves['from_to'])
    try:
        patten.remove(path[move_count][move[0]])
        patten.remove(path[move_count][move[1]])
    except:
        # print(move_count, move, patten)
        pass
    path.popitem()
    move_count -=1

    return False
    # patten = []

def game(bottle_list):
    global path, it_break
    swap = False
    point_possibles = []
    path = {} # {1, (bottle_list, point_possibles)},
    find_and_pour(bottle_list)




steps = {}
move_count = 0
patten = []
success_steps = []

empty = f" {'. '*len(A)} "
it_break = False
cnt = 0
back = copy.deepcopy(bottle_list)
print(f'GAME start {bottle_list}')
game(bottle_list)
print('sorry, no solution!')
exit()

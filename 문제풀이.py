# def integer_input(msg,msg2):
#     n , m = input(msg) , input(msg2)
#     if n.isdigit() and m.isdigit():
#         return n,m
#     else:
#         print("숫자가 아닙니다.")
    

# test = integer_input('a : ','b : ')
# print(test)
# [2.5,3.1,1.7,2.8,2.4]

#1번

# class Fishs:
#     def __init__(self,data):
#         self.data = data
        
#     def average(self):
#         aver = sum(self.data) / len(self.data)
#         return print(f'물고기 평균무게:{aver:.2f} Kg')

# water_tank = Fishs([2.5,3.1,1.7,2.8,2.4])
# water_tank.average()

# 2번

# def get_first_letters(s):
#     split_data = s.split(' ')
#     return ''.join(map(lambda x:x[0],split_data))

# print(get_first_letters("Hello World! I Love Python"))
# print(get_first_letters("이스트소프트 오르미 1기 여러분 반가워요!"))   
# print(get_first_letters("복잡한 세상 편하게 살자")) 

# 3번
# def common_elements(list1,list2):
#     data = list1 + list2
#     dup = []
#     not_dup = []
    
#     for i in data:
#         if i in not_dup:
#             dup.append(i)
#         else:
#             not_dup.append(i)
            
#     return dup

# print(common_elements([1, 2, 3, 4, 5], [4, 5, 6, 7, 8]))
# print(common_elements(['est', 'weniv', 'ormi'], ['licat', 'ormi']))
# print(common_elements([1, 2, 3], [4, 5, 6])  )

# 4번

# def find_longest_word(list1):
#     first = list(list1[0])
#     second = []
#     final = []
#     for i in list1[1:]:
#         for j in i:
#             if j in first:
#                 if j in second:
#                     final.append(j)
#                 else:
#                     print(j)
#                     second.append(j)
#     return ''.join(final)

# def find_longest_word(list1):
#     first = list(list1[0])
#     second = []
#     final = []
#     for i in list1[1:]:
#         for j in i:
#             if j in first and j in second:
#                 final.append(j)
#             else:
#                 second.append(j)
#     return ''.join(final)

# print(find_longest_word(['이스트소프트', '이스트', '이스트소']) )
# print(find_longest_word(['behind', 'hind']) )
# print(find_longest_word(['오르미', '오르다', '오름']))

# 5번

# import bisect

# def length_of_lis(nums):
#     dp = [nums[0]]

#     for i in range(len(nums)):
#         if nums[i] > dp[-1]:
#             dp.append(nums[i])
#         else:
#             idx = bisect.bisect_left(dp, nums[i])
#             dp[idx] = nums[i]
#     return len(dp)



def length_of_lis(nums):
    dp = [1 for _ in range(len(nums))] # 1로 세팅
    
    for i in range(1, len(nums)):
        print('i 값 = ',i)
        for j in range(i): # array의 처음부터 i-1번째 인덱스까지
            print('j 값 = ',j)
            if nums[i] > nums[j]: # 숫자의 크기를 비교하여 현재 값이 더 크면
                
                # 101 > 10
                # 1/1 + 1
                
                # 101 > 9
                # 2/1 + 1
                
                # 101 > 2
                # 2 / 2 + 1
                
                # 101 > 5
                # 3 / 2 + 1
                
                # 101 > 5
                # 3 / 2 + 1
                
                dp[i] = max(dp[i], dp[j] + 1) # dp 배열의 값을 더 큰 값으로 갱신
                print(f'dp_i 값 : {dp[i]} , dp_j값 : {dp[j]}')
                print('dp 값 = ',dp)
        print('**********다음***********')
    return max(dp)

# nums1 = [1, 2, 3, 4, 5]
# print(length_of_lis(nums1))

# nums2 = [5, 4, 3, 2, 1]
# print(length_of_lis(nums2))

nums3 = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums3))

# nums4 = [4, 5, 2, 3, 1, 2]
# print(length_of_lis(nums4))


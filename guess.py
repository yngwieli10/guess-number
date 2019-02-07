import random
r = random.randint(1,100)
count = 0
while True:
    count += 1
    num = input('請輸入數字：　')
    num = int(num)
    if num == r:
        print('猜對了')
        print('這是你猜的第', count, '次')
        break
    elif num >r:
        print('您的數字比答案大')
    elif r >num:
        print('您的數字比答案小')
    print('這是你猜的第', count, '次')
        
        
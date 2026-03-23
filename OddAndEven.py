result = int(input('정수를 입력하세요:'))

if result >0 :
    print('양수입니다')
elif result <0 :
    print('음수입니다')
elif result ==0 :
    print('0입니다')

if result %2 ==0:
    print('짝수입니다')
elif result %2 ==1:
    print('홀수입니다')
    
result = int(input('정수를 입력하세요: '))

if result > 0:
    if result % 2 == 0:
        print('양수이며 짝수입니다!')
    else:
        print('양수이며 홀수입니다!')
elif result < 0:
    if result % 2 == 0:
        print('음수이며 짝수입니다!')
    else:
        print('음수이며 홀수입니다!')
else:
    print('0입니다!')

numbers = [273,103,5,32,65,9,72,800,99]
for number in numbers:
    if number > 100 :
        print('- 100이상의 수:',number)
        
for number in numbers:
    if number %2 == 0:
        print(f'{number}은 짝수입니다.')
    else:
        print(f'{number}은 홀수입니다.')
        
for answer in numbers:
    if 10<=answer<100 :
        print(f'{answer} 는 2 자릿수입니다.')
    elif answer>=100 :
        print(f'{answer} 는 3 자릿수입니다.')
    else :
        print(f'{answer} 는 1 자릿수입니다.')
        


numbers = [1, 415, 35, 156, 777773, 525, 626, 34, 1, 6]
for ak in numbers:
    meter = len(str(ak))
    if ak %2 ==0:
        print(f'{ak}은/는 짝수이며,{meter} 자릿수입니다,')
    else:
        print(f'{ak}은/는 홀수이며,{meter} 자릿수입니다,')

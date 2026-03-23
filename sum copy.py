want = input('정수를 입력해주세요 :')
want = int(want)

if want %2 == 0 :
    print('짝수입니다!')
else :
    print('홀수입니다!')

print(sum(range(1, 101)))

sample = int(input('1부터 어디까지 더할까요? 숫자를 입력하세요:'))
n = sample*(sample+1)//2
print(f'1부터 {sample}까지 더한 숫자는 {n}입니다!')
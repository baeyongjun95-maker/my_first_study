jk = int(input('정수를 입력해주세요:'))

if jk %2 == 0:
    if jk >0 :
        print('짝수이면서 양수입니다.')
    else :
        print('짝수이면서 음수입니다.')
if jk %2 == 1:
    if jk >0 :
        print('홀수이면서 양수입니다.')
    else :
        print('홀수이면서 음수입니다.')
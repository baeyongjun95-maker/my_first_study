numbers = [1, 415, 35, 156, 777773, 525, 626, 34, 1, 6]
for ak in numbers:
    meter = len(str(ak))
    if ak %2 ==0:
        print(f'{ak}은/는 짝수이며,{meter} 자릿수입니다,')
    else:
        print(f'{ak}은/는 홀수이며,{meter} 자릿수입니다,')
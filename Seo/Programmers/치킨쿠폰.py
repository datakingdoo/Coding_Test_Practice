def solution(chicken):
    a = [chicken // 10, chicken % 10] # [서비스 쿠폰, 남은 쿠폰]
    total = a[0]

    while 1:
        a = [(a[0] + a[1]) // 10, (a[0] + a[1]) % 10]
        total = total + a[0]
        if a[0] + a[1] < 10:
            break
    return total

print(solution(1081))

# 1081개 -> 쿠폰 1081장 -> 1081//10=108마리 서비스 , 쿠폰 1장남음 => (서비스로 받은 쿠폰 108장 + 나머지 1장)//10 = 10마리, 쿠폰 9장남음
# => (서비스 쿠폰 10장 + 나머지 9장)//10 = 1마리 , 쿠폰 9장 남음 => 1+9=10 1마리 => 서비스로 받은 쿠폰 1장.
# 108+10+1+1=120

# 남은쿠폰 =  (전단계 남은쿠폰 + 전단계 서비스쿠폰) % 10

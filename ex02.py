numbers = input("숫자 5개를 , 로 구분하여 입력하세요 : ")
list = list(numbers.split(","))
count = len(list)
sum = 0
print(len(list))
for x in list:
    sum += int(x)
avg = sum/count
print("갯수",count)
print("합계",sum)
print("평균",avg)
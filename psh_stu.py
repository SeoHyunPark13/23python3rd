# 다섯명의 성적을 입력 받아 평균을 내는 프로그램을 만든다.
# 반복문과 조건문을 사용한다.
# 변수는 total, counter, grade, average
total = 0           # 변수 total은 0으로 선언하였다.
counter = 1             # 변수 counter은 1로 선언하였다.
while counter <= 10 :       # 반복문 while을 사용하여 counter가 10보다 작거나 같을 때 다음 내부 문장으로 넘어간다.
    grade = int(input("성적을 입력하시오."))
    total = grade + total   # 변수 grade에 int(정수형 변환)와 사용자로부터 입력을 받는 input을 사용하여 정수를 받는다.
                # 변수 total에 성적 grade와 total을 합한 값을 선언한다.
    counter = counter + 1           # 변수 counter은 초기 선언한 counter의 값에 실행할 때마다 1씩 추가된다.
average = total // 10            # 변수 average에 반복문에서 계산한 total 값을 10으로 나눈다.
print(average) # 평균값을 출력.
# write by 박서현

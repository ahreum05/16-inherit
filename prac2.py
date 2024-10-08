from customer import Customer

customer = Customer()

while True:
    print('1. 입력')
    print('2. 출력')
    print('3. 수정')
    print('4. 이름검색')
    print('5. 종료')
    print('-------------')
    num = int(input('번호: '))
    print()
    
    if num == 1 : customer.input()
    elif num == 2 : customer.output() 
    elif num == 3 : customer.update()
    elif num == 4 : customer.searchName()
    elif num == 5 : 
        print('종료합니다.')
        break
    print()
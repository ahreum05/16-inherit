from customerVO import CustomerVO

class Customer :
    def __init__(self):
        self.customers = []

    #입력
    def input(self) :
        num = input('고객번호 : ')
        name = input('이    름 : ')
        tel = input('전화번호 : ')
        
        for customer in self.customers:
            if customer.num == num:
                print(num + " 고객번호가 존재합니다.")
                print("다른 번호를 선택해 주세요")
                return   # 함수 강제 종료
        
        vo = CustomerVO(num, name, tel)
        self.customers.append(vo)
    
    #출력
    def output(self) :
        print("{:5}\t{:5}\t{:10}".format('고객번호', '이름', '전화번호'))
        for customer in self.customers:
            print(customer)   # customer.__str__()
            
    #수정
    def update(self) :
        name = input('수정할 이름? ')
        print()
        for customer in self.customers:
            if customer.name == name:
                print("{:5}\t{:5}\t{:10}".format('고객번호', '이름', '전화번호'))
                print(customer)
                print()
                
                customer.num = input("고객번호: ")
                customer.name = input("이    름: ")
                customer.tel = input("전화번호: ")
                break
    
    #검색
    def searchName(self) :
        is_exist = False    # 존재하는지 저장, True : 존재, False : 없음
        name = input('검색할 이름? ')
        print()
        for customer in self.customers:
            if customer.name == name:
                print("{:5}\t{:5}\t{:10}".format('고객번호', '이름', '전화번호'))
                print(customer)
                is_exist = True
              
        if not is_exist : print(name + " 님이 존재하지 않습니다.")
                
                
                
    
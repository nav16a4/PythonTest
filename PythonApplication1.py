coffee = {"일반커피": 350,"고급커피":600 }
coin = 100
select = input("메뉴를 선택해주세요")
insert = coffee[select]

sum=0
while True:
    money= int(input("%d원 넣어주세요 "%(insert-sum)))
    print("%d원 동전 넣음"%money)
    sum=sum+money
    if(insert<=sum):
        break
print("메뉴가 나옵니다.")
print("거스름돈 %d원"%(sum-insert))
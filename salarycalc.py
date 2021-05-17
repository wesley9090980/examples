def main():
        achievement=input('请输入您的业绩：')
        achievement=int(achievement)
        salary=2000
        year_end_bonus=0
        if 0<achievement<=20000:
            salary+=achievement*0.12
            year_end_bonus=achievement*0.02
            print("月工资为{}，对应年终奖为{}".format(salary,year_end_bonus))
        elif 20001<=achievement<=50000:
            salary+=(2400+(achievement-20000)*0.18)
            year_end_bonus=400+(achievement-20000)*0.04
            print("月工资为{}，对应年终奖为{}".format(salary,year_end_bonus))
        elif 50001<=achievement<=80000:    
            salary+=2400+5400+(achievement-50000)*0.25
            year_end_bonus=400+1200+(achievement-50000)*0.05
            print("月工资为{}，对应年终奖为{}".format(salary,year_end_bonus))
        elif 80001<=achievement<=150000:
            salary+=2400+5400+7500+(achievement-80000)*0.3
            year_end_bonus=400+1200+1500+(achievement-80000)*0.06
            print("月工资为{}，对应年终奖为{}".format(salary,year_end_bonus))
        elif achievement>=150001:
            salary+=2400+5400+7500+21000+(achievement-150000)*0.45
            year_end_bonus=400+1200+1500+4200+(achievement-150000)*0.08
            print("月工资为{}，对应年终奖为{}".format(salary,year_end_bonus))
        else:
            print("输入错误！！")

while True:
    try:
        main()
    except:
        print("请重新输入！")
        continue
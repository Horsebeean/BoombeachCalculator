GoldData = 3000001
OFSUB_VALUE = 0 #假设不溢出
# globals.csv 的 数值
# 可以参考 LogicGlobals::createReferences
CONST_155 = 2   #620 是 RESOURCE_BUYING_COST_DIVSOR_1
CONST_624 = 150 #624 是 RESOURCE_BUYING_COST_DIVSOR_2
CONST_636 = 50  #636 是 RESOURCE_BUYING_COIN_MULTIPLIER
CONST_157 = 4   #628 是 BIG_RESOURCE_BUYING_COST_DIVSOR_1
CONST_632 = 30  #632 是 BIG_RESOURCE_BUYING_COST_DIVSOR_2

# bundleTest(101000,25200,8200) 预期结果：246 （已实现！！！！）
# getResourceDiamondCost(3000001,360000,360000,114514) 预期结果：185（已实现！！！！）

def sqrt(base):return int(base**(1/2))


def bundleTest(gold,wood,stone,iron):
    result = 0
    if gold>0:
        result += getResourceDiamondCost(3000001,gold,gold,114514)  
    if wood>0:
        result += getResourceDiamondCost(3000002,wood,wood,114514)    
    if stone>0:
        result += getResourceDiamondCost(3000003,stone,stone,114514)
    if iron>0:
        result += getResourceDiamondCost(3000004,iron,iron,114514)
    return result

def getResourceDiamondCost(LGPUPtr,a2:int,a3:int,a4:int):
    # a2和a3要设为同一个值，为资源数量
    #
    
    AttackCostMaybe = a3
    result = 9999999
    v7 = a2

    if( a2 <= 100000000 and (a3 - 1) <= 99999999 ):
        v10 = CONST_155
        if v7 < 0:
            v7 = 0
        if AttackCostMaybe < 100001:
            v16 = CONST_624
            v15 = 1
        else:
            v10 = CONST_157
            v16 = CONST_632
            v15 = 35
        v17 = sqrt(AttackCostMaybe) // v10
        v18 = v17
        v21 = OFSUB_VALUE
        v19 = v17 == 1024;
        v20 = v17 - 1024 < 0
        v22 = v18 * v18
        if (v20^v21)|v19:
            v23 = v22 * v18 // v16
        else:
            v23 = v22 // v16 * v18
        v24 = sqrt(v23)
        v25 = v24 + v15
        v26 = GoldData
        if GoldData == LGPUPtr:
            v28 = (1374389535 * CONST_636 * v25) >> 32
            v25 = (v28 >> 5) + (v28 >> 31)
        if AttackCostMaybe > 1000000:
            v7 = v7//200
            AttackCostMaybe //= 200
        v29 = (1374389535 * 200 * v7 // AttackCostMaybe * v25) >> 32
        result = max(1, (v29 >> 6) + (v29 >> 31))

    return result

if __name__=="__main__":
    print("== Resource Calculator ==")
    print("Press [Ctrl] + [C] to quit.")
    while(1):
        diamond_count = bundleTest( int(input("Gold:  ")), int(input("Wood:  ")), int(input("Stone: ")), int(input("Iron:  ")) )
        print(f"Diamonds: {diamond_count}")

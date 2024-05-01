CONST_616 = 16 # 616 是 SPEED_UP_COST_DIVISOR

# 不建议将升级/建造时间调至12天以上。

def sqrt(base): return int(base**(1/2))

def getSpeedUpCost(LGPtr:int,a2:int): # 其实LGPtr参数不被使用。
    "CONST_616 不能为0"
    v2 = sqrt(50*(a2//60))
    v3 = sqrt(v2*v2*v2)
    v5 = v3 // CONST_616
    #v5 = v3 // 16
    return max(1,v5)

def getSpeedUpCostWithMultiplier(LGPUPtr:int,A2:int,A3:int): # LGPUPtr = 100 A2总时间 A3剩余时间
    if(LGPUPtr==0):
        return 0
    GlobalPtr = 1 # = 1
    v8 = getSpeedUpCost(GlobalPtr,A2) * A3 // 100
    v9 = v8 * LGPUPtr
    if v8 * LGPUPtr <= 0:
        return 100 * (LGPUPtr // 100 * v8 // A2) # 此时可返回0，但是实际上至少为1钻石，所以之后需要额外处理
    v11 = v9 % A2
    result = v9 // A2
    if(v11!=0):
        result += 1
    return result

def getSpeedUpCostWithMultiplierOptimized(total_time,remaining_time):
    "确保剩余1~3时秒时间不会0钻石。（不考虑剩余0秒时秒时间的情况。）"
    return max(1,getSpeedUpCostWithMultiplier(100,total_time,remaining_time))

if __name__=="__main__":
    print("== Time Calculator ==")
    print("Press [Ctrl] + [C] to quit.")
    while(1):
        print(getSpeedUpCostWithMultiplier(100,int(input("Total Time(Sec)：")),int(input("Remaining Time(Sec)："))))

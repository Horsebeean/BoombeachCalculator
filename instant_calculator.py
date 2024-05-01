import time_calculator
import resource_calculator

# calculator instant upgrade

def instantDiamonds(sec,gold,wood,stone,iron):
    result = 0
    try:
        result += time_calculator.getSpeedUpCostWithMultiplierOptimized(sec,sec)
    except ZeroDivisionError:
        print("ZeroDivisionError occurs when calculating diamonds for TIME！")
        pass
    result += resource_calculator.bundleTest(gold,wood,stone,iron)
    return result


if __name__=="__main__":
    print("== Instant Upgrade Calculator ==")
    print("Press [Ctrl] + [C] to quit.")
    while(1):
        diamond_count = instantDiamonds( int(input("Time:  ")), int(input("Gold:  ")), int(input("Wood:  ")), int(input("Stone: ")), int(input("Iron:  ")) )
        print(f"Diamonds: {diamond_count}")

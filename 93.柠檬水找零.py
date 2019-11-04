def lemonadeChange(bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        wallet = {5: 0, 10: 0, 20: 0}           # 钱包
        for bill in bills: 
            if bill == 5:                       # 如果收到5元钞票
                wallet[5] += 1
            elif bill == 10:                    # 收到10元钞票
                if wallet[5] > 0:
                    wallet[5] -= 1
                    wallet[10] += 1
                else:
                    return False
            else:                               # 收到20元钞票
                if wallet[10] > 0 and wallet[5] > 0:
                    wallet[10] -= 1
                    wallet[5] -= 1
                    wallet[20] += 1
                elif wallet[5] > 2:
                    wallet[5] -= 3
                    wallet[20] += 1
                else:
                    return False
        return True
                    
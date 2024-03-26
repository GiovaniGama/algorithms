
from typing import List


def isPrefix(strs: List[str]) -> str:
    if not strs:
        return ""
    
    ans = ''
    orderList = sorted(strs)
    first = orderList[0]
    last = orderList[-1]

    for i in range(min(len(first), len(last))):
        if(first[i] != last[i]):
            return ans
        ans += first[i]
    return ans

print(isPrefix(['apple', 'app', 'aplicativo']))
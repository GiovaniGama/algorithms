def romanToInt(s: str) -> int:
    romanNumbers = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    i = 0

    while i < len(s):
        if i < len(s) and romanNumbers[s[i]] < romanNumbers[s[i+1]]:
            total += romanNumbers[s[i + 1]] - romanNumbers[s[i]]
            i += 2
        else:
            total += romanNumbers[s[i]]
            i += 1
    return total

print(romanToInt('MCMXCIV'))
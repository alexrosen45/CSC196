def permutations(n: int) -> list[list[int]]:
    permutations = []
    for i in range(0,2**n):
        permutations.append(list(bin(i)[2:].zfill(n)))
    return permutations

def significand_value(n: int, permutation: list[int]) -> float:
    significand_value = 1
    for i in range(n):
        significand_value += float(permutation[i])*2**(-i-1)
    return significand_value

def check_exponent_value(max: int, min: int, t: int, permutations: list[int]):
    import math
    for permutation in permutations:
        if math.log(t/permutation, 2) in range(min, max):
            return (math.log(target/permutation, 2), permutation)
    return False

if __name__ == '__main__':
    significand_digits = 3
    p = permutations(significand_digits)
    significand_permutations = [
        significand_value(
            significand_digits,
            permutation
        )
        for permutation in p
    ]

    target = 15
    exponent_max_value = 8 # 15 (1111 from binary to decimal) minus 2^(4-1)-1=7
    exponent_min_value = -7 # 0 (0000 from binary to decimal) minus 2^(4-1)-1=7

    # check if 17 divided by each permutation yields any integer power of 2
    exponent_value = check_exponent_value(
        exponent_max_value,
        exponent_min_value,
        target,
        significand_permutations
    )

    if exponent_value == False:
        print("no solutions")
    else:
        if int(exponent_value[1]) in range(exponent_min_value, exponent_max_value+1):
            print("Yes, using the exponent value 2^"+str(exponent_value[0])
            +" and the significand value "+str(exponent_value[1]))
        else:
            print("no solutions: requires more exponent bits")
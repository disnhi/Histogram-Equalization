
def equalize(num):
    cdf = []
    for i in range(len(num)):
        cdf.append(num[0])
        cdf[i]= cdf[i-1] + num[i]

    return cdf


def main():
    nums = [1,2,3,4,5]
    print(equalize(num))

main()

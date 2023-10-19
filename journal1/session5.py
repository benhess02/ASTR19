import math

def main():
    for i in range(1000):
        x = i * (2 * math.pi) / 1000
        print("sin(%s) = %s" % (x, math.sin(x)))

if __name__ == "__main__":
    main()
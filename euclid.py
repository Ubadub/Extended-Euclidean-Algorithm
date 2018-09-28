def euclid(a, b):
    """
    Returns a triple (g, x, y) such that gcd(a, b) = g = ax + by
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = euclid(b % a, a)
        return (g, y - (b // a) * x, x)

def main():
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print(euclid(x, y))

if __name__ == '__main__':
    main()
a = 2500
b = 1500

### Keane Pereira, 7
### GCD using Euclid's Algorithm

def GCD(a, b):
    if b == 0:
        return a

    return GCD(b, a % b)

print(GCD(a, b))

A, B, C = map(float, input().split())

if abs(B - C) < A < (B + C) and abs(A - C) < B < (A + C) and abs(A - B) < C < (A + B):
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = ((A + B) * C) / 2
    print(f"Area = {area:.1f}") 
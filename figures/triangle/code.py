a, b, c = 7, 2, 8


def triangle_perimeter(m=a, n=b, k=c):
    """Периметр треугольника"""
    return m + n + k


def triangle_area(m=a, n=b, k=c):
    """Площадь треугольника"""
    p = triangle_perimeter(m, n, k) / 2
    return (p * (p - m) * (p - n) * (p - k)) ** 0.5

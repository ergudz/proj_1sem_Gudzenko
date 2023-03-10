default_radius = 5


def circle_perimeter(radius: int = default_radius):
    """Периметр окружности"""
    return 2 * 3.14 * radius


def circle_area(radius: int = default_radius):
    """Площадь окружности"""
    return 3.14 * (radius ** 2)

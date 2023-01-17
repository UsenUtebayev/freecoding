# link to kata: https://www.codewars.com/kata/56606694ec01347ce800001b/train/python
def is_triangle(a, b, c):
    if a + b <= c:
        return False
    elif c + a <= b:
        return False
    elif c + b <= a:
        return False
    return True

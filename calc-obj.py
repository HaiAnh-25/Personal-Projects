class Calculator(object):
  def __init__(self, n):
    self.n = n
  def __add__(self, other):
    return self.n + other.n
  def __sub__(self, other):
    return self.n - other.n
  def __mul__(self, other):
    return self.n * other.n
  def __truediv__(self, other):
    return self.n / other.n
  
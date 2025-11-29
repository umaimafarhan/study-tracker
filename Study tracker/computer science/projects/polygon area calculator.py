def set_height(self, height):
 self.set_side(height)

def __str__(self):
 return f"Square(side={self.width})"


# Usage example
if __name__ == "__main__":
 rect = Rectangle(10, 5)
 print(rect.get_area()) # 50
 rect.set_height(3)
 print(rect.get_perimeter()) # 26
 print(rect)
 print(rect.get_picture())

sq = Square(9)
print(sq.get_area()) # 81
sq.set_side(4)
print(sq.get_diagonal()) # 5.656854249492381
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq)) # 8

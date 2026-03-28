# Bài 5: Giải phương trình bậc 2
import math

# Nhập các hệ số a, b, c từ bàn phím
print("Nhập hệ số a:")
a = float(input())

print("Nhập hệ số b:")
b = float(input())

print("Nhập hệ số c:")
c = float(input())

# Kiểm tra trường hợp đặc biệt a = 0
if a == 0:
    # Nếu a = 0, phương trình trở thành phương trình bậc nhất: b*x + c = 0
    if b == 0:
        # Nếu cả a và b đều bằng 0
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        # Nếu a = 0 và b khác 0, có một nghiệm duy nhất
        x = -c / b
        print(f"Phương trình có một nghiệm duy nhất: x = {x}")
else:
    # Tính biệt thức delta = b^2 - 4ac
    delta = b**2 - 4*a*c

    # Kiểm tra các trường hợp của delta
    if delta > 0:
        # Nếu delta > 0, phương trình có hai nghiệm phân biệt
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print(f"Phương trình có hai nghiệm phân biệt:")
        print(f"x1 = {x1}")
        print(f"x2 = {x2}")
    elif delta == 0:
        # Nếu delta = 0, phương trình có nghiệm kép
        x = -b / (2*a)
        print(f"Phương trình có nghiệm kép: x = {x}")
    else:
        # Nếu delta < 0, phương trình vô nghiệm thực
        print("Phương trình vô nghiệm thực.")
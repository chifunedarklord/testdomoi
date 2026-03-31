# Bài 3: Tìm số chia hết cho 2 và 3 trong khoảng 80-100

# Yêu cầu: In ra các số trong khoảng từ 80 đến 100 (bao gồm cả 80 và 100)
# thỏa mãn đồng thời hai điều kiện:
# 1. Chia hết cho 2
# 2. Chia hết cho 3

# Chúng ta sẽ sử dụng vòng lặp for để duyệt qua từng số trong khoảng đã cho.
# Điều kiện để một số chia hết cho cả 2 và 3 chính là nó chia hết cho bội chung nhỏ nhất của 2 và 3.
# Bội chung nhỏ nhất của 2 và 3 là 6.
# Do đó, chúng ta chỉ cần kiểm tra xem số đó có chia hết cho 6 hay không.

# Vòng lặp for sẽ bắt đầu từ 80 và kết thúc ở 100 (bao gồm 100).
# Hàm range(start, stop) sẽ tạo ra một dãy số từ start đến stop-1.
# Để bao gồm cả 100, ta cần dùng range(80, 101).
for so in range(80, 101):
    # Kiểm tra xem số hiện tại có chia hết cho 6 hay không.
    # Toán tử % (modulo) trả về số dư của phép chia.
    # Nếu số % 6 == 0, nghĩa là số đó chia hết cho 6.
    if so % 6 == 0:
        # Nếu điều kiện được thỏa mãn, in số đó ra màn hình.
        print(so)

# Không có trường hợp đặc biệt cần xử lý cho bài toán này vì khoảng xác định rõ ràng (80-100)
# và điều kiện cũng rõ ràng.
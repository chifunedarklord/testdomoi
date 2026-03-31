# Bài 12: Viết phương trình cộng đơn giản
# Nhập hai số từ người dùng
# Chuyển đổi chuỗi nhập vào thành số nguyên
# Kiểm tra xem việc chuyển đổi có thành công không
try:
    so1 = int(input("Nhập số thứ nhất: "))
    so2 = int(input("Nhập số thứ hai: "))
    # Thực hiện phép cộng
    ket_qua = so1 + so2
    # In kết quả ra màn hình
    print(f"Kết quả của {so1} + {so2} là: {ket_qua}")
except ValueError:
    # Xử lý trường hợp người dùng nhập không phải là số
    print("Lỗi: Bạn đã nhập không phải là số nguyên. Vui lòng nhập lại.")
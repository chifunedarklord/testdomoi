# Bài 10: Giải mã phương trình chữ

# Yêu cầu:
# Tìm các chữ số tương ứng với các chữ 'a', 'b', 'c', 'q', 'x' sao cho phương trình "abc + qax = 123" là đúng.
# Mỗi chữ cái tương ứng với một chữ số từ 0 đến 9.
# Các chữ cái khác nhau phải tương ứng với các chữ số khác nhau.
# 'a' và 'q' không thể bằng 0 vì chúng đứng đầu của các số có 3 chữ số.

# Duyệt qua tất cả các khả năng cho các chữ số từ 0-9 cho từng chữ cái.
# Cách tiếp cận là thử mọi kết hợp có thể và kiểm tra xem phương trình có đúng không.
# Số lượng chữ cái cần xác định là 5: a, b, c, q, x.

# Khai báo biến để lưu trữ các chữ số tương ứng
a, b, c, q, x = -1, -1, -1, -1, -1

# Lặp qua tất cả các số có thể có cho 'a' (từ 1 đến 9, vì 'a' không thể là 0)
for val_a in range(1, 10):
    # Lặp qua tất cả các số có thể có cho 'b' (từ 0 đến 9)
    for val_b in range(10):
        # Kiểm tra xem 'b' đã được gán giá trị khác 'a' chưa
        if val_b != val_a:
            # Lặp qua tất cả các số có thể có cho 'c' (từ 0 đến 9)
            for val_c in range(10):
                # Kiểm tra xem 'c' đã được gán giá trị khác 'a' và 'b' chưa
                if val_c != val_a and val_c != val_b:
                    # Lặp qua tất cả các số có thể có cho 'q' (từ 1 đến 9, vì 'q' không thể là 0)
                    for val_q in range(1, 10):
                        # Kiểm tra xem 'q' đã được gán giá trị khác 'a', 'b', 'c' chưa
                        if val_q != val_a and val_q != val_b and val_q != val_c:
                            # Lặp qua tất cả các số có thể có cho 'x' (từ 0 đến 9)
                            for val_x in range(10):
                                # Kiểm tra xem 'x' đã được gán giá trị khác 'a', 'b', 'c', 'q' chưa
                                if val_x != val_a and val_x != val_b and val_x != val_c and val_x != val_q:
                                    # Tạo các số từ các chữ số đã chọn
                                    num_abc = val_a * 100 + val_b * 10 + val_c
                                    num_qax = val_q * 100 + val_a * 10 + val_x

                                    # Kiểm tra xem tổng có bằng 123 không
                                    if num_abc + num_qax == 123:
                                        # Gán giá trị cho các biến nếu tìm thấy lời giải
                                        a = val_a
                                        b = val_b
                                        c = val_c
                                        q = val_q
                                        x = val_x
                                        # Dừng các vòng lặp vì chúng ta đã tìm thấy lời giải
                                        break
                            # Nếu đã tìm thấy lời giải, thoát khỏi vòng lặp 'x'
                            if a != -1:
                                break
                        # Nếu đã tìm thấy lời giải, thoát khỏi vòng lặp 'q'
                        if a != -1:
                            break
                    # Nếu đã tìm thấy lời giải, thoát khỏi vòng lặp 'c'
                    if a != -1:
                        break
                # Nếu đã tìm thấy lời giải, thoát khỏi vòng lặp 'b'
                if a != -1:
                    break
            # Nếu đã tìm thấy lời giải, thoát khỏi vòng lặp 'a'
            if a != -1:
                break

# In kết quả nếu tìm thấy lời giải
if a != -1:
    print(f"Lời giải tìm được:")
    print(f"a = {a}, b = {b}, c = {c}, q = {q}, x = {x}")
    print(f"Kiểm tra: {a}{b}{c} + {q}{a}{x} = {a*100+b*10+c} + {q*100+a*10+x} = {a*100+b*10+c + q*100+a*10+x}")
else:
    print("Không tìm thấy lời giải nào.")
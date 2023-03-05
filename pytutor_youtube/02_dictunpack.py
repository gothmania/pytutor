"""
PYTUTOR - YOUTUBE
Tập 2: dict, unpacking

  Trong tập này, các bạn sẽ làm quen với kiểu dữ liệu từ điển (dict).
Tương tự list comprehension, chúng ta sẽ có kĩ thuật dictionary comprehension.
Ngoài ra, chúng ta sẽ bắt đầu làm quen với một kĩ thuật quan trọng trong
Python tên là unpacking.


NHIỆM VỤ
--------
Lập một từ điển từ chuỗi kí tự kết quả thi như sau:
"Toán: 9,   Địa lí: 7, Văn: 6.5 , Hóa học: 10".

"""


#%% BƯỚC 1: Khởi tạo từ điển trống
ketqua_dict = {}


#%% BƯỚC 2: Split tên và kết quả của từng môn
# Ví dụ: "Toán: 9"
ketqua = "Toán: 9,   Địa lí: 7, Văn: 6.5 , Hóa học: 10"
ketqua.split(",")


#%% BƯỚC 3a: Lặp qua tên và kết quả từng môn
# Với mỗi chuỗi kí tự tên và kết quả, tiếp tục split
# để tách riêng tên môn và điểm thi, sau đó in ra màn hình
for s in ketqua.split(","):
    print(s.split(":"))

#%% BƯỚC 3b: Lặp qua tên và kết quả từng môn
# Với mỗi chuỗi kí tự tên và kết quả, tiếp tục split
# để tách riêng tên môn và điểm thi, lưu vào hai biến
# `mon` và `diem`, loại bỏ dấu cách thừa, rồi in ra màn hình
for s in ketqua.split(","):
    ketqua_s = s.split(":")
    mon = ketqua_s[0]
    diem = ketqua_s[1]
    print(mon, diem)

#%% BƯỚC 3c: Lặp qua tên và kết quả từng môn
# Với mỗi chuỗi kí tự tên và kết quả, tiếp tục split
# để tách riêng tên môn và điểm thi, lưu vào hai biến
# `mon` và `diem` bằng UNPACKING, rồi in ra màn hình
for s in ketqua.split(","):
    mon, diem = s.split(":")
    print(mon, diem)

#%% BƯỚC 3c: Lặp qua tên và kết quả từng môn
# Với mỗi chuỗi kí tự tên và kết quả, tiếp tục split
# để tách riêng tên môn và điểm thi, lưu vào hai biến
# `mon` và `diem`, rồi lưu vào từ điển (đã loại bỏ dấu cách thừa)
for s in ketqua.split(","):
    mon, diem = s.split(":")
    ketqua_dict[mon.strip()] = diem.strip()

print(ketqua_dict)


#%% BƯỚC 4: Sử dụng dictionary comprehension
# {phan_tu1: phan_tu2 for phan_tu1, phan_tu2 in [s.split() for s in danh_sach]}
{mon.strip(): diem.strip() for mon, diem in [s.split(":") for s in ketqua.split(",")]}
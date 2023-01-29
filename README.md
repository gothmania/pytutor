# Python tutorial

Cảm ơn bạn đã ghé thăm Github Repo này của mình, một repo dành cho những bạn mới bắt đầu với lập trình Python. Nêu bạn hoàn toàn chưa biết gì về Python, xin hãy đi theo đúng trình tự các bài dưới đây. Còn nếu bạn đã biết về Python rồi và muốn củng cố thêm kiến thức về một chủ đề nào đó, bạn có thể đi thẳng đến bài tương ứng với chủ đề bạn quan tâm.

Chúc bạn học vui vẻ và yêu thích ngôn ngữ Python như mình.

## Python là gì?

[Python](https://www.python.org/) là một ngôn ngữ lập trình thông dịch bậc cao. Khác với ngôn ngữ biên dịch (từ mã lệnh được dịch ra thành mã máy rồi mới chạy được), mã lệnh của Python được một nhân phiên dịch xử lí và chạy trực tiếp. Do vậy, việc sửa đổi mã lệnh để tùy biến theo nhu cầu của người dùng rất dễ dàng. Mặc dù Python được biết tới nhiều nhất trong Machine Learning và Data Science, nó vẫn được sử dụng cho nhiều mục đích khác.


# Danh sách bài học

Các bài viết sẽ được nhóm lại theo từng chủ đề để các bạn dễ theo dõi. Lưu ý: do mình sử dụng Windows và không biết dùng Mac/Linux, tất cả các hướng dẫn trong bài viết sẽ chỉ áp dụng cho Windows.

## B - Nhập môn (Basic)

1. [Hello World: làm quen với Python](./01_basic/01_helloworld.ipynb)
2. [Biến và Toán tử cơ bản](./01_basic/02_varop.ipynb)
3. [Danh sách (`list`), điều kiện (`if`), và vòng lặp (`while`)](./01_basic/03_listifwhile.ipynb)
4. [`str`, `list`, và vòng lặp `for`](./01_basic/04_strlistfor.ipynb)
5. [List comprehension](./01_basic/05_listcomp.ipynb)
6. [Tiếp tục về `str` (`split`, `join`, `upper`)](./01_basic/06_str.ipynb)
7. [Hàm (def)](./01_basic/07_def.ipynb)
8. [Bộ (`tuple`), Từ điển (`dict`), và Tập (`set`)](./01_basic/08_tupdictset.ipynb)
9. [Giải nén (unpacking)](./01_basic/09_unpacking.ipynb)
10. [Slicing](./01_basic/10_slicing.ipynb)
11. [Định dạng chuỗi kí tự (string formatting)](./01_basic/11_strformat.ipynb)
12. [Tìm kiếm trong chuỗi kí tự](./01_basic/12_strfind.ipynb)

## I - Chủ đề trung cấp (Intermediate)

1. [`zip()`, `enumerate()`](./02_inter/01_zipenum.ipynb)
2. [Lambda, `map()`, `filter()`, và `reduce()`](./02_inter/02_lambda.ipynb)
3. [`yield` và generator comprehension](./02_inter/03_yield.ipynb)
4. [Bit và tính toán theo bit](./02_inter/04_bit.ipynb)
5. [Ngoại lệ (Exceptions)](./02_inter/05_exceptions.ipynb)

## M - Toán (Math)

1. [Tính toán vector hóa (Vectorized calculation)](./03_math/01_vectorized.ipynb)
2. [Tạo số ngẫu nhiên](./03_math/02_random.ipynb)
3. [Slicing trong NumPy](./03_math/03_slicing.ipynb)
4. [Thống kê](./03_math/04_stats.ipynb)

## D - Dữ liệu (Data)

1. [Pandas: Data frame và Series](./04_data/01_pandas.ipynb)
2. [Tên cột (columns) và hàng (index)](./04_data/02_colindex.ipynb)
3. [Slicing trong Pandas](./04_data/03_slicing.ipynb)
4. [Thay thế dữ liệu: `replace()`, `map()`, `mask()`, và `where()`](./04_data/04_replace.ipynb)
5. [Đối xử với dữ liệu NA](./04_data/05_na.ipynb)
6. [Thống kê cơ bản và `groupby()`](./04_data/06_groupby.ipynb)
7. [Biến đổi dữ liệu (transformation): `apply()`](./04_data/07_apply.ipynb)
8. [Tổng hợp dữ liệu (aggregation): kết hợp `groupby()` và `apply()`](./04_data/08_agg.ipynb)
9. [Biến đổi dữ liệu với `groupby()`](./04_data/09_transform.ipynb)
10. [Biến đổi cấu trúc (reshaping)](./04_data/10_reshape.ipynb)
11. [Pivot tables và cross-tabulation](./04_data/11_tabulation.ipynb)
12. [Ghép các bộ dữ liệu](./04_data/12_merge.ipynb)
13. [Số liệu dạng chuỗi kí tự](./04_data/13_string.ipynb)
14. [Số liệu thời gian](./04_data/14_datetime.ipynb)
15. [Số liệu dạng danh mục (categorical)](./04_data/15_categorical.ipynb)
16. [Ví dụ: Data dictionary](./04_data/16_datadict.ipynb)
17. [Deep copy](./04_data/17_deepcopy.ipynb)
18. [MultiIndex](./04_data/18_multiindex.ipynb)

## R - Regular Expression (RegEx)
1. [Tìm kiếm cơ bản](./05_regex/01_basic.ipynb)
2. [Nhóm, lookahead và lookbehind](./05_regex/02_group.ipynb)
3. [Ví dụ](./05_regex/03_examples.ipynb)
4. [Ví dụ: Điểm thi tốt nghiệp cấp 3](./05_regex/04_diemthi.ipynb)

## G - Đồ họa (Graphics)
1. [Thư viện Matplotlib: Figure và Axes, hàm `plot()`](./06_graph/01_intro.ipynb)
2. [Bar, line, histogram, box, KDE](./06_graph/02_plot.ipynb)
3. [Scatter, LOESS, error bar, pairplot, heatmap](./06_graph/03_plot.ipynb)
4. [Nhãn và chú thích](./06_graph/04_label.ipynb)
5. [Tùy biến định dạng nội dung](./06_graph/05_customize.ipynb)
6. [Tùy biến trục tọa độ](./06_graph/06_axis.ipynb)
7. Vẽ nhiều biểu đồ, thêm trục tọa độ thứ ba
8. Thêm chữ và tô màu
9. Ví dụ: Mô phỏng khoảng tin cậy 95%
10. Ví dụ: Mô phỏng P-value
11. Ví dụ: Mô phỏng biến động của quần thể nghiên cứu
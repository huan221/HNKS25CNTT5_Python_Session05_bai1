# Nhập số chi nhánh
branch_count = int(input("Nhập số lượng chi nhánh: "))
month_count = 3

# Tạo danh sách lưu doanh thu
data = []

# Nhập dữ liệu
for branch in range(1, branch_count + 1):
    branch_data = []
    print(f"\n--- Chi nhánh {branch} ---")
    
    for month in range(1, month_count + 1):
        revenue = int(input(f"Nhập doanh thu tháng {month}: "))
        branch_data.append(revenue)
    
    data.append(branch_data)

# In báo cáo
print("\n------ KẾT QUẢ ------")

for branch in range(1, branch_count + 1):
    for month in range(1, month_count + 1):
        print(f"Chi nhánh {branch}, tháng {month}: {data[branch-1][month-1]} triệu đồng")
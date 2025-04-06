import PyPDF2

# ===== 配置部分 =====
input_pdf_path = '1.pdf'  # 原始PDF文件路径
color_pages = [1, 38, 51, 59, 60, 64, 66, 67]  # 需要彩色打印的页码（从1开始）
color_pages = set(p - 1 for p in color_pages)  # 转为0-based索引

color_output = 'color_pages.pdf'
bw_output = 'bw_pages.pdf'

# ===== 主逻辑 =====
reader = PyPDF2.PdfReader(input_pdf_path)
color_writer = PyPDF2.PdfWriter()
bw_writer = PyPDF2.PdfWriter()
total_pages = len(reader.pages)

i = 0
while i < total_pages:
    # 当前双页（正面和背面）
    front = i
    back = i + 1

    # 判断这两页中是否任意一页是彩色页
    is_color = (front in color_pages) or (back in color_pages)

    # 写入相应 writer
    if is_color:
        color_writer.add_page(reader.pages[front])
        if back < total_pages:
            color_writer.add_page(reader.pages[back])
    else:
        bw_writer.add_page(reader.pages[front])
        if back < total_pages:
            bw_writer.add_page(reader.pages[back])

    i += 2  # 处理下一对页

# ===== 保存输出文件 =====
with open(color_output, 'wb') as f:
    color_writer.write(f)

with open(bw_output, 'wb') as f:
    bw_writer.write(f)

print("✅ Done! Generated double-sided color and black-white PDFs.")

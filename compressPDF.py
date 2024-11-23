import fitz  # PyMuPDF

def compress_pdf(input_pdf_path, output_pdf_path, dpi=150):
    # 打開原始 PDF
    pdf_document = fitz.open(input_pdf_path)
    
    # 創建一個新的 PDF 文件
    compressed_pdf = fitz.open()

    # 遍歷每一頁
    for page_num in range(pdf_document.page_count):
        # 獲取每一頁
        page = pdf_document.load_page(page_num)

        # 將頁面轉換為圖像，並指定解析度（例如 150 DPI）
        pix = page.get_pixmap(dpi=dpi)

        # 將圖像保存為 PDF 頁面
        img_pdf = fitz.open()  # 建立一個新的空 PDF
        img_pdf.insert_pdf(fitz.open("pdf", pix.tobytes("pdf")))

        # 將新頁添加到壓縮的 PDF 文件中
        compressed_pdf.insert_pdf(img_pdf)

    # 保存壓縮後的 PDF
    compressed_pdf.save(output_pdf_path, deflate=True)
    print(f"PDF 已壓縮並儲存至: {output_pdf_path}")

# 使用範例
input_pdf_path = 'input.pdf'  # 請替換為你的 PDF 檔案路徑
output_pdf_path = 'compressed_output.pdf'  # 壓縮後的 PDF 路徑

compress_pdf(input_pdf_path, output_pdf_path, dpi=150)

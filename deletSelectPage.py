import fitz  # PyMuPDF

def delete_pdf_pages(input_pdf_path, output_pdf_path, pages_to_delete):
    # 打開 PDF 文件
    pdf_document = fitz.open(input_pdf_path)
    
    # 按照指定頁面刪除頁面，注意頁面索引從 0 開始
    for page_num in sorted(pages_to_delete, reverse=True):
        if 0 <= page_num < pdf_document.page_count:
            pdf_document.delete_page(page_num)
            print(f"刪除頁面: {page_num + 1}")
        else:
            print(f"頁面 {page_num + 1} 不存在")
    
    # 儲存修改後的 PDF
    pdf_document.save(output_pdf_path)
    print(f"PDF 已儲存至: {output_pdf_path}")

# 使用範例
input_pdf_path = 'input.pdf'  # 請替換為你的 PDF 檔案路徑
output_pdf_path = 'output.pdf'  # 儲存刪除頁面後的 PDF 路徑
pages_to_delete = [1, 3]  # 要刪除的頁面列表（例如，刪除第2頁和第4頁）

delete_pdf_pages(input_pdf_path, output_pdf_path, pages_to_delete)

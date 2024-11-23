import fitz  # PyMuPDF
from PIL import Image
import io
import os

def pdf_to_jpg(pdf_path, output_folder):
    # 確保輸出資料夾存在
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # 打開 PDF 文件
    pdf_document = fitz.open(pdf_path)
    
    # 遍歷 PDF 的每一頁
    for page_num in range(pdf_document.page_count):
        # 取得每一頁
        page = pdf_document.load_page(page_num)
        
        # 將頁面轉換為像素圖（默認解析度 72）
        pix = page.get_pixmap(dpi=300)  # 可以設置更高的 DPI 以提高圖像解析度
        
        # 將圖像轉為 JPG 格式
        img = Image.open(io.BytesIO(pix.tobytes("png")))  # 轉為 PIL 圖像對象
        output_path = os.path.join(output_folder, f"page_{page_num + 1}.jpg")
        
        # 儲存 JPG 圖像
        img.save(output_path, "JPEG")
        print(f"已儲存: {output_path}")

# 使用範例
pdf_path = '07.pdf'  # 請替換為你的 PDF 檔案路徑
output_folder = './output'  # 請替換為你希望儲存圖片的資料夾路徑

pdf_to_jpg(pdf_path, output_folder)
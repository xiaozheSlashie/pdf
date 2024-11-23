from PIL import Image
import os

def jpg_to_pdf(image_folder, output_pdf_path):
    # 確保圖像資料夾存在
    if not os.path.exists(image_folder):
        print(f"資料夾 {image_folder} 不存在")
        return
    
    # 取得所有 JPG 圖片檔案
    images = []
    for filename in sorted(os.listdir(image_folder)):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img_path = os.path.join(image_folder, filename)
            img = Image.open(img_path)

            # 確保圖像是 RGB 模式，PDF 需要 RGB 或 CMYK 模式
            if img.mode != 'RGB':
                img = img.convert('RGB')

            images.append(img)

    # 檢查是否有圖片
    if not images:
        print("資料夾中沒有 JPG 圖片")
        return

    # 將多個圖片合併成一個 PDF，圖片按順序排列
    images[0].save(output_pdf_path, save_all=True, append_images=images[1:], resolution=100.0)
    print(f"PDF 已儲存至: {output_pdf_path}")

# 使用範例
image_folder = './images'  # 請替換為你的 JPG 圖片資料夾
output_pdf_path = 'output.pdf'  # 壓縮後的 PDF 路徑

jpg_to_pdf(image_folder, output_pdf_path)

import os
import rembg
from PIL import Image

def rigb (input_folder_path,model):
    fileNum = 0
    totalNum = len(os.listdir(input_folder_path)) #统计输入文件夹内文件数量
    
    base_path = os.path.split(input_folder_path)
    output_folder = os.path.join(base_path[0], 'output')  # 新建一个 output文件夹，用于存储输出文件
    os.makedirs(output_folder, exist_ok=True)  #若文件夹不存在则创建
    
    for filename in os.listdir(input_folder_path):
        # 如果是图片文件
        if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".jpeg"):
            fileNum += 1
        
        # 读取图像文件
            input_image = Image.open(os.path.join(input_folder_path, filename))
        
        # 使用rembg库对图像进行分割
            output_image = rembg.remove(input_image,model)
        
        # 构建输出文件的路径
            output_file_path = os.path.join(output_folder, filename[:-4] + ".png")
        
        # 保存处理后的图像文件
            output_image.save(output_file_path, "PNG")
        
        # 关闭打开的图像文件
            input_image.close()
            output_image.close()
            print("图片 %s 已处理完成，整体处理进度(%d / %d) ！" %(filename,fileNum,totalNum))

if __name__ == '__main__':

    input_folder_path = r"C:\Users\MS-PC\Desktop\image" #输入待处理图片文件夹路径
    model = rembg.new_session("u2net") #设置预训练模型 u2net u2net_human_seg u2net_cloth_seg
    
    rigb(input_folder_path,model)
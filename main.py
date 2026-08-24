import os


video_path = input("Pls input video path:\n").strip('"')
audio_path = input("Pls input audio path:\n").strip('"')
output_path = video_path[:-12] + ".mp4"
txt = 'ffmpeg -i ' + video_path + ' -i ' + audio_path + ' -codec copy ' + output_path
file_path = ''

def remove_first_nine_bytes(file_path):
    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"错误：文件不存在 → {file_path}")
        return False

    # 检查文件大小
    file_size = os.path.getsize(file_path)
    if file_size < 9:
        print(f"错误：文件太小（{file_size}字节），不足9字节无法删除")
        return False

    # 读取文件内容（二进制模式）
    with open(file_path, 'rb') as f:
        data = f.read()

    # 删除前9个字节
    modified_data = data[9:]

    # 直接覆盖原文件
    with open(file_path, 'wb') as f:
        f.write(modified_data)

    print(f"成功：已从 {os.path.basename(file_path)} 删除前9个字节")
    print(f"原始大小: {file_size} 字节 → 新大小: {len(modified_data)} 字节")
    return True


if __name__ == "__main__":

    i = 1

    while 0 < i < 3:
        if i == 1:
            file_path = video_path
            i+=1
        else:
            file_path = audio_path
            i+=1

        # 自动添加扩展名（如果用户忘记输入）
        if not file_path.lower().endswith('.m4s'):
            file_path += '.m4s'
            print(f"提示：已自动添加扩展名 → {file_path}")

        remove_first_nine_bytes(file_path)




f = "main.bat"             #创建的文件名
fp = open(f,"w+")          #打开文件，如果没有，则新建一个
fp.write(txt)              #向文件写入内容
fp.close()                 #关闭文件，若不关闭，则有可能写入失败

os.system(f)

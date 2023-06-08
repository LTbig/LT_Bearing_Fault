import os
import win32com.client


def word_to_pdf(input_path, output_path):
    # 创建Word应用程序对象
    word = win32com.client.Dispatch("Word.Application")

    # 打开Word文档
    doc = word.Documents.Open(input_path)

    # 将Word文档另存为PDF
    doc.SaveAs(output_path, FileFormat=17)

    # 关闭Word文档和应用程序对象
    doc.Close()
    word.Quit()


# 测试代码
input_path = r"C:\Users\newtown\Desktop\new中文版.doc"
output_path = r"C:\Users\newtown\Desktop\new中文版.pdf"
word_to_pdf(input_path, output_path)

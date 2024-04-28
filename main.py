# 这是一个示例 Python 脚本。
import logging
import json
# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。
from pdf_parser import PDFParser



# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    logging.basicConfig(filename=f'./basic.log',
                        encoding='utf-8',
                        level=logging.INFO,
                        filemode='w',
                        format='%(process)d-%(levelname)s-%(message)s')
    logging.getLogger().addHandler(logging.StreamHandler())

    logging.info('** pdf parsing **')
    pdf_path = f'announcements/东方新能源汽车主题混合型证券投资基金2023年中期报告.PDF'
    parser = PDFParser(pdf_path)

    # 2 文字: 标题，章节目录，章节对应的文字内容
    logging.info('== extract text ==')
    parser.extract_text()
    logging.info('-- title --')
    logging.info(parser.text.title)
    logging.info('-- section --')
    for title, section in parser.text.section.items():
        logging.info(title)
    # 指定保存的文件路径
    json_file_path = f"./sections.json"
    # 使用 json.dump() 将字典保存为 JSON 文件
    with open(json_file_path, 'w') as json_file:
        json.dump(parser.text.section, json_file)

    # 3 图片
    logging.info('== extract image ==')
    parser.extract_images()
    images = parser.images
    for image in images:
        # 将图像保存为文件
        image_filename = f"./image_{image.page_num}_{image.title[:10]}.png"
        with open(image_filename, "wb") as image_file:
            logging.info(image.title)
            logging.info(image.page_num)
            image_file.write(image.image_data)

    # 4 表格：表格和对应的标题
    logging.info('== extract table ==')
    parser.extract_tables()
    for i, table in enumerate(parser.tables):
        logging.info(table.title)
        csv_filename = f"./table_i_{table.page_num}_{table.title[:10]}.csv"
        table.table_data.to_csv(csv_filename)

# 访问 https://www.jetbrains.com/help/pycharm/ 获取 PyCharm 帮助

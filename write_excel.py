import xlwt


def sheet_write(sheet):
    sheet.write(0, 0, "raw_id")
    sheet.write(0, 1, "new_id")
    for i in range(0, 251):
        sheet.write(i+1, 0, i)


if __name__ == "__main__":
    book_name = "翻转处理后人脸关键点对应关系.xls"
    book = xlwt.Workbook(encoding='utf-8')  # 创建Workbook，相当于创建Excel
    # 创建sheet，Sheet1为表的名字，cell_overwrite_ok为是否覆盖单元格
    sheet1 = book.add_sheet(u'Sheet1', cell_overwrite_ok=True)
    sheet_write(sheet1)
    book.save(book_name)
    print(book_name+"创建完成**************")

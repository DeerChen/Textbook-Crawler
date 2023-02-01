from PIL import Image
import os


def sort_pic(book: str) -> list:
    '''
    description: 图片排序
    param       {str} book
    return      {*}
    author     : Senkita
    '''
    files: list = []
    for file in os.listdir(book):
        if file[-4:] == '.jpg':
            files.append(file[:-4])

    files.sort(key=lambda ele: int(ele))
    return files


def generate_pdf(book: str, files: list) -> None:
    '''
    description: 生成PDF
    param       {str} book
    param       {list} files
    return      {*}
    author     : Senkita
    '''
    pics: list = []
    pdf: Image.Image = Image.open('{}/{}.jpg'.format(book, files[0]))

    files.pop(0)

    for pic in files:
        img: Image.Image = Image.open('{}/{}.jpg'.format(book, pic))
        if img.mode == 'RGBA':
            img = img.convert('RGB')
        pics.append(img)

    pdf.save(
        './{}.pdf'.format(book),
        'PDF',
        resolution=100.0,
        save_all=True,
        quality=100,  # 清晰度
        subsampling=0,
        append_images=pics,
    )
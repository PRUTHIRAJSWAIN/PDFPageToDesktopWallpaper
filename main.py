import ctypes
import os
from PIL import Image, ImageDraw, ImageFont
import PyPDF2
from datetime import datetime


def create_image_with_text(text, image_path, font_size=20, image_size=(1920, 1080), text_position=(800, 100),
                           text_color=(255, 255, 255), background_color=(0, 0, 0)):
    image = Image.new("RGB", image_size, background_color)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("arial.ttf", font_size)
    draw.text(text_position, text, font=font, fill=text_color)
    image.save(image_path)

def set_wallpaper(image_path):
    SPI_SETDESKWALLPAPER = 20

    if not os.path.exists(image_path):
        print(f"Error: The file {image_path} does not exist.")
        return
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, image_path)


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        num_pages = len(pdf_reader.pages)
        text = []
        for page_num in range(num_pages):
            page = pdf_reader.pages[page_num]
            text.append(page.extract_text())
    return text


if __name__ == '__main__':
    StartingPage = 34
    starting_date = '2023-05-15'
    current_date = datetime.now()

    # Convert the starting_date string to a datetime object
    starting_date = datetime.strptime(starting_date, '%Y-%m-%d')

    # Calculate the difference between the current_date and starting_date
    date_difference = current_date - starting_date
    pdf_file_path = r'C:\Users\PRUTHIRAJ\Desktop\sample.pdf'
    pdf_text = read_pdf(pdf_file_path)
    page_to_display= StartingPage + date_difference.days
    print(page_to_display)
    text_to_display = pdf_text[page_to_display]
    length = 0
    for i in pdf_text:
        length += len(i)
    output_image_path = "output_image.png"
    create_image_with_text(text_to_display, output_image_path)
    set_wallpaper("D:\personalproject\output_image.png") # Use Absolute Location

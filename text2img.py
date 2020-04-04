"""
Author: Reljod T. Oreta
Date created: April 4, 2020

Description: To convert text from command or file to Image.
"""

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from shutil import copyfile
from subprocess import getstatusoutput
from sys import argv


class CommandReader:
    def get_cmd_output(self, command):
        stat_out = getstatusoutput(command)
        if self._cmd_error_report(stat_out):
            return stat_out[1]
        return ""

    def _cmd_error_report(self, stat_out):
        if stat_out[0] == 0:
            return True
        print(stat_out[1])
        return False


class FileReader:

    def read_file(self, file_path):
        with open(file_path, 'r') as fp:
            file_text = fp.read()
        return file_text


class TextReader:
    def __init__(self, text):
        self.text = text
        self.text_list = text.split('\n')
        self.num_lines = len(self.text_list)
        self.max_width_line = max(self.text_list, key = lambda s: len(s))


class Text2ImageGenerator(FileReader, CommandReader, TextReader):
    """
    Author: Reljod T. Oreta

    Default values:

    bg_color = #000
    text_color = #FFF
    left_pad = 3
    right_pad = 5
    font_size = 14
    font_path = "~/projects/Test-Report-Automation-Project/fonts/arial.ttf"
    width = 200
    height = 500
    img_fname = "image.png"

    Change these value by initializing by different parameters:
    t2i = Text2ImageGenerator(bg_color="#FFF", text_color="#000")

    """
    prop = {
        "bg_color" : "#000",
        "text_color" : "#FFF",
        "left_pad" : 3,
        "right_pad" : 50,
        "font_size" : 14,
        "font_path" : "~/projects/Test-Report-Automation-Project/fonts/arial.ttf",
        "width" : 200,
        "height" : 500,
        "img_fname" : "image.png"
    }

    def __init__(self, **properties):
        self.prop.update(properties)
        self.font = ImageFont.truetype(self.prop["font_path"], 
                                       self.prop["font_size"])
        self.font = ImageFont.truetype()
    
    def _generate_img(self):
        self.line_height = self.font.getsize(self.text)[1]
        img_height = self.line_height * self.num_lines
        img_width = self.font.getsize(self.max_width_line)[0] + self.prop["right_pad"]

        img = Image.new("RGBA", (img_width, img_height), self.prop["bg_color"])
        return img

    def _draw_image(self, img):
        draw = ImageDraw.Draw(img)
        y = 0
        for line in self.text_list:
            draw.text((self.prop["left_pad"], y),
                       line, 
                       self.prop["text_color"],
                       font=self.font)
            y += self.line_height
        return img

    def generate_from_text(self, text):
        TextReader.__init__(self, text)
        img = self._generate_img()
        img = self._draw_image(img)
        self.image = img

    def generate_from_file(self, file_path):
        text_file = self.read_file(file_path)
        self.generate_from_text(text_file)

    def generate_from_command(self, command):
        text_command = self.get_cmd_output(command)
        self.generate_from_text(text_command)

    def save_image(self):
        self.image.save(self.prop["img_fname"])


if __name__ == "__main__":
    target_path = "/mnt/c/users/Reljod/Desktop/"

    t2i = Text2ImageGenerator(font_size=1_000, bg_color="#F00")  
    t2i.generate_from_command("echo Imelda")
    img_fname = t2i.prop["img_fname"]
    copyfile(img_fname, target_path + img_fname)
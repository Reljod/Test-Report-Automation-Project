
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from shutil import copyfile
from subprocess import getstatusoutput
from sys import argv


class CommandReader:
    def __init__(self, command):
        self.command = command

    def get_cmd_output(self):
        stat_out = getstatusoutput(self.command)
        if self._cmd_error_report(stat_out):
            return stat_out[1]
        return ""

    def _cmd_error_report(self, stat_out):
        if stat_out[0] == 0:
            return True
        print(stat_out[1])
        return False


class FileReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path, 'r') as fp:
            file_text = fp.readlines()
        return file_text


class Text2ImageGenerator(FileReader, CommandReader):
    prop = {
        "bg_color" : "#000",
        "text_color" : "#FFF",
        "left_pad" : 3,
        "right_pad" : 50,
        "font_size" : 14,
        "font_path" : "/home/reljod/projects/Test-Report-Automation-Project/fonts/Hack-Regular.ttf",
        "width" : 200,
        "height" : 500
    }

    def __init__(self, **properties):
        self.prop.update(properties)
        if "file_path" in properties.keys():
            file_path = properties["file_path"]
            FileReader.__init__(self, file_path)

        if "command" in properties.keys():
            command = properties["command"]
            CommandReader.__init__(self, command)
        

        self.font = ImageFont.truetype(self.prop["font_path"], 
                                       self.prop["font_size"])
        

    def generate(self, text):
        text_list = text.split('\n')
        num_lines = len(text_list)

        max_width_line = max(text_list, key = lambda s: len(s))

        line_height = self.font.getsize(text)[1]

        img_height = line_height * num_lines
        img_width = self.font.getsize(max_width_line)[0] + self.prop["right_pad"]

        img = Image.new("RGBA", (img_width, img_height), self.prop["bg_color"])
        draw = ImageDraw.Draw(img)

        y = 0
        for line in text_list:
            draw.text((self.prop["left_pad"], y),
                       line, 
                       self.prop["text_color"],
                       font=self.font)
            y += line_height

        self.save_image(img, "image.png")
        self.copy_image_src_to_dir("image.png", "/mnt/c/users/Reljod/Desktop/image.png")


    def generate_from_file(self):
        text_file = self.read_file()
        self.generate(text_file)

    def generate_from_command(self):
        text_command = self.get_cmd_output()
        self.generate(text_command)

    def save_image(self, image, image_path):
        image.save(image_path)

    def copy_image_src_to_dir(self, source_path, target_path):
        copyfile(source_path, target_path)


if __name__ == "__main__":
    t2i = Text2ImageGenerator(command='cat subproc_text2img.py')  
    t2i.generate_from_command()  
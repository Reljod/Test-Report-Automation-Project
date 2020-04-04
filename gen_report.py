from text2img import Text2ImageGenerator
from shutil import copyfile

img_target_path = "/mnt/c/users/Reljod/Desktop/"
txtfile_spath = "./samp_files/report1.txt"

t2i = Text2ImageGenerator(font_size=20)
# t2i.generate_from_command("cat text2img.py")
t2i.generate_from_file(txtfile_spath)
t2i.save_image()

img_fname = t2i.prop["img_fname"]
copyfile(img_fname, img_target_path + img_fname)
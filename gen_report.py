from text2img import Text2ImageGenerator
from shutil import copyfile


class SchemaDiffReport:
    pass


if __name__ == "__main__":
    from sys import argv

    db1 = argv[1]
    db2 = argv[2]

    t2i = Text2ImageGenerator(img_fname = "schema_diff.png")
    t2i.generate_from_command("sdiff {} {}".format(db1, db2))
    t2i.save_image()
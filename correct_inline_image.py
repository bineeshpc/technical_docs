import argparse
import re
import os

def parse_cmdline():
    parser = argparse.ArgumentParser(
        description='correct inline images in md file')
    parser.add_argument('filename', 
                        type=str,
                        help='filename')
    parser.add_argument('output_filename', 
                        type=str,
                        help='output filename')
    args = parser.parse_args()
    return args

image_regex = r"\[\[(.*)\]\]"
image_compiled_regex = re.compile(image_regex)


def correct_inline_image(filename, output_filename):
    def is_code_output():
        return line.find('``` {.example}') != -1

    def is_image(line):
        return image_compiled_regex.match(line) != None

    def get_filename(line):
        return image_compiled_regex.match(line).group(1)

    def is_code_example_end(line):
        return line.find('```') != -1

    with open(filename) as f, open(output_filename, 'w') as f2:
        for line in f:
            if is_code_output():
                for line in f:
                    if is_image(line):
                        output = "![alt {fn}]({fn})\n".format(fn=get_filename(line))
                        f2.write(output)
                    if is_code_example_end(line):
                        f2.write(line)
                        break
            else:
                f2.write(line)


def main():
    args = parse_cmdline()
    correct_inline_image(args.filename, args.output_filename)
    os.rename(args.output_filename, args.filename)

if __name__ == "__main__":
    main()
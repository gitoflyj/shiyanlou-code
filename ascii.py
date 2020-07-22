from PIL import Image
import argparse

#define char_list
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")

#processing parameters
parser = argparse.ArgumentParser()

parser.add_argument('file')    #input file
parser.add_argument('--output')   #output file
parser.add_argument('--width', type = int, default = 80)  #output width
parser.add_argument('--height', type = int, default = 80) #output height

#get parameters
args = parser.parse_args()
IMG = args.file
WIDTH = args.width
HEIGHT = args.height
OUTPUT = args.output


#RGB to char
def get_char(r, g, b, alpha = 256):
    #determine the value of  alpha
    if alpha == 0:
        return ' '
    length = len(ascii_char)
    gray = int((2126 * r + 7152 * g + 722 * b)/10000)
    #gray / 256 = x / length
    return ascii_char[int(gray * length / 257.0)]

if __name__ == '__main__':

    #open picture
    im = Image.open(IMG)
    #im = im.convert('RGB')
    im = im.resize((WIDTH, HEIGHT),Image.NEAREST)

    #init string
    txt = ""

    #traverse line
    for i in range(HEIGHT):
        #traverse row
        for j in range(WIDTH):
            txt += get_char(*im.getpixel((j,i)))
        txt += '\n'
    print(txt)

    #output file
    with open("output.txt", 'w') as f:
        f.write(txt)

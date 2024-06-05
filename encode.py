from PIL import Image
import math

# Конвертер файла в PNG

# Указываете путь до файла (похуй какого, читается в байтах всё равно) и получаете картинку в PNG формате

def readFileToHex(filePath):
    with open(filePath, 'rb') as file:
        hexString = file.read().hex()
        hexString += '00000000FFFAAAFFFAAAFFFAAAFFFAAAFFF00000000'
    return str(hexString).upper()

def hexToRgb(hexString):
    if len(hexString) < 6:
        hexString = hexString.ljust(6, '0')
    return tuple(int(hexString[i:i+2], 16) for i in range(0, 6, 2))

def createImageFromHex(hexString):
    rgbValues = [hexString[i:i+6] for i in range(0, len(hexString), 6)]
    numPixels = len(rgbValues)
    sideLength = math.ceil(math.sqrt(numPixels))
    
    image = Image.new('RGB', (sideLength, sideLength), color=(255, 255, 255))
    pixels = image.load()
    for i, hexColor in enumerate(rgbValues):
        rgb = hexToRgb(hexColor)
        row = i // sideLength
        col = i % sideLength
        pixels[col, row] = rgb

    return image

def convertTxtToPng(inputFilename, outputImageFilename):
    hexString = readFileToHex(inputFilename)
    image = createImageFromHex(hexString)
    image.save(outputImageFilename)

if __name__ == "__main__":
    inputFilename = input("Path >> ")
    outputImageFilename = 'output_image.png'
    convertTxtToPng(inputFilename, outputImageFilename)

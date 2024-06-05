from PIL import Image

# Конвертер PNG обратно в файл

# Указываете путь до PNG и получаете исходный файл

def imageToHex(imagePath):
    img = Image.open(imagePath)
    pixels = img.load()
    width, height = img.size

    hexString = ''
    for y in range(height):
        for x in range(width):
            hexString += '{:02X}{:02X}{:02X}'.format(*pixels[x, y])

    hexString = hexString.split("00000000FFFAAAFFFAAAFFFAAAFFFAAAFFF00000000")[0]

    return hexString

def convertPngToTxt(imagePath, outputFilename):
    hexString = imageToHex(imagePath)
    binaryData = bytes.fromhex(hexString)
    with open(outputFilename, 'wb') as file:
        file.write(binaryData)

if __name__ == "__main__":
    inputImagePath = input("Path >> ")
    outputFilename = 'output_text.txt'
    convertPngToTxt(inputImagePath, outputFilename)

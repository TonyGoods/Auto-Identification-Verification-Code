from PIL import Image
import numpy as np

'''
    首先将获取的图片二值化   √
    再切割得到左半部分      √
    之后进行去噪           √
    再将图片保存           √

'''


def changeToGreyImage(fileName, index):
    print(index)
    image = Image.open(fileName)
    binary_image = image.convert('1')
    binary_array = np.array(binary_image, dtype='i')
    cutting_array = binary_array[:24, 2:54]

    image_shape = cutting_array.shape
    for i in range(image_shape[0]):
        for j in range(image_shape[1]):
            if cutting_array[i, j] == 0:
                if i - 1 > -1 and cutting_array[i - 1, j] == 0:
                    continue
                elif i + 1 < image_shape[0] and cutting_array[i + 1, j] == 0:
                    continue
                elif j + 1 < image_shape[1] and cutting_array[i, j + 1] == 0:
                    continue
                elif j - 1 > -1 and cutting_array[i, j - 1] == 0:
                    continue
                cutting_array[i, j] = 1
            else:
                if i - 1 > -1 and cutting_array[i - 1, j] == 1:
                    continue
                elif i + 1 < image_shape[0] and cutting_array[i + 1, j] == 1:
                    continue
                elif j + 1 < image_shape[1] and cutting_array[i, j + 1] == 1:
                    continue
                elif j - 1 > -1 and cutting_array[i, j - 1] == 1:
                    continue
                cutting_array[i, j] = 0

    cutting_array_1 = cutting_array[:, :int(image_shape[1] / 4 + 2)]
    cutting_array_2 = cutting_array[:, int(image_shape[1] / 4 - 1): int(image_shape[1] / 4 * 2 + 1)]
    cutting_array_3 = cutting_array[:, int(image_shape[1] / 4 * 2 - 1):int(image_shape[1] / 4 * 3 + 1)]
    cutting_array_4 = cutting_array[:, int(image_shape[1] / 4 * 3 - 2):int(image_shape[1])]
    cutting_image_1 = Image.fromarray(cutting_array_1 * 255).convert('RGB')
    cutting_image_2 = Image.fromarray(cutting_array_2 * 255).convert('RGB')
    cutting_image_3 = Image.fromarray(cutting_array_3 * 255).convert('RGB')
    cutting_image_4 = Image.fromarray(cutting_array_4 * 255).convert('RGB')
    cutting_image_1.save('cuttingImage/' + str(index * 4) + '.jpg')
    cutting_image_2.save('cuttingImage/' + str(index * 4 + 1) + '.jpg')
    cutting_image_3.save('cuttingImage/' + str(index * 4 + 2) + '.jpg')
    cutting_image_4.save('cuttingImage/' + str(index * 4 + 3) + '.jpg')

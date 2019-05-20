import os
import matrix_to_image

converter = matrix_to_image.converter

os.system('clear')

path = os.getcwd() + '/'
print('path: ' + path)

log = converter(
    path = path,
    file_name = '1.neutral',
    extension = '.sim',
    log = 'ON'
)


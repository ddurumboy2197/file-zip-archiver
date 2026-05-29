import zipfile
import os

def zip_files(directory, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                zip_file.write(file_path, rel_path)

# directory - zip qilish uchun fayl yoki direktoriya
# output_filename - zip faylini saqlash uchun nom
directory = '/path/to/your/files'
output_filename = 'output.zip'
zip_files(directory, output_filename)
```

```python
import os
import zipfile

def zip_files(directory, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zip_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                rel_path = os.path.relpath(file_path, directory)
                zip_file.write(file_path, rel_path)

# directory - zip qilish uchun fayl yoki direktoriya
# output_filename - zip faylini saqlash uchun nom
directory = '/path/to/your/files'
output_filename = 'output.zip'
zip_files(directory, output_filename)

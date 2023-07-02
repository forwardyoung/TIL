## zip 파일 압축하기

python 내장 모듈인 Zipfile 모듈을 이용하여 간단한 이미지 폴더를 압축하였다.

![image-20230703001629896](C:\Users\User\Desktop\zip_test_1.jpg)

```python
import os
import zipfile

# folder_path : 압축할 폴더의 경로
# zip_path : 생성될 파일의 경로와 이름
def zip_folder(folder_path, zip_path):
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zip_file.write(file_path, os.path.relpath(file_path, folder_path))


folder_path = r'C:\Users\User\Desktop\cats'

zip_path = r'C:\Users\User\Desktop\cats.zip'

zip_folder(folder_path, zip_path)
```

새 파일 => `w` 

`os.walk` : 폴더 내 모든 하위 폴더와 파일 반복

`zip_file.write` : 파일을 압축 파일에 추가

`os.path.relpath` : 압축 파일 내 relative path(상대 경로) 유지



![image-20230703001703731](C:\Users\User\Desktop\zip_test_2.jpg)

바탕화면에 `cats.zip`이라는 압축 파일이 생성되었다!
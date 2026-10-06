# import os

# print(os.listdir())

# import os  

# for item in os.listdir():
#     print(item)

# import os 

# os.mkdir("test")

# print("Folder created")

# import os

# folder = "data"

# if os.path.exists(folder):
#     print("folder exists")

# else:
#     print("folder does not exists")

# import os 

# for file in os.listdir():
#     if file.endswith(".jpg"):

#      elif file.endswith(".pdf"):

#      elif file.endswith(".py"):

# import os
# os.mkdir("test")

# import os 
# os.makedirs("project/data/raw")

# import os 
# print(os.path.isfile("module_5.py"))

# import os 

# for item in os.listdir():
#     if os.path.isdir(item):
#         print(item)

# from pathlib import Path
# print(Path.cwd())

# from pathlib import Path 
# path = Path("data")

# print(path)
# print(type(path))

# from pathlib import Path
# path = Path("data")
# print(path.exists())

# from pathlib import Path
# path = Path("data")
# print(path.is_dir())

# from pathlib import Path

# folder = Path("data")

# folder.mkdir(exist_ok=True)

# print("Done")

# from pathlib import Path

# path = Path("data")

# for item in path.iterdir():
#     print(item)

# a = "2"
# b = "3"

# print(a - b)

# from pathlib import Path

# file  = Path("Photo.jpg")

# print(file.suffix)

# from pathlib import Path 

# path = Path("data/sales.csv")

# print(path.parent)

# from pathlib import Path

# base = Path(("project"))

# data = base / "data"
# raw = data / "raw"
# file = raw / "sales.csv"

# print(file)

# from pathlib import Path

# path = Path("project")

# for file in path.glob("*.py"):
#     print(file)

# from pathlib import Path

# path = Path("project")

# for file in path.rglob("*.py"):
#     print(file)

# from pathlib import Path

# old = Path("old.txt")

# old.rename("new.txt")

# from pathlib import Path  

# folder = Path("project")

# for item in folder.iterdir():
#     if item.is_file():

#         print("File:",item.name)
#         print("Extension")

# from pathlib import Path

# folder = Path("project")

# for item in folder.iterdir():
#     if item.is_file():

#         print("File:",item.name)
#         print("Extension:",item.suffix)
#         print()

# from pathlib import Path

# file = Path("hello.txt")

# with  open("hello.txt", "a") as file:
#     file.write("\nwelcome to Advanced Python!")


# from pathlib import Path

# file = Path("hello.txt")
# content = file.read_text()

# print(content)

# with open("hello.txt", "a") as file:
#     file.write("\nWelcome to Advanced Python!")

# with open("hello.txt", "a") as file:
#     file.write("\nWelcome to Advanced Python!")

# with open("hello.txt", "r") as file:
#     print(file.read())

# from pathlib import Path

# file = Path("hello.txt")

# file.rename("welcome.txt")

# from pathlib import Path
# base = Path("downloads")

# (base / "images").mkdir(parents=True, exist_ok=True)
# (base / "Documents").mkdidr(parents=True, exists_ok=True)
# (base / "Videos").mkdir(parents=True, exist_ok=True)
# (base / "Music").mkdir(parents=True, exist_ok=True)

# import numpy as np

# marks = np.array([78, 85, 92, 88, 76])

# print(marks*2)

import numpy as np

a= np.array([10,20,30,40,50])

print(a)
print(type(a))
print(a.shape)
print(a.ndim)
print(a.size)
print(a.dtype)

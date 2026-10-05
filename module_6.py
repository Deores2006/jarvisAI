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

from pathlib import Path

for file in path.glob("*"):
    print(file)
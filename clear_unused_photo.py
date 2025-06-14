import os
# 用于清理md文件中没有用到的图片（位于assets） 后续进一步升级，实现文件和目录的选择
folder = "assets"
md_files = []
photo_in_folder = []
photo_exist = []
md_contents = []
photo_delete=[]
for i, j, k in os.walk(folder):
    photo_in_folder = k

for i, j, k in os.walk("."):
    for a in k:
        if a.split(".")[-1] == "md":
            md_files.append(a)
print("Current folder has", md_files)

for i in md_files:
    with open(i, "r", encoding="utf-8") as file:
        md_contents.append(file.read())
for i in photo_in_folder:
    for j in md_contents:
        if i in j and i not in photo_exist:
            photo_exist.append(i)
print("photos not in *.md:")
for i in photo_in_folder:
    if i not in photo_exist:
        photo_delete.append(i)
        print(i)

if photo_delete and input("Delete them?[N/y]:") in ["Y","y"]:
    for i in photo_delete:
        os.remove(folder+"/"+i)
    print("cleared photos!")
elif not photo_delete:
    print("no photos can be deleted!")
print("Thanks for using!")
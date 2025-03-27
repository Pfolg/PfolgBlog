import os
import datetime

directory="./directory.md"

def getFileCreatTime(p):
    # 获取创建时间戳（Windows上为创建时间）
    if os.path.exists(p):
        creation_timestamp = os.path.getctime(p)

        # 转换为可读时间格式
        creation_time = datetime.datetime.fromtimestamp(creation_timestamp)
        formatted_time = creation_time.strftime("%Y-%m-%d %H:%M:%S")

        return formatted_time
    else:
        return None

def sortData(data):
    # 定义当前时间
    now = datetime.datetime.now()
    # 转换为可排序的列表（保留键值关系）
    sorted_items = sorted(
        data.items(),
        key=lambda item: abs(now - datetime.datetime.strptime(item[1]['time'], "%Y-%m-%d %H:%M:%S"))
    )

    # 输出排序结果（按时间由近到远）
    # for key, value in sorted_items:
    #     print(f"{key}: {value['time']}")

    # 如果需要生成新的有序字典
    from collections import OrderedDict
    ordered_data = OrderedDict(sorted_items)
    return ordered_data

passages_infor={}
print("正在读取文章数据……")
for i,j,k in os.walk("Passages"):
    # print("\ni="+str(i)+"\nj="+str(j)+"\nk="+str(k))
    if i=="Passages":
        for a in j:
            passages_infor[a]={
            "folder":i+"/"+a,
            "time":getFileCreatTime(i+"/"+a)
        }
# print("-"*50)
print("文章获取完毕，进一步分析……")
for item in passages_infor.keys():
    folder=passages_infor.get(item).get("folder")
    for i,j,k in os.walk(folder):
        # print("\ni="+str(i)+"\nj="+str(j)+"\nk="+str(k))
        if "\\" in i:
            continue
        elif k:
            psg=[]
            for p in k:
                if ".md" in p:
                    psg.append(folder+"/"+p)
            psg_dict=passages_infor.get(item)
            psg_dict["psg"]=psg
            passages_infor[item]=psg_dict



print("文章数据分析完毕……\n开始自动整理目录……")
# print(passages_infor)
passages_infor=sortData(passages_infor)
# 清空原数据
with open(directory,"w",encoding="utf-8") as file:
    file.write("# 目录\n\n")

msg=""
with open(directory,"a",encoding="utf-8") as file:
    for i in passages_infor.keys():
        file.write(f"### {i}\n\n**创建时间：** {passages_infor.get(i).get('time')}\n\n")
        psg=passages_infor.get(i).get("psg")
        for j in psg:
            title=j.replace('/','.').split('.')[-2]
            if title in ["main"]:
                title=i
            file.write(f"[{title}]({j})\n\n")
        if " " in j:
            msg="\n如果路径包含空格可能无法生成正常链接！"

print("目录文件生成完毕！",msg)
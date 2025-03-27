**编写时间：** 2024年9月5日10:36:40

**Fortran环境配置：** Visual Studio 2022 + Intel® oneAPI Base Toolkit + Intel® HPC Toolkit

**演示环境：** Windows 10 x64 VMware虚拟机

# 准备工作
## 下载 Visual Studio 2022
下载链接：
https://visualstudio.microsoft.com/zh-hans/

 Visual Studio 2022还可以在store里面下载到

![image](https://github.com/user-attachments/assets/11988cff-40fe-4fdc-ba92-cbd41fb32f4b)

## 下载Intel® oneAPI Base Toolkit

下载链接：
https://www.intel.cn/content/www/cn/zh/developer/tools/oneapi/base-toolkit-download.html?operatingsystem=windows&windows-install-type=online
![32b8af8aac8727c2d36a50f6c9727edd](https://github.com/user-attachments/assets/994d7496-922f-4b98-92f3-e8cb2e791f72)

**你也可以自己登录账户下载，本演示不进行任何登录**

## 下载Intel® HPC Toolkit
下载链接：
https://www.intel.com/content/www/us/en/developer/tools/oneapi/hpc-toolkit-download.html?operatingsystem=windows&windows-install-type=online

![68dd4d145df4f0440b88d12bb5f50abf](https://github.com/user-attachments/assets/ad75aef2-d359-452a-ad62-b6c4385d1851)

# 安装
![image-1](https://github.com/user-attachments/assets/6512b517-a7f3-47d6-9ca2-6f8657f26e83)

**请以VS->Base->HPC的顺序进行安装，不能三个同时安装！**
## Visual Studio

出现此页面之前可无脑操作

![image-2](https://github.com/user-attachments/assets/2b2f7200-9a09-4932-bae5-75ef45a08bc1)

注意：这三个项不能放到同一文件夹内

建议：直接将路径前的 **[C]** 替换为 **[D]**

![image-3](https://github.com/user-attachments/assets/b75bac5f-d0b3-4aad-8036-4a15a39f335c)

等待安装完成，完成后直接关闭，没有多余操作。

## Intel® oneAPI Base Toolkit
* 1
![image-4](https://github.com/user-attachments/assets/06ec31b0-c72f-4ed9-a420-fa8a90966751)
* 2
![image-5](https://github.com/user-attachments/assets/1bb93aca-4325-41ee-9d19-cbbd9af45d4c)

* 3 

    **除了这两个，其他全部取消勾选，** 下方可以更改安装路径

  ![image-6](https://github.com/user-attachments/assets/46f03bdc-22dd-442b-937f-5166806a85ef)

* 4 

  集成到Visual Studio 2022

    ![image-7](https://github.com/user-attachments/assets/8a701a95-023b-4855-af39-964feb164561)


* 5

    不让它收集个人信息，install

    ![image-8](https://github.com/user-attachments/assets/5d057582-84de-4574-bb1c-a9b78c8e8c0e)

* 6

    最后点击finish
## Intel® HPC Toolkit

与上面类似，这里这样选择

![image-9](https://github.com/user-attachments/assets/a347ffcf-6a9f-4a62-b1a5-f0949d978722)

# HelloWorld

**请在所有安装完成后进行此步骤**

* 启动Visual Studio 2022

    ![image-10](https://github.com/user-attachments/assets/c3704231-0c01-46bd-8821-4f7e59c2eb2c)


* 进行初始设定，本演示**不登录**

* 创建新项目

    ![image-11](https://github.com/user-attachments/assets/18656a0d-212f-4c26-994f-a6d0c12e37e0)


    ![image-12](https://github.com/user-attachments/assets/32b98d3e-4996-440d-8b9b-26e851190843)


    ![image-13](https://github.com/user-attachments/assets/b8a4b0ff-3fe2-4120-8b3f-18d21ab9bf8c)

* 运行

    ![image-14](https://github.com/user-attachments/assets/98dfc0c2-0a11-4b62-b348-445cbafb6317)


* END

    ![image-15](https://github.com/user-attachments/assets/1be6568d-7cf7-4bae-a904-c843d09cf2a4)


**本教程到此结束**

参考视频：

 https://www.bilibili.com/video/BV1oh411o7AT/?spm_id_from=..search-card.all.click

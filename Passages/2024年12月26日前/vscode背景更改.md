# 效果
![](https://github.com/user-attachments/assets/8fec340b-ff7c-441b-8040-6ca534e8bf7e)
# 实现方法
**第0步** 以管理员身份运行VScode
## 首先
需要安装这个扩展
![](https://github.com/user-attachments/assets/c54a68b8-32a4-4a2d-964a-7c9db6d52688)

## 然后

![](https://github.com/user-attachments/assets/019b192b-4d83-4516-837a-b5f07c2a75ac)

## 接下来
找到配置文件
![](https://github.com/user-attachments/assets/d8b3b593-25e0-4279-ad65-af0fc940f453)
## 再后来
在配置文件的下面但不超过最后一个大括号的地方加入以下内容

~~~java
"update.enableWindowsBackgroundUpdates": true,

"background.fullscreen": {//设置全屏背景
      "images": ["file:///D:/Wallpaper/black-background-monochrome-selective-coloring-anime-girls-simple-background-Oshi-no-Ko-2252942-wallhere.com.png"], // urls of your images 在“///”后面添加自己的图片路径
      "opacity": 0.9, // 0.85 ~ 0.95 recommended 不透明度
      "size": "cover", // also css, `cover` to self-adaption (recommended)，or `contain`、`200px 200px`
      "position": "center", // alias to `background-position`, default `center`
      "interval": 0 // seconds of interval for carousel, default `0` to disabled.
},

"background.useFront": true,
"background.useDefault": false, //是否使用默认图片
"background.styles": [

    {},
    {},
    {}
],
~~~
# 问题
## 警告-安装损坏
来自官方文档的解决方法
~~~
Warns
This extension works by editting the vscode's css file.

So, a warning appears while the first time to install or vscode update. U can click the [never show again] to avoid it.
~~~
这个扩展通过修改VScode的css文件进行工作

警告信息会在第一次安装或更新VScode时出现，你可以点击 **[不再显示]** 来避免

## 卸载方法
搬运的官方文档

three ways

1. (recommended)

press `F1` to open Command Palette, enter and chose `Background - Uninstall (remove extension)` , automatically complete uninstall.

2. 
Set the config  {"background.enabled": false}  in settings.json, then uninstall the plugin.

3. An unfriendly way:

If you uninstall this plugin directly, don't worry.
Exit vscode completely, then open, then reload. Now it's clean :D
(I know it's strange... Because of the limit of vscode)

## 更多设置

你可以查阅扩展的描述信息以了解更多，如果你有一个全局划词翻译软件或者OCR程序会有助于你的阅读。

**参考了以下文章或网站**

[VSCode设置背景图片的两种方式](https://blog.csdn.net/ycx60rzvvbj/article/details/105615993)

[扩展描述](https://marketplace.visualstudio.com/items?itemName=shalldie.background)

[我找壁纸的网站](https://wallhere.com/zh/)
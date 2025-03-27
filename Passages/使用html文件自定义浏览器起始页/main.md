### 敲键盘的缘由

这是360浏览器的起始页

![alt text](image.png)

这是Edge的，还是优化后的，不然和360一样——满屏广告

![alt text](image-1.png)

可是360的无法通过一般设置改成Edge那样的。

### 那你问我

Q：怎么办？

~~A：摆！~~

A：自己动手，丰衣足食！

Look——

![alt text](image-2.png)

![alt text](image-3.png)

### 那你问我——怎么做？

那简单啊，其实只要有想法就行。

用JavaScript（其实我不会）写一个html文件出来，不会？把想要实现的想法给AI就行，让它帮你写：

这是DeepSeek帮我写的（作为一个开发者，改改代码还是可以的），以下代码实现的就是上面那种效果：
~~~html
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        * { 
            margin: 0; 
            padding: 0; 
            box-sizing: border-box; 
        }

        /* 新增文字容器样式 */
        .center-text {
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            font-size: 7rem;      /* 字体大小 */
            font-weight: bold;     /* 加粗 */
            color: rgb(201, 176, 234);         /* 字体颜色 */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5); /* 文字阴影 */
            z-index: 1;           /* 确保文字在图片上方 */
        }
    </style>
    <title>主页</title>
</head>
<body>
    <script>
        // 动态创建图片
        const img = document.createElement('img');
        img.src = "D:/Users/21460/Pictures/wallpaper/2d6eb26d900a4631817007b08e7bf93e.jpg";
        img.alt = '全屏图片';
        
        // 通过 JS 设置全屏样式
        Object.assign(img.style, {
            width: '100vw',
            height: '100vh',
            objectFit: 'cover',
            position: 'fixed',
            top: '0',
            left: '0'
        });

        // 创建文字容器
        const textDiv = document.createElement('div');
        textDiv.className = 'center-text';
        textDiv.textContent = "Hello, World!";

        // 先插入文字再插入图片（保持文字在上层）
        document.body.appendChild(textDiv);
        img.onload = () => document.body.appendChild(img);
    </script>
</body>
</html>
~~~
把这个html文件放到系统的某个位置
![alt text](image-4.png)

然后改一下浏览器的起始页：
![alt text](image-6.png)
![alt text](image-5.png)

设置到此结束，再麻烦360锁定一下主页，除了你，谁都不能再动你的主页啦！

如果你JavaScript比较强得话，在这个页面上实现一些功能也未尝不可。
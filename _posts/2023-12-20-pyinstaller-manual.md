---
title: "Pyinstaller使用注意事项"
layout: post
date: 2023-12-20 10:23
tag: pyinstaller
headerImage: false
description: "Pyinstaller using notes"
category: blog
author: haibo

---

## 介绍

> 代码编写完成，如何在没有python环境的电脑上运行？如何把文件打包好，发给别人直接使用？其实最简单的办法就是把.py源文件，打包成可执行程序员exe文件，别人直接双击exe文件就可以运行了。  
> 
> python实现打包exe有很多方案，主要有py2exe、cxfreeze、PyInstaller三种，py2exe和cxfreeze的安装过程比较麻烦，且对高版本python支持不好，虽然pyinstaller打包后文件相对较大，但是其安装的简单性和易用性得到广大Python使用者的青睐。

## 安装

```bash
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```

## 使用

由于打包后的文件较大，建议创建虚拟环境后，安装必要的包之后再打包。

1. 在当前虚拟环境下，进入到项目的目录。
2. 使用如下命令打包主程序代码：

```bash
pyinstaller -F demo.py
```

3. 打包完成后，会出现build, dist两个文件夹以及.spec文件，把dist中的exe文件拖到与主程序同一个目录下即可。分享给他人时候，需要打包build文件夹以及.exe, .spec两个文件。

![files image][1]

## 可能出现的问题

### 问题一：\**\* Unable to access jarfile \*\* C:\Users\jaquedeveloper\AppData\Local\Temp_MEI58442\tabula\tabula-1.0.1-jar-with-dependencies.jar*

两种解决方案

1. **在打包完成的.spec文件中：**

```bash
# 在最上方加上
from PyInstaller.utils.hooks import collect_data_files

# 替换datas=[]
datas=collect_data_files("tabula")
```

最后，用如下代码重新打包：

```bash
PyInstaller your-app-name.spec
```

2. **在打包程序的时候，直接添加需要的文件，把路径修改为你的tabula包的实际路径**

```bash
pyinstaller --F --add-binary "D:\\anaconda\\envs\\pdf_extract\\Lib\\site-packages\\tabula\\tabula-1.0.5-jar-with-dependencies.jar;./tabula/" myapp.py
```

之后，你的.spec文件中的binaries会变为下面的样子：

```bash
binaries=[('D:\\anaconda\\envs\\pdf_extract\\Lib\\site-packages\\tabula\\tabula-1.0.5-jar-with-dependencies.jar', './tabula/')]
```

### 问题二：运行完exe程序后闪退，无法看到报错信息

打开cmd，进入到当前目录后，运行exe程序即可。

### 问题三：自己电脑上可以运行，分享给他人报错 *jpype._jvmfinder. JVMNotFoundException: No JVM sharedlibrary file (jvm.dll)*

![error image][2]

可能是由于打包的某些python包需要特定环境下才能运行，比如tabula，底层需要用到java环境。Pyinstaller无法打包java，需要用户下载java。

[1]: ../assets/images/post/pyinstaller_manual/files.jpg

[2]: ../assets/images/post/pyinstaller_manual/share_error.jpg
# Markdown 基本语法的学习

<a id="index"></a>
## 目录
<!-- MarkdownTOC -->

- [1 分级标题](#1-分级标题)
- [2 斜体和粗体](#2-斜体和粗体)
- [3 超链接](#3-超链接)
    - [3.1 行内式](#31-行内式)
    - [3.2 参考式](#32-参考式)
    - [3.3 自动链接](#33-自动链接)
- [4 锚点](#4-锚点)
- [5 列表](#5-列表)
    - [5.1 无序列表](#51-无序列表)
    - [5.2 有序列表](#52-有序列表)
    - [5.3 定义型列表](#53-定义型列表)
    - [5.4 任务列表](#54-任务列表)
    - [5.5 列表嵌套](#55-列表嵌套)
    - [5.6 列表缩进](#56-列表缩进)
        - [5.6.1 段落格式对齐](#561-段落格式对齐)
        - [5.6.2 多个段落在一个列表项中](#562-多个段落在一个列表项中)
    - [5.7 列表的一个错误生成情况](#57-列表的一个错误生成情况)
- [6 引用](#6-引用)
    - [6.1 一般引用](#61-一般引用)
    - [6.2 嵌套引用](#62-嵌套引用)
- [7 插入图像](#7-插入图像)
    - [7.1 行内式](#71-行内式)
    - [7.2 参考式](#72-参考式)
    - [7.3 插入图片方式](#73-插入图片方式)
        - [7.3.1 插入本地图片](#731-插入本地图片)
        - [7.3.2 插入网站图片](#732-插入网站图片)
        - [7.3.3 将图片插入到md文件中](#733-将图片插入到md文件中)
- [8 注脚](#8-注脚)
- [9 LaTeX 公式](#9-latex-公式)
    - [9.1 行内公式](#91-行内公式)
    - [9.2 整行公式](#92-整行公式)
- [10 表格](#10-表格)
- [11 分隔线](#11-分隔线)
- [代码](#代码)
    - [12.1 行内代码](#121-行内代码)
    - [12.2 多行代码](#122-多行代码)

<!-- /MarkdownTOC -->

<a id="1-分级标题"></a>
## 1 分级标题
分级标题共分六级，用1~6个 `#` 放在标题开头或者将标题夹在中间。
```
# 一级标题
## 二级标题
### 三级标题
#### 四级标题
##### 五级标题
###### 六级标题
```

<a id="2-斜体和粗体"></a>
## 2 斜体和粗体
代码：
```
*斜体* 或 _斜体_
**粗体**
***加粗斜体***
~~删除线~~
```
效果：  
*这是一段斜体文字*  
**这是一段粗体文字**  
***这是一段加粗倾斜文字***  
~~这是一段带删除线的文字~~

<a id="3-超链接"></a>
## 3 超链接
<a id="31-行内式"></a>
### 3.1 行内式
代码：`[链接文字](链接地址)`  
示例：[MK_Devil的GitHub主页](https://github.com/MKDevil)

<a id="32-参考式"></a>
### 3.2 参考式
格式：
>`[显示名称][位置标记(可选)]`  
>`[位置标记]:example.com "鼠标悬停的提示(可选)"`

代码：
```
常用的搜索引擎：[谷歌][0]，[百度][baidu]，[必应][]

[0]:https://www.google.com.hk "谷歌"
[baidu]:https://www.baidu.com "百度"
[必应]:https://cn.bing.com
```
效果：  
常用的搜索引擎：[谷歌][0]，[百度][baidu]，[必应][]

[0]:https://www.google.com.hk "谷歌"
[baidu]:https://www.baidu.com "百度"
[必应]:https://cn.bing.com

<a id="33-自动链接"></a>
### 3.3 自动链接
使用`<>`将网址或电子邮箱包起来即可  
代码：`<https://www.baidu.com>`  
效果：<https://www.baidu.com>

<a id="4-锚点"></a>
## 4 锚点
插入锚点：使用`{#标记}`插入锚点，需要在前方留一个空格  
<p><font color=red>注意：在GitHub的markdown语法（GFM）中无法使用</font></p>
使用锚点：`[显示名称](#锚点名称)`  
跳转到[目录](#index)

<a id="5-列表"></a>
## 5 列表
<a id="51-无序列表"></a>
### 5.1 无序列表
使用`*`，`+`，`-`表示无序列表，需要在后方留空格  
三种指示符可以混用，不影响最终效果

* 无序列表一
* 无序列表二
* 无序列表三

<a id="52-有序列表"></a>
### 5.2 有序列表
使用英文数字接一个英文句号，需要在后方留空格

1. 有序列表一
2. 有序列表二
3. 有序列表三

<a id="53-定义型列表"></a>
### 5.3 定义型列表
定义+解释，一行写定义，紧跟一行写解释，解释左边需要一个冒号和空格

Markdown
: 一种标记型语言，可以转换为HTML或者PDF

<a id="54-任务列表"></a>
### 5.4 任务列表
可以显示多选（无法修改选项）  
代码：
```
* [x] 选项一
* [ ] 选项二
* [x] 选项三
```
效果：

* [x] 选项一
* [ ] 选项二
* [x] 选项三

<a id="55-列表嵌套"></a>
### 5.5 列表嵌套
使用`tab`缩进  
代码：
```
* 第一章
    * 第一节
```
效果：

* 第一类
    - 第二类

<a id="56-列表缩进"></a>
### 5.6 列表缩进
<a id="561-段落格式对齐"></a>
#### 5.6.1 段落格式对齐
如果一个段落很长，可以通过将其转换为列表的方式进行对齐，效果如下

* Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。
* Markdown具有一系列衍生版本，用于扩展Markdown的功能（如表格、脚注、内嵌HTML等等），这些功能原初的Markdown尚不具备，它们能让Markdown转换成更多的格式。

<a id="562-多个段落在一个列表项中"></a>
#### 5.6.2 多个段落在一个列表项中
如果一个列表有多个段落，可以在后续段落缩进一个tab（或四个空格）将其转换为一个列表。  
代码：
```
* Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。

    Markdown具有一系列衍生版本，用于扩展Markdown的功能（如表格、脚注、内嵌HTML等等），这些功能原初的Markdown尚不具备，它们能让Markdown转换成更多的格式。

    以及很多东西。
```
效果：

* Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。

    Markdown具有一系列衍生版本，用于扩展Markdown的功能（如表格、脚注、内嵌HTML等等），这些功能原初的Markdown尚不具备，它们能让Markdown转换成更多的格式。

同样，我们可以实现列表与引用的类似缩进形式  
代码：
```
* 第一章

    > 第一章的段落一

    > 第一章的段落二

* 第二章

    > 第二章的段落一
    > 
    > 第二章的段落二
```
效果：

* 第一章

    > 第一章的段落一  
    > 第一章的段落二

* 第二章  

    > 第二章的段落一
    > 
    > 第二章的段落二

<a id="57-列表的一个错误生成情况"></a>
### 5.7 列表的一个错误生成情况
首行出现`数字+句点+空白`，会自动生成列表

代码：`2345. markdown`  
效果：  
2345. markdown

可以通过对句点加`\`来避免这个问题

代码：`2345\. markdown`  
效果：  
2345\. markdown

<a id="6-引用"></a>
## 6 引用
<a id="61-一般引用"></a>
### 6.1 一般引用
在被引用的文本前加上`>`即可  
代码：
```
> 第一行引用  
> 第二行引用  
> 第三行引用
```
效果：  
> 第一行引用  
> 第二行引用  
> 第三行引用

也可以只在第一行加`>`来实现
代码：
```
> 第一行引用  
第二行引用  
第三行引用
```
效果：  
> 第一行引用  
第二行引用  
第三行引用

<font color="FF0000" size="3">注意：上面的代码是用双空格回车进行换行的，否则会显示在同一行！</font>

<a id="62-嵌套引用"></a>
### 6.2 嵌套引用
类似于标题的格式，使用多个`>`可以实现多层引用
代码：
```
> 第一层引用
> > 第二层引用
```
效果：  
> 第一层引用
> > 第二层引用

<a id="7-插入图像"></a>
## 7 插入图像
<a id="71-行内式"></a>
### 7.1 行内式
代码：`![图片载入失败提示](图片URL "图片Title")`

效果：
![图片载入失败](https://www.baidu.com/img/baidu_jgylogo3.gif "百度")

<a id="72-参考式"></a>
### 7.2 参考式
代码：
```
![图片载入失败][baidulogo]

[baidulogo]: https://www.baidu.com/img/baidu_jgylogo3.gif "百度"
```
效果：
![图片载入失败][baidulogo]

[baidulogo]: https://www.baidu.com/img/baidu_jgylogo3.gif "百度"

<a id="73-插入图片方式"></a>
### 7.3 插入图片方式
<a id="731-插入本地图片"></a>
#### 7.3.1 插入本地图片
<a id="732-插入网站图片"></a>
#### 7.3.2 插入网站图片
<a id="733-将图片插入到md文件中"></a>
#### 7.3.3 将图片插入到md文件中
代码：`![图片载入失败提示](data:image/png;base64,iVBORw0......)`  
或者：
```
![图片载入失败提示][标记]

[标记]: data:image/png;base64,iVBORw0......
```
效果：  
![图片载入失败][b64IMG]

<a id="8-注脚"></a>
## 8 注脚
在需要添加注脚的文字后边加上`[^注脚名称]`  
脚注会自动被 Markdown 调整到文章最后  
脚注可以随意命名，在显示的时候，会自动按照数字顺序从1开始排列  
代码：
```
需要先取得建设用地规划许可证[^用地]，才可以办理建设工程规划许可证

[用地]: 建设用地规划许可证
```
效果：

需要先取得建设用地规划许可证[^用地]，才可以办理建设工程规划许可证

[^用地]: 建设用地规划许可证

<a id="9-latex-公式"></a>
## 9 LaTeX 公式
<a id="91-行内公式"></a>
### 9.1 行内公式
<a id="92-整行公式"></a>
### 9.2 整行公式
<font color="FF0000">注：公式暂时无法使用，具体原因未知</font>

<a id="10-表格"></a>
## 10 表格
对齐方式，用英文冒号，在第二行（分隔行）标注，左边为左对齐，右边为右对齐，两边都有为居中  
代码：
```
| nameeeeee | age | grade |
| :-        | :-: | -:    |
| Tom       | 12  | 84    |
| Mike      | 13  | 67    |
| Alice     | 12  | 77    |
```
效果：

| nameeeeee | age | grade |
| :-        | :-: | -:    |
| Tom       | 12  | 84    |
| Mike      | 13  | 67    |
| Alice     | 12  | 77    |

<a id="11-分隔线"></a>
## 11 分隔线
在一行中用三个以上的 `---`、`***` 或 `* * *`  
如果连续使用了 `n` 行分隔线，则实际显示的分隔线为 `n+1` 条  

效果：

---
***
* * *

<a id="代码"></a>
## 代码
<a id="121-行内代码"></a>
### 12.1 行内代码
使用倒引号 <code>`</code> 括起来
<a id="122-多行代码"></a>
### 12.2 多行代码
使用三个倒引号 <code>```</code> 括起来


<br><br><br><br>
<font size="4">
**注释：**
</font>
[b64IMG]: data:image/png;base64,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

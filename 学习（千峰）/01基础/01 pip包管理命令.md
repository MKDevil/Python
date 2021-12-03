<!--
 * @Author: MK_Devil
 * @Date: 2021-08-27 16:56:20
 * @LastEditTime: 2021-12-03 15:31:07
 * @LastEditors: MK_Devil
-->

# pip包管理命令

## 查看

`pip --version` 查看版本

`pip list` 查看包

`pip xxx --help` 查看xxx包的帮助文件

## 包管理

`pip install xxx==2.1.1` 安装2.1.1版本的xxx包

`pip install xxx -i URL` 从URL镜像源下载xxx包

> 默认从Python官方网站下载包，使用国内镜像源网址可以提高下载速度

修改镜像源：

在`user/用户名/pip/pip.ini`中修改镜像源网址

```ini
[global]
timeout=6000
index-url=https://pypi.tuna.tsinghua.edu.cn/simple
trust-host=pypi.tuna.tsinghua.edu.cn
```

`pip uninstall xxx` 卸载xxx包

`pip freeze > requirements.txt` `pip freeze -r xrequirements.txt` 获取安装的Python包到指定文件

`pip install -r requirements.txt` 安装指定文件列表中的包

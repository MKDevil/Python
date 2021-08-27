<!--
 * @Author: MK_Devil
 * @Date: 2021-08-27 16:56:20
 * @LastEditTime: 2021-08-27 17:37:32
 * @LastEditors: MK_Devil
-->

# pip包管理命令

## 查看

`pip --version` 查看版本

`pip list` 查看包

`pip xxx --help` 查看xxx包的帮助文件

## 包管理

`pip install xxx==2.1.1` 安装2.1.1版本的xxx包

`pip uninstall xxx` 卸载xxx包

`pip freeze > requirements.txt` `pip freeze -r xrequirements.txt` 获取安装的Python包到指定文件

`pip install -r requirements.txt` 安装指定文件列表中的包

# 面向对象 - OOP

## OOP 中的重要概念

* 实例创建 - 填充实例属性
* 行为方法 - 在类方法中封装逻辑
* 运算符重载 - 为打印这样的内置操作提供行为
* 定制行为 - 重新定义子类中的行为使其特殊化
* 定制构造函数 - 为超类步骤添加初始化逻辑

## 复合对象

不使用类的继承，而是把对象彼此嵌套组成**复合对象**

使用 `__getattr__` 进行运算符重载来实现

## 在 Python 3.0 中捕获内置属性

> 参照 `person.py` 中的 `Manager` 类（使用复合对象）

\_\_getattr__
: 从复合的类中，获取当前类中**没有定义过的属性**

\_\_getattribute__
: 从复合的类中，获取**所有属性**

在 Python 3.0 中，类中的运算符重载方法（如 `__str__`）无法使用 `__getattr__` 和 `__getattribute__` 获取

因此在定义的 `Manager` 类中，重新定义了 `__str__` 方法

## 内省工具 - 特殊类属性

内省工具允许编写以通用方式处理类的代码

原理如下

* 内置的 `instance.__class__` 属性提供了一个从实例到创建他的类的链接。类有一个 `__name__` 还有一个 `__bases__` 序列，链接到超类。
* 内置的 `object.__dict__` 提供了一个字典，带有一个键/值对，以便每个属性都附加到一个命名空间对象（模块、类、实例）

## 进阶方向

GUI
: 添加一个图形化的界面，使其对用户更加友好。使用 Python 自带的 tkinter，或者可移植到 WxPython 和 PyQt 这样的第三方工具 GUI

Web 站点
: 使用 Python 自带的 CGI 脚本编程工具来构建。也可以使用像 Django、TurboGears、Pylons、web2Py、Zope 或 Google's App Engine 等第三方 Web 开发框架来完成

Web 服务
: 通过像 SOAP 或 XML-RPC 这样的 Web 服务接口来调用 Python 自身或第三方开源域所支持的 API，这样的 API 以一种更加直接的形式返回数据，而不是嵌入一个回应页面的 HTML 中

数据库
: 将数据从 shelve 转移到像开源的 ZODB 面向对象数据库系统（OODB）这样的一个功能更完备的存储机制中。或者是像 MySQL、Oracle、PostgreSQL 或 SQLite 这样的一个更传统的基于 SQL 的数据库系统中。Python 自身带有一个内置的、正在使用的 SQLite 数据库

ORM
: 对象关系映射器（ORM），例如 SQLObject 和 SQLAlchemy，可以自动实现关系表和行与 Python 的类和实例之间的映射，这样一来，就可以使用常规的 Python 语法来处理存储的数据。

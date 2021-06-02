# Django 框架--首先安装Django 
#### pip install Django 
#### pip install django-simpleui

* 创建Django项目

        django-admin startproject HelloWorld 工程名 
    
* 创建appname应用

        python manage.py startapp appname

* 集成 simpleui UI框架（首先要安装 simpleui）

* INSTALLED_APPS = [
   * 'simpleui', //在这里添加 simpleui
   *  'django.contrib.admin',
   *  'django.contrib.auth',
    ....
]
* 使用sqlsite生成迁移文件

       python manage.py makemigrations
* 根据迁移文件去创建数据库表结构

        python manage.py migrate
* 后台管理,创建超级管理员      
        
        python manage.py createsuperuser      
* 目录说明：

    * HelloWorld: 项目的容器。
    * manage.py: 一个实用的命令行工具，可让你以各种方式与该 Django 项目进行交互。
    * HelloWorld/__init__.py: 一个空文件，告诉 Python 该目录是一个 Python 包。
    * HelloWorld/asgi.py: 一个 ASGI 兼容的 Web 服务器的入口，以便运行你的项目。
    * HelloWorld/settings.py: 该 Django 项目的设置/配置。
    * HelloWorld/urls.py: 该 Django 项目的 URL 声明; 一份由 Django 驱动的网站"目录"。
    * HelloWorld/wsgi.py: 一个 WSGI 兼容的 Web 服务器的入口，以便运行你的项目。
    
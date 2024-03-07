
1、克隆项目

```bash
git clone https://github.com/opscolin/django-examples.git
```

2、进入手机管理项目

```bash
cd django-examples/django_phone_management
```

3、查看目录结构

```bash
# tree .
.
├── ReadMe.md
├── cmdb
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── migrations
│   │   └── __init__.py
│   ├── models
│   │   ├── __init__.py
│   │   └── phone.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── django_phone_management
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

4 directories, 16 files
```

4、执行初始化

```python
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

5、启动服务

```python
python manage.py runserver 0.0.0.0:8090
```

然后浏览器访问 http://127.0.0.1:8090/admin 

6、具体的代码分析解释详见公众号 “菩提老鹰” 或者扫码关注 

![菩提老鹰](http://mp-weixin.colinspace.com/mpwechat/qrcode_for_gh_da4929fed8ed_258.jpg)


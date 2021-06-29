# findclassmate

#### 介绍
{}

#### 软件架构
front-end: vue
back-end: django
database: mysql

#### 安装教程

1.  (intall requirements) pip install -r requirements.txt
2.  

#### SQL download instru (can reference [https://www.jianshu.com/p/694d7d0a170b])
1. sudo apt install mysql-client-core-8.0     # version 8.0.25-0ubuntu0.20.04.1, or
    sudo apt install mariadb-client-core-10.3  # version 1:10.3.29-0ubuntu0.20.04.1
2. sudo apt-get install mysql-server
3. (create user for remote access) CREATE USER 'admin'@'%' IDENTIFIED BY '';
4. (set previlege) GRANT ALL privileges ON *.* TO 'admin'@'%' WITH GRANT OPTION;
    a. (change password) SET PASSWORD FOR 'username'@'host' = PASSWORD('newpassword');
    b. (delete user) DROP USER 'username'@'host';
5. flush privileges;
6. (if previous not working!!) 修改 /etc/percona-server.conf.d 目录下的 mysqld.cnf  文件 -> 注释掉 “bind 127.0.0.1” -> 去掉 “bind-address = 0.0.0.0” 这行的注释
最后重启mysql: service mysql restart

#### frontend setup
(basic set up in )  [https://auth0.com/blog/building-modern-applications-with-django-and-vuejs/]
(don't need this step) npm install --save axios

## 服务管理
# 启动
sudo service mysql start
# 停止
sudo service mysql stop
# 服务状态
sudo service mysql status

#### 使用说明

1.  all repeated subject will only choose and create the first one
2.  everytime put it into a new server, unquote some code in views.py to create local database
3.  xxxx

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)

# CAVA3
# CAVA3测试开发框架部署工程

# centos7 x86_64 安装方法
# 【备注】linux cava二进制程序需要根据不同发行版本编译，故不在此一一陈列，有需要单独联系

# 1.将以下内容复制到.sh文件中，账号密码需要修改成自己的，并重命名为cava_install_linux.sh
#!/bin/sh
mode_branch=centos7_x86_64
username="your username"
password="your password"
url="github.com/yezhibin/CAVA3.git"
cmd="git clone https://${username}:${password}@${url} ./CAVA3"

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] start install cava3. url is: ${url}"

${cmd}

ln -s /usr/local/bin/CAVA3/CAVA_SPACE3/src/cava
ln -s ./CAVA3/Python37/lib/python3.7/site-packages/robotframework-3.0.3-py3.7.egg/EGG-INFO/scripts/pybot
ln -s ./CAVA3/Python37/lib/python3.7/site-packages/pip/pip3
ln -s ./CAVA3/Python37/bin/python3.7 python3

chmod 755 -R CAVA3
cd ./CAVA3
git fetch "origin"
git branch -va
git stash
git checkout -b ${mode_branch} remotes/origin/${mode_branch}
git branch   
git pull

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] download files success."
time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] ${mode_branch} install cava3 success."


# 2.将cava_install_linux.sh放到linux /usr/local/bin下，添加执行权限，并执行sh cava_install_linux.sh，执行无报错即表示部署成功

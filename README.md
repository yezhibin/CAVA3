# CAVA3
# CAVA3测试开发框架部署工程

CAVA3框架，是基于python3+robot framework二次开发，支持多任务并发、跨平台运行、周期重复执行的自动化测试用例框架，
同时也是一套集成了Python3.7+pyqt4等的python开发环境。

Windows(64位系统)环境部署请切换到master分支，centos7 x86_64环境请切换到centos7_x86_64分支，
在对应的README.ME指导下，git clone部署工程到执行机上，其余系统环境暂时未适配。

CAVA3在环境上通过脚本自动部署完成后，在windows cmd或者linux shell终端下输入cava -h可以看到框架命令行参数的使用帮助。
**备注：**Linux下可能需要在/etc/profile中手动设置相应环境变量，参考如下：

export LD_LIBRARY_PATH=/usr/local/lib:/usr/local/bin:$LD_LIBRARY_PATH
export PATH=/usr/local/lib:/usr/local/bin:$PATH

然后在shell中执行source /etc/profile，使环境变量生效。

# centos7 x86_64 安装方法
# 【备注】linux cava二进制程序需要根据不同发行版本编译，故不在此一一陈列，有需要单独联系

# 1.将以下内容复制到.sh文件中，账号密码需要修改成自己的，并重命名为cava_install_linux.sh
#!/bin/sh
mode_branch=centos7_x86_64
username="yourname"
password="your password"
url="gitee.com/zoudaohoutian/CAVA3.git"
cmd="git clone https://${username}:${password}@${url} ./CAVA3"

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] start install cava3. url is: ${url}"

${cmd}

ln -s /usr/local/bin/CAVA3/CAVA_SPACE3/src/cava
ln -s ./CAVA3/Python37/lib/python3.7/site-packages/robotframework-3.0.3-py3.7.egg/EGG-INFO/scripts/pybot
ln -s ./CAVA3/Python37/lib/python3.7/site-packages/pip/pip3
ln -s ./CAVA3/Python37/bin/python3.7 python3

cd ./CAVA3
git fetch "origin"
git branch -va
git stash
git checkout -b ${mode_branch} remotes/origin/${mode_branch}
git branch   
git pull

cd ..
chmod 755 -R CAVA3

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] download files success."
time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] ${mode_branch} install cava3 success."


# 2.将cava_install_linux.sh放到linux /usr/local/bin下，添加执行权限，并执行sh cava_install_linux.sh，执行无报错即表示部署成功

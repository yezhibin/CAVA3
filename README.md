# CAVA3
# CAVA3测试开发框架部署工程

# 1.将以下内容复制到.sh文件中，账号密码需要修改成自己的，并重命名为cava_install_ext.sh
#!/bin/sh
mode=$1
username="your name"
password="your password"
url="github.com/yezhibin/CAVA3.git"
cmd="git clone https://${username}:${password}@${url} d:/CAVA3"


time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] start install cava3. url is: ${url}"

#windows批处理设置环境变量
if [ ! $mode ]; then
	./env_var.bat
	time=$(date "+%Y-%m-%d %H:%M:%S")
	echo "[${time}][info] set env success."
fi

${cmd}
cd d:/CAVA3
git fetch "origin"
git branch -va
git branch
git pull

cp  -rf /d/CAVA3/CAVA_SPACE3/src/tools/RIDE.lnk ~/Desktop

time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] download files success."
time=$(date "+%Y-%m-%d %H:%M:%S")
echo "[${time}][info] install cava3 success."

# 2.将以下内容复制到.bat文件中，并重命名为env_var.bat
%1 start "" mshta vbscript:CreateObject("Shell.Application").ShellExecute("cmd.exe","/c %~s0 ::","","runas",1)(window.close)&&exit
setx path "D:\CAVA3\Python37;D:\CAVA3\Python37\Scripts;D:\CAVA3\CAVA_SPACE3\src\libs;D:\CAVA3\Python37\Lib\site-packages\PyQt4;%path%" /m
setx PYTHONPATH "D:\CAVA3\CAVA_SPACE3\src" /m
pause

# 3.将cava_install_ext.sh、env_var.bat放到统一目录下，并用git bash执行 sh ./cava_install_ext.sh，执行无报错即表示部署成功
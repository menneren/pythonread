### python的pip库安装

网址：https://pypi.org/project/pip/

python3.10 get-pip.py install

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py   # 下载安装脚本
sudo python3.10 get-pip.py    # 运行安装脚本
```

```
pip install pyautogui
```

**显示版本和路径**

```
pip --version
```

**获取帮助**

```
pip --help
```

**升级 pip**

```
pip install -U pip
```

> ```
> pip install --upgrade SomePackage
> ```
>
> 升级指定的包，通过使用==, >=, <=, >, < 来指定一个版本号。
>
> **卸载包**
>
> ```
> pip uninstall SomePackage
> ```
>
> **搜索包**
>
> ```
> pip search SomePackage
> ```
>
> **显示安装包信息**
>
> ```
> pip show 
> ```
>
> **查看指定包的详细信息**
>
> ```
> pip show -f SomePackage
> ```
>
> **列出已安装的包**
>
> ```
> pip list
> ```
>
> **查看可升级的包**
>
> ```
> pip list -o
> ```
>
> ### 

**卸载包**

```
pip uninstall SomePackage
```

①卸载PIP的命令：python -m pip uninstall pip

②重装PIP的命令：easy_inatall pip

### 解决问题

pip install  -i https://pypi.doubanio.com/simple/  --trusted-host pypi.doubanio.com    --target=/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages    urllib3

### 问题1

Requirement already satisfied: pyobjc-framework-CoreWLAN==8.5 in /Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages (from pyobjc->pyautogui) (8.5)

切换到python/site-packages目录                                     pip install --taget=h:\users\29187\appdata\local\programs\python\python37\lib\site-packages requests

pip install --taget=/Library/Frameworks/Python.framework/Versions/3.10/lib/python3.10/site-packages requests

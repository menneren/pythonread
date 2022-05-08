## git文件上传

### ...或在命令行上创建一个新的存储库

```
echo "# python" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/menneren/python.git
git push -u origin main
```

***…或从命令行推送现有的存储库\***

```
git remote add origin https://github.com/menneren/python.git
git branch -M main
git push -u origin main
```

*** …或从其他存储库导入代码\***

```
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.
```



 
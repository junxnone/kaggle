---
Title | Download Kaggle Dataset
-- | --
Create Date | `2019-11-06T02:01:58Z`
Update Date | `2021-11-16T16:53:07Z`
Edit link | [here](https://github.com/junxnone/kaggle/issues/5)

---
1. 从web页面点击下载
2. 通过kaggle 命令行下载
3. 也可以在google colab 中使用 kaggle 命令行下载，**速度贼快**

# kaggle 命令行下载
1. 在虚拟环境中安装kaggle
```
pip3 install kaggle
```
2. 如果有代理，设置代理
```
kaggle config set -n proxy -v  your_proxy
```
3. 去My Count 页面下create NEW API Token
![image](https://user-images.githubusercontent.com/2216970/68261850-50d06200-007c-11ea-9acd-e5e3da5b23d2.png)

4. 把得到的kaggle.json 放在linux 下~/.kaggle下

5. copy命令到命令行，开始下载数据
![image](https://user-images.githubusercontent.com/2216970/68261892-70678a80-007c-11ea-984b-f37af43cebb4.png)


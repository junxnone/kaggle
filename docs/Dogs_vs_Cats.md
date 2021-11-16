---
Title | Dogs vs Cats
-- | --
Create Date | `2019-07-02T07:24:08Z`
Update Date | `2021-11-16T14:14:00Z`
Edit link | [here](https://github.com/junxnone/kaggle/issues/4)

---
## Reference
- [~~Dogs vs. Cats~~ 此版本不可提交](https://www.kaggle.com/c/dogs-vs-cats/)
- [Dogs vs. Cats Redux: Kernels Edition](https://www.kaggle.com/c/dogs-vs-cats-redux-kernels-edition)
- [手把手教你如何在Kaggle猫狗大战冲到Top2%](https://ypw.io/dogs-vs-cats-2/#more)

## Brief

### Data & Label

- Data

```
../input
└── dogs-vs-cats
    ├── test1
    │   └── test1 - 12500
    └── train
        └── train - 25000 
           └── cat images 12500
           └── dog images 12500
```

- Label

```
cat = 0
dog = 1
```

## Score
![image](https://user-images.githubusercontent.com/2216970/68277561-69577100-00aa-11ea-82da-a025b2d164de.png)

- n is the number of images in the test set
- ŷ i is the predicted probability of the image being a dog
- yi is 1 if the image is a dog, 0 if cat
- log() is the natural (base e) logarithm


## Submission File
label 为 图片为dog的概率

```
id,label
1,0.5
2,0.5
3,0.5
....
```



## Tricks
- 将每个预测值限制到 [0.005, 0.995] 个区间内
>  LogLoss，对于预测正确的样本，0.995 和 1 相差无几，但是对于预测错误的样本，0.005 和 0.00001 的差距非常大，是 5和 12 的差别

![image](https://user-images.githubusercontent.com/2216970/69119261-f64df180-0ad0-11ea-9b0a-1f6b3fdb160d.png)


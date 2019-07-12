# 钉钉群机器人提醒

### 1.创建钉钉群机器人

**添加群机器人，获取机器人的webhook，记录下来**

### 2.注册图灵机器人  
[图灵机器人](http://www.tuling123.com)

- 创建机器人
- 点击机器人获取apikey

### 3.修改脚本
替换remind.py中12行钉钉的webhook为步骤1获取的，21行的apikey为步骤2获取到

### 4.计划任务
写个定时计划任务分别对应上班跟下班

```
crontab -e
50 8 * * * python remind.py 0
50 17 * * * python remind.py 1
```

### 5.显示效果

![](images/1.png)  
**上班显示今天的天气预报，下班显示明天的天气预报**

### 后序
图灵机器人知识库种类奇多，完全可以定制各种不同的信息发送，例如菜谱群、星座运势群等等，钉钉机器人发送模式众多，可以根据[开发文档](https://open-doc.dingtalk.com/microapp/serverapi2/qf2nxq)自己考核
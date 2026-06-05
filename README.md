# HDU 我爱记单词 · 自动答题脚本
✨ 完美模拟手机端 + 自动识别题目 + AI 秒出答案 + 自动点击 + 全程无人值守 ✨

## 功能介绍
- 自动登录杭电智慧校园
- 自动进入英语答题页面
- 完整读取题目与 A/B/C/D 选项
- AI 自动给出正确答案
- 自动点击选项、自动跳题
- 100% 伪装手机端，不被检测为电脑

## 使用方法
1. 安装依赖：
2. pip install playwright requests -i https://pypi.tuna.tsinghua.edu.cn/simple
   playwright install chrome
3. 修改以下配置:
- username = "你的HDU账号"
- password = "你的HDU密码"

- API_KEY = "YOUR API_KEY"
4.
- DeepSeek Key 获取教程
- 打开 DeepSeek 开放平台官网注册账号：https://platform.deepseek.com/
- 个人中心→API Keys→创建密钥，复制密钥粘贴到代码API_KEY；新用户赠送免费额度，足够日常刷题。
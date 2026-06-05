from playwright.sync_api import sync_playwright
import re
import requests

username = "你的HDU账号"
password = "你的HDU密码"

API_KEY = "YOUR API_KEY"
API_URL = "https://api.deepseek.com/v1/chat/completions"

# 手机 UA（iPhone 15 Safari）
MOBILE_UA = (
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) "
    "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1"
)

def get_answer(question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{
            "role": "user",
            "content": f"英语选择题，只返回答案字母A/B/C/D，不要多余文字：{question}"
        }],
        "temperature": 0.1
    }
    try:
        res = requests.post(API_URL, headers=headers, json=data, timeout=10).json()
        ans = res["choices"][0]["message"]["content"].strip().upper()
        return ans[0] if ans and ans[0] in "ABCD" else "A"
    except:
        return "A"

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            user_agent=MOBILE_UA,
            viewport={"width": 390, "height": 844},
            is_mobile=True,
            has_touch=True,
            device_scale_factor=3
        )
        page = context.new_page()

        page.goto("https://skl.hdu.edu.cn")
        print("="*60)
        print("👉 请手动登录 → 进入英语答题页面")
        print("="*60)

        page.wait_for_timeout(2000)
        page.get_by_placeholder("请输入学工号/绑定手机/证件号").fill(username)
        page.get_by_placeholder("请输入密码").fill(password)
        print("请点击登录")

        page.wait_for_selector("text='自动下一题'", timeout=0)
        print("✅ 检测到答题页面，开始脚本！")

        for _ in range(200):
            page.wait_for_timeout(1500)
            # ===================== ✅ 100%完整读题，绝不丢D =====================
            current_text = page.inner_text("body")
            current_question = current_text

            match = re.search(r'QUESTION\s*(\d+)', current_text)
            real_num = match.group(1) if match else "?"

            print(f"\n===== 第 {real_num} 题 =====")
            print("📝 完整题目已读取")

            ans = get_answer(current_question)
            print(f"AI答案:{ans}")

            try:
                page.get_by_text(ans, exact=True).click(timeout=1500)
                print("✅ 点击成功！")
            except:
                page.get_by_text("A").click()
                print("⚠️ 随机点击")

        browser.close()

if __name__ == "__main__":
    main()
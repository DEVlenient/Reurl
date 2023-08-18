import requests
import tkinter as tk
from tkinter import messagebox
import pyperclip

def shorten_url():
    url_to_shorten = entry_url.get()

    headers = {
        "Content-Type": "application/json",
        "reurl-api-key": api_key
    }

    payload = {
        "url": url_to_shorten,
        "utm_source": "FB_AD"
    }

    response = requests.post(api_endpoint, json=payload, headers=headers)
    data = response.json()

    if data.get("res") == "success":
        short_url = data["short_url"]
        original_url = data["original_url"]
        result_text.config(state=tk.NORMAL)
        result_text.delete("1.0", tk.END)  # 清空文字框
        result_text.insert(tk.END, f"縮短後的URL: {short_url}\n原始URL: {original_url}")
        result_text.config(state=tk.DISABLED)
        copy_button.config(state=tk.NORMAL)  # 啟用複製按鈕
    else:
        failure_msg = data["msg"]
        messagebox.showerror("縮短URL失敗", f"錯誤訊息: {failure_msg}")
        copy_button.config(state=tk.DISABLED)  # 停用複製按鈕

def copy_short_url():
    short_url = result_text.get("1.0", "1.0 lineend").split(": ")[1]
    pyperclip.copy(short_url)
    messagebox.showinfo("已複製", "已複製縮短後的URL到剪貼板")

api_endpoint = "https://api.reurl.cc/shorten"
api_key = "替換為自己的API" # https://reurl.cc/dev/main/tw

# 建立GUI介面
root = tk.Tk()
root.title("URL縮短工具")
root.geometry("600x400")  # 設定視窗大小

# 輸入框
entry_url = tk.Entry(root, width=60)
entry_url.pack(pady=10)

# 縮短按鈕
shorten_button = tk.Button(root, text="縮短URL", command=shorten_url)
shorten_button.pack()

# 顯示結果的文字框
result_text = tk.Text(root, wrap=tk.WORD, height=8, state=tk.DISABLED)
result_text.pack(pady=10)

# 複製按鈕
copy_button = tk.Button(root, text="複製縮短後的URL", command=copy_short_url, state=tk.DISABLED)
copy_button.pack()

root.mainloop()
# URL縮短工具

這是一個使用 Python 和 Tkinter 創建的簡單的URL縮短工具，可以通過 API 縮短輸入的網址。

## 使用方法

1. 輸入您想要縮短的網址到輸入框中。
2. 點擊「縮短URL」按鈕，工具將會使用 API 縮短網址。
3. 如果成功縮短網址，您將會在文字框中看到縮短後的URL和原始URL。
4. 點擊「複製縮短後的URL」按鈕，將縮短後的URL複製到剪貼板。

## 範例演示

<img src="pic/url.gif" alt="示例圖片" width="600">

## 安裝和運行

1. 安裝所需的 Python 庫：在命令行中執行以下命令
    ```
    pip install requests
    ```
    ```
    pip install pyperclip
    ```

2. 執行程式：在命令行中執行以下命令
    ```
    python reurl.py
    ```

3. 輸入網址，點擊「縮短URL」按鈕，即可看到 `縮短後的URL` 和 `原始URL`，以及 `複製縮短後的URL` 的選項。

## API 金鑰

請確保您在程式中設置了正確的 API 金鑰，以便使用 API 縮短網址。將 `api_key` 替換為您的 API 金鑰。

## 授權訊息

這個程式遵循 [MIT 授權](LICENSE.txt)，您可以自由地使用、修改和分享這個程式。

## 注意事項

- 本工具使用了 `requests` 和 `pyperclip` Python 庫，請確保您已安裝這些庫。
- 網址縮短服務的可用性可能受限，請確保 API 端點正常運行。
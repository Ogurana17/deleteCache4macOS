# deleteCache4macOS

macOSのキャッシュファイルを削除します。

## 使い方

動作にはpython3以降が必要です。

```brew
brew install python
```

[こちら](https://github.com/Ogurana17/deleteCache4macOS/archive/refs/heads/main.zip)から本体をダウンロード。
下記で必要なパッケージをインストール。

```pip
pip install -r requirements.txt
```

## 自動実行

macOSにあるcrontabを利用します。
ターミナルを開きます。

```crontab
crontab -e
```

下記は毎日4時間毎に実行する設定。（例:00:01, 04:01, ... 22:01）
詳細はcron式で調べてください。

```crontab_add
1 */4 * * * /usr/local/bin/python3 "xxx/deleteCache.py"> "xxx/deleteCache.log"
```

# TODOs

目前進度
---

### 用戶加入
- [x] 已可以辨識用戶訊息
- [ ] 加入好友圖文選單
    - [x] 功能
    - [ ] 背景圖片
- [ ] 帳號頭貼、背景圖
- [ ] 帳號貼文設定

### 訊息相關
- [x] 確認可以收到用戶文字訊息
- [x] 確認可以收到用戶照片訊息
- [x] 確認可以收到用戶影片訊息
- [x] 確認可以收到用戶聲音訊息

### 引入模型
- [ ] 資料預處理
- [ ] 模型使用
- [ ] 存取辨識成果

### 機器人劇本
- [ ] 用戶訊息劇本編寫
    - [x] 歡迎訊息
    - [x] 如何讓怪獸增長
    - [ ] 關於我們資訊
    - [ ] 資訊整合

### 怪獸集點系統
- [ ] 創建怪獸角色
  - [ ] 輸入名稱
- [ ] 集點卡實作

Unknown, Error Handler
---
### UnknownHandler
- [x] `handle_unknown_text_message`
- [x] `handle_unknown_image_message`
- [x] `handle_unknown_video_message`
- [x] `handle_unknown_audio_message`
### ErrorHandler

圖文選單
---
### Check Rank
- [x] `handle_check_rank_welcome_message`

### About Us
- [x] `handle_about_us_welcome_message`
  - [x] `handle_about_us_ho_message`
  - [x] `handle_about_us_chou_message`
  - [x] `handle_about_us_yeh_message`
  - [x] `handle_about_us_huang_message`
  - [x] `handle_about_us_aaron_message` 

DEBUG USED (Optional)
---
- [ ] `linebot.v3` version `run.py`
- [x] Receive text, video, audio type message
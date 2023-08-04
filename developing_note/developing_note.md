# Developing Note


Data File Structure
---
```
data/
├── bottle/
│   ├── bottle_front/
│   ├── bottle_up/
│   ├── bottle_down/
│   ├── bottle_flatten_front/
│   ├── bottle_flatten_side/
│   ├── bottle_flatten_up/
│   └── bottle_flatten_down/
├── cup/
│   ├── cup_front/
│   ├── cup_up/
│   ├── cup_down/
│   ├── cup_flatten_front/
│   ├── cup_flatten_side/
│   ├── cup_flatten_up/
│   └── cup_flatten_down/
├── aluminum/
|   ├── aluminum_front/
|   ├── aluminum_side/
|   ├── aluminum_up/
|   ├── aluminum_down/
|   ├── aluminum_flatten_front/
|   ├── aluminum_flatten_side/
|   ├── aluminum_flatten_up/
|   └── aluminum_flatten_down/
└── ...
```

`Drama.py`
---

### `class AboutUsDrama`

```python
class AboutUsDrama:
    
    def __init__(self, line_bot_api: LineBotApi, handler: WebhookHandler):
        self.LINE_BOT_API = line_bot_api
        self.HANDLER = handler

    def handle_about_us_test(self, event: MessageEvent) -> None:

    def handle_about_us_welcome_message(self, event: MessageEvent) -> None:

    def handle_about_us_ho_message(self, event: MessageEvent) -> None:

    def handle_about_us_chou_message(self, event: MessageEvent) -> None:

    def handle_about_us_yeh_message(self, event: MessageEvent) -> None:

    def handle_about_us_huang_message(self, event: MessageEvent) -> None:
        
    def handle_about_us_aaron_message(self, event: MessageEvent) -> None:
```
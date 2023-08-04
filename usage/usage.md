# Enviroment Usage

Create Virtual Environment
---
With pip vertial environment: python request: `3.9.6`

### For Linux/MacOS
```shell
$ pip3 install virtualenv
$ virtualenv venv --python=python3.9.6
$ source venv/bin/activate
$ pip install -r requirements.txt
$ deactivate
$ rm -rf venv     # remove the venv
```

### For Windows
```shell
$ pip install virtualenv
$ virtualenv venv
$ venv\Scripts\activate
$ pip install -r requirements.txt
$ deactivate
$ rmdir /s venv     # remove the venv
```

Add LINE BOT Developer Config
---
You should duplicate the file `config/linebot_template.conf` and rename into `config/linebot.conf`

```js
{
    "CHANNEL_ACCESS_TOKEN": "YOUR_CHANNEL_ACCESS_TOKEN",    // LINE BOT API
    "CHANNEL_SECRET": "YOUR_CHANNEL_SECRET"                 // LINE BOT Handler
}
```


### With ngrok free server

```SHELL
$ brew install ngrok --cask
$ ngrok config add-authtoken YOUR_TOKEN
$ python run.py
$ ngrok http 5002
```

### Start multiple tunnel

```bash
$ ngrok config check
Valid configuration file at YOUR_PATH/ngrok/ngrok.yml
```

### Setting your `ngrok` token

Add the below code in `YOUR_PATH/ngrok/ngrok.yml`

```yml
version: "2"
authtoken: "YOUR_TOKEN"
# Please avoid making any changes to the content provided below
tunnels:
  first:
    addr: 5002
    proto: http    
  second:
    addr: 5012
    proto: http
```

type `ngrok start --all` in terminal to start `ngrok`

Build docs website
---

```shell
$ mkdocs build
$ mkdocs serve
```
Workflow permissions
- [x] Read and Write Permissions

Project Structure
---
```
PROJECT_ROOT
├── test/
│   ├── test_main.py/
│   ├──   :
│   └──   :
├── Monster/
│   ├── Drama.py
│   ├── Utils.py
│   └──   :
├── config/
│   ├── linebot.conf
│   ├── chatgpt.conf
│   └──   :
├── log/
│   ├── date/
│   └──   :
├── run.py
├── LICENSE
└── README.md
```

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
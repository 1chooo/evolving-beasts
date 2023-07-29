from pyimgur import Imgur
import os
import json

try:
    config_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'config')
    config_path = os.path.join(config_dir, 'imgur.conf')
    imgur_config = json.load(open(config_path, 'r', encoding='utf8'))

    imgur_client = Imgur(imgur_config["client_id"], imgur_config["client_secret"])
    image_path = os.path.abspath(
        os.path.join(
            "..", "log", "20230729", "imgs", "20230729_466039808469762614.jpg"
        )
    )
    uploaded_image = imgur_client.upload_image(
        image_path, 
        title="Uploaded with PyImgur"
    )

    print(uploaded_image.title)
    print(uploaded_image.link)
    print(uploaded_image.size)
    print(uploaded_image.type)

except Exception as e:
    print(f"Error: {e}")
    print(f"Current working directory: {os.getcwd()}")

# -*- coding:utf-8 -*-

from liffpy import (
    LineFrontendFramework as LIFF,
    ErrorResponse
)

LIFF_SITE = 'https://weather-shakespeare.github.io/'

def main():
    liff_api = LIFF("YOUR_CHANNEL_ACCESS_TOKEN")

    try:
        # If you want to add LIFF app
        liff_id = liff_api.add(
            view_type="compact",
            view_url=f"https://{LIFF_SITE}")
            # 400 Error or 401 Error
        try:
            # If you want to update LIFF app
            liff_api.update(liff_id, 
            view_type="full",
            view_url=f"https://{LIFF_SITE}")
        except ErrorResponse as err:
            # 401 Error or 404 Error
            print(err.message)
            return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

    try:
        # If you want to get all LIFF apps
        apps_info = liff_api.get()
        for app_info in apps_info:
            try:
                # If you want to delete LIFF app
                liff_api.delete(app_info["liffId"])
            except ErrorResponse as err:
                # 401 Error or 404 Error
                print(err.message)
                return 
    except ErrorResponse as err:
        # 401 Error or 404 Error
        print(err.message)
        return 

if __name__ == '__main__':
    main()
import subprocess
import webbrowser
import time

def get_current_ssid():
    # 使用 subprocess 调用 netsh 命令来获取当前连接的 SSID
    result = subprocess.run(['netsh', 'wlan', 'show', 'interfaces'], capture_output=True, text=True)
    output = result.stdout

    # 查找包含 "SSID" 的行并返回对应的 SSID
    for line in output.splitlines():
        if "SSID" in line:
            ssid = line.split(":")[1].strip()
            return ssid
    return None

def switch_wifi(target_ssid):
    # 使用 netsh wlan connect 来切换到指定的网络
    print(f"正在切换到 Wi-Fi 网络: {target_ssid}")
    subprocess.run(['netsh', 'wlan', 'connect', 'name=' + target_ssid])

    # 如果切换到 RD-TEST_5G_02，自动打开网页
    if target_ssid == "RD-TEST_5G_02":
        print("切换到 RD-TEST_5G_02，正在打开网页...")
        time.sleep(1)  # 等待网络连接完成
        webbrowser.open("https://10.10.133.253/UniExServices/user/toLogin.html")

def main():
    # 获取当前连接的 SSID
    current_ssid = get_current_ssid()

    if current_ssid is None:
        print("没有连接到任何 Wi-Fi 网络，默认切换到 POCO F5 Pro")
        switch_wifi("POCO F5 Pro")
        return

    print(f"当前连接的网络是: {current_ssid}")

    # 根据当前的 SSID 判断并切换网络
    if current_ssid == "POCO F5 Pro":
        print("当前网络是 POCO F5 Pro，切换到 RD-TEST_5G_02")
        switch_wifi("RD-TEST_5G_02")
    elif current_ssid == "RD-TEST_5G_02":
        print("当前网络是 RD-TEST_5G_02，切换到 POCO F5 Pro")
        switch_wifi("POCO F5 Pro")
    else:
        print("当前网络不是 POCO F5 Pro 或 RD-TEST_5G_02，切换到 POCO F5 Pro")
        switch_wifi("POCO F5 Pro")

if __name__ == "__main__":
    main()

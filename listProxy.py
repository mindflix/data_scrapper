from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import DesiredCapabilities
from selenium.webdriver.common.proxy import Proxy, ProxyType

import time

chromedriver = "./env/bin/chromedriver"

co = webdriver.ChromeOptions()
co.add_argument("log-level=3")
co.add_argument("--headless")


def get_proxies(co=co):
    driver = webdriver.Chrome(executable_path=chromedriver, options=co)
    driver.get("https://free-proxy-list.net/")
    PROXIES = []

    while len(PROXIES) < 100:
        proxies = driver.find_elements(By.CSS_SELECTOR, "tr[role='row']")
        for p in proxies:
            result = p.text.split(" ")

            if result[-1] == "yes":
                PROXIES.append(result[0] + ":" + result[1])

        driver.find_element(By.LINK_TEXT, "Next").click()
    driver.close()

    with open("proxies.txt", "w") as file:
        for ele in PROXIES:
            file.write(ele + "\n")
        file.close()

    return PROXIES


ALL_PROXIES = get_proxies()


def proxy_driver(PROXIES, co=co):
    prox = Proxy()

    if len(PROXIES) < 1:
        print("--- Proxies used up (%s)" % len(PROXIES))
        PROXIES = get_proxies()

    pxy = PROXIES[-1]

    prox.proxy_type = ProxyType.MANUAL
    prox.http_proxy = pxy
    prox.ssl_proxy = pxy

    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)

    driver = webdriver.Chrome(
        executable_path=chromedriver,
        options=co,
        desired_capabilities=capabilities,
    )

    return driver


# --- YOU ONLY NEED TO CARE FROM THIS LINE ---
# creating new driver to use proxy
pd = proxy_driver(ALL_PROXIES)

# code must be in a while loop with a try to keep trying with different proxies
running = True

while running:
    try:
        pass

        # you
    except:
        new = ALL_PROXIES.pop()

        # reassign driver if fail to switch proxy
        pd = proxy_driver(ALL_PROXIES)
        print("--- Switched proxy to: %s" % new)
        time.sleep(1)
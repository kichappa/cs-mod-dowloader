import asyncio
import json
from urllib.parse import parse_qs, urlsplit

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


async def get_dowload_link(item_id):
    try:
        # Send a GET request to the collection URL and retrieve the HTML source code
        url = "https://smods.ru/?s={}&app=255710".format(item_id)
        # Create a new instance of the Firefox driver
        print("approaching url, ", url)
        await asyncio.sleep(0)
        # driver = webdriver.Firefox()
        # driver.get(url)
        response = requests.get(url)
        print("received response for ", item_id)
        await asyncio.sleep(0)
        html_content = response.content

        # Use Beautiful Soup to parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Find the div with class "post-inner"
        post_inner_div = soup.find("div", {"class": "post-inner"})

        # Find the anchor with class "skymods-excerpt-btn" that is a grandchild of the div
        skymods_anchor = post_inner_div.find("a", {"class": "skymods-excerpt-btn"})

        # Extract the href from the anchor
        href = skymods_anchor["href"]

        print("Got one link, ", href)
        await asyncio.sleep(0)
        return href
    except Exception as e:
        print('Except "{}" occurred in {} with url, {}'.format(e, item_id, url))
        return ""


async def get_dowload_links(item_ids):
    tasks = [get_dowload_link(i) for i in item_ids]
    results = await asyncio.gather(*tasks)
    return results


def openSteamLinks(fileLocation):
    # open links from links.txt
    with open(fileLocation, "r") as file:
        # Read the contents of the file
        lines = file.readlines()

    # Create an empty list to store the URLs
    urls = []

    # Iterate through the lines of the file
    for line in lines:
        # Remove any whitespace from the line
        line = line.strip()
        # Add the URL to the list
        urls.append(line)
    print(urls)

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    links = []
    item_ids = []
    # For each link, navigate to the website
    for url in urls:

        # Send a GET request to the collection URL and retrieve the HTML source code
        response = requests.get(url)
        html_content = response.content

        # Use Beautiful Soup to parse the HTML source code
        soup = BeautifulSoup(html_content, "html.parser")
        collection = soup.find("div", {"class": "collectionChildren"})

        # print(collection.find_all("div", {"class": "workshopItem"}))

        # Extract the item ids from the HTML source code
        item_ids.extend(
            [
                parse_qs(urlsplit(a["href"]).query).get("id")[0]
                for div in collection.find_all("div", {"class": "workshopItem"})
                for a in div.find_all("a")
            ]
        )
        driver.get(url)

        # input()

    print(item_ids)
    links.extend(asyncio.run(get_dowload_links(item_ids)))
    print(links, sep="\n")

    return links


async def downloadLink(link):
    try:
        if link == "":
            return True
        # Send a GET request to the collection URL and retrieve the HTML source code
        # Use Selenium to open a web browser and navigate to the website
        driver = webdriver.Firefox()
        driver.get(link)

        # Find the button element and click it
        button = driver.find_element_by_id("method_free")
        button.click()

        # Wait for the new page to load
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.ID, "downloadbtn")))

        # Find the button element and click it
        button = driver.find_element_by_id("downloadbtn")
        button.click()
        return True
    except Exception as e:
        print("Error occurred while downloading, {}".format(e))
        return False


async def downloadLinks(links):
    tasks = [downloadLink(i) for i in links]
    results = await asyncio.gather(*tasks)
    return results


links = openSteamLinks("links.txt")
with open("download.txt", "w") as file:
    # Read the contents of the file
    file.write(json.dumps(links))

# open links from download.txt
# with open("download.txt", "r") as file:
#     # Read the contents of the file
#     links = json.loads(file.read())

i = 0
for link in links:
    i += 1
    print(i, "\t", link)

# for link in links:
#     if link == "":
#         break
#     # Use Selenium to open a web browser and navigate to the website
#     options = webdriver.FirefoxOptions()
#     # options.headless = True
#     driver = webdriver.Firefox(options=options)
#     driver.get(link)

#     # Find the button element and click it
#     button = driver.find_element(By.ID, "method_free")
#     button.click()
#     print("Clicked once")

#     try:
#         # Wait for the new page to load
#         wait = WebDriverWait(driver, 30)
#         wait.until(EC.presence_of_element_located((By.ID, "downloadbtn")))
#     except Exception as e:
#         print(e)
#         with open("logs.html", "w") as file:
#             file.write(driver.page_source)

#     # Find the button element and click it
#     button = driver.find_element(By.ID, "downloadbtn")
#     print("Clicked second")
#     button.click()
# input()

# asyncio.run(downloadLinks(lines))

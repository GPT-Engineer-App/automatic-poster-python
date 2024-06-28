import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Initialize the WebDriver and open WhatsApp Web
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://web.whatsapp.com")
input("Press Enter after scanning QR code")

def send_message(contact, message):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(message)
    message_box.send_keys(Keys.ENTER)

def send_image(contact, image_path, description):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    attachment_box = driver.find_element(By.XPATH, '//div[@title="Attach"]')
    attachment_box.click()
    image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    image_box.send_keys(image_path)
    time.sleep(2)
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    message_box.send_keys(description)
    message_box.send_keys(Keys.ENTER)

def send_bulk_messages(contact, messages):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
    for message in messages:
        message_box.send_keys(message)
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)

def send_bulk_images(contact, images_with_descriptions):
    search_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')
    search_box.clear()
    search_box.send_keys(contact)
    search_box.send_keys(Keys.ENTER)
    time.sleep(2)
    for image_path, description in images_with_descriptions:
        attachment_box = driver.find_element(By.XPATH, '//div[@title="Attach"]')
        attachment_box.click()
        image_box = driver.find_element(By.XPATH, '//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
        image_box.send_keys(image_path)
        time.sleep(2)
        message_box = driver.find_element(By.XPATH, '//div[@contenteditable="true"][@data-tab="1"]')
        message_box.send_keys(description)
        message_box.send_keys(Keys.ENTER)
        time.sleep(1)

if __name__ == "__main__":
    contacts = ["Contact 1", "Contact 2"]
    messages = ["Hello!", "How are you?"]
    images_with_descriptions = [("path/to/image1.jpg", "Description 1"), ("path/to/image2.jpg", "Description 2")]

    for contact in contacts:
        send_bulk_messages(contact, messages)
        send_bulk_images(contact, images_with_descriptions)
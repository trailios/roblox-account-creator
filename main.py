import time
import random
import string
import tkinter as tk
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC

window_size = (1000, 1000)
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument(f"--window-size={window_size[0]},{window_size[1]}")

chromedriver_path = r'webdriver\chromedriver.exe'

def generate_random_username(prefix, length):
    if length <= len(prefix):
        raise ValueError("Length should be greater than the length of the prefix.")
    random_chars = ''.join(random.choices(string.digits, k=length - len(prefix)))
    username = f"{prefix}{random_chars}"
    return username

def generate_random_password(length):
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def save_account_to_file(random_username, random_password):
    with open("Account.txt", "a") as file:
        file.write(f"{random_username}:{random_password}\n")

def create_account():
    num_iterations = int(iterations_entry.get())
    starting_name = name_entry.get()
    name_length = int(namelength_entry.get())
    
    for _ in range(num_iterations):
        driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
        driver.get("https://www.roblox.com/")
        wait = WebDriverWait(driver, 30)
        
        cooki = driver.find_element(By.XPATH, "//button[@class='btn-secondary-lg cookie-btn btn-primary-md btn-min-width']")
        cooki.click()
        
        time.sleep(1)

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()
        time.sleep(1)

        option_29 = driver.find_element(By.XPATH, "//option[text()='29']")
        option_29.click()

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()

        option_january = driver.find_element(By.XPATH, "//option[@value='Jan']")
        option_january.click()

        dropdown = driver.find_element(By.CLASS_NAME, 'rbx-select')
        dropdown.click()

        option_1999 = driver.find_element(By.XPATH, "//option[@value='1999']")
        option_1999.click()

        username = driver.find_element(By.XPATH, "//*[@id='signup-username']")
        random_username = generate_random_username(starting_name, name_length)
        username.send_keys(random_username)

        password = driver.find_element(By.XPATH, "//*[@id='signup-password']")
        random_password = generate_random_password(12)
        password.send_keys(random_password)

        selected_function = random.choice([lambda: Gender1(driver), lambda: Gender2(driver)])
        selected_function()

        try:
            sign = driver.find_element(By.XPATH, "//*[@id='signup-button']")
            sign.click()
        except:
            num_iterations += 1
            time.sleep(1)
            driver.quit()

        time.sleep(5)
        while True:
            try:
                driver.find_element(
                    By.XPATH, "/html/body/div[9]/div[2]/div/div/div/div"
                )
                print("[ info ] >>> [ Solve captcha! ]")
                time.sleep(1)
            except NoSuchElementException:
                print("[ info ] >>> [ Captcha solved or no captcha found ]")
                break

        time.sleep(5)
        try:
            element = driver.find_element(By.XPATH, "//*[@id='header-menu-icon']/button[2]")
            element.click()
            driver.quit()
        except:
            num_iterations += 1
            time.sleep(1)
            driver.quit()
        save_account_to_file(random_username, random_password)
        
    result_label.config(text="Finished creating accounts")

def Gender1(driver):
    Gender = driver.find_element(By.XPATH, "//*[@id='MaleButton']")
    Gender.click()

def Gender2(driver):
    Gender2 = driver.find_element(By.XPATH, "//*[@id='FemaleButton']")
    Gender2.click()

# Create the GUI
root = tk.Tk()
root.title("roblox account creator selenium")
root.geometry("300x250")
root.resizable(False, False)

# Labels and Entry widgets for Iterations
iterations_frame = tk.Frame(root)
iterations_frame.pack(pady=10)

iterations_label = tk.Label(iterations_frame, text="Enter the number of iterations:")
iterations_label.grid(row=0, column=0, padx=5, pady=5)

iterations_entry = tk.Entry(iterations_frame)
iterations_entry.grid(row=0, column=1, padx=5, pady=5)

# Labels and Entry widgets for Starting Name
name_frame = tk.Frame(root)
name_frame.pack(pady=10)

name_label = tk.Label(name_frame, text="Starting name:")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(name_frame)
name_entry.grid(row=0, column=1, padx=5, pady=5)

# Labels and Entry widgets for Name Length
length_frame = tk.Frame(root)
length_frame.pack(pady=10)

namelength_label = tk.Label(length_frame, text="Name length:")
namelength_label.grid(row=0, column=0, padx=5, pady=5)

namelength_entry = tk.Entry(length_frame)
namelength_entry.grid(row=0, column=1, padx=5, pady=5)

# Create Accounts Button
create_button = tk.Button(root, text="Create Accounts", command=create_account)
create_button.pack(pady=10)

# Label for EU Edition Fork
edition_label = tk.Label(root, text="EU Edition fork")
edition_label.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()

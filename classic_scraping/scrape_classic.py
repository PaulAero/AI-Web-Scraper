from selenium.webdriver import Remote, FirefoxOptions
from selenium import webdriver
from selenium.webdriver.firefox.service import Service  # Importation du service pour Firefox
from bs4 import BeautifulSoup
import os

def scrape_website(website):
    print("Launching Firefox browser...")

    firefox_driver_path = "geckodriver"  # Spécifiez ici le chemin vers GeckoDriver pour Firefox
    options = webdriver.FirefoxOptions()

    # Lancer Firefox avec le service GeckoDriver
    driver = webdriver.Firefox(service=Service(firefox_driver_path), options=options)

    try:
        driver.get(website)  # Ouvrir l'URL spécifiée
        print("Page loaded...")
        html = driver.page_source  # Récupérer le code source de la page
        return html
    finally:
        driver.quit()  # Fermer le navigateur une fois terminé


def extract_body_content(html_content):
    soup = BeautifulSoup(html_content, "html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""


def clean_body_content(body_content):
    soup = BeautifulSoup(body_content, "html.parser")

    for script_or_style in soup(["script", "style"]):
        script_or_style.extract()

    # Get text or further process the content
    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(
        line.strip() for line in cleaned_content.splitlines() if line.strip()
    )

    with open("cleaned_content.txt", "w") as file:
        file.write(cleaned_content)
        print("Page HTML nettoyé enregistrer (cleaned_content.txt)")

    return cleaned_content


def split_dom_content(dom_content, max_length=12000):
    return [
        dom_content[i : i + max_length] for i in range(0, len(dom_content), max_length)
    ]

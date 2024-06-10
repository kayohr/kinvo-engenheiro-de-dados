from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By


def scrape_news():
    print("Iniciando raspagem de notícias...")

    # Se quiser, adicione prints para verificar se o Selenium está funcionando corretamente
    print("Configurando Selenium...")

    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(service=service, options=chrome_options)

    print("Acessando URL...")
    url = 'https://www.spacemoney.com.br/ultimas-noticias'
    driver.get(url)

    news = []
    elements = driver.find_elements(By.XPATH, '//div[@class="linkNoticia crop"]')
    for element in elements[:5]:
        title = element.text
        link = element.find_element(By.TAG_NAME, 'a').get_attribute('href')
        news.append({'title': title, 'link': link})

    driver.quit()

    print("Raspagem de notícias concluída.")
    print("Notícias encontradas:", news)

    return news

# type: ignore
# Selenium - Automatizando tarefas no navegador
from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
EDGE_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'


def make_edge_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()

    # edge_options.add_argument('--headless')
    if options is not None:
        for option in options:
            edge_options.add_argument(option)

    edge_service = Service(
        executable_path=str(EDGE_DRIVER_EXEC),
    )

    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options,
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 20

    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_edge_browser(*options)

    # Como antes
    browser.get('https://www.bing.com')

    # Espere para encontrar o input
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'b_mcw')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()

    # Dorme por 10 segundos
    sleep(TIME_TO_WAIT)

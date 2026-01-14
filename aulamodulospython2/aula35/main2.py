import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ROOT_FOLDER = Path(__file__).parent
EDGE_DRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'


def make_chrome_browser(*options: str) -> webdriver.Edge:
    edge_options = webdriver.EdgeOptions()
    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            edge_options.add_argument(option)  # type: ignore

    edge_service = Service(
        executable_path=str(EDGE_DRIVER_EXEC),
    )

    browser = webdriver.Edge(
        service=edge_service,
        options=edge_options,
    )

    return browser


if __name__ == '__main__':
    # Example
    # options = '--headless', '--disable-gpu',
    options = ('--headless')
    browser = make_chrome_browser(*options)
    # Como antes
    browser.get('https://www.google.com')
    # Dorme por 10 segundos
    time.sleep(10)

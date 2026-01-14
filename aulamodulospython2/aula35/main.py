import time
from pathlib import Path
from selenium import webdriver
from selenium.webdriver.edge.service import Service

ROOT_FOLDER = Path(__file__).parent
EDGEDRIVER_EXEC = ROOT_FOLDER / 'drivers' / 'msedgedriver.exe'

print(EDGEDRIVER_EXEC)

edge_options = webdriver.EdgeOptions()
edge_service = Service(executable_path=str(EDGEDRIVER_EXEC))
edge_browser = webdriver.Edge(
    service=edge_service,
    options=edge_options,
)

edge_browser.get('https://www.bing.com.br')
time.sleep(30)

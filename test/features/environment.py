import os
import threading
from wsgiref import simple_server
from wsgiref.simple_server import WSGIRequestHandler
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

import converter
from converter import app

file = 'C:/Users/Hp/Downloads/chromedriver_win32 (1)/chromedriver.exe'
CHROME_DRIVER = os.path.join(os.path.join(os.path.dirname(file), 'driver'), 'chromedriver.exe')

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-proxy-server')
chrome_options.add_argument("--proxy-server='direct://'")
chrome_options.add_argument("--proxy-bypass-list=*")


def before_all(context):
    context.server = simple_server.WSGIServer(("", 5000), WSGIRequestHandler)
    context.server.set_app(app)
    context.pa_app = threading.Thread(target=context.server.serve_forever)
    context.pa_app.start()

    context.browser = webdriver.Chrome(ChromeDriverManager().install())
    context.browser.set_page_load_timeout(time_to_wait=200)


def after_all(context):
    context.browser.quit()
    context.server.shutdown()
    context.pa_app.join()


def before_feature1(context, feature):
    if 'browser' in feature.tags:
        context.server = simple_server.WSGIServer(('', 8000, Exception))
        context.server.set_app(converter.app(environment='test'))
        context.thread = threading.Thread(target=context.server.serve_forever)
        context.thread.start()
        context.browser = webdriver.WebDriver()
        yield context.browser


def after_feature1(context, feature):
    if 'browser' in feature.tags:
        context.server.shutdown()
        context.thread.join()
        context.browser.quit()

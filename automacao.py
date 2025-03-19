from playwright.sync_api import sync_playwright
import time
import os

download_path = os.path.abspath("downloads")
os.makedirs(download_path, exist_ok=True)

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    contexto = navegador.new_context(accept_downloads=True)
    pagina = contexto.new_page()

    pagina.goto("https://siafic.rio.rj.gov.br/Flexvision/")
    pagina.fill('//*[@id="gwt-uid-5"]', '80634869787')
    pagina.fill('//*[@id="gwt-uid-7"]', 'ait1234')
    pagina.locator('//*[@id="Flexvision-267413183"]/div/div[2]/div/div/div/div/div[2]/div/div/div/div/div/div[7]/div/div[1]/div').click()
    pagina.locator('//*[@id="Flexvision-267413183"]/div/div[2]/div/div[1]/div/div/div[4]/div[11]/span/span[2]').click()
    pagina.fill('//*[@id="Flexvision-267413183"]/div/div[2]/div/div[3]/div/div/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/input', '009745')
    pagina.locator('//*[@id="Flexvision-267413183"]/div/div[2]/div/div[3]/div/div/div/div[1]/div/div/div[3]/div/div[2]/div/div[3]/table/tbody/tr[3]/td/div/div/span[2]').click()
    pagina.locator('//*[@id="Flexvision-267413183"]/div/div[2]/div/div[3]/div/div/div/div[3]/div/div/div[3]/div/div[3]/table/tbody/tr/td[2]').click()
    pagina.locator('//*[@id="Flexvision-267413183"]/div/div[2]/div/div[3]/div/div/div/div[3]/div/div/div[1]/div/div/div[8]/div/span/span[1]').click()
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').click()
    for _ in range(13):  
        pagina.keyboard.press("ArrowDown")
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').press('Tab')
    anos = pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[2]/td[3]/div/div').click()
    for _ in range(len(anos[-2])):  
        pagina.keyboard.press("ArrowDown")
    '''for _ in range(18):  
        pagina.keyboard.press("ArrowDown")'''
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').press('Tab')
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[3]/div/div/div[3]/div/span/span[2]').click()
    pagina.fill('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div[3]/div/div/div[3]/div/div/div[1]/div/div/div[1]/div/div/div[1]/input', '140001')
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div/div/div/div/div[3]/div/div/div[3]/div/div/div[1]/div/div/div[11]/div/div/div/div/span').click()
    
    with pagina.expect_download() as download_info:
        pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[4]/div/div/div[1]/div/span/span[2]').click()

    download = download_info.value
    download_path_full = os.path.join(download_path, download.suggested_filename)
    download.save_as(download_path_full)



   #pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').click()
    
    


     

    







    time.sleep(20)
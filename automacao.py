from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
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
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[2]/td[3]/div/div').click()
    for _ in range(18):  
        pagina.keyboard.press("ArrowDown")
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').press('Tab')
    pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[3]/div/div/div[3]/div/span/span[2]').click()
    



   #pagina.locator('//*[@id="Flexvision-267413183-overlays"]/div[3]/div/div/div[3]/div/div/div[1]/div/div/div/table/tbody/tr[1]/td[3]/div/div').click()
    
    


     

    







    time.sleep(20)
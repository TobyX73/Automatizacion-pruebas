from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)
driver.maximize_window()

def searchHotels():
    driver.get("https://reservas.hotelesbagu.com/portal/es-es/?idHotel=2350&fechaDesde=&fechaHasta=&forzarLimpiar=true&adultos=&ninios=")

    try:
        wait = WebDriverWait(driver, 15)

        fecha_ingreso = wait.until(EC.element_to_be_clickable((By.ID, "fechaDesdeLateral")))
        fecha_ingreso.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "datepicker")))

        while "Mayo 2025" not in driver.find_element(By.CLASS_NAME, "datepicker-switch").text:
            driver.find_element(By.CLASS_NAME, "next").click()
            time.sleep(0.5)

        for dia in driver.find_elements(By.XPATH, "//td[@class='day' and text()='20']"):
            if dia.is_displayed():
                dia.click()
                break

        fecha_salida = wait.until(EC.element_to_be_clickable((By.ID, "fechaHastaLateral")))
        fecha_salida.click()
        wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "datepicker")))

        while "Mayo 2025" not in driver.find_element(By.CLASS_NAME, "datepicker-switch").text:
            driver.find_element(By.CLASS_NAME, "next").click()
            time.sleep(0.5)

        for dia in driver.find_elements(By.XPATH, "//td[@class='day' and text()='25']"):
            if dia.is_displayed():
                dia.click()
                break

        time.sleep(1)

        label_adulto = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[input[@name='optionsA' and @value='1']]")))
        label_adulto.click()

        label_nino = wait.until(EC.element_to_be_clickable((By.XPATH, "//label[input[@name='optionsN' and @value='0']]")))
        label_nino.click()

        time.sleep(1)

        print("\nDatos seleccionados.")
        print(f"   - Ingreso: {fecha_ingreso.get_attribute('value')}")
        print(f"   - Salida: {fecha_salida.get_attribute('value')}")
        print(f"   - Adultos: 1")
        print(f"   - Niños: 0\n")

        driver.execute_script("document.body.click();")

        boton_consultar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-buscar")))
        try:
            driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", boton_consultar)
            time.sleep(1)
        except Exception as e:
            print(f"Error haciendo scroll: {e}")

        if boton_consultar.is_enabled():
            boton_consultar.click()
            print("Consulta enviada correctamente.")
            wait.until(EC.url_changes(driver.current_url))
            print("Página de resultados cargada.")
           
        else:
            print("El botón 'Consultar' está deshabilitado.")
            return



    except Exception as e:
        print(f"\n[Error]: {e}")

    finally:
        time.sleep(5)
        driver.quit()

if __name__ == "__main__":
    searchHotels()



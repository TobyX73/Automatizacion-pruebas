from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Configuración del WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def searchHotels():
    driver.get("https://reservas.hotelesbagu.com/portal/es-es/?idHotel=2434")  

    try:
        wait = WebDriverWait(driver, 10)

        # Seleccionar la fecha de ingreso
        fecha_ingreso = wait.until(EC.element_to_be_clickable((By.ID, "fechaDesdeLateral")))
        driver.execute_script("arguments[0].value = 'Abr 9, 2025'; arguments[0].dispatchEvent(new Event('change'))", fecha_ingreso)

        # Seleccionar la fecha de salida
        fecha_salida = wait.until(EC.element_to_be_clickable((By.ID, "fechaHastaLateral")))
        driver.execute_script("arguments[0].value = 'Abr 11, 2025'; arguments[0].dispatchEvent(new Event('change'))", fecha_salida)

        time.sleep(2)

      
        adultos = wait.until(EC.presence_of_element_located((By.NAME, "optionsA")))
        driver.execute_script("arguments[0].click();", adultos)
        driver.execute_script("arguments[0].value = '1'; arguments[0].dispatchEvent(new Event('change'))", adultos)

        # Seleccionar niños (Ejemplo: 1 niño)
        ninos = wait.until(EC.presence_of_element_located((By.NAME, "optionsN")))
        driver.execute_script("arguments[0].click();", ninos)
        driver.execute_script("arguments[0].value = '0'; arguments[0].dispatchEvent(new Event('change'))", ninos)

        time.sleep(2)  

       
        print("\n📊 Valores capturados en el navegador:")
        print(f"   - Fecha ingreso: {fecha_ingreso.get_attribute('value')}")
        print(f"   - Fecha salida: {fecha_salida.get_attribute('value')}")
        print(f"   - Adultos: {adultos.get_attribute('value')}")
        print(f"   - Niños: {ninos.get_attribute('value')}\n")

       
        driver.execute_script("document.body.click();")
       

        boton_consultar = None
        for _ in range(5):  
            try:
                boton_consultar = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='submit' and @value='Consultar']")))
                if boton_consultar and boton_consultar.is_displayed():
                    break
            except:
                print("🔄 Reintentando encontrar el botón 'Consultar'...")
               
        
        if boton_consultar and boton_consultar.is_displayed():
            driver.execute_script("arguments[0].scrollIntoView(true);", boton_consultar)
            print("🔎 Estado del botón 'Consultar':", boton_consultar.is_enabled())

            if boton_consultar.is_enabled():
                driver.execute_script("arguments[0].click();", boton_consultar)
                print("✅ Consulta enviada correctamente.")
                wait.until(EC.url_changes(driver.current_url))
                print("✅ Página de resultados cargada correctamente.")
            else:
                print("⚠️ El botón 'Consultar' está deshabilitado. Puede haber un problema en la selección de valores.")
        else:
            print("❌ No se pudo encontrar el botón 'Consultar' después de varios intentos.")

    except Exception as e:
        print(f"❌ Error: {e}")

    finally:
        time.sleep(2)  
        driver.quit()

if __name__ == "__main__":
    searchHotels()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

# Configuración del WebDriver
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

def makereservation():
    driver.get("https://reservas.hotelesbagu.com/portal/es-es/hotel/reservahotel/?idHotel=2350&track=paso2&SESSIONPORTAL=le9cjg25lhnl92u5m07ib7trta")

    try:
        wait = WebDriverWait(driver, 20)

        wait.until(EC.element_to_be_clickable((By.ID, "nombre"))).send_keys("Juan")
        wait.until(EC.element_to_be_clickable((By.ID, "apellido"))).send_keys("Pérez")
        wait.until(EC.element_to_be_clickable((By.ID, "telefono"))).send_keys("123456789")
        
        # Seleccionar Nacionalidad
        nacionalidad_dropdown = wait.until(EC.presence_of_element_located((By.ID, "pais")))
        select = Select(nacionalidad_dropdown)
        select.select_by_index(8) 

        # Seleccionar tipo de doc
        TipoDoc_dropdown = wait.until(EC.presence_of_element_located((By.ID, "tipodoc")))
        select = Select(TipoDoc_dropdown)
        select.select_by_index(1) 

        wait.until(EC.element_to_be_clickable((By.ID, "nrodoc"))).send_keys("12345678")
        wait.until(EC.element_to_be_clickable((By.ID, "email"))).send_keys("juan.perez@example.com")
        wait.until(EC.element_to_be_clickable((By.ID, "email2"))).send_keys("juan.perez@example.com")
        wait.until(EC.element_to_be_clickable((By.ID, "direccion"))).send_keys("Avenida Siempre Viva 742")
        wait.until(EC.element_to_be_clickable((By.ID, "peticiones"))).send_keys("cerradura electronica y reposeras")

        # Aceptar términos y condiciones
        aceptar_terminos = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='checkbox']")))
        aceptar_terminos.click()
        
        # Enviar formulario
        confirmar_reserva = wait.until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Confirmar reserva')]")))
        driver.execute_script("arguments[0].scrollIntoView(true);", confirmar_reserva)
        ActionChains(driver).move_to_element(confirmar_reserva).click().perform()
        
        print("✅ Reserva completada con éxito")
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    makereservation()

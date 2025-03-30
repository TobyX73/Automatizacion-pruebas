from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains

# Configuración del WebDriver
options = webdriver.ChromeOptions()
# Elimina "--headless" para depurar visualmente
driver = webdriver.Chrome(options=options)

def fill_contact_form():
    driver.get("https://hotelesbagu.com/contacto/")
    
    try:
        # Esperar que el formulario esté disponible
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "Nombre")))

        # Identificar los campos del formulario
        name_field = driver.find_element(By.NAME, "Nombre")
        last_name_field = driver.find_element(By.NAME, "Apellido")
        email_field = driver.find_element(By.NAME, "Email")
        phone_field = driver.find_element(By.NAME, "Telefono")
        subject_field = driver.find_element(By.NAME, "Asunto")
        hotel_field = driver.find_element(By.NAME, "Hotel")
        message_field = driver.find_element(By.NAME, "Comentario")
        
        # Seleccionar el botón de envío
        submit_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='submit']"))
        )
        
        # Llenar el formulario
        name_field.send_keys("Juan")
        last_name_field.send_keys("Pérez")
        email_field.send_keys("juan.perez@example.com")
        phone_field.send_keys("123456789")
        subject_field.send_keys("Necesito mas información")
        hotel_field.send_keys("Bagu Buenos Aires")
        message_field.send_keys("Hola, estoy interesado en más información sobre el hotel.")
        
        # Desplazarse al botón antes de hacer clic
        driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
        
        # Intentar hacer clic en el botón usando ActionChains
        try:
            actions = ActionChains(driver)
            actions.move_to_element(submit_button).click().perform()
        except Exception as e:
            print(f"❌ Error al hacer clic en el botón: {e}")
            raise

        
        print("✅ Formulario rellenado correctamente y enviado con éxito")
    except TimeoutException:
        print("❌ Error: Tiempo de espera agotado al buscar un elemento.")
    except NoSuchElementException as e:
        print(f"❌ Error: No se encontró un elemento. Detalles: {e}")
    except AssertionError as e:
        print(f"❌ Error: {e}")
    except Exception as e:
        print(f"❌ Error inesperado: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    fill_contact_form()

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def ejecutar_robot_aspirante():
    # Inicializar el navegador (Selenium Manager gestiona el driver automáticamente)
    options = webdriver.ChromeOptions()
    # options.add_argument("--headless") # Descomenta si quieres ejecutarlo en segundo plano sin ver la ventana
    driver = webdriver.Chrome(options=options)

    try:
        # 1. URL del formulario
        url = "https://qa-practice.netlify.app/bugs-form"         
        driver.get(url)
        driver.maximize_window()

        # Configurar espera explícita (máximo 10 segundos)
        wait = WebDriverWait(driver, 10)

        # 2. Esperar a que cargue el formulario e identificar campos por ID, Name o XPath
        print("Cargando formulario y rellenando datos...")
        
        # Campo First Name
        nombre = wait.until(EC.presence_of_element_located((By.ID, "firstName")))
        nombre.send_keys("Carolina")

        # Campo Last Name
        nombre = wait.until(EC.presence_of_element_located((By.ID, "lastName")))
        nombre.send_keys("Gutierrez")

        # Campo Phone Number
        nombre = wait.until(EC.presence_of_element_located((By.ID, "phone")))
        nombre.send_keys("3004372258")

        # Campo Email Address
        email = driver.find_element(By.ID, "emailAddress")
        email.send_keys("carito.guti@outlook.com")

        # Seleccionar una opción de un menú desplegable
        dropdown_countries = driver.find_element(By.ID, "countries_dropdown_menu")
        select = Select(dropdown_countries)
        select.select_by_visible_text("Colombia")

        # Campo Password
        nombre = wait.until(EC.presence_of_element_located((By.ID, "password")))
        nombre.send_keys("12345678")

        # Aceptar términos y condiciones (Checkbox)
        #checkbox_terms = driver.find_element(By.ID, "terminosCondiciones")
        #  if not checkbox_terms.is_selected():
        #    checkbox_terms.click()*/

        # 3. Hacer clic en el botón Register
        print("Enviando el formulario...")
        boton_enviar = driver.find_element(By.ID, "registerBtn")
        boton_enviar.click()

        # 4. Validar el éxito del envío esperando un mensaje de confirmación
        mensaje_exito = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "mensaje-exito")) # Cambia por la clase o ID real de éxito
        )
        print("¡Registro completado con éxito!", mensaje_exito.text)

    except Exception as error:
        print(f"Ocurrió un error durante la ejecución del robot: {error}")

    finally:
        # Pausa breve para visualizar el resultado final antes de cerrar
        time.sleep(5)
        driver.quit()
        print("Navegador cerrado.")

if __name__ == "__main__":
    ejecutar_robot_aspirante()
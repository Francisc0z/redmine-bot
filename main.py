from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters, Updater

def login():
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username = 'Francisco_Silva'
    password = 'Michimochi1'

    username_field.send_keys(username)
    password_field.send_keys(password)

    login_button = driver.find_element(By.NAME, "login")
    login_button.click()


    enlace_despues_de_login = driver.find_element(By.CLASS_NAME, "my-page")
    enlace_despues_de_login.click()

    enlace_despues_de_login = driver.find_element(By.XPATH, '//*[@id="list-top"]/div/h3/a')
    enlace_despues_de_login.click()

def hoursToday():
    select_element = driver.find_element(By.ID, 'operators_spent_on')

    select = Select(select_element)

    select.select_by_visible_text('hoy')

    enlace_despues_de_login = driver.find_element(By.XPATH, '//*[@id="query_form_with_buttons"]/p/a[1]')
    enlace_despues_de_login.click()

    horas_hoy = int(driver.find_element(By.CLASS_NAME, 'hours-int').text)
    # Cerrar la ventana del navegador
    print(f"horas cargadas hoy: ", horas_hoy)

    if horas_hoy != 8:
        print(f"Aun faltan cargar")

    return horas_hoy

def proyects():
    enlace_despues_de_login = driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul/li[3]/a')
    enlace_despues_de_login.click()

    proyectos = driver.find_elements(By.CLASS_NAME, 'my-project')

    for proyecto in proyectos:
        print(proyecto.text)

def requirements():
    #Aca deberia mandar los proyectos al usuario
    enlace_despues_de_login = driver.find_element(By.XPATH, '//*[@id="projects-index"]/ul/li[7]/div/a')
    enlace_despues_de_login.click()

    enlace_despues_de_login = driver.find_element(By.CLASS_NAME, "issues")
    enlace_despues_de_login.click()

    select_element = driver.find_element(By.ID, 'add_filter_select')

    select = Select(select_element)

    select.select_by_visible_text('Asignado a')

    select_element = driver.find_element(By.ID, 'values_assigned_to_id_1')

    select = Select(select_element)

    select.select_by_visible_text('SILVA TIENGO JUAN FRANCISCO')

def addHours(horas_hoy):
    enlace_despues_de_login = driver.find_element(By.XPATH, '//*[@id="query_form_with_buttons"]/p/a[1]')
    enlace_despues_de_login.click()

    enlaces_peticiones = driver.find_elements(By.CLASS_NAME, 'id')

    enlace = []

    for elements in enlaces_peticiones:
        enlace.append(elements.find_element(By.TAG_NAME, 'a'))

    enlace[0].click()

    enlace_añadir_tiempo = driver.find_element(By.CLASS_NAME, 'icon-time-add')
    enlace_añadir_tiempo.click()

    print(f"Faltan por añadir ", (8 - horas_hoy))

    input_horas =  driver.find_element(By.NAME, "time_entry[hours]")
    input_coment = driver.find_element(By.NAME, "time_entry[comments]")

    hours = '8'
    comment = 'Michimochi1'

    input_horas.send_keys(hours)
    input_coment.send_keys(comment)

    select_element = driver.find_element(By.ID, 'time_entry_activity_id')

    select = Select(select_element)

    select.select_by_visible_text('Desarrollo')

    boton_aceptar  = driver.find_element(By.NAME, "commit")
    boton_aceptar.click()


driver = webdriver.Firefox()

driver.get('https://customers.itrsa.com.ar:8443/login?back_url=https%3A%2F%2Fcustomers.itrsa.com.ar%3A8443%2F')

def main():
    
    login()
    horas_hoy = hoursToday()
    proyects()
    requirements()
    addHours(horas_hoy)

main()

# driver.quit()

#telegram integration

# token = "6783890177:AAHaiYYeNGD0f9640sPPitngbIOJuaKNevA"

# def start(update, context):
#     update.message.reply_text('Hola! Bienvenido al bot de prueba.')

# def echo(update, context):
#     update.message.reply_text(update.message.text)

# def main():
#     updater = Updater(token, True)

#     # Registra los manejadores de comandos y mensajes
#     dp = updater.dispatcher
#     dp.add_handler(CommandHandler("start", start))
#     dp.add_handler(MessageHandler(filters.text & ~filters.command, echo))

#     # Inicia el bot
#     updater.start_polling()
#     updater.idle()

# if __name__ == '__main__':
#     main()
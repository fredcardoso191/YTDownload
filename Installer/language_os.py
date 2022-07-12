import locale

lang = str(locale.getdefaultlocale())
en = "('en_US', 'cp1252')"
pt = "('pt_BR', 'cp1252')"
es = "('es_ES', 'cp1252')"

def pathinvalid():
    if lang == en:
        return "Please provide a valid path."
    if lang == pt:
        return "Forneça um caminho válido."
    if lang == es:
        return "Proporcione una ruta válida."

def title():
    if lang == en:
        return "App message"
    if lang == pt:
        return "Mensagem do aplicativo"
    if lang == es:
        return "Mensaje de la aplicación"

def finish():
    if lang == en:
        return "Select Destination Location"
    if lang == pt:
        return "Selecione o local de destino"
    if lang == es:
        return "Seleccione la ubicación de destino"

def finishbutton():
    if lang == en:
        return "Finish"
    if lang == pt:
        return "Finalizar"
    if lang == es:
        return "Finalizar"

def cancel():
    if lang == en:
        return "Cancel"
    if lang == pt:
        return "Cancelar"
    if lang == es:
        return "Anular"

def browse():
    if lang == en:
        return "Browse..."
    if lang == pt:
        return "Navegar..."
    if lang == es:
        return "Para navegar..."

def install():
    if lang == en:
        return "Install"
    if lang == pt:
        return "Instalar"
    if lang == es:
        return "Instalar"

def installfinish():
    if lang == en:
        return "Installation completed successfully"
    if lang == pt:
        return "Instalação concluída com sucesso"
    if lang == es:
        return "La instalación se completó con éxito"
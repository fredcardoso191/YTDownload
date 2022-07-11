import locale

lang = str(locale.getdefaultlocale())
en = "('en_US', 'cp1252')"
pt = "('pt_BR', 'cp1252')"
es = "('es_ES', 'cp1252')"

def button(option):
    if option == "video":
        if lang == en:
            return "Video download"
        if lang == pt:
            return "Baixar video"
        if lang == es:
            return "Descargar vídeo"
    if option == "audio":
        if lang == en:
            return "Audio download"
        if lang == pt:
            return "Baixar audio"
        if lang == es:
            return "Descargar audio"

def successfuldownload():
    if lang == en:
        return "Download completed successfully."
    if lang == pt:
        return "Download concluído com sucesso."
    if lang == es:
        return "Descarga completada con éxito."

def downloaderror():
    if lang == en:
        return "Download error."
    if lang == pt:
        return "Erro de download."
    if lang == es:
        return "Error de descarga."

def invalidurl():
    if lang == en:
        return "Invalid URL. Enter the valid URL."
    if lang == pt:
        return "URL inválida. Digite a URL novamente."
    if lang == es:
        return "URL invalida. Introduzca la URL de nuevo."

def title():
    if lang == en:
        return "App message"
    if lang == pt:
        return "Mensagem do aplicativo"
    if lang == es:
        return "Mensaje de la aplicación"
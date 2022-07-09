import locale

# Messages
def successfuldownload():
    lang = str(locale.getdefaultlocale())
    if lang == "('en_US', 'cp1252')":
        return " has been successfully downloaded."
    if lang == "('pt_BR', 'cp1252')":
        return " foi baixado com sucesso."

def enterurl():
    lang = str(locale.getdefaultlocale())
    if lang == "('en_US', 'cp1252')":
        return "CTRL + C or enter quit to exit.\nEnter the URL of the video you want to download: \n>> "
    if lang == "('pt_BR', 'cp1252')":
        return "CTRL + C ou digite quit para sair.\nDigite o URL do vídeo que você deseja baixar: \n>> "

def downloaderror():
    lang = str(locale.getdefaultlocale())
    if lang == "('en_US', 'cp1252')":
        return "Download error."
    if lang == "('pt_BR', 'cp1252')":
        return "Erro de download."

def option():
    lang = str(locale.getdefaultlocale())
    if lang == "('en_US', 'cp1252')":
        return "1- Video download. 2- Audio download.\n>> "
    if lang == "('pt_BR', 'cp1252')":
        return "1- Baixar vídeo. 2- Download audio.\n>> "

def invalidurl(url):
    lang = str(locale.getdefaultlocale())
    if lang == "('en_US', 'cp1252')":
        return f"Invalid URL ({url}). Enter the valid URL (Ex: https://www.youtube.com/watch?v=...)"
    if lang == "('pt_BR', 'cp1252')":
        return f"URL inválido ({url}). Insira URL novamente (https://www.youtube.com/watch?v=...)"
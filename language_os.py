import locale

lang = str(locale.getdefaultlocale())
en = "('en_US', 'cp1252')"
pt = "('pt_BR', 'cp1252')"

# Messages
def enterurl():
    if lang == en:
        return "CTRL + C or enter quit to exit.\nEnter the URL of the video you want to download:\n>> "
    if lang == pt:
        return "CTRL + C ou digite quit para sair.\nDigite o URL do vídeo que você deseja baixar:\n>> "

def option():
    if lang == en:
        return "1- Video download. 2- Audio download.\n>> "
    if lang == pt:
        return "1- Baixar vídeo. 2- Download audio.\n>> "

def invalidoption():
    if lang == en:
        return "Invalid option. Enter an option again."
    if lang == pt:
        return "Opção inválida. Digite uma opção novamente."

def successfuldownload(): 
    if lang == en:
        return " has been successfully downloaded."
    if lang == pt:
        return " foi baixado com sucesso."

def downloaderror():
    if lang == en:
        return "Download error."
    if lang == pt:
        return "Erro de download."

def invalidurl(url):
    if lang == en:
        return f"Invalid URL ({url}). Enter the valid URL (Ex: https://www.youtube.com/watch?v=...)"
    if lang == pt:
        return f"URL inválido ({url}). Insira URL novamente (Ex: https://www.youtube.com/watch?v=...)"
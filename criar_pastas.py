import os
import shutil
import re  # Para limpar caracteres inválidos

def limpar_nome(nome):
    """Remove caracteres inválidos para nomes de pastas no Windows."""
    nome = nome.strip()  # Remove espaços extras no início e fim
    nome = re.sub(r'[<>:"/\\|?*]', '', nome)  # Remove caracteres inválidos
    return nome

def organizar_arquivos(diretorio):
    if not os.path.exists(diretorio):
        print("O diretório especificado não existe.")
        return
    
    for arquivo in os.listdir(diretorio):
        caminho_arquivo = os.path.join(diretorio, arquivo)
        
        if os.path.isfile(caminho_arquivo):  # Verifica se é um arquivo
            nome_pasta = limpar_nome(os.path.splitext(arquivo)[0])  # Limpa o nome da pasta
            caminho_pasta = os.path.join(diretorio, nome_pasta)
            
            os.makedirs(caminho_pasta, exist_ok=True)  # Cria a pasta
            
            try:
                shutil.move(caminho_arquivo, os.path.join(caminho_pasta, arquivo))  # Move o arquivo
                print(f"Arquivo '{arquivo}' movido para '{caminho_pasta}'")
            except Exception as e:
                print(f"Erro ao mover '{arquivo}': {e}")

diretorio_alvo = "Autor Desconhecido"  
organizar_arquivos(diretorio_alvo)

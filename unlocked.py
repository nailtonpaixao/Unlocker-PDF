import sys
from pathlib import Path
from pypdf import PdfReader, PdfWriter
from getpass import getpass

'''
 _    _       _            _            _        _____  _____  ______ 
| |  | |     | |          | |          | |      |  __ \|  __ \|  ____|
| |  | |_ __ | | ___   ___| | _____  __| |______| |__) | |  | | |__   
| |  | | '_ \| |/ _ \ / __| |/ / _ \/ _` |______|  ___/| |  | |  __|  
| |__| | | | | | (_) | (__|   <  __/ (_| |      | |    | |__| | |     
 \____/|_| |_|_|\___/ \___|_|\_\___|\__,_|      |_|    |_____/|_|     

Script desenvolvido para desbloqueio de PDFs com senha. Por Nailton P.
 '''


def unlock_pdf():
    # 1. Verifica se o argumento foi passado
    if len(sys.argv) < 2:
        print("Uso: python unlocked.py nome_do_arquivo.pdf")
        return

    # 2. Captura e trata o caminho do arquivo
    input_path = Path(sys.argv[1])
    
    if not input_path.exists():
        print(f"Erro: O arquivo '{input_path}' não foi encontrado.")
        return

    # 3. Define o nome de saída (ex: unlocked_arquivo.pdf)
    output_path = input_path.parent / f"unlocked_{input_path.name}"

    try:
        reader = PdfReader(str(input_path))

        # 4. Lógica de Desbloqueio
        if reader.is_encrypted:
            password = getpass(f"Digite a senha do PDF: ")
            
            # Tenta abrir com a senha fornecida
            result = reader.decrypt(password)
            
            if result == 0:
                print("❌ Senha incorreta!")
                return
        else:
            print("💡 O arquivo já está desbloqueado.")

        # 5. Salva o novo arquivo
        writer = PdfWriter()
        
        for page in reader.pages:
            writer.add_page(page)

        with open(output_path, "wb") as f:
            writer.write(f)

        print(f"✅ Sucesso! Arquivo salvo em:\n{output_path}")

    except Exception as e:
        print(f"❌ Erro ao processar o PDF: {e}")

if __name__ == "__main__":
    unlock_pdf()

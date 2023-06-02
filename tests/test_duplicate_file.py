import shutil
from pathlib import Path

TEST_SOURCE_DIR = Path("test_source")
TEST_DEST_DIR = Path("test_dest")

# Prepara os diretórios de teste
TEST_SOURCE_DIR.mkdir(exist_ok=True)
TEST_DEST_DIR.mkdir(exist_ok=True)

# Verifica se o arquivo já existe na pasta de origem
source_file = TEST_SOURCE_DIR / "file1.txt"
if not source_file.exists():
    # Cria um arquivo de teste
    source_file.touch()

# Verifica se o arquivo já foi copiado anteriormente
already_copied = (TEST_DEST_DIR / "file1.txt").is_file()

# Copia o arquivo para o diretório de destino
shutil.copy2(source_file, TEST_DEST_DIR)

# Verifica se o arquivo foi copiado corretamente
assert (TEST_DEST_DIR / "file1.txt").is_file()

# Tenta copiar o mesmo arquivo novamente
shutil.copy2(source_file, TEST_DEST_DIR)

# Verifica se o arquivo não foi copiado novamente
assert (TEST_DEST_DIR / "file1.txt").is_file()
assert already_copied == ((TEST_DEST_DIR / "file1.txt").stat().st_mtime == source_file.stat().st_mtime)

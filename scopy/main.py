import typer
from pathlib import Path
import shutil

def copy_files(source_dir: str, dest_dir: str, extension: str):
    source_path = Path(source_dir)
    dest_path = Path(dest_dir)
    files = source_path.rglob(f"*{extension}")
    for file in files:
        dest_file = dest_path / file.relative_to(source_path)

        # Verifica se o arquivo já existe no diretório de destino
        if dest_file.is_file():
            typer.echo(f"O arquivo {file.name} já existe no diretório de destino. Pulando para o próximo arquivo.")
            continue
        else:
            typer.echo("Files copied successfully.")    

        dest_file.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(file, dest_file)

def main(source_dir: str, dest_dir: str, extension: str):
    copy_files(source_dir, dest_dir, extension)
    

if __name__ == "__main__":
    typer.run(main)


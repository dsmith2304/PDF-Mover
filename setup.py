from cx_Freeze import setup, Executable

base = None

executables = [Executable("pdf-mover.py", base=base)]

packages = ["idna","pdfminer","pathlib","shutil","time","os","sys","pdfminer.high_level","pdfminer.layout"]
options = {
    'build_exe': {
        'packages':packages,
    },
}

setup(
    name = "InvoiceMover",
    options = options,
    version = "1",
    description = 'Moves pdf files with client numbers to another directory based on that client number',
    executables = executables
)
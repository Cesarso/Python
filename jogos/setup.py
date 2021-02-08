import cx_Freeze
executables = [cx_Freeze.Executable("jogos.py")]
cx_Freeze.setup(
    name="Jogo da Forca",    # Voce pode colocar outro nome para seu jogo
    options={"build_exe": {"packages": ["jogos"],
                           "include_files": [
                               "advinhacao.py", "forca.py", "Jogos.py", "palavras.txt"
                            # Nome do arquivo ou arquivos de imagens, sons, etc, separados por virgula
                            # Exemplo "racecar.png"
                           ]}},
    executables=executables
)
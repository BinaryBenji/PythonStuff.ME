from cx_Freeze import setup, Executable

# On appelle la fonction setup
setup(
    name = "poi",
    version = "1",
    description = "smiley",
    executables = [Executable("poisone.py")],
)
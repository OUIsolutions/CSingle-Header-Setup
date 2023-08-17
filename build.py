import Build.CToolKit as ct
from Build.exemple_build import create_exemples
from Build.full_folder_zip import zip_folder
from props import *



ct.generate_amalgamated_code(STARTER,OUTPUT)


test = ct.FolderTestPreset(
    folder='tests',
    side_effect_folder='side_effect',
    use_valgrind=USE_VALGRIND
)

test.generate_ouptut(reconstruct=False)
test.start_test()

ct.include_code_in_markdown('README.md',save_file=True)
zip_folder(ZIP_NAME)

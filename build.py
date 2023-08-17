from platform import system as osname
import Build.CToolKit as ct
from Build.exemple_build import create_exemples
from Build.full_folder_zip import zip_folder
from props import *



ct.generate_amalgamated_code(STARTER,OUTPUT_TEST)


test = ct.FolderTestPreset(
    folder='tests',
    side_effect_folder='side_effect',
    use_valgrind=USE_VALGRIND
)

test.generate_ouptut(reconstruct=False)
test.start_test()
create_exemples(TEST_NAME,OUTPUT)

ct.include_code_in_markdown('README.md',save_file=True)
ct.generate_amalgamated_code(STARTER,OUTPUT)


zip_folder(ZIP_NAME)

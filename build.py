from platform import system as osname
import Build.CToolKit as ct
from Build.exemple_build import create_exemples
from Build.full_folder_zip import zip_folder
from props import *



ct.generate_amalgamated_code(STARTER,OUTPUT_TEST)
use_valgrind = True 

if osname() == 'Windows':
    use_valgrind = False



test = ct.FolderTestPreset(
    folder='tests/main_test',
    side_effect_folder='tests/target',
    use_valgrind=use_valgrind
    )
test.generate_ouptut(reconstruct=False)
test.start_test()
create_exemples(TEST_NAME,OUTPUT)

ct.include_code_in_markdown('README.md',save_file=True)
ct.generate_amalgamated_code(STARTER,OUTPUT)


zip_folder(ZIP_NAME)
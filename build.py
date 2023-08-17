import Build.CToolKit as ct
from Build.exemple_build import create_exemples
from Build.full_folder_zip import zip_folder
from os.path import isdir
from os import mkdir
from props import *



ct.generate_amalgamated_code(STARTER,OUTPUT)

if SIDE_EFFECT_FOLDER is None:
    SIDE_EFFECT_FOLDER = 'side_effect'

if not isdir(SIDE_EFFECT_FOLDER):
    mkdir(SIDE_EFFECT_FOLDER)


test = ct.FolderTestPreset(
    folder=TEST_FOLDER,
    side_effect_folder=SIDE_EFFECT_FOLDER,
    use_valgrind=USE_VALGRIND
)

test.generate_ouptut(reconstruct=RECONSTRUCT)
test.start_test()

create_exemples()
ct.include_code_in_markdown('README.md',save_file=True)
zip_folder(ZIP_NAME)

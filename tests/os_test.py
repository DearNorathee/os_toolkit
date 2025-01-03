import unittest
from pathlib import Path
from os_toolkit.utils_ost import *
from os_toolkit.cant_use_ost import *

def test_filesize_in_folder():
    path01 = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted\English"
    actual01 = filesize_in_folder(path01)
    expect01 = []

    path02 = r"H:\D_Video\The Ark Season 01 Portuguese\Audio Extracted"
    actual02 = filesize_in_folder(path02)
    print(actual01)

def test_extract_folder_structure():
    root_folder = r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS\os_toolkit\tests\test_output\test_create_folder_structure"
    actual01 = extract_folder_structure(root_folder)
    expect01 =  {
    "Portuguese": {
        "Westworld Portuguese": {
            "Westworld Portugues 01": None,
            "Westworld Portugues 02": ["folder1", "folder2"],
            "Westworld Portugues 03": None,
            "Westworld Portugues 04": None,
        },
        "BigBang Portuguese": [
            "BigBang PT Season 01",
            "BigBang PT Season 02",
            "BigBang PT Season 03",
            "BigBang PT Season 04",
            "BigBang PT Season 05",
            "BigBang PT Season 06",
            "BigBang PT Season 07",
            "BigBang PT Season 08",
            "BigBang PT Season 09",
            "BigBang PT Season 10",
            "BigBang PT Season 11",
        ],
        "The 100 PT": [
            "The 100 Season 01 Portuguese",
            "The 100 Season 02 Portuguese",
            "The 100 Season 03 Portuguese",
            "The 100 Season 04 Portuguese",
            "The 100 Season 05 Portuguese",
                    ],
                }
            }
    assert actual01 == expect01

def test_create_folder_structure():
    structure = {
    "Portuguese": {
        "Westworld Portuguese": {
            "Westworld Portugues 01": None,
            "Westworld Portugues 02": ["folder1", "folder2"],
            "Westworld Portugues 03": None,
            "Westworld Portugues 04": None,
        },
        "BigBang Portuguese": [
            "BigBang PT Season 01",
            "BigBang PT Season 02",
            "BigBang PT Season 03",
            "BigBang PT Season 04",
            "BigBang PT Season 05",
            "BigBang PT Season 06",
            "BigBang PT Season 07",
            "BigBang PT Season 08",
            "BigBang PT Season 09",
            "BigBang PT Season 10",
            "BigBang PT Season 11",
        ],
        "The 100 PT": {
            "The 100 Season 01 Portuguese": None,
            "The 100 Season 02 Portuguese": None,
            "The 100 Season 03 Portuguese": None,
            "The 100 Season 04 Portuguese": None,
            "The 100 Season 05 Portuguese": None,
                    },
                }
            }

    root_folder = r"C:\Users\Heng2020\OneDrive\Python MyLib\Python MyLib 01\10 OS\os_toolkit\tests\test_output\test_create_folder_structure"
    create_folder_structure(root_folder,structure)

def test_clean_filename():
    name01 = "This has . and ?"
    name02 = "our colleague/friendship"
    
    
    expect01 = "This has  and "
    expect02 = "our colleague friendship"
    
    actual01 = clean_filename(name01)
    actual02 = "our colleague friendship"
    
    assert actual01 == expect01, f"Not equal 01"
    # print(actual01)
    assert actual02 == expect02, f"Not equal 02"

class Test_auto_rename_series(unittest.TestCase):
    path01 = r"H:\D_Video\BigBang Portugues\BigBang PT Season 05_testPython"
    def test_basic01_prefix_no_space(self):
        auto_rename_series(self.path01,prefix="BigBang PT")
    
    def test_basic01_prefix_with_space(self):
        auto_rename_series(self.path01,prefix="BigBang PT ")
    
class Test_extract_filename(unittest.TestCase):
    path01_01 = r'H:\\D_Video\\The Ark Season 01 Portuguese\\The Ark S01E02 PT.mkv'
    path02_01 = r"H:\D_Video\The Ark Season 01 Portuguese\The Ark S01E03 PT.mkv"
    path03_01 = r"H:/D_Video/The Ark Season 01 Portuguese/The Ark S01E04 PT.mkv"

    path04_01 = r"H:/D_Video/The Ark Season 01 Portuguese/The Ark S01.E04. PT.mkv"

    path_list01 = [path01_01,path02_01,path03_01]

    path01_02 = Path(path01_01)
    path02_02 = Path(path02_01)
    path03_02 = Path(path03_01)

    path04_02 = Path(path04_01)

    def test_basice01_with_extension(self):
        actual01 = extract_filename(self.path01_01)
        actual02 = extract_filename(self.path02_01)
        actual03 = extract_filename(self.path03_01)

        expected01 = 'The Ark S01E02 PT.mkv'
        expected02 = 'The Ark S01E03 PT.mkv'
        expected03 = 'The Ark S01E04 PT.mkv'

        self.assertEqual(actual01,expected01)
        self.assertEqual(actual02,expected02)
        self.assertEqual(actual03,expected03)
    
    def test_basice02_list_input(self):
        actual = extract_filename(self.path_list01)
        expect = ['The Ark S01E02 PT.mkv','The Ark S01E03 PT.mkv','The Ark S01E04 PT.mkv']

        self.assertEqual(actual,expect)
    
    def test_with_path_dot_no_extension(self):
        actual = extract_filename(self.path04_02,with_extension=False)
        expect = 'The Ark S01.E04. PT'

        msg = f"Input: '{self.path04_02}' \nActual: '{actual}' \nExpect: '{expect}' "
        self.assertEqual(actual,expect,msg)

def test__auto_rename_series():
    path01 = r"H:\D_Video\BigBang Portugues\BigBang PT Season 05_testPython"
    
    auto_rename_series(path01,prefix="BigBang PT")
    auto_rename_series(path01,prefix="BigBang PT ")
    
def try_auto_rename_series():
    
    path_list = [
        r"H:\GoogleDrive\The 100\Portuguese\The 100 Season 01 Portuguese",
        r"H:\GoogleDrive\The 100\Portuguese\The 100 Season 02 Portuguese",
        r"H:\GoogleDrive\The 100\Portuguese\The 100 Season 03 Portuguese",
        r"H:\GoogleDrive\The 100\Portuguese\The 100 Season 04 Portuguese",
        r"H:\GoogleDrive\The 100\Portuguese\The 100 Season 05 Portuguese",
    ]
    for folder in path_list:
        auto_rename_series(folder,prefix="The 100 PT_")

if __name__ == '__main__':
    # unittest.main()
    test_filesize_in_folder()
    test_extract_folder_structure()
    # test_create_folder_structure()
    # try_auto_rename_series()


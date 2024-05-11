from pathlib import Path
from typing import List, Tuple, Union, Literal

# Sub
def create_folders(folder: Union[str, Path], 
                   name_list: List[str], 
                   replace: bool = True) -> None:
    import os
    import shutil
    """
    Create directories in the specified folder based on names provided in name_list.

    Parameters:
    folder (Union[str, Path]): The path where the directories will be created.
    name_list (List[str]): A list of directory names to create.

    Returns:
    None
    """
    
    # Ensure the folder path is a Path object
    folder = Path(folder)
    
    # Iterate through the list of names and create each folder
    for name in name_list:
        dir_path = folder / name  # Construct the full path for the new directory
        if not dir_path.exists():  # Check if the directory already exists
            os.makedirs(dir_path)  # Create the directory if it does not exist
            # print(f"Created directory: {dir_path}")
        else:
            if replace:
                shutil.rmtree(dir_path)
                os.makedirs(dir_path) 
                print(f"Directory already exists and replaced: {dir_path}")
            else:
                print(f"Directory already exists: {dir_path}")
                
#%%
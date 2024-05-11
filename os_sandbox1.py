from pathlib import Path
from typing import List, Tuple, Union, Literal

def filesize_in_folder(folder_path: Union[str, Path]) -> pd.DataFrame:
    # Convert folder_path to Path object if it's a string
    if isinstance(folder_path, str):
        folder_path = Path(folder_path)

    # Get a list of all files and folders in the specified folder
    items = [item for item in folder_path.glob('*')]

    # Create a list to store the file/folder information
    data = []

    # Calculate the total size of all files and folders
    total_size = sum(item.stat().st_size for item in items)

    # Iterate over each file/folder and collect the necessary information
    for item in items:
        name = item.name
        size = item.stat().st_size
        size_prop = size / total_size if total_size > 0 else 0

        data.append([name, size, size_prop])

    # Create a pandas DataFrame from the collected data
    df = pd.DataFrame(data, columns=['name', 'filesize', 'filesize_prop'])

    return df

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
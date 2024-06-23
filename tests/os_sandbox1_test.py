from os_toolkit.sandbox1_ost import *
def test_filesize_in_folder():
    path01 = r"E:"
    path02 = r"E:\Videos"

    actual01 = filesize_in_folder(path01)
    actual02 = filesize_in_folder(path02)
    print("test_filesize_in_folder Passed")


def test_create_audio_folder():
    # specify column manually for now
    # will change this to proper function later
    # based on pd. 2.1.3
    import py_string_tool as pst
    import dataframe_short as ds
    from tqdm import tqdm
    from playsound import playsound
    from pathlib import Path
    
    excel_path = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\NLP_2024\NLP 11_Local_TTS\Duolingo French 02.xlsm"
    sheet_name = "formated"
    out_folder01 = r"C:\Users\Heng2020\OneDrive\D_Code\Python\Python NLP\NLP 02\01 OutputData\test_create_audio_folder\test_01"
    
    vocab_df01 = ds.pd_read_excel(excel_path,sheet_name = sheet_name)
    vocab_df02 = vocab_df01.iloc[:,:3]
    vocab_df02 = vocab_df01.iloc[:,1:3]
    vocab_dict_df01 = ds.pd_split_into_dict_df(vocab_df02,add_prefix_index = True)
    test02 = detect_language(vocab_df01.iloc[:,0])
    test = detect_language(vocab_df01.iloc[:,1])
    
    chapter_limit = 10
    chapter_limit = "all"

    chapter_limit_in = chapter_limit if isinstance(chapter_limit,int) else len(vocab_dict_df01.items())
    chosen_index = 0
    # use 0-index to refer to OrderDictt
    curr_df = list(vocab_dict_df01.items())[0][1]
    
    chapter_list = list(vocab_dict_df01.keys())
    create_folders(out_folder01, chapter_list)
    
    progress_bar = tqdm(total=chapter_limit_in)
    i = 0
    for key,value in tqdm(vocab_dict_df01.items()):
        if i > chapter_limit_in:
            break
        chapter = key
        out_chapter_folder = Path(out_folder01) / chapter
        # out_chapter_folder_str just for debugging
        out_chapter_folder_str = str(out_chapter_folder)
        curr_df = value.copy()
        rename_col_by_index(curr_df,0,"French")
        rename_col_by_index(curr_df,1,"English")
        
        try:
            # first_df.rename(columns={first_df.columns[0]: 'French'}, inplace=True)
            # first_df.rename(columns={first_df.columns[1]: 'English'}, inplace=True)
            n_digit = len(str(curr_df.shape[0]))
            curr_df['formatted_index'] = (curr_df.index + 1).astype(str).str.zfill(n_digit)
            curr_df['English'] = curr_df['English'].astype(str)
            curr_df['filename_dirty'] =  curr_df['French'] + '_' + curr_df['English']
            curr_df['filename'] = curr_df.apply(
                lambda row: pst.clean_filename(row['filename_dirty']),
                axis = 1)
            
            audio_from_df(curr_df, 
                          audio_col = "French",
                          output_folder = out_chapter_folder,
                          filename_col = 'filename' ,
                          
                          )
        except ValueError:
            print(f"Error at chapter: {chapter}")
        i += 1
        progress_bar.update(1)
             
    print("test_create_audio_folder Pass !!!")
    print("Don't forget to rename your folder is generating is successfull !!!")


test_filesize_in_folder()

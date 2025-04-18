import os
import shutil

def copy_all_files_from_sources(source, destination):
    items = os.listdir(source)
    print(f"List of elements inside {source} : {items}")
    for item in items:
        item_source = f"{source}/{item}"
        item_dest = f"{destination}/{item}"

        if os.path.isdir(item_source):
            print(f"Copying folder {item_source} to {item_dest}")
            os.mkdir(item_dest)
            copy_all_files_from_sources(item_source, item_dest)
        else:
            print(f"Copying file {item_source} to {item_dest}")
            shutil.copy(item_source, item_dest)
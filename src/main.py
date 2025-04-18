import os
import shutil
from pathlib import Path
from copy_static import copy_all_files_from_sources
from page_generator import generate_pages_recursive

def main():
    #Setting up all paths
    script_path = Path(__file__).parent.parent
    public_path = script_path / "public"
    static_path = script_path / "static"
    content_path = script_path / "content"
    
    #Deleting public folder + creating new empty one
    if os.path.exists(public_path):
        shutil.rmtree(public_path)
    os.mkdir(public_path)

    #Copying all static resources from static dir to public dir
    print("Starting copy process... Generating public folder...")
    copy_all_files_from_sources(static_path, public_path)

    #Generating all web pages
    generate_pages_recursive(content_path, f"{script_path}/template.html", public_path)

main()
import os
import re

def generate_main_tex():
    """
    Generates a main.tex file for a LaTeX project.

    The script scans for subdirectories named 'chapter<number>-<anystring>',
    sorts them numerically, and generates a main.tex file that includes a
    preamble.tex file, a title page, and then includes the main.tex file
    from each of the sorted chapter directories.
    """
    # Define the project root and the main LaTeX file
    project_root = os.path.dirname(os.path.abspath(__file__))
    main_tex_path = os.path.join(project_root, 'main.tex')
    preamble_tex_path = os.path.join(project_root, 'preamble.tex')

    # Regular expression to match 'chapter<number>-<anystring>'
    chapter_pattern = re.compile(r'^chapter(\d+)-.*$')

    # Get a list of all subdirectories that match the pattern
    chapters = []
    for d in os.listdir(project_root):
        if os.path.isdir(os.path.join(project_root, d)):
            match = chapter_pattern.match(d)
            if match:
                # Store the folder name and its number for sorting
                chapters.append((int(match.group(1)), d))

    # Sort the chapters by their number
    chapters.sort()

    # The content of the main.tex file
    main_tex_content = []
    
    # Add document class and preamble
    main_tex_content.append(r"\documentclass{report}")
    main_tex_content.append(r"\usepackage{xcolor}") # Example of a package that could be in a preamble
    main_tex_content.append(r"\input{preamble.tex}")
    main_tex_content.append(r"")

    # Add title, author, and date
    main_tex_content.append(r"\title{Yanshu Wang's Notebook}")
    main_tex_content.append(r"\author{Yanshu Wang}")
    main_tex_content.append(r"\date{\today}")
    main_tex_content.append(r"")

    # Begin the document, create the title page, and then start the main content
    main_tex_content.append(r"\begin{document}")
    main_tex_content.append(r"\maketitle")
    
    # Add an \include command for each chapter
    for _, chapter_folder in chapters:
        # Assuming the chapter file inside is named the same as the folder, but with a .tex extension
        chapter_file_path = f"{chapter_folder}/main.tex"
        main_tex_content.append(f"\\subfiles{{{chapter_file_path}}}")

    main_tex_content.append(r"")
    main_tex_content.append(r"\end{document}")
    
    # Write the content to main.tex
    with open(main_tex_path, 'w') as f:
        f.write('\n'.join(main_tex_content))

    print(f"main.tex has been successfully generated with {len(chapters)} chapters.")

if __name__ == "__main__":
    generate_main_tex()
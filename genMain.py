import os
import re

def generate_main_tex():
    # Define the project root and the main LaTeX file
    project_root = os.path.dirname(os.path.abspath(__file__))
    main_tex_path = os.path.join(project_root, 'main.tex')

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
    main_tex_content.append(r"\documentclass{report}")
    main_tex_content.append(r"")  # Add a blank line for readability
    main_tex_content.append(r"\begin{document}")

    # Add an \include command for each chapter
    for _, chapter_folder in chapters:
        # Assuming the chapter file inside is named the same as the folder, but with a .tex extension
        chapter_file_path = f"{chapter_folder}/{chapter_folder}.tex"
        main_tex_content.append(f"\\include{{{chapter_file_path}}}")

    main_tex_content.append(r"\end{document}")
    
    # Write the content to main.tex
    with open(main_tex_path, 'w') as f:
        f.write('\n'.join(main_tex_content))

    print(f"main.tex has been successfully generated with {len(chapters)} chapters.")

if __name__ == "__main__":
    generate_main_tex()


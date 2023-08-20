# Extracting (some) Annotations from PDFs

A short script that uses the [pypdf](https://pypi.org/project/pypdf/) library to extract a list of annotations from a PDF. 

Currently only works for the following types of annotations:
- Highlighted Notes:
<img src="https://github.com/sonebu/pdf-annotation-extraction/assets/25130839/5380a7d7-3676-4310-8ab3-a8611f8eda5f" width=30% height=30%>

- "Caret" annotations (strikethrough, but with a text suggestion):
<img src="https://github.com/sonebu/pdf-annotation-extraction/assets/25130839/c1b6addf-216f-4fc3-bc71-cf8252ab8cd0" width=10% height=10%>

- Strikethrough annotations (just says "remove this part"):
<img src="https://github.com/sonebu/pdf-annotation-extraction/assets/25130839/29834bf8-580d-4b90-b3f4-f99683146f3e" width=10% height=10%>


Probably useful for grad students who need to make sure they address every comment/annotation their advisor or a reviewer makes on a PDF they shared (e.g., article, response letter etc.). I used this to simply generate a list of action items over which I can check my work and tell whether I missed a review point / comment. 

Note that the annotations are saved as vector items on the page coordinate frame rather than as attached to certain parts of the text, which is how the author typically remembers parts of the text. In other words, you don't get which word was striked out, you can only get its location on the page, and that is not extremely useful since it's in some metric form that is not intuitive. 

### Installation

Just install [pypdf](https://pypi.org/project/pypdf/) via `pip install pypdf`

### Usage

`python extract_annotations.py pdffile.pdf > example_output.txt`

### References

Inspired by the following discussions:
- https://superuser.com/questions/698811/how-to-export-comments-from-a-pdf-file
- https://stackoverflow.com/a/12502560/3811558
- https://stackoverflow.com/a/54823050/3811558
- https://unix.stackexchange.com/questions/520258/way-to-search-pdf-for-annotations-edits-and-other-review-markings

and the following page from the pypdf documentation:
- https://pypdf.readthedocs.io/en/stable/user/reading-pdf-annotations.html?highlight=annots#text

IF [%1] == [] (
    echo Pls input argument. 
    goto :EOF
)

set FOLDER=%1
set CURRENTFOLDER=%~dp0
python %CURRENTFOLDER%\find_untrans_pdfs.py %FOLDER%
rem python %CURRENTFOLDER%\test_pdf2docx.py %FOLDER%
python %CURRENTFOLDER%\doc_to_docx.py %FOLDER%
python %CURRENTFOLDER%\trans_docx3.py %FOLDER%
python %CURRENTFOLDER%\test_docx2pdf.py %FOLDER%

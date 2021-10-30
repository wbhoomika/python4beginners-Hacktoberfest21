#we first need to install docx by pip install python-docx
#we then need to insatll pyttsx3 by pip install pyttsx3
#we then need to install PyPDF2 by pip install PyPDF2
"""
In this python script we are trying to open a pdf file and make an automatic text to speech converter
we are able to do this using pyttsx to make a offline text to speech convertor
this does not save a audio file and it will directly run the speech function
we are able to read the pdf file by using the package PyPDF2
We have also added the readability of docx files
and this is done using docx package
this package helps us to read simple pdf text files
"""
import docx
import pyttsx3
import PyPDF2

#getting the path
path = input("Please give us the path to the pdf file or docx(Word) file")
mytext=""
#checking if it is of proper file type
if(path.endswith(".pdf") or path.endswith(".docx")):
    try:
        #we use a try and except block to check if we can open the file
        if(path.endswith(".pdf")):
            #reading the pdf file
            pdfFileObj = open(path, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            for i in range (0,pdfReader.numPages):
                mytext+=pdfReader.getPage(i).extractText()
        else:
            #reading the docx file
            text=[]
            doc= docx.Document(path)
            for para in doc.paragraphs:
                mytext+=para.text
            print(mytext)
    except (Exception) as e:
        # if we cant open the file or an error occurs during reading
        print(e)
    if(mytext!=""):
        try:
            #the text to speech function
            engine=pyttsx3.init()
            engine.say(mytext)
            engine.runAndWait()
        except (Exception)as e:
            print(e)
    else:
        print("The given path does contains a empty pdf file")
    
else:
    # if the type is not correct
    print("Please ensure that u provide a pdf or docx file")

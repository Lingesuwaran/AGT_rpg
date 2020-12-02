import fitz
file_name=input("Enter the file name with extention")
pdf=fitz.open("/content/Books"+file_name)
n=pdf.pageCount
for i in range(n):
  page = pdf.loadPage(i)
  text = page.getText('text')
  with open('data.txt','a')as file:
	  file.write(text.replace('\t',''))
pdf.close()

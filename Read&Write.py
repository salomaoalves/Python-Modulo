#WRITE EM ARQUIVOS
#arq = open('Teste.docx','w')
texto1 = "Hello World \n To doidão \n\n"
#arq.write(texto1)
texto = ['Lista de Alunos\n','-----------\n','Jooao\n','Jorge']
#arq.writelines(texto)

#READ EM ARQUIVOS
arq = open('Teste.docx','r')
#texto1 = arq.read()
texto1 = arq.readlines()
print(texto1)
#print(texto1[1])

arq.close()
Bem-vindo à documentação do projeto Healthy.
Este documento fornece informações sobre como instalar, configurar e contribuir com o projeto.


1. Visão Geral do Projeto
O Healthy é uma plataforma projetada para proporcionar uma experiência completa e personalizada na busca por uma vida mais saudável e equilibrada. Abrangendo áreas como nutrição, exercícios e gestão do peso corporal, o projeto oferece funcionalidades para auxiliar os usuários em sua jornada para uma vida mais saudável.

Contribuidores
Júlia Veríssimo - jov@cesar.school
Lucca da Veiga - lvg2@cesar.school
Luiz Flavius - lfvsf@cesar.school
Luisa Coimbra - mlcl@cesar.school
Luiza Calife - mlcdf@cesar.school
Mirna Lustosa - mlam@cesar.school

2. Instalação
Siga os passos abaixo para instalar o projeto localmente:
Para configurar o ambiente e iniciar a aplicação, siga os passos abaixo:
-Clonar o repositório do projeto com o seguinte comando:
git clone https://github.com/Luiiizks/Projeto-Healthy
ou, para clonar apenas a versão mais recente:
git clone --depth=1 https://github.com/Luiiizks/Projeto-Healthy
-Instale as extensões necessárias no VS Code:
Após abrir o VS Code, pesquise e instale as seguintes extensões:
ms-python.vscode-pylance
ms-python.python
batisteo.vscode-django
-Crie um ambiente virtual executando o comando:
python -m venv venv
-Ative o ambiente virtual (para Windows) com o seguinte comando:
venv\Scripts\activate
-Instale as dependências do projeto a partir do arquivo requirements.txt:
pip install -r ./requirements.txt

3. Uso
Inicie a aplicação executando, no terminal, o comando:
 “ manage.py runserver “ 

Acesse http://localhost:3000 para utilizar a aplicação.

4. Contato
Para dúvidas ou mais informações, entre em contato através do e-mail: juliiaveriisiimo@gmail.com

5. Como fazer sua contribuição
Faça um fork do projeto.
Crie uma branch com as suas modificações git checkout -b exemplo.
Faça commit das suas alterações git commit -m 'Implementação do exemplo'
Faça um push na sua branch git push origin exemplo.
Faça um pull request com suas alterações.

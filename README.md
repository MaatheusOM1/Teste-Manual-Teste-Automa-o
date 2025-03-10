🛒 Teste Automatizado com Selenium e API

📌 Descrição
Este repositório contém scripts para automação de testes no site Advantage Online Shopping. As funcionalidades cobertas incluem:

✅ Testes Web com Selenium:

Busca e adição de produtos ao carrinho
Verificação do carrinho
Tratamento de erros comuns
✅ Testes de API com Requests:

Registro de um novo usuário
Login e obtenção de token
Busca de produtos
Atualização da imagem de um produto
⚙️ Requisitos
🔹 Ambiente necessário:

Python (3.x recomendado)
Google Chrome
ChromeDriver compatível
Bibliotecas Python: selenium, requests
📥 Instalação das dependências:

sh
Copiar
Editar
pip install selenium requests
🔍 Baixe e configure o ChromeDriver:

Verifique sua versão do Chrome acessando:
arduino
Copiar
Editar
chrome://settings/help
Baixe a versão correspondente do ChromeDriver:
https://sites.google.com/chromium.org/driver/
Adicione o ChromeDriver ao PATH do sistema (se necessário).
🚀 Como Executar
🖥️ Testes Web (Selenium)
sh
Copiar
Editar
python teste_selenium.py
🌐 Testes de API (Requests)
sh
Copiar
Editar
python teste_api.py
🔎 Teste Web com Selenium
📌 Passos executados:
✅ Acessa o site
✅ Busca o produto "HP CHROMEBOOK 14 G1(ES)"
✅ Adiciona o produto ao carrinho
✅ Confirma se o item está no carrinho
✅ Trata exceções (TimeoutException, StaleElementReferenceException)

⚠️ Possíveis problemas e soluções:

❌ Erro de compatibilidade com o ChromeDriver → Atualize o Chrome e o driver
❌ Elementos não encontrados → Aumente o tempo de espera no Selenium
🌐 Testes de API
📌 Passos executados:
✅ Cria um usuário via API
✅ Realiza login e obtém token JWT
✅ Busca um produto na API
✅ Atualiza a imagem do produto autenticado

⚠️ Possíveis problemas e soluções:

❌ Erro 401 (Unauthorized) → Verifique o login e token
❌ Erro 500 na API → O servidor pode estar fora do ar

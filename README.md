<h1>🛠️ Teste Automatizado com Selenium e API</h1>

<h2>📌 Descrição</h2>
<p>Este repositório contém scripts para automação de testes no site <strong>Advantage Online Shopping</strong>. As funcionalidades cobertas incluem:</p>

<ul>
<li>✅ Acesso ao site e busca de produtos usando Selenium</li>
<li>✅ Adição de produtos ao carrinho e verificação do carrinho</li>
<li>✅ Registro de um novo usuário via API</li>
<li>✅ Login do usuário registrado e obtenção de token de autenticação</li>
<li>✅ Busca de produtos na API</li>
<li>✅ Atualização da imagem de um produto via API</li>
</ul>

<hr>

<h2>📋 Requisitos</h2>
<p>Antes de executar os scripts, certifique-se de ter os seguintes itens instalados:</p>

<ul>
<li><strong>Python</strong></li>
<li><strong>Google Chrome</strong></li>
<li><strong>WebDriver compatível</strong> com a versão do Chrome (Chromedriver)</li>
<li><strong>Bibliotecas Python:</strong></li>
<ul>
<li><code>selenium</code></li>
<li><code>requests</code></li>
</ul>
</ul>

<h3>🔧 Instalação</h3>

<ol>
<li>Instale as bibliotecas necessárias via pip:</li>
<pre><code>pip install selenium requests</code></pre>

<li>Baixe e configure o ChromeDriver:</li>
<ul>
<li>Verifique sua versão do Chrome digitando na barra de endereço:</li>
<pre><code>chrome://settings/help</code></pre>

<li>Baixe a versão correspondente do ChromeDriver em: <a href="https://sites.google.com/chromium.org/driver/">Google ChromeDriver</a></li>
<li>Adicione o caminho do ChromeDriver ao sistema (caso necessário) ou apenas coloque na mesma pasta dos aquivos python</li>
</ul>
</ol>

<hr>

<h2>🚀 Como Executar</h2>

<ol>
<li>Salve os códigos em arquivos Python separados (ex: <code>teste_selenium.py</code> e <code>teste_api.py</code>)</li>
<li>Execute os scripts no terminal ou prompt de comando:</li>
<pre><code>python teste_selenium.py
python teste_api.py</code></pre>
</ol>

<hr>

<h2>🖥️ Teste Web com Selenium</h2>
<p>O script de <strong>Selenium</strong> realiza:</p>

<ul>
<li>🔹 Acesso ao site</li>
<li>🔹 Busca do produto <strong>"HP CHROMEBOOK 14 G1(ES)"</strong></li>
<li>🔹 Cliques nos elementos corretos para adicionar ao carrinho</li>
<li>🔹 Verificação da presença do produto no carrinho</li>
<li>🔹 Tratamento de erros comuns, como <code>TimeoutException</code> e <code>StaleElementReferenceException</code></li>
</ul>

<hr>

<h2>🌐 Testes de API</h2>
<p>O script de <strong>API</strong> realiza:</p>

<ol>
<li>**Registro de um novo usuário** via API</li>
<li>**Login do usuário** registrado e obtenção de token</li>
<li>**Busca de um produto** na API</li>
<li>**Atualização da imagem** do produto usando autenticação JWT</li>
</ol>

<h3>🛑 Atenção</h3>
<ul>
<li><strong>Para a parte de criação de usuário, certifique-se de usar um nome de login único e senha contendo letras, números e caracteres especiais, a fim de não ocorrer problemas</strong></li>
<li><strong>Baixe uma imagem de sua preferência e salve no mesmo local do programa com o nome "imagem.jpg" (obrigatório ser jpg)</strong></li>
</ul>

<h3>❗ Possíveis Problemas e Soluções</h3>

<p>⚠️ <strong>Se o teste falhar, verifique:</strong></p>
<ul>
<li>Se o site está online</li>
<li>Se o ChromeDriver é compatível com sua versão do Chrome</li>
</ul>

<hr>

<h2>📌 Considerações Finais</h2>

<ul>
<li>🔹 O script de <strong>Selenium</strong> inclui um <code>time.sleep(15)</code> antes de fechar o navegador para que o usuário possa visualizar o resultado.</li>
<li>🔹 O script de <strong>API</strong> lida com autenticação e envio de arquivos.</li>
<li>🔹 Para aumentar a robustez, considere utilizar logs e screenshots para melhor depuração.</li>
</ul>

<hr>

<p>📌 <em>Matheus Oliveira Macedo</em></p>

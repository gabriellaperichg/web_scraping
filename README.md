## Web Scraping com Scrapy

### Iniciar projeto

1. `$ source venv\Scripts\activate`
2. `$ pip install scrapy`
3. `$ scrapy startproject [nome_do_projeto]`
4. `$ scrapy genspider [nome] [link]`

O Spider faz:

- Request (acessar o site);
- Parser (de/para);
- Next_page (troca de páginas)

`$ scrapy shell`

- No terminal, testar e encontrar as informações no HTML
- Escrever o código no arquivo .py do spider
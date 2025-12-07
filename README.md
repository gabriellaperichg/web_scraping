## Web Scraping com Scrapy

### Iniciar projeto

`$ source venv\Scripts\activate`
`$ pip install scrapy`
`$ scrapy startproject [nome_do_projeto]`
`$ scrapy genspider [nome] [link]`

O Spider faz:

- Request (acessar o site);
- Parser (de/para);
- Next_page (troca de páginas)

`$ scrapy shell`
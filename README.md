# Agregador de conteúdo web

Rss é um formato de  protocolo que consegue entregar feeds sobre qualquer coisa. Deriva do XML, porém, a principal
diferença está na abordagem realizada sobre o sistema: enquanto o XML mapeia a hierarquia e
lista as URLs no sitemap, o RSS retorna as últimas alterações, isso é, as novidades naquele sistema.
Um ponto interessante também está no fato de arquivos RSS serem menores que os XML, pois retornam um número menor de resultados.


A premissa da aplicação aggreGATOR é agregar essas informações em uma interface web, cumprindo a função de um agregador RSS,
que primariamente separa e organiza os sites cadastrados em  páginas, e dentro dessas páginas mostram as últimas novidades,
junto com um link para o conteúdo completo.

Começamos requisitando os dados RSS da página com a biblioteca requests, e parseando esse resultado com a
biblioteca BeautifulSoup.

À partir de então, temos uma string, que será o bloco de texto do blog. Salvamos eles em arquivos. Os mesmos serão
carregados toda vez que iniciarmos o script.


O script principal, por si só, chamará APLICAÇÃO, que usará a biblioteca Flask para criar páginas web formatadas. O site terá interfaces de usuário e mostrará posts salvos de blogs.

# Usage

```python
source ./caminho-para-virtualenv/venv/bin/activate #ativa a virtualenv
cd news-feed
sh serve.sh #serve o Flask. A porta socket é "localhost:5000" ou "127.0.0.1:5000" no browser.
```


# Implementações

[X] selecionar 1 site pra pegar o RSS
[]  converter

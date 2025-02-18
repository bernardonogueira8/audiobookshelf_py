# Ebooks para pastas de Livros

## Descrição

Este script automatiza a criação de pastas individuais para cada livro/ebook para ser enviado para **Audiobookshelf**. Ele facilita a organização da biblioteca, garantindo que cada audiolivro/ebook tenha sua próprio diretório.

## Requisitos

-   Python 3.x

## Instalação

1. Clone este repositório:
    ```bash
    git clone https://github.com/bernardonogueira8/audiobookshelf_py.git
    ```
2. Navegue até o diretório do projeto:
    ```bash
    cd audiobookshelf_py
    ```
3. (Opcional) Crie um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/Mac
    venv\Scripts\activate  # Windows
    ```

## Uso

1. Crie uma pasta chamada `Autor Desconhecido` e coloque os arquivos ebook.
2. Execute o script para criar as pastas conforme os nomes dos livros:

```bash
python criar_pastas.py
```

## Contribuição

1. Fork este repositório.
2. Crie um branch para sua melhoria:
    ```bash
    git checkout -b minha-melhoria
    ```
3. Realize suas alterações e faça commit:
    ```bash
    git commit -m "Melhoria: Adicionada nova funcionalidade"
    ```
4. Envie para o repositório remoto:
    ```bash
    git push origin minha-melhoria
    ```
5. Crie um Pull Request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).

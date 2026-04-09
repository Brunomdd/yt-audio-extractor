# yt-audio-extractor

Aplicação de linha de comando em Python para baixar o **áudio** de vídeos do YouTube a partir de uma URL informada pelo usuário.

O objetivo é oferecer uma ferramenta simples, rápida e amigável no terminal para extrair apenas o áudio de vídeos (por exemplo, para ouvir offline).

---

## Funcionalidades

- Validação de URL (garante que é uma URL válida **e** do YouTube).
- Exibição de informações do vídeo antes do download (título, duração em minutos/segundos, etc.).
- Download do **áudio** usando `get_audio_only()` da biblioteca `pytubefix`.
- Escolha do diretório de destino (criação automática se não existir).
- Tratamento de erros mais comuns durante o download.
- Interface de menu no terminal com opções:
  - `1 - Converter`
  - `2 - Histórico de Download` (planejado)
  - `3 - Sair`

---

## Dependências

### Linguagem

- **Python 3.8+** (recomendado)

### Bibliotecas Python

Instale as dependências manualmente:

```bash
pip install pytubefix colorama validators
```

- [`pytubefix`](https://pypi.org/project/pytubefix/): fork do `pytube` para download de vídeos/áudios do YouTube.[web:317]
- [`colorama`](https://pypi.org/project/colorama/): adiciona cores ao terminal de forma portátil (Windows, Linux, macOS).[web:321]
- [`validators`](https://validators.readthedocs.io/): fornece funções de validação, incluindo validação de URL.[web:322]

Outras dependências são da biblioteca padrão do Python (`os`, etc.).

---

## Instalação

Clonar o repositório:

```bash
git clone https://github.com/seu-usuario/yt-audio-extractor.git
cd yt-audio-extractor
```

Criar e ativar um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

Instalar as dependências:

```bash
pip install pytubefix colorama validators
```

---

## Como usar

Execute o script principal:

```bash
python main.py
```

Você verá algo como:

```text
------------------------------
        yt-audio-extractor
------------------------------
1 - Converter
2 - Historico de Download
3 - Sair
escolha uma opção:
```

### Opção 1 – Converter

Fluxo da opção **Converter**:

1. **URL**  
   - O programa pede a URL do vídeo.
   - Valida se é uma URL bem formada (`validators.url(url)`).
   - Valida se pertence ao domínio do YouTube (`"youtube.com"` ou `"youtu.be"`).

2. **Criação do objeto `YouTube`**  
   - Se a URL for válida, é criado um objeto `yt = YouTube(url)` (a partir de `pytubefix`).  

3. **Destino do arquivo**  
   - Você informa o diretório de destino.
   - Se deixar em branco, o diretório padrão é o atual (`.`).
   - Se informar um caminho, o diretório é criado automaticamente com `os.makedirs(destino, exist_ok=True)`.

4. **Interface do vídeo**  
   - A função `interface(yt)` é chamada para exibir:
     - Título do vídeo.
     - Canal (se desejado).
     - Duração convertida de segundos para **minutos e segundos**.
     - Outras informações úteis.

5. **Confirmação de download**  
   - O programa pergunta: `Quer baixar o arquivo? [S/N]:`
   - A função `confirmar` obriga a resposta a ser `S` ou `N` (case insensitive), repetindo em caso de erro.

6. **Download do áudio**  
   - Se a resposta for `S`, chama `baixar_audio(yt, destino)`.
   - Em caso de sucesso, mostra o caminho completo do arquivo gerado.
   - Em caso de erro, mostra uma mensagem amigável explicando o problema.

### Opção 2 – Histórico de Download

- Ainda não implementado.
- Ideia futura:
  - Registrar cada download em um arquivo (JSON, CSV ou banco de dados).
  - Exibir a lista de downloads anteriores (data, título, URL, caminho do arquivo).

### Opção 3 – Sair

- Imprime uma mensagem de saída e encerra o programa.

---

## Estrutura do projeto

```text
yt-audio-extractor/
├── main.py          # Ponto de entrada, menu e fluxo principal
├── baixar.py        # Função baixar_audio(yt, destino)
├── interface.py     # Exibição de informações do vídeo (título, duração, etc.)
├── uteis.py         # Funções auxiliares: cabecalho, linha, leiaint, confirmar...
└── README.md        # Este arquivo
```

---

## Explicação dos módulos

### `main.py`

Responsável por:

- Exibir o menu.
- Ler e validar opções do usuário.
- Ler e validar URL do YouTube.
- Criar o objeto `YouTube`.
- Perguntar destino e criar pasta, se necessário.
- Chamar:
  - `interface(yt)` para mostrar informações.
  - `baixar_audio(yt, destino)` para fazer o download.

---

### `uteis.py`

Funções auxiliares que deixam o código mais organizado:

- `linha(txt=32)`: retorna uma string com `-` repetidos (separador visual).
- `cabecalho(txt)`: imprime um cabeçalho com bordas, centralizando o texto.
- `leiaint(msg)`: lê um inteiro do usuário, tratando `ValueError` e exibindo mensagem de erro amigável (com `colorama`).
- `confirmar(msg)`: só aceita respostas `S` ou `N`, repetindo enquanto a entrada for inválida.

---

### `baixar.py`

Encapsula a lógica de download do áudio:

```python
def baixar_audio(yt, destino='.'):
    try:
        audio = yt.streams.get_audio_only()
        audio_final = audio.download(output_path=destino)
        return {"status": "sucesso", "caminho": audio_final}
    except VideoRemovedByYouTubeForViolatingTOS:
        return {"status": "erro", "mensagem": "o áudio foi removido do youtube por violar os direitos autorais"}
    except VideoUnavailable:
        return {"status": "erro", "mensagem": "o áudio está indisponível"}
    except Exception as error:
        return {"status": "erro", "mensagem": f"Erro ao baixar o áudio: {error}"}
```

---

### `interface.py`

Responsável por exibir informações amigáveis do vídeo:

- Recebe o objeto `yt`.
- Mostra título, canal, duração, etc.
- Converte `yt.length` (segundos) para minutos e segundos para exibição.

---

## Tratamento de erros

- Erros de entrada:
  - Menu: `leiaint` garante inteiro válido.
  - Confirmação: `confirmar` garante resposta `S` ou `N`.
  - URL: validação com `validators` e checagem do domínio YouTube.
- Erros de download:
  - Vídeo removido por violação de termos.
  - Vídeo indisponível.
  - Exceções genéricas tratadas com mensagem descritiva.

---

## Ideias futuras

- Implementar o **Histórico de Download**.
- Permitir escolher qualidade/bitrate do áudio.
- Adicionar testes automatizados com `pytest`.
- Suporte a múltiplos idiomas (pt-BR, en, etc.).

---

## Licença

Este projeto está licenciado sob a licença MIT.


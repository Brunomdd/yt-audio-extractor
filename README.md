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

- [`pytubefix`](https://pypi.org/project/pytubefix/): fork do `pytube` para download de vídeos/áudios do YouTube com correções mais recentes.[web:317]
  - Usado para criar objetos `YouTube` e acessar `yt.streams.get_audio_only()`.
- [`colorama`](https://pypi.org/project/colorama/): adiciona cores ao terminal de forma portátil (Windows, Linux, macOS).[web:321]
  - Usado para destacar mensagens de erro, sucesso e cabeçalhos.
- [`validators`](https://validators.readthedocs.io/): fornece funções de validação, incluindo validação de URL.[web:322]
  - Usado para checar se a URL informada é bem formada (antes de testar se é do YouTube).

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
pip install -r requirements.txt
```

Se você ainda não tiver o `requirements.txt`, pode gerar assim (no seu ambiente local):

```bash
pip freeze > requirements.txt
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
   - Se a URL for válida, é criado um objeto `yt = YouTube(url)` (a partir de `pytubefix`).[web:292]

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

## Estrutura do projeto (sugestão)

```text
yt-audio-extractor/
├── main.py          # Ponto de entrada, menu e fluxo principal
├── baixar.py        # Função baixar_audio(yt, destino)
├── interface.py     # Exibição de informações do vídeo (título, duração, etc.)
├── uteis.py         # Funções auxiliares: cabecalho, linha, leiaint, confirmar...
├── requirements.txt # Dependências do projeto
└── README.md        # Este arquivo
```

---

## Explicação dos módulos e funções

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

Esse módulo é o “cérebro” do fluxo da aplicação.

---

### `uteis.py`

**Objetivo:** concentrar funções reutilizáveis, deixando o código mais limpo e organizado.

- `linha(txt=32)`  
  Retorna uma string com `-` repetidos, usada como separador visual no terminal.

- `cabecalho(txt)`  
  Imprime um cabeçalho com bordas usando `linha()`, centralizando o texto em 32 caracteres. Pode ser combinado com `Fore` e `Style` (do `colorama`) para colorir o título.

- `leiaint(msg)`  
  Lê um número inteiro do usuário, tratando `ValueError`:
  - Enquanto o usuário não digitar um inteiro válido, mostra uma mensagem de erro em vermelho usando `colorama`.

- `confirmar(msg)`  
  Lê uma resposta do usuário e só aceita `S` ou `N`:
  - Remove espaços (`strip()`).
  - Converte para maiúsculas (`upper()`).
  - Se for diferente de `S` ou `N`, mostra mensagem de erro em vermelho e pergunta novamente.

---

### `baixar.py`

**Objetivo:** encapsular toda a lógica de download do áudio.

Assinatura atual (conceito):

```python
def baixar_audio(yt, destino='.'):
    ...
```

Passos principais:

1. Recebe um objeto `YouTube` já instanciado e um destino.
2. Seleciona o stream de áudio:
   ```python
   audio = yt.streams.get_audio_only()
   ```
3. Baixa o arquivo de áudio para a pasta de destino:
   ```python
   audio_final = audio.download(output_path=destino)
   ```
4. Retorna um dicionário com:
   - Em caso de sucesso:
     ```python
     {"status": "sucesso", "caminho": audio_final}
     ```
   - Em caso de erro específico:
     - `VideoRemovedByYouTubeForViolatingTOS`: áudio removido por violação de direitos/autorização.
     - `VideoUnavailable`: áudio indisponível.
   - Em caso de erro genérico:
     ```python
     {"status": "erro", "mensagem": f"Erro ao baixar o áudio: {error}"}
     ```

---

### `interface.py`

**Objetivo:** mostrar informações amigáveis do vídeo antes do download.

Fluxo típico:

- Recebe o objeto `yt` (instância de `YouTube`).
- Lê atributos como:
  - `yt.title`
  - `yt.author` (ou canal)
  - `yt.length` (duração em segundos)[web:292]
- Converte `yt.length` em minutos e segundos:
  - `minutos = yt.length // 60`
  - `segundos = yt.length % 60`
- Imprime essas informações formatadas e, opcionalmente, com cores (`colorama`).

---

## Tratamento de erros

O projeto trata erros em dois níveis:

1. **Erros de entrada do usuário**
   - Números inválidos no menu → tratados por `leiaint`.
   - Respostas diferentes de `S` ou `N` → tratadas por `confirmar`.
   - URL inválida ou que não é do YouTube → bloqueia antes de tentar criar o objeto `YouTube`.

2. **Erros de download / YouTube**
   - Vídeo removido por violação de termos.
   - Vídeo indisponível.
   - Exceções genéricas (problemas de rede, mudanças na API, etc.).

As mensagens são pensadas para serem claras e amigáveis para o usuário.

---

## Ideias de futuras melhorias

- Implementar o **Histórico de Download**:
  - Gravar cada download em um arquivo (JSON, CSV ou SQLite).
  - Mostrar uma lista de downloads com filtros (por data, por vídeo, etc.).
- Permitir escolher:
  - Qualidade/bitragem de áudio.
  - Formato de saída (por exemplo, `.mp3` após conversão).
- Criar testes automatizados com `pytest` para:
  - `uteis.py` (validação de entrada).
  - `baixar.py` (com mocks para não chamar o YouTube de verdade).
- Adicionar suporte a múltiplos idiomas (pt-BR, en, etc.).

---

## Licença

Este projeto está licenciado sob a licença MIT.


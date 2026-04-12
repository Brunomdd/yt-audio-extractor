# yt-audio-extractor

Aplicação de linha de comando em Python para baixar o **áudio** de vídeos do YouTube a partir de uma URL informada pelo usuário.

O projeto usa a biblioteca [`pytubefix`](https://pypi.org/project/pytubefix/) para acessar os streams do YouTube, `colorama` para destacar mensagens no terminal e `validators` para validar URLs.

---

## Funcionalidades

- Validação de URL (estrutura válida **e** domínio do YouTube).
- Exibição de informações do vídeo antes do download (incluindo duração em minutos e segundos).
- Download apenas do **áudio** do vídeo.
- Escolha do diretório de destino, com criação automática se não existir.
- Tratamento de erros comuns (vídeo removido, indisponível, etc.).
- Interface simples de menu no terminal:
  - `1 - Converter`
  - `2 - Histórico de Download` (planejado)
  - `3 - Sair`

---

## Tecnologias e dependências

- **Linguagem:** Python 3.8+ (recomendado)
- **Bibliotecas:**
  - [`pytubefix`](https://pypi.org/project/pytubefix/) – download de vídeos/áudios do YouTube.[web:317]
  - [`colorama`](https://pypi.org/project/colorama/) – texto colorido no terminal.
  - [`validators`](https://python-validators.github.io/validators/reference/url/) – validação de URLs.

Instalação das dependências:

```bash
pip install pytubefix colorama validators
```

---

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seu-usuario/yt-audio-extractor.git
cd yt-audio-extractor
```

( Opcional, mas recomendado ) Crie e ative um ambiente virtual:

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# ou
.venv\Scripts\activate     # Windows
```

Instale as dependências:

```bash
pip install pytubefix colorama validators
```

---

## Como usar

Execute o script principal:

```bash
python main.py
```

Você verá um menu como:

```text
------------------------------
        yt-audio-extractor
------------------------------
1 - Converter
2 - Historico de Download
3 - Sair
escolha uma opção:
```

### Fluxo da opção “Converter”

1. Informe a **URL** do vídeo do YouTube.
2. O sistema valida:
   - se a URL é bem formada (`validators.url`);
   - se o domínio pertence ao YouTube (`youtube.com` ou `youtu.be`)
3. Se for válida, o sistema carrega os dados do vídeo com `pytubefix.YouTube`
4. Informe o **diretório de destino**:
   - Se deixar em branco, será usado o diretório atual (`.`).
   - Se informar um caminho, ele será criado se não existir.
5. O sistema exibe informações do vídeo, incluindo a **duração convertida para minutos e segundos**.
6. Você confirma se quer baixar o arquivo (`[S/N]`):
   - Em caso de **S**, o áudio é baixado para o diretório escolhido.
   - Em caso de **N**, o download é cancelado e o menu é exibido novamente.

### Opção “Histórico de Download”

- Reservada para implementação futura de um histórico (lista de downloads realizados).

### Opção “Sair”

- Mostra uma mensagem de encerramento e finaliza a aplicação.

---

## Regras de negócio (resumo)

- Só URLs válidas e do domínio YouTube são aceitas para download.
- A duração do vídeo é sempre mostrada em **minutos e segundos** antes de baixar.
- O usuário deve confirmar explicitamente o download (`S` ou `N`); qualquer outra resposta é rejeitada até ser digitado um valor válido.
- Diretório em branco significa “diretório atual”; diretórios informados são criados automaticamente se não existirem.
- Em qualquer erro de download (vídeo removido, indisponível ou erro inesperado), nenhuma saída parcial é considerada válida e o usuário é informado com mensagem clara.

---

## Estrutura do projeto

```text
yt-audio-extractor/
├── main.py          # Ponto de entrada, menu e fluxo principal
├── baixar.py        # Lógica de download do áudio
├── interface.py     # Exibição das informações do vídeo
├── uteis.py         # Funções auxiliares e validações de entrada
└── README.md        # Documentação do projeto
```

---

## Futuras melhorias

- Implementar o **Histórico de Download**.
- Permitir escolher qualidade/bitrate do áudio.
- Adicionar testes automatizados.
- Suporte a múltiplos idiomas.

---

## Licença

Este projeto está licenciado sob a licença MIT.  

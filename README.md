# TOPGAME
Um simples RPG, feito em python. Sem interfaces apenas sobre o terminal. 

~ Execute o arquivo "main.py"

### Menus
- menu iniciar
    - novo jogo
    - salvos
    - sair
- menu principal
    - batalha
        - atacar
        - defender
        - magia
        - fugir
    - mercado
        - armas
        - escudos
        - armaduras
        - poções
        - magias
        - sair
    - status
    - salvar
    - sair

### Arquivos
- main.py
    - clear.py
    - story.py
    - games.py
        - clear.py
        - option.py
    - batalha.py
        - clear.py
        - option.py
        - storage.py
        - fight.py
            - option.py
            - suspense.py
            - damage.py
                - suspense.py
        - market.py
            - clear.py
            - option.py
            - show_items.py
            - show_player_items.py
            - buy.py
            - items.py
            - sell.py
                - update_player_stats.py

### Nova Estrutura
TOPGAME/
│
├── TOPGAME/                  
│   ├── __init__.py
│   ├── main.py                     # Arquivo principal que inicializa o jogo
│   ├── battle/                     # Lógica de batalha
│   │   ├── __init__.py
│   │   ├── battle.py               # 
│   │   ├── fight.py                # Controle da luta
│   │   ├── damage.py               # Lógica de dano
│   │   └── option.py               # Opções durante a luta
│   ├── game/                       # Mecânicas gerais do jogo
│   │   ├── __init__.py
│   │   ├── clear.py                # Funções de limpar tela ou estados
│   │   └── story.py                # Lógica de história e enredo
│   ├── market/                     # Sistema de mercado
│   │   ├── __init__.py
│   │   ├── market.py               # 
│   │   ├── buy.py                  # Lógica de compra
│   │   ├── sell.py                 # Lógica de venda
│   │   ├── items.py                # Definição dos itens disponíveis
│   │   ├── update_player_stats.py  # Atualização dos atributos do jogador
│   │   ├── show_items.py           # Exibição de itens
│   │   └── show_player_items.py    # Exibição de itens do jogador
│   ├── storage/                    # Controle de dados persistentes
│   │   ├── __init__.py
│   │   ├── games.py                # 
│   │   ├── storage.py              # Lógica para salvar/carregar progresso
│   ├── utils/                      # Utilitários e funções auxiliares
│   │   ├── __init__.py
│   │   ├── option.py               #
│   │   ├── clear.py                # Função para limpar tela
│   │   └── suspense.py             # Controle de suspense nas batalhas
│   └── README.md                   # Descrição do projeto
│
├── tests/                          # Testes unitários
│   ├── test_battle.py
│   ├── test_market.py
│   └── test_storage.py
│
├── .gitignore                      # Arquivo Gitignore
└── requirements.txt                # Dependências do projeto (se houver)

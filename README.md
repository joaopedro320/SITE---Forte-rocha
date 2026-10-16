# Marmoraria Forte Rocha — site institucional (padrão QH4)

Site estático no layout do site original do cliente (cores, fontes Raleway/Open Sans, logo e ordem das seções), com SEO + AEO + GEO. Sem dependências externas de JS.

## Como editar
- Textos fixos: `src/sections/*.html` · layout geral: `src/layout.html`
- Dados (empresa, serviços, obras, pedras, acabamentos, FAQ): `src/data.py`
- Depois de editar: `python3 src/build.py` (gera as páginas, sitemap, robots, llms.txt, 404 e manifest)

## Páginas
`/` · `/empresa/` · `/servicos/` · `/obras/` · `/produtos/` · `/dicas/` · `/contato/`

As URLs antigas (`empresa.html`, `servicos.html`, `produtos.html` etc.) redirecionam para as novas.

## Pendências (conferir com o cliente)
- CEP e coordenada exata (`EMPRESA['cep']`, `lat`/`lng`) — hoje a coordenada aponta para o centro de Paulínia
- Dias de funcionamento (o site antigo só informa 8h–17h; deixei segunda a sexta)
- Área atendida ("Paulínia e região de Campinas")
- `GTM_ID` em `src/data.py`
- Fotos: as do site antigo têm baixa resolução (~600px). Fotos novas das obras elevam muito o resultado.

"""Dados do site Marmoraria Forte Rocha — fonte única para HTML, schema.org, llms.txt e JS."""

SITE = 'https://www.marmorariaforterocha.com.br'

# Google Tag Manager — preencher com o ID do contêiner (ex.: 'GTM-ABC1234').
# Vazio = o snippet não é inserido. GA4, Meta Pixel e Hotjar entram pelo GTM.
GTM_ID = ''

EMPRESA = {
    'nome': 'Marmoraria Forte Rocha',
    'curto': 'Forte Rocha',
    'slogan': 'Pedra natural, feita sob medida.',
    'rua': 'Rua Shirlei Ramos Maia de Souza, 930 — Parque dos Servidores',
    'bairro': 'Parque dos Servidores',
    'cidade': 'Paulínia', 'uf': 'SP',
    # TODO: conferir CEP e coordenada exata no Google Business Profile (hoje: centro de Paulínia)
    'cep': '',
    'lat': -22.7611, 'lng': -47.1544,
    'whatsapp': '+55 19 99364-8081', 'whatsapp_digits': '5519993648081',
    'telefone_br': '(19) 99364-8081',
    'email': 'comercial@marmorariaforterocha.com.br',
    'facebook': 'https://www.facebook.com/marmorariaforterocharmc/',
    # TODO: confirmar dias de funcionamento (o site antigo informa só o horário 8h–17h)
    'horario': 'Segunda a sexta, das 8h às 17h',
    'horario_schema': ['Mo-Fr 08:00-17:00'],
    'area': 'Paulínia e região de Campinas',
    'resumo': ('A Marmoraria Forte Rocha é uma marmoraria de Paulínia/SP especializada em mármores e granitos '
               'nacionais e importados, além de quartzo, limestone, ônix, travertino e porcelanato. Fabrica e '
               'instala sob medida — com medição no local — bancadas de cozinha, lavatórios, cubas esculpidas, '
               'rebaixo italiano, escadas, pisos, soleiras, churrasqueiras e peças especiais para obras '
               'residenciais e comerciais em Paulínia e região de Campinas.'),
}

NUMEROS = [(300, '+', 'clientes satisfeitos'), (250, '+', 'projetos entregues'), (10, '', 'profissionais na equipe')]

MATERIAIS = [
    dict(id='marmore', nome='Mármore', img='site/textura-branco', foto='site/banheiro-marmore',
         txt='Veios únicos e brilho elegante. Ideal para pisos, escadas, lavatórios, bordas de banheira e mesas.'),
    dict(id='granito', nome='Granito', img='site/textura-imperador', foto='site/cuba-granito',
         txt='Dureza e resistência para o dia a dia. Ideal para pias, balcões, lavatórios, pisos, escadas e lareiras.'),
    dict(id='travertino', nome='Travertino', img='site/textura-crema', foto='site/escada-travertino',
         txt='Textura natural e tom quente. Ideal para acabamento de ambientes residenciais e comerciais.'),
    dict(id='especiais', nome='Quartzo & Ônix', img='site/textura-nero', foto='site/ilha-marmore-branco',
         txt='Quartzo, ônix, limestone e porcelanato: para projetos contemporâneos, com corte e acabamento de precisão.'),
]
OUTRAS_PEDRAS = ['Quartzo', 'Limestone', 'Ônix', 'Porcelanato']

SERVICOS = [
    dict(id='bancadas', nome='Bancadas e tampos', icon='i-bancada',
         txt='Tampos para cozinhas, banheiros e áreas de serviço — com frontão, rebaixo e recorte para cuba e cooktop.'),
    dict(id='lavatorios', nome='Lavatórios e cubas esculpidas', icon='i-cuba',
         txt='Lavatórios, cubas esculpidas na própria pedra e bancadas para lavabos e banheiros.'),
    dict(id='rebaixo', nome='Rebaixo italiano', icon='i-rebaixo',
         txt='Cuba esculpida com caimento oculto e escoamento discreto: o acabamento mais desejado dos banheiros atuais.'),
    dict(id='ilhas', nome='Ilhas e cascatas', icon='i-ilha',
         txt='Ilhas, penínsulas e bancadas em cascata com meia esquadria, para a pedra parecer uma peça única.'),
    dict(id='escadas', nome='Revestimento de escadas', icon='i-escada',
         txt='Pisos e espelhos de degraus, com friso antiderrapante e acabamento sob medida para cada lance.'),
    dict(id='pisos', nome='Pisos e paredes', icon='i-piso',
         txt='Revestimento de pisos e paredes, soleiras, divisórias e testeiras em mármore, granito e porcelanato.'),
    dict(id='gourmet', nome='Churrasqueiras e áreas gourmet', icon='i-fogo',
         txt='Revestimento de churrasqueiras, balcões e bancadas para espaços gourmet internos e externos.'),
    dict(id='porcelanato', nome='Serviços em porcelanato', icon='i-porcelanato',
         txt='Corte, montagem e acabamento de bancadas e revestimentos em porcelanato de grandes formatos.'),
    dict(id='restauracao', nome='Restauração e revitalização', icon='i-brilho',
         txt='Polimento, revitalização, restauração e impermeabilização para devolver o brilho e proteger a pedra.'),
    dict(id='especiais', nome='Peças especiais', icon='i-peca',
         txt='Mesas, aparadores, nichos, túmulos e peças fora do padrão, cortadas e acabadas sob medida.'),
]

ETAPAS = [
    ('Conversa e orçamento', 'Você conta o projeto pelo WhatsApp ou na loja. O orçamento é sem compromisso.'),
    ('Medição no local', 'Nossa equipe mede a obra in loco para a peça sair exata, sem improviso na instalação.'),
    ('Escolha da pedra', 'Ajudamos a escolher material, cor e acabamento de borda ideais para cada ambiente.'),
    ('Fabricação', 'Corte e acabamento em máquinas de alta capacidade, com mão de obra especializada.'),
    ('Instalação', 'Instalamos com cuidado e entregamos no prazo — um dos menores da região.'),
]

# Obras: (arquivo em assets/img/obras, categoria, título)
CATEGORIAS_OBRAS = [('cozinhas', 'Cozinhas'), ('banheiros', 'Banheiros e lavabos'), ('escadas', 'Escadas'),
                    ('gourmet', 'Gourmet e churrasqueiras'), ('servico', 'Áreas de serviço')]
OBRAS = [
    ('cozinha-l-granito-preto', 'cozinhas', 'Cozinha em L com granito preto'),
    ('rebaixo-italiano-marmore', 'banheiros', 'Rebaixo italiano em mármore branco'),
    ('escada-branca-iluminada', 'escadas', 'Escada branca com iluminação embutida'),
    ('lavatorio-cuba-dourada', 'banheiros', 'Lavatório com cuba de apoio dourada'),
    ('ilha-cascata-granito-preto', 'cozinhas', 'Ilha em cascata de granito preto'),
    ('churrasqueira-revestida', 'gourmet', 'Churrasqueira revestida em pedra'),
    ('cozinha-gourmet-ilha', 'cozinhas', 'Cozinha gourmet com ilha'),
    ('lavatorio-cuba-esculpida-branca', 'banheiros', 'Cuba esculpida em pedra branca'),
    ('escada-travertino', 'escadas', 'Escada revestida em travertino'),
    ('ilha-granito-preto-madeira', 'cozinhas', 'Ilha de granito preto com madeira'),
    ('lavatorio-cuba-cobre', 'banheiros', 'Lavatório com cuba de cobre'),
    ('area-gourmet-granito-preto', 'gourmet', 'Área gourmet em granito preto'),
    ('cozinha-bancada-bistro', 'cozinhas', 'Bancada bistrô integrada'),
    ('bancada-lavatorio-dupla', 'banheiros', 'Bancada de lavatório com duas cubas'),
    ('escada-granito-preto', 'escadas', 'Escada em granito preto'),
    ('cozinha-l-granito-preto-frontao', 'cozinhas', 'Cozinha em L com frontão'),
    ('lavatorio-cuba-esculpida-saia', 'banheiros', 'Cuba esculpida com saia'),
    ('churrasqueira-granito', 'gourmet', 'Churrasqueira com acabamento em granito'),
    ('copa-bancada-granito', 'cozinhas', 'Copa com bancada de granito'),
    ('lavatorio-bicolor', 'banheiros', 'Lavatório bicolor com cuba esculpida'),
    ('escada-quartzo-branco', 'escadas', 'Escada em quartzo branco'),
    ('ilha-granito-preto-cooktop', 'cozinhas', 'Ilha com cooktop em granito preto'),
    ('lavatorio-cuba-apoio-preto', 'banheiros', 'Lavatório preto com cuba de apoio'),
    ('area-gourmet-bancada', 'gourmet', 'Bancada de área gourmet'),
    ('lavatorio-cuba-esculpida-canto', 'banheiros', 'Cuba esculpida de canto'),
    ('area-servico-bancada-cinza', 'servico', 'Área de serviço com bancada cinza'),
    ('cozinha-peninsula-granito', 'cozinhas', 'Cozinha com península em granito'),
    ('lavatorio-cuba-apoio-marrom', 'banheiros', 'Lavatório marrom com cuba de apoio'),
    ('balcao-granito-preto', 'gourmet', 'Balcão em granito preto'),
    ('bancada-branca-cooktop', 'cozinhas', 'Bancada branca com cooktop'),
    ('lavatorio-rebaixo-cinza', 'banheiros', 'Lavatório com rebaixo em pedra cinza'),
    ('bancada-cinza-cascata', 'servico', 'Bancada cinza em cascata'),
    ('cozinha-granito-preto-cuba', 'cozinhas', 'Cozinha com cuba em granito preto'),
    ('bancada-banheiro-cuba-esculpida', 'banheiros', 'Bancada de banheiro com cuba esculpida'),
    ('bancada-l-granito-preto', 'gourmet', 'Bancada em L de granito preto'),
    ('balcao-cascata-granito-claro', 'cozinhas', 'Balcão em cascata de granito claro'),
    ('lavatorio-branco-cuba-apoio', 'banheiros', 'Lavatório branco com cuba de apoio'),
    ('balcao-granito-madeira', 'gourmet', 'Balcão de granito com madeira'),
    ('pia-granito-preto-inox', 'cozinhas', 'Pia em granito preto com cuba inox'),
    ('bancada-granito-claro-cooktop', 'servico', 'Bancada em granito claro com cooktop'),
    ('cozinha-granito-claro-mesa', 'cozinhas', 'Cozinha com bancada de granito claro'),
]
OBRAS_HOME = ['cozinha-l-granito-preto', 'rebaixo-italiano-marmore', 'escada-branca-iluminada', 'lavatorio-cuba-dourada',
              'ilha-cascata-granito-preto', 'churrasqueira-revestida', 'cozinha-gourmet-ilha', 'escada-travertino']

# Pedras do mostruário: (slug, nome, tom)
GRANITOS = [
    ('amarelo-florida', 'Amarelo Flórida', 'quente'), ('amarelo-humaita', 'Amarelo Humaitá', 'quente'),
    ('amarelo-ornamental', 'Amarelo Ornamental', 'quente'), ('arabesco', 'Arabesco', 'claro'),
    ('bege-dunas', 'Bege Dunas', 'quente'), ('bege-ipanema', 'Bege Ipanema', 'claro'),
    ('branco-ceara', 'Branco Ceará', 'claro'), ('cafe-imperial', 'Café Imperial', 'escuro'),
    ('cinza-andorinha', 'Cinza Andorinha', 'claro'), ('cinza-corumba', 'Cinza Corumbá', 'escuro'),
    ('ocre-itabira', 'Ocre Itabira', 'quente'), ('preto-sao-gabriel', 'Preto São Gabriel', 'escuro'),
]
MARMORES = [
    ('branco-carrara', 'Branco Carrara', 'claro'), ('branco-pigues', 'Branco Piguês', 'claro'),
    ('branco-rajado', 'Branco Rajado', 'claro'), ('coralito', 'Coralito', 'quente'),
    ('crema-marfil', 'Crema Marfil', 'claro'), ('marrom-imperador', 'Marrom Imperador', 'escuro'),
    ('nero-marquina', 'Nero Marquina', 'escuro'), ('rosa-verona', 'Rosa Verona', 'quente'),
    ('travertino-romano', 'Travertino Romano', 'quente'), ('travertino', 'Travertino', 'claro'),
    ('verde-alpi', 'Verde Alpi', 'escuro'), ('botticino', 'Botticino', 'claro'),
]

# Acabamentos (glossário). perfil = id do desenho SVG da borda (ou None)
ACABAMENTOS = [
    ('Reto', 'reto', 'Borda simples, polida do jeito que foi cortada, sem acabamento especial. Visual limpo e contemporâneo.'),
    ('Boleado', 'boleado', 'Borda arredondada usada em pias e bancadas de mármore ou granito. Pode ser simples, duplo ou meio boleado.'),
    ('Meio boleado', 'meio-boleado', 'Arredonda apenas a aresta superior: suaviza o toque e mantém a lateral reta.'),
    ('Bisotê', 'bisote', 'Modelo de acabamento lateral com chanfro, muito usado nas bordas de bancadas.'),
    ('Bisotado', 'bisotado', 'Arremate que cria chanfros em tampos e bancadas. Em pisos, tira o corte das arestas e evita que as beiradas quebrem.'),
    ('Meia esquadria', 'meia-esquadria', 'Encontro de duas peças a 45°. Não mostra o fio de cola na emenda e dá aspecto de peça única — é o acabamento das cascatas.'),
    ('Meia cana', 'meia-cana', 'Acabamento lateral côncavo, geralmente usado nas bordas de lavatórios.'),
    ('Peito de pombo', 'peito-pombo', 'Acabamento lateral curvo e encorpado, usado principalmente em lavatórios e aparadores.'),
    ('Saia', 'saia', 'Faixa de 10 a 15 cm na borda para esconder a cuba de lavatórios e lavabos que não terão armário.'),
    ('Frontão', 'frontao', 'Arremate entre a parede e a pia, o lavatório ou outras bancadas. Costuma medir de 7 a 10 cm de altura.'),
    ('Guarnição', 'guarnicao', 'Arremate sobressalente nas bordas de pias em áreas molhadas: com 4 cm de espessura, salienta 2 cm e impede que a água escorra.'),
    ('Engrosso', 'engrosso', 'Material acrescentado sob a borda para engrossar a espessura lateral onde serão feitos alguns acabamentos.'),
    ('Friso antiderrapante', 'friso', 'Frisos feitos na pedra, geralmente em degraus de escada, para evitar que fique escorregadia.'),
    ('Área molhada', None, 'Bancada com rebaixo e guarnição para a água não cair no chão. Exemplo: pia de cozinha.'),
    ('Área seca', None, 'Bancada sem rebaixo, usada onde geralmente não haverá água. Exemplo: balcões e aparadores.'),
    ('Faixa (tabeira)', None, 'Na composição de pisos em mármore ou granito, é a moldura que contorna o ambiente.'),
    ('Bruto', None, 'Superfície sem qualquer acabamento, como a pedra é encontrada na natureza — apenas serrada.'),
]

DEPOIMENTOS = [
    ('Lisa Soares', 'Conhecendo a história dessa empresa, sua trajetória, seriedade e compromisso consciente com a qualidade, posso indicar e recomendá-la.'),
    ('Jhonatas Martins', 'Atendimento excelente… acabamento ficou muito caprichado. Obrigada pelo prazo. Ficamos encantados com o trabalho.'),
    ('Mary Dantas', 'Eu recomendo o trabalho deles: acabamento perfeito, amei, ficou muito lindo. Super indico, entregou na data certa, tudo perfeito. Obrigada!'),
]

PARCERIAS = ['Criação de projetos', 'Profissionais especializados', 'Parceria com construtoras', 'Parceria com planejados']

# ---------- Perguntas frequentes (visíveis na página + FAQPage) ----------
E = EMPRESA
F_ONDE = ('Onde fica a Marmoraria Forte Rocha?',
          f'A Forte Rocha fica na {E["rua"]}, em Paulínia - SP. Atendemos obras residenciais e comerciais em {E["area"]}.')
F_ORCAMENTO = ('Como pedir um orçamento?',
               f'Mande fotos ou medidas aproximadas do ambiente pelo WhatsApp {E["telefone_br"]} ou pelo formulário da página de contato. O orçamento é sem compromisso e, para fechar o projeto, a equipe faz a medição no local.')
F_MEDICAO = ('Vocês fazem a medição no local?',
             'Sim. Todas as peças são feitas sob medida, com medição in loco pela nossa equipe — assim a bancada, a escada ou o revestimento chegam exatos para a instalação.')
F_DIFERENCA = ('Qual a diferença entre mármore e granito?',
               'O granito é mais duro e menos poroso, por isso resiste melhor a riscos, calor e manchas — é o mais indicado para pias e bancadas de cozinha. O mármore tem veios marcantes e brilho mais elegante, mas é mais sensível a ácidos e riscos; é ideal para lavatórios, pisos, escadas e mesas.')
F_REBAIXO = ('O que é rebaixo italiano?',
             'É uma cuba esculpida na própria pedra, com o fundo levemente inclinado e o escoamento escondido em uma fenda ou tampa da mesma pedra. A água "some" sem ralo aparente, deixando o lavatório com visual limpo e contínuo.')
F_PRAZO = ('Qual o prazo de entrega?',
           'Trabalhamos com um dos menores prazos da região. O prazo exato depende do material escolhido e do tamanho do projeto, e é informado já no orçamento.')
F_PAGAMENTO = ('Quais as formas de pagamento?',
               'A Forte Rocha tem diversas formas de pagamento e flexibilidade na negociação. Consulte as condições para o seu projeto pelo WhatsApp.')
F_MATERIAIS = ('Com quais materiais vocês trabalham?',
               'Mármores e granitos nacionais e importados, além de quartzo, limestone, ônix, travertino e porcelanato.')
F_SERVICOS = ('Quais serviços a Forte Rocha faz?',
              'Bancadas e tampos de cozinha, banheiro e área de serviço, lavatórios e cubas esculpidas, rebaixo italiano, ilhas e cascatas, revestimento de escadas, pisos e paredes, soleiras, divisórias, churrasqueiras, peças especiais, serviços em porcelanato, impermeabilização, revitalização e restauração.')
F_COZINHA = ('Qual a melhor pedra para bancada de cozinha?',
             'Para a cozinha, o granito costuma ser a melhor escolha pela resistência a riscos, calor e manchas. Pedras escuras como o Preto São Gabriel disfarçam o uso diário; tons claros como o Branco Ceará e o Cinza Andorinha deixam o ambiente mais iluminado. Quartzo também é uma ótima opção.')
F_BORDA = ('Qual acabamento de borda escolher?',
           'O reto é o mais contemporâneo; o boleado suaviza as quinas e é ótimo para quem tem crianças; a meia esquadria esconde a emenda e faz a pedra parecer uma peça maciça. Na página de dicas explicamos cada modelo com desenho do perfil.')
F_VARIACAO = ('A pedra instalada fica igual à foto?',
              'As fotos são ilustrativas. Mármores, granitos e outras pedras naturais têm variações de veios e tonalidade de chapa para chapa — por isso recomendamos ver a chapa pessoalmente antes do corte.')
F_HORARIO = ('Qual o horário de atendimento?',
             f'{E["horario"]}. Pelo WhatsApp {E["telefone_br"]} você também pode mandar sua mensagem a qualquer hora e retornamos no horário comercial.')
F_CONTATO = ('Como falar com a Forte Rocha?',
             f'Pelo WhatsApp {E["telefone_br"]} (resposta mais rápida), pelo e-mail {E["email"]} ou pessoalmente na loja em Paulínia - SP.')
F_RESTAURA = ('Vocês restauram mármore e granito antigos?',
              'Sim. Fazemos polimento, revitalização, restauração e impermeabilização de pisos, bancadas e escadas para recuperar o brilho e proteger a pedra contra manchas.')
F_PORCELANATO = ('Vocês fazem bancada de porcelanato?',
                 'Sim. Cortamos, montamos e damos acabamento em bancadas, ilhas e revestimentos de porcelanato, inclusive em peças de grande formato com meia esquadria.')

FAQS = {
    'home': [F_ORCAMENTO, F_MEDICAO, F_DIFERENCA, F_ONDE, F_PRAZO, F_PAGAMENTO],
    'empresa': [F_ONDE, F_MATERIAIS, F_SERVICOS, F_PAGAMENTO],
    'servicos': [F_SERVICOS, F_REBAIXO, F_MEDICAO, F_RESTAURA, F_PORCELANATO, F_PRAZO],
    'obras': [F_VARIACAO, F_ORCAMENTO, F_MEDICAO],
    'produtos': [F_DIFERENCA, F_COZINHA, F_MATERIAIS, F_VARIACAO],
    'dicas': [F_BORDA, F_REBAIXO, F_DIFERENCA],
    'contato': [F_CONTATO, F_ONDE, F_HORARIO, F_ORCAMENTO, F_PAGAMENTO],
}

# ---------- Home (estrutura do site original) ----------
SLIDES = [
    ('site/hero-cozinha-marmore', 'Mármores', '&amp; Granitos', 'Bancadas, ilhas, lavatórios e revestimentos sob medida — com medição no local.'),
    ('obras/cozinha-gourmet-ilha', 'Projetos', 'sob medida', 'Cozinhas, banheiros e áreas gourmet com acabamento impecável.'),
    ('obras/escada-quartzo-branco', 'Escadas &amp;', 'revestimentos', 'Pisos, degraus e soleiras em pedra natural para toda a obra.'),
]
INFO = [('i-projeto', 'Criação de Projetos', 'Ajudamos a desenhar cada peça'),
        ('i-equipe', 'Profissionais Especializados', 'Mão de obra qualificada'),
        ('i-predio', 'Parceria com Construtoras', 'Obras residenciais e comerciais'),
        ('i-planejado', 'Parceria com Planejados', 'Integração com marcenaria')]
HOME_MATERIAIS = [
    ('site/banheiro-marmore', 'Mármore', 'Ideal para revestimentos de pisos, escadas, lavatórios, bordas de banheira e mesas.'),
    ('site/cuba-granito', 'Granito', 'Ideal para revestimentos de pisos, escadas, pias, balcões, lavatórios, lareiras etc.'),
    ('site/escada-travertino', 'Travertinos', 'Ideal para acabamento de ambientes residenciais e comerciais.'),
]
HOME_PRODUTOS = [('marmore', 'nero-marquina', 'Nero Marquina'), ('marmore', 'marrom-imperador', 'Marrom Imperador'),
                 ('marmore', 'crema-marfil', 'Crema Marfil'), ('marmore', 'branco-carrara', 'Branco Carrara')]

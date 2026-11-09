#!/usr/bin/env python3
"""Monta o site estático da Marmoraria Forte Rocha (padrão QH4: SEO + AEO + GEO).

Layout fiel ao site original do cliente (marmorariaforterocha.com.br): topo marrom, header branco,
slider, faixa bege de diferenciais, materiais, obras em fundo grafite, contadores, depoimentos,
atendimento, produtos, parceiros e rodapé marrom — com acabamento e animações atualizados.

Uso:  python3 src/build.py
Edite dados em src/data.py e o layout em src/layout.html, depois rode de novo.
"""
import html as H
import json
import re
from datetime import date
from pathlib import Path
from urllib.parse import quote

from data import (ACABAMENTOS, CATEGORIAS_OBRAS, DEPOIMENTOS, EMPRESA as E, ETAPAS, FAQS, GRANITOS, GTM_ID,
                  HOME_MATERIAIS, HOME_PRODUTOS, INFO, MARMORES, NUMEROS, OBRAS, OUTRAS_PEDRAS, SERVICOS, SITE,
                  SLIDES)

SRC = Path(__file__).parent
ROOT = SRC.parent
HOJE = date.today()
VERSAO = format(int(__import__('time').time()), 'x')
OG_IMAGE = f'{SITE}/assets/og/forterocha-og.jpg'
IMG = json.loads((ROOT / 'assets/img/manifest.json').read_text())

NAV = [('/', 'Home'), ('/empresa/', 'Empresa'), ('/servicos/', 'Serviços'), ('/obras/', 'Obras Realizadas'),
       ('/produtos/', 'Produtos'), ('/dicas/', 'Dicas'), ('/contato/', 'Contato')]

esc = H.escape
WA_MSG = 'Olá! Vim pelo site da Forte Rocha e quero um orçamento.'


def wa(msg=WA_MSG):
    return f'https://wa.me/{E["whatsapp_digits"]}?text={quote(msg)}'


def img(path, alt, lazy=True, extra=''):
    w, h = IMG[f'{path}.webp']
    load = ' loading="lazy" decoding="async"' if lazy else ''
    return f'<img src="/assets/img/{path}.webp" alt="{esc(alt)}" width="{w}" height="{h}"{load}{extra}>'


def title(a, b, tag='h2', center=True, light=False, sub='', ghost=None):
    """Título no padrão do site original: palavra forte + palavra em destaque marrom, com traço embaixo.
    A palavra-fantasma grande ao fundo dá hierarquia sem fugir da identidade (Raleway 800)."""
    cls = 'sec-title' + (' is-center' if center else '') + (' is-light' if light else '')
    s = f'<p class="sec-sub">{sub}</p>' if sub else ''
    g = f'<span class="ghost" aria-hidden="true">{ghost or b}</span>'
    return f'<div class="{cls} rv">{g}<{tag}>{a} <span>{b}</span></{tag}><i class="sec-line"></i>{s}</div>'


OBRA = {slug: (cat, titulo) for slug, cat, titulo in OBRAS}
CAT_NOME = dict(CATEGORIAS_OBRAS)
SERV_IMG = {'bancadas': 'obras/cozinha-l-granito-preto', 'lavatorios': 'obras/lavatorio-cuba-dourada',
            'rebaixo': 'obras/rebaixo-italiano-marmore', 'ilhas': 'obras/ilha-cascata-granito-preto',
            'escadas': 'obras/escada-branca-iluminada', 'pisos': 'site/banheiro-marmore',
            'gourmet': 'obras/churrasqueira-revestida', 'porcelanato': 'obras/bancada-branca-cooktop',
            'restauracao': 'obras/escada-travertino', 'especiais': 'obras/lavatorio-bicolor'}
PEDRAS = [('granito', s, n, t) for s, n, t in GRANITOS] + [('marmore', s, n, t) for s, n, t in MARMORES]
HOME_OBRAS = ['churrasqueira-revestida', 'escada-travertino', 'rebaixo-italiano-marmore', 'cozinha-l-granito-preto',
              'escada-branca-iluminada', 'lavatorio-cuba-dourada', 'ilha-granito-preto-cooktop', 'copa-bancada-granito']


# =====================================================================
# Seções
# =====================================================================
def page_header(t, crumb, bg='site/ilha-marmore-branco', lead=''):
    l = f'<p class="ph-lead">{lead}</p>' if lead else ''
    return f'''  <section class="page-header">
    <div class="ph-bg" aria-hidden="true">{img(bg, '', lazy=False)}</div>
    <div class="container ph-inner">
      <h1>{t}</h1>
      {l}
      <nav class="crumbs" aria-label="Você está em"><a href="/">Home</a><span aria-hidden="true">»</span><span aria-current="page">{crumb}</span></nav>
    </div>
  </section>
'''


def resumo(pergunta, resposta):
    """Resposta direta para buscadores e IAs (AEO), no estilo do site."""
    return f'''  <section class="resumo" aria-label="Resposta rápida">
    <div class="container">
      <div class="resumo-box rv">
        <h2 class="resumo-q">{pergunta}</h2>
        <p class="resumo-a">{resposta}</p>
      </div>
    </div>
  </section>
'''


def slider():
    slides = []
    n = len(SLIDES)
    for i, (bg, l1, l2, sub) in enumerate(SLIDES):
        tag = 'h1' if i == 0 else 'p'
        slides.append(f'''      <div class="slide{' is-on' if i == 0 else ''}">
        <div class="slide-bg">{img(bg, '', lazy=i > 0, extra=' fetchpriority="high"' if i == 0 else '')}</div>
        <div class="container slide-cap">
          <p class="slide-kicker">Marmoraria em Paulínia · SP</p>
          <{tag} class="slide-title">{l1}<br><span>{l2}</span></{tag}>
          <p class="slide-sub">{sub}</p>
          <div class="slide-btns">
            <a class="btn btn-brown" href="{wa()}" target="_blank" rel="noopener" data-track="whatsapp_slider"><svg><use href="#i-wa"/></svg> Fale agora</a>
            <a class="btn btn-ghost" href="/obras/">Ver obras realizadas</a>
          </div>
        </div>
      </div>''')
    dots = ''.join(f'<button type="button" aria-label="Slide {i + 1}"{" class=is-on" if i == 0 else ""}><i></i></button>' for i in range(n))
    return f'''  <section class="slider" aria-label="Destaques">
{chr(10).join(slides)}
      <div class="sl-count" aria-hidden="true"><b class="sl-cur">01</b><i></i><span>{n:02d}</span></div>
      <a class="sl-card" href="{wa()}" target="_blank" rel="noopener" data-track="whatsapp_slider_card">
        <span class="sl-card-swatch" aria-hidden="true">{img('pedras/marmore-branco-carrara', '')}</span>
        <span><b>Orçamento sem compromisso</b><small>Medição no local · Paulínia e região</small></span>
        <svg class="sl-card-go" aria-hidden="true"><use href="#i-arrow"/></svg>
      </a>
      <button class="sl-arrow sl-prev" type="button" aria-label="Slide anterior"><svg><use href="#i-chev"/></svg></button>
      <button class="sl-arrow sl-next" type="button" aria-label="Próximo slide"><svg><use href="#i-chev"/></svg></button>
      <div class="sl-dots">{dots}</div>
  </section>
'''


def info_band(overlap=True):
    items = ''.join(f'''
        <div class="info-item rv" style="--d:{i}">
          <span class="info-ic"><svg aria-hidden="true"><use href="#{ic}"/></svg></span>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>''' for i, (ic, t, d) in enumerate(INFO))
    return f'''  <section class="info-band{' is-overlap' if overlap else ''}" aria-label="Diferenciais">
    <div class="container info-grid">{items}
    </div>
  </section>
'''


MAT_SWATCH = ['pedras/marmore-branco-carrara', 'pedras/granito-preto-sao-gabriel', 'pedras/marmore-travertino-romano']


def materiais():
    cards = ''.join(f'''
        <article class="mat-card rv" style="--d:{i}">
          <a class="mat-media" href="/produtos/">{img(p, f'{n} — Marmoraria Forte Rocha')}<span class="mat-num">0{i + 1}</span></a>
          <span class="mat-swatch" aria-hidden="true">{img(MAT_SWATCH[i], '')}</span>
          <div class="mat-body">
            <h3>{n}</h3>
            <p>{t}</p>
            <a class="more" href="/produtos/">Ver opções <svg><use href="#i-arrow"/></svg></a>
          </div>
        </article>''' for i, (p, n, t) in enumerate(HOME_MATERIAIS))
    return f'''  <section class="sec bg-gray">
    <div class="container">
      {title('Nossos', 'materiais', sub='Mármores e granitos nacionais e importados, além de quartzo, limestone, ônix e porcelanato.')}
      <div class="mat-grid">{cards}
      </div>
    </div>
  </section>
'''


def gal_item(s, i=0, home=False):
    c, t = OBRA[s]
    return f'''
        <a class="gal-item rv" style="--d:{i % 4}" id="{s}" href="/assets/img/obras/{s}.webp" data-cat="{c}" data-cap="{esc(t)}" data-lightbox="obras">
          {img('obras/' + s, t + ' — Marmoraria Forte Rocha')}
          <span class="gal-over"><svg aria-hidden="true"><use href="#i-zoom"/></svg><b>{esc(t)}</b><small>{CAT_NOME[c]}</small></span>
        </a>'''


def obras_home():
    items = ''.join(gal_item(s, i) for i, s in enumerate(HOME_OBRAS))
    return f'''  <section class="sec bg-ink obras-sec" aria-label="Obras realizadas">
    <div class="container obras-head">
      {title('Obras', 'realizadas', light=True, center=False, sub='Cada projeto medido, cortado e instalado pela nossa equipe. Clique para ampliar.')}
      <a class="btn btn-ghost rv" href="/obras/">Ver todas as obras <svg><use href="#i-arrow"/></svg></a>
    </div>
    <div class="container"><div class="gal-bento">{items}
    </div></div>
  </section>
'''


def sobre_home():
    return f'''  <section class="sec bg-white sobre">
    <div class="container two-col">
      <div class="collage rv" aria-hidden="true">
        <figure class="c-main">{img('site/cozinha-ilha-marmore', '', extra=' data-par="-6"')}</figure>
        <figure class="c-small">{img('obras/lavatorio-cuba-dourada', '', extra=' data-par="8"')}</figure>
        <div class="c-badge"><b data-count="250">250</b><span>projetos<br>realizados</span></div>
        <span class="c-swatch">{img('pedras/marmore-nero-marquina', '')}</span>
      </div>
      <div class="rv" style="--d:1">
        {title('Sobre a', 'Forte Rocha', center=False, ghost='Sobre')}
        <p class="txt">Somos uma empresa especializada em mármores e granitos, nacionais e importados, entre outras pedras ornamentais como limestone, quartzo, ônix e também o porcelanato.</p>
        <p class="txt">Executamos os mais variados serviços — pisos, revestimentos, tampos, pias, lavatórios, churrasqueiras, escadas e peças especiais — feitos sob medida “in loco” e com diversos acabamentos.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg> Medição e instalação in loco</li>
          <li><svg><use href="#i-check"/></svg> Um dos menores prazos de entrega da região</li>
          <li><svg><use href="#i-check"/></svg> Flexibilidade na negociação e no pagamento</li>
        </ul>
        <a class="btn btn-brown" href="/empresa/">Conheça a empresa</a>
      </div>
    </div>
  </section>
'''


def processo_home():
    etapas = ''.join(f'''<li class="rv" style="--d:{i}"><b>{i + 1:02d}</b><h3>{t}</h3><p>{d}</p></li>''' for i, (t, d) in enumerate(ETAPAS))
    return f'''  <section class="sec bg-gray">
    <div class="container">
      {title('Como', 'trabalhamos', ghost='Processo', sub='Do primeiro contato à instalação, com a mesma equipe acompanhando sua obra.')}
      <ol class="steps">{etapas}</ol>
    </div>
  </section>
'''


def contadores(texto=True):
    icons = ['i-heart', 'i-users', 'i-folder']
    nums = ''.join(f'''
          <div class="count rv" style="--d:{i}">
            <span class="count-ic"><svg aria-hidden="true"><use href="#{icons[i]}"/></svg></span>
            <b data-count="{n}">{n}</b>
            <span>{esc(l)}</span>
          </div>''' for i, (n, _, l) in enumerate([(300, '', 'Clientes satisfeitos'), (10, '', 'Nossos funcionários'), (250, '', 'Projetos realizados')]))
    sobre = f'''
        <div class="counter-text rv">
          <h2>Sobre</h2>
          <p>Somos uma empresa especializada em mármores e granitos, nacionais e importados, entre outras pedras ornamentais como limestone, quartzo, ônix e também o porcelanato.</p>
          <p>Executamos os mais variados serviços: pisos, revestimentos, tampos, pias, lavatórios, churrasqueiras, escadas, dentre outras peças especiais, feitas sob medida “in loco” e com diversos acabamentos.</p>
          <a class="btn btn-white" href="/empresa/">Conheça a empresa</a>
        </div>''' if texto else ''
    return f'''  <section class="counterup{'' if texto else ' is-solo'}">
    <div class="counter-bg" aria-hidden="true">{img('site/textura-imperador', '', extra=' data-par="10"')}</div>
    <div class="container counter-grid">{sobre}
        <div class="counts">{nums}
        </div>
    </div>
  </section>
'''


def depoimentos():
    cards = ''.join(f'''
          <figure class="depo">
            <span class="depo-av" aria-hidden="true"><svg><use href="#i-user"/></svg></span>
            <div class="stars" aria-label="5 estrelas">{'<svg><use href="#i-star"/></svg>' * 5}</div>
            <blockquote>“{esc(t)}”</blockquote>
            <figcaption>{esc(n)}</figcaption>
          </figure>''' for n, t in DEPOIMENTOS)
    return f'''  <section class="sec bg-white">
    <div class="container">
      {title('Clientes', 'testemunhos', ghost='Clientes')}
      <div class="depo-wrap rv">
        <div class="depo-track">{cards}
        </div>
      </div>
      <div class="depo-dots" aria-hidden="true"></div>
    </div>
  </section>
'''


def form_html(dark=True):
    return f'''<form class="ct-form" id="orcamento-form" novalidate>
          <div class="field-row">
            <div class="field"><label for="f-nome">Nome</label><input id="f-nome" name="nome" autocomplete="name" required></div>
            <div class="field"><label for="f-tel">Telefone / WhatsApp</label><input id="f-tel" name="telefone" type="tel" inputmode="tel" autocomplete="tel" required></div>
          </div>
          <div class="field-row">
            <div class="field"><label for="f-tipo">Tipo de projeto</label>
              <select id="f-tipo" name="tipo"><option>Bancada de cozinha</option><option>Banheiro / lavatório</option><option>Rebaixo italiano</option><option>Escada</option><option>Piso / revestimento</option><option>Churrasqueira / gourmet</option><option>Restauração / polimento</option><option>Outro</option></select></div>
            <div class="field"><label for="f-mat">Material</label>
              <select id="f-mat" name="material"><option>Ainda não sei</option><option>Granito</option><option>Mármore</option><option>Quartzo</option><option>Travertino</option><option>Porcelanato</option><option>Outro</option></select></div>
          </div>
          <div class="field"><label for="f-msg">Mensagem</label><textarea id="f-msg" name="mensagem" rows="4" placeholder="Medidas, cidade da obra, prazo…"></textarea></div>
          <button class="btn btn-brown" type="submit"><svg><use href="#i-wa"/></svg> Enviar</button>
          <p class="form-msg" role="status" aria-live="polite"></p>
        </form>'''


def contato_info():
    return f'''<ul class="ct-list">
            <li><svg><use href="#i-pin"/></svg><span>{E['rua'].replace(' — ', ' - ')} - {E['cidade']} - {E['uf']}</span></li>
            <li><svg><use href="#i-wa"/></svg><a href="{wa()}" target="_blank" rel="noopener" data-track="whatsapp_contato_box">{E['telefone_br']}</a></li>
            <li><svg><use href="#i-mail"/></svg><a href="mailto:{E['email']}">{E['email'].replace('@', '@<wbr>')}</a></li>
            <li><svg><use href="#i-clock"/></svg><span>{E['horario']}</span></li>
          </ul>'''


def atendimento():
    return f'''  <section class="request">
    <div class="request-bg" aria-hidden="true">{img('site/hero-cozinha-marmore', '')}</div>
    <div class="container request-grid">
      <div class="rv">
        {title('Atendimento ao', 'cliente', center=False, light=True)}
        <p class="request-lead">Conte o que você precisa. Ao enviar, abrimos o WhatsApp com a sua mensagem pronta — o orçamento é sem compromisso.</p>
        {form_html()}
      </div>
      <aside class="ct-box rv" style="--d:1">
        <h3>Contato</h3>
        {contato_info()}
        <a class="btn btn-white" href="{wa()}" target="_blank" rel="noopener" data-track="whatsapp_contato_box_btn"><svg><use href="#i-wa"/></svg> Chamar no WhatsApp</a>
      </aside>
    </div>
  </section>
'''


def produtos_home():
    cards = ''.join(f'''
        <a class="prod rv" style="--d:{i}" href="/assets/img/pedras/{t}-{s}.webp" data-lightbox="home-pedras" data-cap="{n}" data-wa="{esc(wa(f'Olá! Quero um orçamento com {n}.'))}">
          <span class="prod-media">{img(f'pedras/{t}-{s}', f'Textura da pedra {n}')}</span>
          <span class="prod-name">{n}</span>
        </a>''' for i, (t, s, n) in enumerate(HOME_PRODUTOS))
    return f'''  <section class="sec bg-gray">
    <div class="container">
      {title('Nossos', 'produtos', ghost='Pedras', sub='Fotos meramente ilustrativas. Mármores, assim como qualquer outro produto extraído da natureza, estão sujeitos a variações de veios e tonalidades.')}
      <div class="prod-grid">{cards}
      </div>
      <div class="center"><a class="btn btn-outline rv" href="/produtos/">Ver todas as pedras</a></div>
    </div>
  </section>
'''


def parceiros():
    one = ''.join('<img src="/assets/img/site/parceiro-dclass.png" alt="D\'class Ambientes Planejados" width="369" height="92" loading="lazy">' for _ in range(6))
    return f'''  <section class="partners" aria-label="Parceiros">
    <div class="partners-track"><div>{one}</div><div aria-hidden="true">{one}</div></div>
  </section>
'''


def faq(slug, bg='bg-white'):
    itens = '\n'.join(
        f'        <details class="rv"{" open" if i == 0 else ""}><summary>{esc(q)}<svg aria-hidden="true"><use href="#i-plus"/></svg></summary><div class="faq-a"><p>{esc(a)}</p></div></details>'
        for i, (q, a) in enumerate(FAQS[slug]))
    return f'''  <section class="sec {bg}" aria-labelledby="faq-t">
    <div class="container faq-grid">
      <div>
        {title('Dúvidas', 'frequentes', center=False)}
        <p class="txt">Não encontrou o que procura? Fale com a gente pelo WhatsApp.</p>
        <a class="btn btn-brown" href="{wa('Olá! Vim pelo site e tenho uma dúvida.')}" target="_blank" rel="noopener" data-track="whatsapp_faq"><svg><use href="#i-wa"/></svg> {E['telefone_br']}</a>
      </div>
      <div class="faq-list">
{itens}
      </div>
    </div>
  </section>
'''


def cta_band(t='Venha fazer um orçamento conosco, <span>sem compromisso!</span>', sub='O menor prazo de entrega da região, com apoio de profissionais especializados e experientes.'):
    return f'''  <section class="cta-band">
    <div class="cta-bg" aria-hidden="true">{img('site/textura-nero', '', extra=' data-par="12"')}</div>
    <div class="container cta-inner rv">
      <div><h2>{t}</h2><p>{sub}</p></div>
      <a class="btn btn-white" href="{wa()}" target="_blank" rel="noopener" data-track="whatsapp_cta"><svg><use href="#i-wa"/></svg> Fale agora</a>
    </div>
  </section>
'''


# ---------- Páginas internas ----------
def empresa_historia():
    return f'''  <section class="sec bg-white">
    <div class="container two-col">
      <div class="rv">
        {title('Nossa', 'história', center=False)}
        <p class="txt">Há anos no mercado, a Forte Rocha Marmoraria concretiza os mais variados e ousados projetos arquitetônicos, de interiores e exteriores, realizando sonhos e desejos de cada cliente.</p>
        <p class="txt">Aprimoramos continuamente nossa atividade para oferecer sempre o melhor produto, com investimentos em equipamentos e mão de obra qualificada. Além disso, temos ótima flexibilidade de negociação e diversas formas de pagamento, visando sempre maior comodidade dos nossos clientes.</p>
      </div>
      <figure class="frame rv" style="--d:1">{img('site/cozinha-ilha-marmore', 'Cozinha com ilha revestida em mármore')}</figure>
    </div>
  </section>
  <section class="sec bg-gray">
    <div class="container two-col is-rev">
      <figure class="frame rv">{img('site/ilha-marmore-branco', 'Ilha em mármore branco com veios cinza')}</figure>
      <div class="rv" style="--d:1">
        {title('Nossa', 'missão', center=False)}
        <p class="txt">Fornecer continuamente as melhores soluções para as obras. Nossa missão é realizar os sonhos de nossos clientes, oferecendo sempre as melhores opções em mármores, granitos e outras pedras, a fim de compor desde os simples aos mais exigentes e complexos projetos, mantendo a qualidade em atendimento, processamento da pedra e excelência em mão de obra.</p>
        <ul class="ticks">
          <li><svg><use href="#i-check"/></svg> Medição e instalação in loco</li>
          <li><svg><use href="#i-check"/></svg> Máquinas de alta capacidade produtiva</li>
          <li><svg><use href="#i-check"/></svg> Diversas formas de pagamento</li>
        </ul>
      </div>
    </div>
  </section>
'''


def servicos_page():
    lista = ''.join(f'<li><svg><use href="#i-check"/></svg>{s}</li>' for s in [
        'Tampos para cozinhas, banheiros e áreas de serviço', 'Rebaixo italiano', 'Revestimento de escadas',
        'Divisórias e testeiras', 'Soleiras', 'Pisos e paredes', 'Cortes e acabamentos', 'Impermeabilização',
        'Revitalização', 'Restauração', 'Lavatórios, ilhas, bancadas e túmulos', 'Serviços em porcelanato'])
    cards = ''.join(f'''
        <article class="serv-card rv" id="{s['id']}" style="--d:{i % 3}">
          <div class="serv-media">{img(SERV_IMG[s['id']], s['nome'])}<span class="serv-ic"><svg aria-hidden="true"><use href="#{s['icon']}"/></svg></span></div>
          <div class="serv-body">
            <h3>{s['nome']}</h3>
            <p>{s['txt']}</p>
            <a class="more" href="{wa('Olá! Quero um orçamento de ' + s['nome'].lower() + '.')}" target="_blank" rel="noopener" data-track="whatsapp_servico_{s['id']}">Pedir orçamento <svg><use href="#i-arrow"/></svg></a>
          </div>
        </article>''' for i, s in enumerate(SERVICOS))
    etapas = ''.join(f'''<li class="rv" style="--d:{i}"><b>{i + 1:02d}</b><h3>{t}</h3><p>{d}</p></li>''' for i, (t, d) in enumerate(ETAPAS))
    return f'''  <section class="sec bg-white">
    <div class="container two-col">
      <div class="rv">
        {title('Nossos', 'serviços', center=False)}
        <p class="txt">Possuímos uma equipe altamente qualificada e, com constantes investimentos em máquinas de alta capacidade produtiva, oferecemos os seguintes serviços:</p>
        <ul class="serv-list">{lista}</ul>
      </div>
      <figure class="frame rv" style="--d:1">{img('site/hero-cozinha-marmore', 'Cozinha com ilha e bancada em mármore branco')}</figure>
    </div>
  </section>
  <section class="sec bg-gray">
    <div class="container">
      {title('O que', 'fazemos')}
      <div class="serv-grid">{cards}
      </div>
    </div>
  </section>
  <section class="sec bg-white">
    <div class="container">
      {title('Como', 'trabalhamos')}
      <ol class="steps">{etapas}</ol>
    </div>
  </section>
'''


def obras_page():
    total = len(OBRAS)
    chips = [f'<button type="button" class="chip is-on" data-f="all" aria-pressed="true">Todas <sup>{total}</sup></button>']
    for c, n in CATEGORIAS_OBRAS:
        k = sum(1 for o in OBRAS if o[1] == c)
        chips.append(f'<button type="button" class="chip" data-f="{c}" aria-pressed="false">{n} <sup>{k}</sup></button>')
    items = ''.join(gal_item(s, i) for i, (s, _, _) in enumerate(OBRAS))
    return f'''  <section class="sec bg-gray">
    <div class="container">
      {title('Algumas', 'fotos', sub='Cozinhas, banheiros, escadas e áreas gourmet entregues pela nossa equipe. Clique para ampliar.')}
      <div class="filters rv" role="toolbar" aria-label="Filtrar obras">{''.join(chips)}</div>
      <div class="gal-grid" id="gal-grid">{items}
      </div>
    </div>
  </section>
'''


def pedra_card(tipo, s, n, tom, i):
    tn = 'Granito' if tipo == 'granito' else ('Travertino' if 'travertino' in s else 'Mármore')
    full = n if tn == 'Travertino' else f'{tn} {n}'
    return f'''
        <a class="prod rv" style="--d:{i % 4}" href="/assets/img/pedras/{tipo}-{s}.webp" data-type="{tipo}" data-tone="{tom}" data-cap="{esc(full)}" data-lightbox="pedras" data-wa="{esc(wa(f'Olá! Quero um orçamento com {full}.'))}">
          <span class="prod-media">{img(f'pedras/{tipo}-{s}', f'Textura da pedra {full}')}</span>
          <span class="prod-name">{esc(n)}</span>
        </a>'''


def produtos_page():
    gran = ''.join(pedra_card('granito', s, n, t, i) for i, (s, n, t) in enumerate(GRANITOS))
    marm = ''.join(pedra_card('marmore', s, n, t, i) for i, (s, n, t) in enumerate(MARMORES))
    return f'''  <section class="sec bg-white">
    <div class="container">
      {title('Alguns', 'granitos', sub='Mais duro e resistente a riscos, calor e manchas — o preferido para pias e bancadas de cozinha.')}
      <div class="prod-grid is-6">{gran}
      </div>
    </div>
  </section>
  <section class="sec bg-gray">
    <div class="container">
      {title('Alguns', 'mármores', sub='Veios marcantes e brilho elegante — ideal para lavatórios, pisos, escadas e mesas.')}
      <div class="prod-grid is-6">{marm}
      </div>
      <p class="note rv">Fotos meramente ilustrativas. Mármores, assim como qualquer outro produto extraído da natureza, estão sujeitos a variações de veios e tonalidades. Também trabalhamos com {', '.join(x.lower() for x in OUTRAS_PEDRAS)} — consulte.</p>
    </div>
  </section>
'''


PERFIS = {
    'reto': ('M0 30H100V50H0Z', ''), 'boleado': ('M0 30H90A10 10 0 0 1 90 50H0Z', ''),
    'meio-boleado': ('M0 30H90Q100 30 100 40V50H0Z', ''), 'bisote': ('M0 30H94L100 36V50H0Z', ''),
    'bisotado': ('M0 30H93L100 37V43L93 50H0Z', ''),
    'meia-esquadria': ('M0 30H100L80 50H0Z M100 30V96H80V50Z', 'M80 50L100 30'),
    'meia-cana': ('M0 30H100V33Q88 40 100 47V50H0Z', ''),
    'peito-pombo': ('M0 30H92C101 30 103 38 97 41C93 43 100 46 100 50H0Z', ''),
    'saia': ('M0 30H100V90H92V50H0Z', 'M92 50H100'), 'frontao': ('M14 50H112V68H14Z M0 14H14V68H0Z', 'M14 50V68'),
    'guarnicao': ('M0 36H86V26H100V58H0Z', 'M86 36V58'), 'engrosso': ('M0 30H100V64H84V50H0Z', 'M84 50H100'),
    'friso': ('M0 30H64V34H68V30H74V34H78V30H84V34H88V30H100V50H0Z', ''),
}


def dicas_page():
    perfis = ''.join(f'''
        <article class="perf rv" style="--d:{i % 4}">
          <svg class="pf" viewBox="-6 6 124 96" role="img" aria-label="Desenho do perfil {esc(n.lower())}"><path class="pf-shape" d="{PERFIS[p][0]}"/>{f'<path class="pf-seam" d="{PERFIS[p][1]}"/>' if PERFIS[p][1] else ''}</svg>
          <h3>{n}</h3>
          <p>{t}</p>
        </article>''' for i, (n, p, t) in enumerate([a for a in ACABAMENTOS if a[1]]))
    glo = ''.join(f'<div class="glo rv"><dt>{n}</dt><dd>{t}</dd></div>' for n, p, t in ACABAMENTOS if not p)
    return f'''  <section class="sec bg-white">
    <div class="container">
      {title('Conheça', 'detalhes', sub='Opções e nomes técnicos usados de acordo com o tipo e o modelo de acabamento desejado. Os desenhos mostram o corte lateral da pedra.')}
      <div class="perf-grid">{perfis}
      </div>
    </div>
  </section>
  <section class="sec bg-gray">
    <div class="container">
      {title('Termos do', 'orçamento')}
      <dl class="glo-grid">{glo}</dl>
    </div>
  </section>
'''


def contato_page():
    return f'''  <section class="sec bg-white">
    <div class="container contact-grid">
      <div class="rv">
        {title('Fale', 'conosco', center=False)}
        <p class="txt">Mande fotos, medidas ou só a ideia. Ao enviar, abrimos o WhatsApp com a sua mensagem pronta.</p>
        {form_html()}
      </div>
      <aside class="ct-box is-solid rv" style="--d:1">
        <h3>Contato</h3>
        {contato_info()}
        <a class="btn btn-white" href="{E['facebook']}" target="_blank" rel="noopener"><svg><use href="#i-fb"/></svg> Facebook</a>
      </aside>
    </div>
    <div class="container ct-map rv">
      <iframe title="Mapa: Marmoraria Forte Rocha em Paulínia - SP" data-src="https://www.google.com/maps?q=Rua+Shirlei+Ramos+Maia+de+Souza,+930,+Paul%C3%ADnia+-+SP&amp;output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
    </div>
  </section>
'''


# =====================================================================
# Páginas
# =====================================================================
PAGES = [
    dict(path='/', slug='home', crumb=None,
         title='Marmoraria em Paulínia SP | Mármore e Granito sob Medida | Forte Rocha',
         description='Bancadas, lavatórios, rebaixo italiano, escadas e pisos em mármore, granito, quartzo e porcelanato, sob medida e com medição no local. Paulínia e região de Campinas.',
         preload='<link rel="preload" as="image" href="/assets/img/site/hero-cozinha-marmore.webp" fetchpriority="high">',
         faq='home',
         body=[slider(), info_band(), sobre_home(), materiais(), obras_home(), contadores(False), processo_home(),
               depoimentos(), produtos_home(), cta_band(), atendimento(), parceiros(), faq('home', 'bg-white')]),
    dict(path='/empresa/', slug='empresa', crumb='Empresa', faq='empresa',
         title='Sobre a Forte Rocha | Marmoraria em Paulínia - SP',
         description='Conheça a Marmoraria Forte Rocha: mármores e granitos nacionais e importados, equipe especializada e projetos sob medida em Paulínia e região de Campinas.',
         body=[page_header('Empresa', 'Empresa', 'site/cozinha-ilha-marmore'),
               resumo('Quem é a Marmoraria Forte Rocha?', E['resumo']),
               empresa_historia(), info_band(False), contadores(False), depoimentos(), faq('empresa', 'bg-gray'), parceiros()]),
    dict(path='/servicos/', slug='servicos', crumb='Serviços', faq='servicos',
         title='Bancadas, Lavatórios e Rebaixo Italiano | Serviços Forte Rocha',
         description='Tampos de cozinha, lavatórios, cubas esculpidas, rebaixo italiano, escadas, pisos, churrasqueiras, porcelanato e restauração de pedras em Paulínia - SP.',
         body=[page_header('Serviços', 'Serviços', 'obras/ilha-cascata-granito-preto'),
               resumo('Quais serviços a Forte Rocha faz?', dict(FAQS['servicos'])['Quais serviços a Forte Rocha faz?']),
               servicos_page(), cta_band(), faq('servicos', 'bg-gray')]),
    dict(path='/obras/', slug='obras', crumb='Obras Realizadas', faq='obras',
         title='Obras Realizadas em Mármore e Granito | Forte Rocha',
         description='Galeria de cozinhas, banheiros, lavatórios, escadas, áreas gourmet e churrasqueiras em mármore, granito e quartzo feitos pela Forte Rocha em Paulínia e região.',
         body=[page_header('Obras Realizadas', 'Obras Realizadas', 'obras/cozinha-l-granito-preto'),
               resumo('Que tipo de obra a Forte Rocha faz?',
                      'Projetos residenciais e comerciais em pedra natural: bancadas e ilhas de cozinha, lavatórios com cuba esculpida e rebaixo italiano, escadas, pisos, áreas gourmet, churrasqueiras e áreas de serviço — em Paulínia e região de Campinas.'),
               obras_page(), cta_band(), faq('obras', 'bg-white')]),
    dict(path='/produtos/', slug='produtos', crumb='Produtos', faq='produtos',
         title='Mármores e Granitos: Cores e Tipos de Pedra | Forte Rocha',
         description='Granitos e mármores: Preto São Gabriel, Branco Ceará, Café Imperial, Nero Marquina, Crema Marfil, Travertino e mais. Veja onde usar cada pedra.',
         body=[page_header('Produtos', 'Produtos', 'site/textura-imperador'),
               resumo('Qual a diferença entre mármore e granito?', dict(FAQS['produtos'])['Qual a diferença entre mármore e granito?']),
               produtos_page(), cta_band(), faq('produtos', 'bg-white')]),
    dict(path='/dicas/', slug='dicas', crumb='Dicas', faq='dicas',
         title='Acabamentos de Borda em Mármore e Granito: Dicas | Forte Rocha',
         description='Reto, boleado, bisotê, meia esquadria, meia cana, peito de pombo, saia, frontão e guarnição: veja o desenho de cada acabamento de borda e onde usar.',
         body=[page_header('Dicas', 'Dicas', 'obras/lavatorio-cuba-esculpida-branca'),
               resumo('Qual acabamento de borda escolher?', dict(FAQS['dicas'])['Qual acabamento de borda escolher?'].replace(' Na página de dicas explicamos cada modelo com desenho do perfil.', '')),
               dicas_page(), cta_band(), faq('dicas', 'bg-white')]),
    dict(path='/contato/', slug='contato', crumb='Contato', faq='contato',
         title='Contato e Orçamento | Marmoraria Forte Rocha Paulínia - SP',
         description=f'Peça seu orçamento: WhatsApp {E["telefone_br"]}, {E["email"]}. Rua Shirlei Ramos Maia de Souza, 930, Parque dos Servidores, Paulínia - SP.',
         body=[page_header('Contato', 'Contato', 'site/ilha-marmore-branco'), contato_page(), faq('contato', 'bg-gray')]),
]


# =====================================================================
# schema.org
# =====================================================================
ORG_ID, BIZ_ID, SITE_ID = f'{SITE}/#organization', f'{SITE}/#loja', f'{SITE}/#website'


def org_nodes():
    endereco = {'@type': 'PostalAddress', 'streetAddress': 'Rua Shirlei Ramos Maia de Souza, 930',
                'addressLocality': E['cidade'], 'addressRegion': E['uf'], 'addressCountry': 'BR'}
    if E['cep']:
        endereco['postalCode'] = E['cep']
    area = [{'@type': 'City', 'name': 'Paulínia'}, {'@type': 'AdministrativeArea', 'name': 'Região Metropolitana de Campinas'}]
    return [
        {'@type': 'Organization', '@id': ORG_ID, 'name': E['nome'], 'url': SITE + '/',
         'logo': {'@type': 'ImageObject', 'url': f'{SITE}/assets/logos/logo-forterocha.png'}, 'image': OG_IMAGE,
         'description': E['resumo'], 'address': endereco, 'email': E['email'],
         'telephone': E['whatsapp'], 'sameAs': [E['facebook']],
         'knowsAbout': ['mármore', 'granito', 'quartzo', 'travertino', 'limestone', 'ônix', 'porcelanato',
                        'rebaixo italiano', 'cuba esculpida', 'bancada de cozinha', 'revestimento de escadas',
                        'acabamento de bordas em pedra'],
         'contactPoint': [{'@type': 'ContactPoint', 'contactType': 'sales', 'telephone': E['whatsapp'],
                           'email': E['email'], 'areaServed': 'BR', 'availableLanguage': 'Portuguese'}]},
        {'@type': ['LocalBusiness', 'HomeAndConstructionBusiness'], '@id': BIZ_ID, 'name': E['nome'],
         'parentOrganization': {'@id': ORG_ID}, 'url': SITE + '/', 'image': OG_IMAGE,
         'telephone': E['whatsapp'], 'email': E['email'], 'address': endereco,
         'geo': {'@type': 'GeoCoordinates', 'latitude': E['lat'], 'longitude': E['lng']},
         'hasMap': 'https://www.google.com/maps/search/?api=1&query=Rua+Shirlei+Ramos+Maia+de+Souza,+930+Paul%C3%ADnia+SP',
         'openingHours': E['horario_schema'], 'areaServed': area, 'priceRange': '$$',
         'hasOfferCatalog': {'@type': 'OfferCatalog', 'name': 'Serviços em pedra natural',
                             'itemListElement': [{'@type': 'Offer', 'itemOffered': {'@type': 'Service', 'name': s['nome'], 'description': s['txt']}}
                                                 for s in SERVICOS]}},
        {'@type': 'WebSite', '@id': SITE_ID, 'url': SITE + '/', 'name': E['nome'], 'inLanguage': 'pt-BR',
         'publisher': {'@id': ORG_ID}},
    ]


def page_graph(p):
    url = SITE + p['path']
    nodes = org_nodes()
    webpage = {'@type': {'empresa': 'AboutPage', 'contato': 'ContactPage', 'obras': 'CollectionPage'}.get(p['slug'], 'WebPage'),
               '@id': url + '#webpage', 'url': url, 'name': p['title'], 'description': p['description'],
               'inLanguage': 'pt-BR', 'isPartOf': {'@id': SITE_ID}, 'about': {'@id': BIZ_ID},
               'primaryImageOfPage': OG_IMAGE, 'dateModified': HOJE.isoformat(),
               'speakable': {'@type': 'SpeakableSpecification', 'cssSelector': ['h1', '.resumo-a']}}
    if p['crumb']:
        nodes.append({'@type': 'BreadcrumbList', '@id': url + '#breadcrumb', 'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': 'Home', 'item': SITE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': H.unescape(p['crumb']), 'item': url}]})
        webpage['breadcrumb'] = {'@id': url + '#breadcrumb'}
    nodes.append(webpage)
    if p.get('faq'):
        nodes.append({'@type': 'FAQPage', '@id': url + '#faq', 'isPartOf': {'@id': url + '#webpage'},
                      'mainEntity': [{'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}}
                                     for q, a in FAQS[p['faq']]]})
    if p['slug'] == 'servicos':
        nodes.append({'@type': 'ItemList', 'name': 'Serviços da Marmoraria Forte Rocha', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'item': {
                '@type': 'Service', '@id': f'{url}#{s["id"]}', 'name': s['nome'], 'description': s['txt'],
                'provider': {'@id': BIZ_ID}, 'areaServed': 'Paulínia e região de Campinas - SP',
                'image': f'{SITE}/assets/img/{SERV_IMG[s["id"]]}.webp'}} for i, s in enumerate(SERVICOS)]})
    if p['slug'] == 'obras':
        nodes.append({'@type': 'ImageGallery', 'name': 'Obras realizadas pela Forte Rocha', 'url': url,
                      'associatedMedia': [{'@type': 'ImageObject', 'contentUrl': f'{SITE}/assets/img/obras/{s}.webp',
                                           'name': t, 'description': f'{t} — {CAT_NOME[c]}', 'creator': {'@id': ORG_ID}}
                                          for s, c, t in OBRAS]})
    if p['slug'] == 'produtos':
        nodes.append({'@type': 'ItemList', 'name': 'Granitos e mármores', 'itemListElement': [
            {'@type': 'ListItem', 'position': i + 1, 'name': f'{"Granito" if t == "granito" else "Mármore"} {n}',
             'image': f'{SITE}/assets/img/pedras/{t}-{s}.webp'} for i, (t, s, n, _) in enumerate(PEDRAS)]})
    if p['slug'] == 'dicas':
        nodes.append({'@type': 'DefinedTermSet', '@id': url + '#glossario', 'name': 'Glossário de acabamentos em mármore e granito',
                      'hasDefinedTerm': [{'@type': 'DefinedTerm', 'name': n, 'description': t,
                                          'inDefinedTermSet': {'@id': url + '#glossario'}} for n, _, t in ACABAMENTOS]})
    return {'@context': 'https://schema.org', '@graph': nodes}


# =====================================================================
# Montagem
# =====================================================================
def head_meta(p, noindex=False):
    url = SITE + p['path']
    t, d = esc(p['title']), esc(p['description'])
    robots = 'noindex, follow' if noindex else 'index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1'
    canon = '' if noindex else f'''
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="pt-BR" href="{url}">
  <link rel="alternate" hreflang="x-default" href="{url}">'''
    return f'''  <title>{t}</title>
  <meta name="description" content="{d}">
  <meta name="robots" content="{robots}">{canon}
  <meta name="author" content="{E['nome']}">
  <meta name="geo.region" content="BR-{E['uf']}">
  <meta name="geo.placename" content="{E['cidade']}">
  <meta name="geo.position" content="{E['lat']};{E['lng']}">
  <meta name="ICBM" content="{E['lat']}, {E['lng']}">
  <link rel="icon" type="image/png" sizes="32x32" href="/assets/icons/favicon-32.png">
  <link rel="icon" type="image/png" sizes="48x48" href="/assets/icons/favicon-48.png">
  <link rel="apple-touch-icon" href="/assets/icons/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="theme-color" content="#7f4f31">
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="{E['nome']}">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:title" content="{t}">
  <meta property="og:description" content="{d}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{OG_IMAGE}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:image:alt" content="Cozinha com ilha em mármore branco — Marmoraria Forte Rocha">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{t}">
  <meta name="twitter:description" content="{d}">
  <meta name="twitter:image" content="{OG_IMAGE}">
  <link rel="alternate" type="text/plain" title="Resumo para IAs (llms.txt)" href="/llms.txt">'''


def gtm():
    if not GTM_ID:
        return ('  <!-- Google Tag Manager: defina GTM_ID em src/data.py (GA4, Meta Pixel e Hotjar entram pelo GTM) -->', '')
    head = f'''  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){{w[l]=w[l]||[];w[l].push({{'gtm.start':new Date().getTime(),event:'gtm.js'}});var f=d.getElementsByTagName(s)[0],j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src='https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);}})(window,document,'script','dataLayer','{GTM_ID}');</script>'''
    body = f'<noscript><iframe src="https://www.googletagmanager.com/ns.html?id={GTM_ID}" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>'
    return head, body


def render(p, layout, noindex=False):
    content = '\n'.join(p['body'])
    cur = ' aria-current="page"'
    nav = '\n        '.join(f'<a href="{href}"{cur if href == p["path"] else ""}>{label}</a>' for href, label in NAV)
    g_head, g_body = gtm()
    jsonld = json.dumps(page_graph(p), ensure_ascii=False, separators=(',', ':'))
    html = layout
    for k, v in {
        '{{gtm_head}}': g_head, '{{gtm_body}}': g_body,
        '{{head_meta}}': head_meta(p, noindex) + ('' if noindex else f'\n  <script type="application/ld+json">{jsonld}</script>'),
        '{{> icons}}': (SRC / 'sections/icons.html').read_text(), '{{slug}}': p['slug'], '{{preload}}': p.get('preload', ''),
        '{{nav}}': nav, '{{wa}}': esc(wa()), '{{whatsapp}}': E['telefone_br'], '{{email_wbr}}': E['email'].replace('@', '@<wbr>'), '{{email}}': E['email'],
        '{{horario}}': E['horario'], '{{endereco}}': f"{E['rua'].replace(' — ', ' - ')} - {E['cidade']} - {E['uf']}",
        '{{facebook}}': E['facebook'], '{{updated}}': HOJE.isoformat(), '{{content}}': content,
    }.items():
        html = html.replace(k, v)
    # versão nos assets: o navegador baixa o CSS/JS novo a cada publicação
    return html.replace('/css/style.css"', f'/css/style.css?v={VERSAO}"').replace('/js/main.js"', f'/js/main.js?v={VERSAO}"')


# =====================================================================
# Arquivos de SEO / GEO
# =====================================================================
def sitemap():
    prio = {'/': '1.0', '/servicos/': '0.9', '/obras/': '0.9', '/produtos/': '0.8', '/dicas/': '0.7',
            '/empresa/': '0.7', '/contato/': '0.8'}
    imgs = {'/': ['site/hero-cozinha-marmore.webp'], '/obras/': [f'obras/{s}.webp' for s, _, _ in OBRAS],
            '/produtos/': [f'pedras/{t}-{s}.webp' for t, s, _, _ in PEDRAS],
            '/servicos/': [f'{v}.webp' for v in SERV_IMG.values()]}
    urls = []
    for p in PAGES:
        im = ''.join(f'\n    <image:image><image:loc>{SITE}/assets/img/{i}</image:loc></image:image>' for i in imgs.get(p['path'], []))
        urls.append(f'''  <url>
    <loc>{SITE}{p['path']}</loc>
    <lastmod>{HOJE.isoformat()}</lastmod>
    <changefreq>{'weekly' if p['path'] in ('/', '/obras/') else 'monthly'}</changefreq>
    <priority>{prio[p['path']]}</priority>{im}
  </url>''')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
            'xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">\n' + '\n'.join(urls) + '\n</urlset>\n')


def robots():
    bots = ['GPTBot', 'OAI-SearchBot', 'ChatGPT-User', 'ClaudeBot', 'Claude-User', 'Claude-SearchBot',
            'anthropic-ai', 'PerplexityBot', 'Perplexity-User', 'Google-Extended', 'Applebot-Extended',
            'Bingbot', 'meta-externalagent', 'CCBot', 'Amazonbot', 'DuckAssistBot', 'cohere-ai', 'MistralAI-User']
    ai = '\n'.join(f'User-agent: {b}' for b in bots)
    return f'''# Marmoraria Forte Rocha — {SITE}
# Buscadores e assistentes de IA são bem-vindos: o conteúdo público pode ser lido e citado.

User-agent: *
Allow: /
Disallow: /src/

# Assistentes e buscadores de IA (GEO)
{ai}
Allow: /

Sitemap: {SITE}/sitemap.xml
'''


def llms_txt():
    pages = '\n'.join(f'- [{H.unescape(p["title"])}]({SITE}{p["path"]}): {p["description"]}' for p in PAGES)
    return f'''# {E['nome']}

> {E['resumo']}

Fatos principais:
- Nome: {E['nome']}
- Endereço: {E['rua']}, {E['cidade']} - {E['uf']}
- Área atendida: {E['area']}
- Materiais: mármores e granitos nacionais e importados, {', '.join(x.lower() for x in OUTRAS_PEDRAS)} e travertino
- Serviços: {'; '.join(s['nome'] for s in SERVICOS)}
- Diferenciais: medição no local (in loco), peças sob medida, orçamento sem compromisso, um dos menores prazos de entrega da região, diversas formas de pagamento, parceria com construtoras e com empresas de móveis planejados
- Números: {'; '.join(f'{n}{s} {l}' for n, s, l in NUMEROS)}
- Horário: {E['horario']}
- Contato: WhatsApp {E['whatsapp']} · {E['email']} · Facebook {E['facebook']}

## Páginas
{pages}
'''


def llms_full():
    serv = '\n'.join(f'- {s["nome"]}: {s["txt"]}' for s in SERVICOS)
    pedras_txt = ('Granitos: ' + ', '.join(n for _, n, _ in GRANITOS) + '.\nMármores e travertinos: '
                  + ', '.join(n for _, n, _ in MARMORES) + '.')
    acab = '\n'.join(f'- {n}: {t}' for n, _, t in ACABAMENTOS)
    proc = '\n'.join(f'{i + 1}. {t}: {d}' for i, (t, d) in enumerate(ETAPAS))
    obras = '\n'.join(f'- {n}: ' + ', '.join(t for _, c, t in OBRAS if c == k) for k, n in CATEGORIAS_OBRAS)
    vistos, faqs = set(), []
    for lista in FAQS.values():
        for q, a in lista:
            if q not in vistos:
                vistos.add(q)
                faqs.append(f'### {q}\n{a}\n')
    return llms_txt() + f'''
---

## Serviços
{serv}

## Produtos (seleção)
{pedras_txt}
Fotos ilustrativas: pedras naturais variam em veios e tonalidade.

## Como trabalhamos
{proc}

## Acabamentos de borda e termos técnicos
{acab}

## Obras realizadas (galeria)
{obras}

## Perguntas frequentes
{''.join(faqs)}'''


def manifest():
    return json.dumps({
        'name': 'Marmoraria Forte Rocha', 'short_name': 'Forte Rocha', 'lang': 'pt-BR', 'start_url': '/',
        'display': 'standalone', 'background_color': '#ffffff', 'theme_color': '#7f4f31',
        'icons': [{'src': '/assets/icons/icon-192.png', 'sizes': '192x192', 'type': 'image/png'},
                  {'src': '/assets/icons/icon-512.png', 'sizes': '512x512', 'type': 'image/png'}]},
        ensure_ascii=False, indent=2)


# URLs do site antigo → novas (preserva links e posicionamento)
REDIRECTS = {'index.html': '/', 'empresa.html': '/empresa/', 'servicos.html': '/servicos/', 'produtos.html': '/produtos/',
             'dicas.html': '/dicas/', 'contato.html': '/contato/', 'residencial.html': '/obras/', 'comercial.html': '/obras/',
             'about.html': '/empresa/', 'our-team.html': '/servicos/', 'services.html': '/produtos/', 'case-studies.html': '/contato/'}


def redirect_page(to):
    return f'''<!DOCTYPE html>
<html lang="pt-BR"><head><meta charset="utf-8"><title>Redirecionando…</title>
<meta name="robots" content="noindex"><link rel="canonical" href="{SITE}{to}">
<meta http-equiv="refresh" content="0; url={to}"><script>location.replace({json.dumps(to)})</script></head>
<body><a href="{to}">Continuar</a>
<script src="https://app-validacao-lp-sapp-validacao-lp.vercel.app/api/t" data-lp="site-forte-rocha" defer></script>
</body></html>
'''


def build():
    layout = (SRC / 'layout.html').read_text()
    for p in PAGES:
        out = ROOT / p['path'].strip('/') / 'index.html'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render(p, layout))
        print('ok', out.relative_to(ROOT))
    p404 = dict(path='/404.html', slug='404', crumb=None, title='Página não encontrada | Marmoraria Forte Rocha',
                description='A página que você procurou não existe.',
                body=[page_header('Página não encontrada', 'Erro 404', 'site/textura-nero',
                                  'A página que você procurou mudou de lugar ou não existe.'),
                      '  <section class="sec bg-white"><div class="container center"><a class="btn btn-brown" href="/">Ir para a Home</a> <a class="btn btn-outline" href="/obras/">Ver obras</a></div></section>'])
    files = {'404.html': render(p404, layout, noindex=True), 'sitemap.xml': sitemap(), 'robots.txt': robots(),
             'llms.txt': llms_txt(), 'llms-full.txt': llms_full(), 'site.webmanifest': manifest()}
    files.update({k: redirect_page(v) for k, v in REDIRECTS.items() if k != 'index.html'})
    for name, txt in files.items():
        (ROOT / name).write_text(txt)
    print('ok', ', '.join(files))


if __name__ == '__main__':
    build()

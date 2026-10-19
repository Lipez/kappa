import json,re,unicodedata
exec(open('units.py').read())
internal=json.load(open('internal.json'))
SERV="Serviço Temporada MME\nConcierge 7 dias por semana. Sob demanda: camareira, mercado abastecido na chegada, cozinheiro e garçom (pagos à parte)."
AC_COND="Os hóspedes têm uso exclusivo de todo o imóvel durante a estadia. As áreas comuns do condomínio podem ser usadas conforme o regulamento interno."
AC_CASA="Os hóspedes têm uso exclusivo de todo o imóvel durante a estadia."
bul=lambda xs:'\n'.join('• '+x for x in xs)
GROUP={ # code -> (grupo/destino, palavras-chave)
 **{c:("Maceió · Ponta Verde","apartamento temporada Ponta Verde, aluguel Maceió") for c in ["HS10J","IW01J","IW02J","LO02J"]},
 "HS01J":("Maceió · Jatiúca","apartamento temporada Jatiúca, aluguel Maceió"),
 **{c:("Maceió · Ipioca Beach Life","apartamento pé na areia Maceió, Ipioca Beach Life") for c in ["HS13J","HS20J","HS27J","MY02J"]},
 **{c:("Barra de São Miguel · Barra Bali","aluguel temporada Barra de São Miguel, Barra Bali") for c in ["HS03J","HS07J"]},
 "HS39J":("Barra de São Miguel · Iloa","Iloa Residence, apartamento Barra de São Miguel"),
 **{c:("Marceneiro · Oka Morada dos Milagres","casa temporada Praia do Marceneiro, Oka Milagres") for c in ["HS06J","HS36J","HS38J","KM01J"]},
 "PB02J":("Marceneiro · Villa Mauí","apartamento Praia do Marceneiro, Villa Mauí"),
 "PJ01J":("Marceneiro · Villa Anahí","apartamento piscina privativa Milagres, Villa Anahí"),
 "HS31J":("São Miguel dos Milagres · Vila Atauá","casa beira-mar São Miguel dos Milagres, Vila Atauá"),
 **{c:("São Miguel dos Milagres · Morada do Toque","casa temporada São Miguel dos Milagres, Morada do Toque") for c in ["HS26J","HS41J"]},
 **{c:("Tatuamunha · Villa Kanui","casa temporada Tatuamunha, Villa Kanui, Milagres") for c in ["HS09J","HS12J"]},
 **{c:("Tatuamunha · Villas do Rio","casa temporada Tatuamunha, Villas do Rio") for c in ["HS05J","HS35J","HS37J"]},
 **{c:("Tatuamunha · Naay Villas","apartamento Tatuamunha, Naay Villas, peixe-boi") for c in ["HS16J","HS18J","HS22J","HS29J","IM01J"]},
 **{c:("Patacho · Azuk Patacho","apartamento Praia do Patacho, Azuk Patacho") for c in ["JI01J","MI02J","NF02J"]},
 "NF04J":("Patacho · Villas Manatee","studio Praia do Patacho, Villas Manatee"),
 "II02J":("Piaçabuçu · Rio São Francisco","casa para grupos Rio São Francisco, Piaçabuçu"),
}
def slug(s):
    s=unicodedata.normalize('NFKD',s).encode('ascii','ignore').decode().lower()
    return re.sub(r'[^a-z0-9]+','-',s).strip('-')
out=[]
for code in sorted(U):
    u=U[code]; grp,kw=GROUP[code]
    base=u['title'].split(' · ')[0]
    st=f"{base} | Temporada MME"
    if len(st)>60: st=u['title'] if len(u['title'])<=60 else base
    assert len(st)<=60 and len(kw)<=60 and len(u['p1'])<=250, code
    ex=u.get('extra_serv')
    faq=(u['faq']+[("Qual o horário de check-in e check-out?",u.get('checkin',CHECKIN)),PETS])[:6]
    fields=[
     ("titulo","Título","Título do anúncio",u['title'],None),
     ("desc","Descrição","Descrição resumida",u['p1'],500),
     ("desc","Descrição","Observações gerais","Destaques\n"+bul(u['dest'])+"\n\nIdeal para\n"+u['ideal'],None),
     ("desc","Descrição","Sobre o espaço","Os quartos\n"+bul(u['quartos']),None),
     ("desc","Descrição","Sobre o acesso ao espaço",AC_CASA if code=="II02J" else AC_COND,None),
     ("desc","Descrição","Sobre interação com anfitrião",SERV+(("\n"+ex) if ex and 'cozinheiro e garçom também' not in ex else ""),None),
     ("desc","Descrição","Sobre a vizinhança","Localização\n"+u['loc_intro']+"\n"+bul(u['loc']),None),
     ("desc","Descrição","Como chegar",bul(u['chegar'])+"\n\nPerguntas frequentes\n"+'\n'.join(f"{q}\n{a}" for q,a in faq),None),
     ("seo","SEO","URL amigável","/"+slug(base),None),
     ("seo","SEO","Título da página",st,60),
     ("seo","SEO","Palavras-chave",kw,60),
     ("seo","SEO","Descrição",u['p1'],270),
    ]
    out.append(dict(code=code,name=internal[code],group=grp,title=u['title'],pend=u['pend'],cad=u['cad'],
        fields=[dict(sec=s,secLabel=sl,label=l,text=t,max=m) for s,sl,l,t,m in fields]))
json.dump(out,open('data.json','w'),ensure_ascii=False)
print(len(out)); print([ (o['code'],o['fields'][9]['text'],o['fields'][8]['text']) for o in out[:4]])

# Conteúdo por unidade no padrão do PDF "Site Temporada MME: auditoria e plano de correções" (13/10/2026).
# Fatos: site temporadamme.com.br (coleta 15/10/2026) + PDF. ⟦ ⟧ = confirmar antes de salvar.

CHECKIN = "Check-in a partir das 14h (15h entre 21/12 e 31/01) e check-out até 12h."
PETS = ("Aceita animais de estimação?", "Não.")
NOCRIB = "Não há berço disponível."

U = {}

# ---------------- MACEIÓ ----------------
U["HS01J"] = dict(
 title="Apto em Jatiúca a 500 m da praia, Maceió · 4 pessoas",
 p1="Apartamento de 1 quarto para até 4 pessoas no Edifício Corais do Mar, em Jatiúca, Maceió, a 500 m da praia e a 120 m de restaurantes. Aluguel por temporada da Temporada MME.",
 dest=["500 m da Praia de Jatiúca, 120 m de restaurantes e 300 m de supermercado",
       "35 m², 1 quarto e 1 banheiro, com cozinha completa",
       "Piscina do prédio com área rasa, espaço kids e área gourmet",
       "1 vaga de garagem gratuita e elevador",
       "Roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Casal ou família de até 4 pessoas que quer fazer tudo a pé. O sofá-cama fica na sala, então os 4 hóspedes dividem dois ambientes. " + NOCRIB,
 quartos=["Quarto: 1 cama de casal, ar-condicionado e guarda-roupa",
          "Sala: 1 sofá-cama de casal, ar-condicionado e TV"],
 loc_intro="Jatiúca é um bairro de orla de Maceió, na região da antiga Avenida Amélia Rosa.",
 loc=["Praia de Jatiúca: 500 m", "Restaurantes: 120 m", "Supermercado: 300 m"],
 chegar=["Aeroporto de Maceió: 23 km, ⟦cerca de X min de carro⟧",
         "Praia, restaurantes e mercado ficam a pé; o carro só é necessário para passeios."],
 faq=[("Tem piscina?", "Sim, a piscina do prédio, com área rasa."),
      ("Tem estacionamento?", "Sim, 1 vaga gratuita."),
      ("Quantas pessoas cabem?", "Até 4: 2 na cama de casal do quarto e 2 no sofá-cama da sala.")],
 pend=["Recepção do prédio: 24 horas ou remota?", "Andar e vista do apartamento"],
 cad=["Desmarcar \"Piscina Privada\" (manter \"Piscina\"), trocar \"Academia (privativa)\" por \"Academia (área comum)\" e desmarcar \"Acesso à praia\"",
      "Trocar a capa (hoje é um close de taças) e tirar fotos repetidas"],
)

U["HS10J"] = dict(
 title="Apto a 200 m da praia de Ponta Verde, Maceió · 5 pessoas",
 p1="Apartamento com suíte para até 5 pessoas no Edifício Smart Stays, em Ponta Verde, Maceió, a 200 m da praia, com vista parcial para o mar. Aluguel por temporada da Temporada MME.",
 dest=["200 m da Praia de Ponta Verde; supermercado e restaurantes a 50 m",
       "2 quartos (1 suíte) e 2 banheiros",
       "Sala com vista parcial para o mar e varanda",
       "Prédio com recepção 24 horas, piscina com área rasa, academia e sala de jogos",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Famílias de até 5 pessoas que querem ficar perto da praia e do comércio de Ponta Verde. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal, ar-condicionado e guarda-roupa",
          "Quarto: 2 camas de solteiro e ar-condicionado",
          "Sala: 1 sofá-cama de solteiro, ar-condicionado e TV"],
 loc_intro="Ponta Verde é um dos bairros de orla mais procurados de Maceió.",
 loc=["Praia de Ponta Verde: 200 m", "Supermercado: 50 m", "Restaurantes: 50 m"],
 chegar=["Aeroporto de Maceió: 24 km, ⟦cerca de X min de carro⟧",
         "Praia, restaurantes e mercado ficam a pé."],
 faq=[("A que distância fica da praia?", "200 m da Praia de Ponta Verde."),
      ("Tem vista para o mar?", "A sala tem vista parcial para o mar."),
      ("Tem estacionamento?", "Sim, 1 vaga gratuita.")],
 pend=["Andar e metragem"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "Capa: usar a foto da piscina com vista para o mar; galeria tem só 17 fotos"],
)

U["IW01J"] = dict(
 title="Apto 3 quartos a 200 m da praia de Ponta Verde · 6 pessoas",
 p1="Apartamento de 3 quartos para até 6 pessoas no Edifício Versa, em Ponta Verde, Maceió, a 200 m da praia, com piscina na cobertura. Aluguel por temporada da Temporada MME.",
 dest=["200 m da Praia de Ponta Verde; supermercado e restaurantes a 190 m",
       "72 m², 3 quartos separados (1 suíte), 2 banheiros e lavabo",
       "Piscina na cobertura do prédio ⟦com vista para o mar⟧",
       "Varanda com mobiliário e espaço para notebook",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias com filhos maiores ou grupos de até 6 pessoas que preferem quartos separados. Silêncio das 21h às 8h e sem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 2 camas de solteiro", "Quarto 3: 2 camas de solteiro"],
 loc_intro="Ponta Verde é um dos bairros de orla mais procurados de Maceió.",
 loc=["Praia de Ponta Verde: 200 m", "Supermercado: 190 m", "Restaurantes: 190 m"],
 chegar=["Aeroporto de Maceió: 24 km, ⟦cerca de X min de carro⟧"],
 faq=[("Quantos quartos tem?", "3: uma suíte de casal e dois quartos com 2 camas de solteiro cada."),
      ("A piscina é do apartamento?", "Não. É a piscina do prédio, na cobertura."),
      ("Pode fazer festa?", "Não. Eventos não são permitidos e o silêncio vai das 21h às 8h.")],
 pend=["A piscina da cobertura tem vista para o mar?"],
 cad=["Capa: usar a vista para o mar; tirar foto repetida",
      "O texto atual diz 150 m e 200 m da praia: usar 200 m em todos os lugares"],
)

U["IW02J"] = dict(
 title="Apto 3 quartos com lava e seca em Ponta Verde · 5 pessoas",
 p1="Apartamento de 3 quartos para até 5 pessoas no Maceió Facilities, em Ponta Verde, Maceió, a 350 m da praia, com lava e seca e piscina na cobertura. Aluguel por temporada da Temporada MME.",
 dest=["350 m da Praia de Ponta Verde; restaurantes a 100 m",
       "75 m², 3 quartos (1 suíte) e 2 banheiros",
       "Máquina de lavar e secar e grades de proteção para bebês",
       "Piscina na cobertura do prédio",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e TV a cabo inclusos"],
 ideal="Famílias com crianças pequenas e estadias longas. O check-in vai só até as 19h. Não há berço, apenas grades de proteção.",
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 2 camas de solteiro", "Quarto 3: 1 cama de solteiro"],
 loc_intro="Ponta Verde é um dos bairros de orla mais procurados de Maceió.",
 loc=["Praia de Ponta Verde: 350 m", "Restaurantes: 100 m", "Supermercado: 200 m"],
 chegar=["Aeroporto de Maceió: 25 km, ⟦cerca de X min de carro⟧"],
 faq=[("Até que horas posso fazer check-in?", "Das 14h às 19h. Check-out até 12h."),
      ("Tem máquina de lavar?", "Sim, de lavar e secar."),
      ("Serve para família com bebê?", "Tem grades de proteção para bebês, mas não oferece berço.")],
 checkin="Check-in das 14h às 19h e check-out até 12h.",
 pend=["Horário de silêncio: o cadastro diz 18h às 8h (parece erro)", "Andar"],
 cad=["Corrigir o horário de silêncio nas Regras",
      "Capa: usar a piscina da cobertura; galeria tem só 14 fotos",
      "Tirar \"Vista para o Mar\" do título até confirmar"],
)

U["LO02J"] = dict(
 title="Apto 2 quartos e 2 banheiros em Ponta Verde · 4 pessoas",
 p1="Apartamento de 78 m² com 2 quartos e 2 banheiros para até 4 pessoas no Maceió Facilities, em Ponta Verde, Maceió, a 350 m da praia. Aluguel por temporada da Temporada MME.",
 dest=["350 m da Praia de Ponta Verde; restaurantes a 100 m",
       "78 m² para 4 pessoas, com 2 banheiros (um com chuveiro acessível)",
       "Varanda voltada para rua tranquila",
       "Piscina na cobertura do prédio",
       "Roupa de cama e banho, Wi-Fi, ar-condicionado e ventilador de teto inclusos"],
 ideal="Casais, famílias de até 4 pessoas ou dois casais que querem banheiros separados. O check-in vai só até as 19h. " + NOCRIB,
 quartos=["Quarto 1: 1 cama de casal", "Quarto 2: 2 camas de solteiro"],
 loc_intro="Ponta Verde é um dos bairros de orla mais procurados de Maceió.",
 loc=["Praia de Ponta Verde: 350 m", "Restaurantes: 100 m", "Supermercado: 200 m"],
 chegar=["Aeroporto de Maceió: 25 km, ⟦cerca de X min de carro⟧"],
 faq=[("Tem estacionamento?", "⟦Confirmar⟧"),
      ("Até que horas posso chegar?", "Check-in das 14h às 19h."),
      ("Quantos banheiros?", "Dois.")],
 checkin="Check-in das 14h às 19h e check-out até 12h.",
 pend=["Tem vaga de garagem? (cadastro mostra 0)"],
 cad=["Fotos 7 a 10 repetem as fotos 1 a 5; galeria tem só 15 fotos"],
)

# ---------------- IPIOCA ----------------
IPI_LOC_INTRO = "A Praia de Ipioca fica no litoral norte de Maceió, a cerca de 20 km do centro. O Ipioca Beach Life tem restaurante, bar e lojas de conveniência."
IPI_CHEGAR = ["Aeroporto de Maceió: cerca de 39 km, ⟦cerca de X min de carro⟧", "Centro de Maceió: cerca de 20 km. Para sair do condomínio, o carro é a melhor opção."]

U["HS13J"] = dict(
 title="Apto com piscina privativa no Ipioca Beach Life · 5 pessoas",
 p1="Apartamento de 2 quartos com piscina e churrasqueira privativas na varanda, para até 5 pessoas, no Ipioca Beach Life, na Praia de Ipioca, em Maceió. Aluguel por temporada da Temporada MME.",
 dest=["Piscina e churrasqueira de uso exclusivo na varanda",
       "Condomínio com acesso direto à Praia de Ipioca",
       "50 m², 2 quartos (1 suíte) e 2 banheiros",
       "Máquina de lavar e secar",
       "Roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Casais ou famílias de até 5 pessoas que querem praia na porta e piscina própria. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 1 cama de casal", "Sala: 1 sofá-cama de solteiro"],
 loc_intro=IPI_LOC_INTRO,
 loc=["Praia de Ipioca: acesso pelo condomínio, ⟦X m⟧", "Boulevard Gastronômico: ⟦X km⟧"],
 chegar=IPI_CHEGAR,
 faq=[("A piscina é só do apartamento?", "Sim, a piscina da varanda é de uso exclusivo."),
      ("É longe do centro de Maceió?", "Cerca de 20 km, no litoral norte."),
      ("Tem estacionamento?", "⟦Confirmar⟧")],
 pend=["Vaga de garagem (cadastro mostra 0)", "Metros da unidade até a areia"],
 cad=["Primeira foto: a piscina privativa da varanda"],
)

U["HS20J"] = dict(
 title="Apto com piscina privativa e vista mar, Ipioca · 6 pessoas",
 p1="Apartamento com piscina privativa e vista lateral para o mar, para até 6 pessoas, no Ipioca Beach Life, na Praia de Ipioca, em Maceió. Aluguel por temporada da Temporada MME.",
 dest=["Vista lateral para o mar da varanda",
       "Piscina e churrasqueira de uso exclusivo",
       "2 quartos (1 suíte) e 2 banheiros, com água quente a gás",
       "Ar-condicionado nos quartos e na sala; máquina de lavar e secar",
       "⟦Acesso sem degraus e porta ampla⟧"],
 ideal="Famílias de até 6 pessoas que querem vista para o mar e piscina própria. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 2 camas de solteiro", "Sala: 1 sofá-cama de casal"],
 loc_intro=IPI_LOC_INTRO,
 loc=["Praia de Ipioca: acesso pelo condomínio, ⟦X m⟧"],
 chegar=IPI_CHEGAR,
 faq=[("Tem vista para o mar?", "Sim, vista lateral."),
      ("A piscina é privativa?", "Sim, de uso exclusivo da unidade."),
      ("É acessível para cadeira de rodas?", "⟦Confirmar acesso, porta do banheiro e box⟧")],
 pend=["Acessibilidade (sem degraus, porta ampla)", "Metragem e vaga"],
 cad=["Trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "Tirar \"Resort\" do título atual"],
)

U["HS27J"] = dict(
 title="Apto 3 quartos com piscina privativa em Ipioca · 6 pessoas",
 p1="Apartamento de 3 quartos com piscina privativa na varanda, para até 6 pessoas, no Ipioca Beach Life, na Praia de Ipioca, em Maceió. Aluguel por temporada da Temporada MME.",
 dest=["3 quartos separados, 2 deles com cama de casal",
       "Piscina e churrasqueira de uso exclusivo na varanda",
       "2 banheiros com água quente",
       "Condomínio com acesso direto à Praia de Ipioca",
       "Roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Dois casais com crianças ou famílias com avós. A unidade não aceita grupos de jovens nem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 1 cama de casal", "Quarto 3: 2 camas de solteiro"],
 loc_intro=IPI_LOC_INTRO,
 loc=["Praia de Ipioca: acesso pelo condomínio, ⟦X m⟧"],
 chegar=IPI_CHEGAR,
 faq=[("Quantas camas de casal?", "Duas, em quartos separados."),
      ("Aceita grupo de amigos jovens?", "Não. A unidade não aceita grupos de jovens."),
      ("A piscina é privativa?", "Sim, na varanda da unidade.")],
 pend=["Metragem e vaga"],
 cad=["Definir a faixa etária de \"grupo de jovens\" nas Regras"],
)

U["MY02J"] = dict(
 title="Apto 3 quartos para 8 com piscina privativa em Ipioca",
 p1="Apartamento de 3 quartos e 3 banheiros para até 8 pessoas no Ipioca Beach Life, na Praia de Ipioca, em Maceió, ⟦com piscina privativa na varanda⟧. Aluguel por temporada da Temporada MME.",
 dest=["Até 8 pessoas, a maior capacidade da Temporada MME no Ipioca",
       "3 quartos (1 suíte) e 3 banheiros",
       "⟦Piscina privativa na varanda⟧",
       "Condomínio com acesso direto à Praia de Ipioca",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias grandes e grupos que precisam de muitas camas e banheiros suficientes. Sem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 3 camas de solteiro ⟦fixas ou auxiliares⟧", "Quarto 3: 3 camas de solteiro ⟦fixas ou auxiliares⟧"],
 loc_intro=IPI_LOC_INTRO,
 loc=["Praia de Ipioca: acesso pelo condomínio, ⟦X m⟧"],
 chegar=IPI_CHEGAR,
 faq=[("Quantas pessoas cabem?", "Até 8."),
      ("Quantos banheiros?", "Três."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["Onde fica a piscina privativa e o tamanho", "Camas de solteiro: fixas ou auxiliares", "Metragem e vista"],
 cad=["Capa repetida na galeria", "Descrição atual tem só 76 palavras e não lista as camas"],
)

# ---------------- BARRA DE SÃO MIGUEL ----------------
U["HS03J"] = dict(
 title="Apto com varanda vista mar no Barra Bali · 6 pessoas",
 p1="Apartamento com varanda vista mar para até 6 pessoas no Condomínio Barra Bali, com acesso direto à praia, em Barra de São Miguel, a 29 km de Maceió. Aluguel por temporada da Temporada MME.",
 dest=["Varanda com mesa, cadeiras e vista para o mar",
       "Condomínio com acesso direto à praia e piscina de borda infinita com área rasa",
       "79 m², 2 quartos (1 suíte) e 2 banheiros",
       "300 m do Praêro Beach Club",
       "Roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias com crianças e casais que querem vista para o mar. O responsável pela reserva precisa ter 18 anos ou mais. Silêncio das 20h às 8h e sem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 1 cama de casal", "Sala: 1 sofá-cama de casal"],
 loc_intro="Barra de São Miguel fica no litoral sul de Alagoas, a 29 km de Maceió.",
 loc=["Praia da Barra de São Miguel: acesso direto pelo condomínio", "Praêro Beach Club: 300 m", "Supermercado e farmácia: ⟦X km⟧"],
 chegar=["Aeroporto de Maceió: 54 km, ⟦cerca de X min de carro⟧", "Maceió: 29 km"],
 faq=[("Tem vista para o mar?", "Sim, da varanda."),
      ("Qual a distância de Maceió?", "29 km."),
      ("Tem estacionamento?", "⟦1 ou 2 vagas — confirmar⟧")],
 pend=["Número de vagas (texto diz 2, cadastro diz 1)", "Distância de supermercado e farmácia"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "Capa repetida na galeria"],
)

U["HS07J"] = dict(
 title="Apto nascente com suíte queen no Barra Bali · 5 pessoas",
 p1="Apartamento nascente com suíte queen para até 5 pessoas no Condomínio Barra Bali, com acesso direto à praia, em Barra de São Miguel, a 29 km de Maceió. Aluguel por temporada da Temporada MME.",
 dest=["Varanda nascente, com sol da manhã",
       "Suíte com cama queen",
       "70 m², 2 quartos e 2 banheiros",
       "Condomínio com acesso direto à praia e piscina de borda infinita",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias de até 5 pessoas que preferem uma suíte com cama maior. Silêncio das 21h às 8h e sem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama queen", "Quarto 2: 2 camas de solteiro", "Sala: 1 sofá-cama de solteiro"],
 loc_intro="Barra de São Miguel fica no litoral sul de Alagoas, a 29 km de Maceió.",
 loc=["Praia da Barra de São Miguel: acesso direto pelo condomínio", "Praêro Beach Club: 300 m"],
 chegar=["Aeroporto de Maceió: 54 km, ⟦cerca de X min de carro⟧", "Maceió: 29 km"],
 faq=[("O apartamento pega sol?", "Sim, é nascente, com sol da manhã na varanda."),
      ("Tem vista para o mar?", "⟦Confirmar⟧"),
      ("Quantos banheiros?", "Dois.")],
 pend=["A varanda tem vista para o mar?", "Horário de silêncio do condomínio: 20h ou 21h (HS03J diz 20h)"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "Corrigir os nomes no quadro de camas (\"Individual\" e \"Duplo\" estão trocados)"],
)

U["HS39J"] = dict(
 title="Apto no Iloa Residence com café opcional · 4 pessoas",
 p1="Apartamento com suíte queen para até 4 pessoas no Iloa Residence, em Barra de São Miguel, a 2 km da praia, com piscina de resort e café da manhã contratável. Aluguel por temporada da Temporada MME.",
 dest=["Café da manhã contratável e servido no apartamento",
       "Condomínio com piscina de resort e bar de piscina terceirizado",
       "46 m², suíte com cama queen e varanda voltada para a área verde",
       "1º andar com elevador",
       "1 vaga de garagem gratuita; roupa de cama e banho e Wi-Fi inclusos"],
 ideal="Casais e famílias de até 4 pessoas que buscam diária acessível. A praia fica a 2 km, então o carro é recomendado. Não tem máquina de lavar. Silêncio das 21h às 8h. " + NOCRIB,
 quartos=["Suíte: 1 cama queen, ar-condicionado e guarda-roupa", "Sala: 1 sofá-cama de casal e ar-condicionado"],
 loc_intro="O Iloa Residence fica no bairro Piaçavas, em Barra de São Miguel, litoral sul de Alagoas.",
 loc=["Praia da Barra de São Miguel: 2 km", "Supermercado e restaurantes: 2,5 km", "Praêro Beach Club: 2,5 km", "Vila Niquim: 2,7 km"],
 chegar=["Aeroporto de Maceió: 50 km, ⟦cerca de X min de carro⟧", "O carro é recomendado para ir à praia e ao comércio."],
 faq=[("O café da manhã está incluído?", "Não. Pode ser contratado à parte e é servido no apartamento."),
      ("A que distância fica da praia?", "2 km."),
      ("Tem máquina de lavar?", "Não.")],
 extra_serv="No condomínio, o café da manhã pode ser contratado e servido no apartamento ⟦valor e horário⟧, e o bar da piscina (terceirizado) serve pratos, petiscos e bebidas.",
 pend=["Valor e horário do café da manhã"],
 cad=["Desmarcar \"Piscina Privada\"; marcar \"Café da manhã disponível (pago)\"",
      "Trocar a capa"],
)

# ---------------- MARCENEIRO ----------------
OKA_INTRO = "A Praia do Marceneiro fica em Passo de Camaragibe, na Rota Ecológica dos Milagres, vizinha a São Miguel dos Milagres."
OKA_LOC = ["Centro de São Miguel dos Milagres: ⟦X km⟧", "Praia do Patacho: ⟦X km⟧", "Santuário do Peixe-Boi, em Porto de Pedras: ⟦X km⟧"]
OKA_CHEGAR = ["Aeroporto de Maceió: ⟦127 km — conferir⟧, ⟦cerca de X h de carro⟧", "Aeroporto do Recife: cerca de 208 km", "O carro é a melhor forma de circular pela região."]
OKA_SERV = "Neste imóvel, cozinheiro e garçom também podem ser contratados (pagos à parte)."

U["HS06J"] = dict(
 title="Casa para 8 no Oka Milagres, acesso à praia · 8 pessoas",
 p1="Casa para até 8 pessoas no condomínio Oka Morada dos Milagres, com acesso direto à Praia do Marceneiro, na Rota dos Milagres, em Alagoas. Aluguel por temporada com serviço de hotel da Temporada MME.",
 dest=["Até 8 pessoas, a maior capacidade entre as casas do Oka Morada dos Milagres",
       "Acesso direto à Praia do Marceneiro pelo condomínio, a ⟦X m⟧ da casa",
       "⟦Piscina privativa⟧, churrasqueira e jardim",
       "3 quartos e 3 banheiros, com ar-condicionado",
       "Enxoval de hotel, kit de amenities, Wi-Fi, TV e artigos de praia inclusos"],
 ideal="Famílias com vários filhos e grupos de amigos de até 8 pessoas. Há só uma cama de casal; as demais são de solteiro. " + NOCRIB,
 quartos=["Suíte master: 1 cama de casal", "Suíte superior: 2 camas de solteiro e 1 cama auxiliar", "Quarto térreo: 2 camas de solteiro e 1 cama auxiliar"],
 loc_intro=OKA_INTRO, loc=OKA_LOC, chegar=OKA_CHEGAR, extra_serv=OKA_SERV,
 faq=[("A piscina é privativa?", "⟦Sim, de uso exclusivo da casa — confirmar⟧"),
      ("Quantos metros até a areia?", "⟦X m, pelo acesso do condomínio⟧"),
      ("Tem estacionamento?", "Sim, ⟦X vagas⟧ gratuitas.")],
 pend=["Piscina: privativa da casa ou do condomínio", "Metros até a areia", "Vagas", "Distâncias da região e tempo até o aeroporto"],
 cad=["Trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "Mostrar a praia nas primeiras fotos (hoje 8 das 10 primeiras são quartos)"],
)

U["HS36J"] = dict(
 title="Casa com piscina no Oka Milagres, acesso à praia · 7 pessoas",
 p1="Casa com piscina para até 7 pessoas no condomínio Oka Morada dos Milagres, com acesso direto à Praia do Marceneiro, na Rota dos Milagres, em Alagoas. Aluguel por temporada com serviço de hotel da Temporada MME.",
 dest=["Acesso direto à Praia do Marceneiro pelo condomínio, a ⟦X m⟧ da casa",
       "Piscina ⟦privativa⟧ no jardim ⟦e churrasqueira⟧",
       "3 quartos, sendo 2 suítes, e 3 banheiros, com ar-condicionado ⟦em todos os quartos⟧",
       "Na maré baixa, formam-se piscinas naturais em frente ao condomínio",
       "Enxoval de hotel, kit de amenities, Wi-Fi e TV inclusos"],
 ideal="Famílias e grupos de até 7 pessoas que querem ir à praia a pé e ter a privacidade de uma casa. " + NOCRIB,
 quartos=["Suíte master: 1 cama de casal", "Suíte superior: 2 camas de solteiro e 1 cama auxiliar", "Quarto térreo: 2 camas de solteiro ⟦e 1 cama auxiliar?⟧"],
 loc_intro=OKA_INTRO, loc=OKA_LOC, chegar=OKA_CHEGAR, extra_serv=OKA_SERV,
 faq=[("A piscina é privativa?", "⟦Sim, é de uso exclusivo da casa.⟧"),
      ("Quantos metros até a areia?", "⟦X m, pelo acesso do condomínio.⟧"),
      ("Tem estacionamento?", "⟦Sim, X vagas gratuitas.⟧")],
 pend=["Quarto térreo tem cama auxiliar? Com as duas auxiliares seriam 8 lugares, e a ficha diz 7", "Piscina privativa e churrasqueira", "Metros até a areia, vagas, distâncias"],
 cad=["Trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Mostrar a praia nas primeiras fotos"],
)

U["HS38J"] = dict(
 title="Casa 4 banheiros no Oka Milagres, acesso à praia · 7 pessoas",
 p1="Casa com 3 quartos e 4 banheiros para até 7 pessoas no condomínio Oka Morada dos Milagres, com acesso direto à Praia do Marceneiro, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["4 banheiros para 7 pessoas",
       "2 quartos com cama de casal",
       "Acesso direto à Praia do Marceneiro pelo condomínio, a ⟦X m⟧ da casa",
       "Máquina de lavar e secar, varanda, jardim e churrasqueira",
       "Enxoval de hotel, kit de amenities, Wi-Fi, TV e artigos de praia inclusos"],
 ideal="Dois casais com até 3 crianças, ou família com avós, que precisam de 2 camas de casal e banheiros suficientes. Capacidade máxima de 7 pessoas. " + NOCRIB,
 quartos=["Suíte master: 1 cama de casal", "Suíte superior: 2 camas de solteiro e 1 cama auxiliar", "Quarto térreo: 1 cama de casal"],
 loc_intro=OKA_INTRO, loc=OKA_LOC, chegar=OKA_CHEGAR, extra_serv=OKA_SERV,
 faq=[("Quantas pessoas cabem?", "Até 7."),
      ("Tem máquina de lavar?", "Sim, de lavar e secar."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["Piscina: privativa ou do condomínio", "Metros até a areia, vagas, distâncias"],
 cad=["Corrigir \"até 08 pessoas\" no texto PT e \"8 People\" no título EN",
      "Trocar \"Academia (privativa)\" por \"Academia (área comum)\"",
      "7 das 10 primeiras fotos são quartos: mostrar a praia antes"],
)

U["KM01J"] = dict(
 title="Casa com 3 camas de casal no Oka Milagres · 6 pessoas",
 p1="Casa com 2 suítes e 3 camas de casal para até 6 pessoas no condomínio Oka Morada dos Milagres, com acesso direto à Praia do Marceneiro, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["3 camas de casal em 2 suítes",
       "3 banheiros para 6 pessoas",
       "Acesso direto à Praia do Marceneiro pelo condomínio, a ⟦X m⟧ da casa",
       "Churrasqueira com utensílios e jardim",
       "Enxoval de hotel, kit de amenities, Wi-Fi, Smart TV e artigos de praia inclusos"],
 ideal="Três casais de amigos ou casal com filhos adolescentes que preferem cama de casal. Eventos não são permitidos. " + NOCRIB,
 quartos=["Suíte master: 1 cama de casal", "Segunda suíte: 2 camas de casal ⟦confirmar⟧", "⟦Sofá-cama: onde fica e se conta na capacidade⟧"],
 loc_intro=OKA_INTRO, loc=OKA_LOC, chegar=OKA_CHEGAR,
 faq=[("Serve para 3 casais?", "Sim. São 3 camas de casal em 2 suítes."),
      ("Pode fazer evento?", "Não."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["Segunda suíte com 2 camas de casal (a ficha diz 3 camas no total)", "Sofá-cama", "Geladeira ou frigobar", "Cozinheiro e garçom valem para esta casa?"],
 cad=["Trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Capa repetida na galeria"],
)

U["PB02J"] = dict(
 title="Apto 2 quartos no Villa Mauí, a 250 m da praia · 4 pessoas",
 p1="Apartamento com 2 quartos de casal e 2 banheiros para até 4 pessoas no condomínio Villa Mauí, a 250 m da Praia do Marceneiro, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["250 m da Praia do Marceneiro",
       "2 quartos com cama de casal e 2 banheiros",
       "Varanda com vista para a piscina e churrasqueira",
       "Máquina de lavar e fechadura eletrônica",
       "1 vaga de garagem gratuita; ⟦roupa de cama e banho⟧, toalhas de piscina, Wi-Fi e Smart TV inclusos"],
 ideal="Dois casais ou família de 4 pessoas. O acesso é só por escadas, então não é indicado para quem tem mobilidade reduzida. Silêncio das 22h às 8h e sem eventos. " + NOCRIB,
 quartos=["Quarto 1: 1 cama de casal", "Quarto 2: 1 cama de casal"],
 loc_intro=OKA_INTRO,
 loc=["Praia do Marceneiro: 250 m", "Santuário do Peixe-Boi, em Porto de Pedras: ⟦X km⟧", "Capela de São Miguel dos Milagres: ⟦X km⟧"],
 chegar=OKA_CHEGAR,
 faq=[("É pé na areia?", "Não. Fica a 250 m da praia."),
      ("Tem escadas?", "Sim, o acesso é só por escadas."),
      ("Roupa de cama está incluída?", "⟦Confirmar⟧")],
 pend=["Piscina: privativa ou do condomínio", "Roupa de cama inclusa ou com taxa"],
 cad=["Desmarcar \"Piscina Privada\" (segundo o PDF)", "Apagar o texto copiado do Oka e o parágrafo repetido",
      "Desmarcar \"Toalhas/Lençóis com sobretaxa\" se o enxoval for incluso"],
)

U["PJ01J"] = dict(
 title="Apto com piscina privativa no Villa Anahí, a 300 m da praia",
 p1="Apartamento com piscina e churrasqueira privativas para até 4 pessoas no Condomínio Villa Anahí, a 300 m da Praia do Marceneiro, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["Piscina (não aquecida) e churrasqueira de uso exclusivo",
       "300 m da Praia do Marceneiro, a pé",
       "2 quartos com cama de casal e 1 banheiro",
       "Carrinho de praia e máscaras de mergulho",
       "Enxoval de cama e banho, toalhas de piscina, Wi-Fi e Smart TV inclusos"],
 ideal="Casais com filhos pequenos ou 2 casais que querem piscina só para o grupo. Há 1 banheiro para 4 pessoas. Sem eventos. " + NOCRIB,
 quartos=["Quarto 1: 1 cama de casal", "Quarto 2: 1 cama de casal"],
 loc_intro=OKA_INTRO,
 loc=["Praia do Marceneiro: 300 m", "Centro de São Miguel dos Milagres: ⟦X km⟧"],
 chegar=["Aeroporto de Maceió: cerca de 105 km, de 1h30 a 2h de carro", "O carro é a melhor forma de circular pela região."],
 faq=[("A piscina é só nossa?", "Sim, é de uso exclusivo da unidade."),
      ("Dá para ir a pé à praia?", "Sim, são 300 m."),
      ("A piscina é aquecida?", "Não.")],
 pend=[],
 cad=["Tirar \"mais de 35 anos\", o rótulo \"Sobre interação com anfitrião\" e o parágrafo repetido do texto atual"],
)

# ---------------- SÃO MIGUEL DOS MILAGRES ----------------
U["HS31J"] = dict(
 title="Casa beira-mar com piscina na Vila Atauá, Milagres · 12 pessoas",
 p1="Casa beira-mar com 5 suítes e piscina privativa para até 12 pessoas na Vila Atauá, na Praia de São Miguel dos Milagres, a 860 m da Capela dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["De frente para o mar, com acesso direto à Praia de São Miguel dos Milagres",
       "5 suítes, 2 com vista para o mar",
       "Piscina privativa, varanda, jardim e churrasqueira",
       "860 m da Capela dos Milagres, ⟦cerca de 10 min⟧ a pé pela praia",
       "Enxoval de cama, mesa e banho, Wi-Fi, TV a cabo e artigos de praia inclusos"],
 ideal="Famílias multigeracionais e grupos de até 12 pessoas, com uma suíte por casal ou núcleo familiar. " + NOCRIB,
 quartos=["Suíte 1 (vista mar): 1 cama queen", "Suíte 2 (vista mar): 1 cama queen e 1 cama auxiliar",
          "Suíte 3: 1 cama queen e 1 cama auxiliar", "Suíte 4: 1 cama queen e 1 cama auxiliar", "Suíte 5 (térrea): 2 camas de solteiro"],
 loc_intro="A Vila Atauá fica na beira-mar de São Miguel dos Milagres, na Rota Ecológica dos Milagres.",
 loc=["Capela dos Milagres: 860 m", "Restaurantes: 1 km", "Mercados: 1,9 km", "Vilinha do Marceneiro: 3,2 km"],
 chegar=["Aeroporto de Maceió: 94 km, ⟦cerca de X h de carro⟧", "O carro é a melhor forma de circular pela região."],
 faq=[("Quantas pessoas cabem?", "Até 12."),
      ("Todas as suítes têm banheiro?", "Sim, são 5 suítes com banheiro."),
      ("A piscina é privativa?", "Sim.")],
 pend=["Capacidade: 12 (ficha) ou 13 (título atual) — o texto novo usa 12", "Tempo a pé até a Capela (860 m em 7 min parece rápido)"],
 cad=["Corrigir o título e preencher o bairro (está vazio)", "Revisar a tarifa mínima: aparece \"a partir de R$ 15.544,55\" na home",
      "Trocar \"acesso exclusivo à praia\" por \"acesso direto\"", "Capa repetida na galeria"],
)

TOQUE_INTRO = "O Morada do Toque fica na via principal de São Miguel dos Milagres, com mercadinhos, farmácias e lanchonetes na mesma rua."
TOQUE_LOC = ["Praia do Toque: ⟦2 km ou 450 m — confirmar⟧", "Praias do Marceneiro, do Riacho, de Lages e do Patacho: acesso de carro ou buggy"]
TOQUE_CHEGAR = ["Aeroporto de Maceió: 97 km, ⟦cerca de X h de carro⟧", "Aeroporto do Recife: 220 km", "O carro é a melhor forma de circular pela região."]

U["HS26J"] = dict(
 title="Casa 2 suítes no centro de Milagres, condomínio · 6 pessoas",
 p1="Casa com 2 suítes, mezanino e 3 banheiros para até 6 pessoas no condomínio Morada do Toque, no centro de São Miguel dos Milagres, perto da Praia do Toque. Aluguel por temporada da Temporada MME.",
 dest=["Localização central, com comércio na mesma rua",
       "2 suítes, mezanino e 3 banheiros",
       "Condomínio com piscina, academia e playground",
       "Varanda com vista para o jardim e a piscina do condomínio; churrasqueira",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias de até 6 pessoas que preferem ficar perto do comércio e circular de carro pelas praias. A casa não é pé na areia. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal", "Suíte 2: 1 cama de casal", "Sala: 1 sofá-cama de casal", "Mezanino: 1 cama de solteiro ⟦conta na capacidade?⟧"],
 loc_intro=TOQUE_INTRO, loc=TOQUE_LOC, chegar=TOQUE_CHEGAR, extra_serv=OKA_SERV,
 faq=[("É perto da praia?", "A Praia do Toque fica a ⟦X⟧. O carro é recomendado."),
      ("A piscina é privativa?", "Não, é do condomínio."),
      ("Quantas pessoas cabem?", "Até 6.")],
 pend=["Distância da Praia do Toque (o texto atual diz 450 m e 2 km)", "Mezanino: camas somam 7 lugares e a ficha diz 6", "Município/bairro: hoje a etiqueta diz Tatuamunha"],
 cad=["Corrigir o título (5 → 6 pessoas) e a etiqueta de bairro", "Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Foto repetida na galeria"],
)

U["HS41J"] = dict(
 title="Casa 3 quartos de casal no centro de Milagres · 6 pessoas",
 p1="Casa com 3 quartos de casal e 3 banheiros para até 6 pessoas no condomínio Morada do Toque, no centro de São Miguel dos Milagres, perto da Praia do Toque. Aluguel por temporada da Temporada MME.",
 dest=["3 quartos, todos com cama de casal",
       "3 banheiros, um deles social no térreo",
       "Localização central, com comércio na mesma rua",
       "Condomínio com piscina, academia e playground",
       "Roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Três casais ou família com filhos adultos que querem cama de casal para todos, gastando menos. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal", "Suíte 2: 1 cama de casal", "Quarto 3: 1 cama de casal"],
 loc_intro=TOQUE_INTRO, loc=TOQUE_LOC, chegar=TOQUE_CHEGAR, extra_serv=OKA_SERV,
 faq=[("Todos os quartos têm cama de casal?", "Sim."),
      ("A piscina é privativa?", "Não, é do condomínio."),
      ("É perto da praia?", "A Praia do Toque fica a ⟦X⟧. O carro é recomendado.")],
 pend=["Distância da Praia do Toque", "Município/bairro na etiqueta"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Tirar o código \"28\" e os termos de Portugal do texto atual"],
)

# ---------------- TATUAMUNHA ----------------
KANUI_INTRO = "O Villa Kanui fica em Tatuamunha, Porto de Pedras, na Rota Ecológica dos Milagres."
KANUI_CHEGAR = ["Aeroporto de Maceió: cerca de 108 km, ⟦cerca de X h de carro⟧", "Aeroporto do Recife: cerca de 187 km", "O carro é a melhor forma de circular pela região."]

U["HS09J"] = dict(
 title="Casa 3 suítes com piscina no Villa Kanui · 9 pessoas",
 p1="Casa de 200 m² com 3 suítes iguais e piscina para até 9 pessoas no Villa Kanui, em Tatuamunha, Porto de Pedras, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["3 suítes iguais, cada uma com cama de casal e cama auxiliar",
       "200 m², 3 banheiros nas suítes e lavabo",
       "Piscina com área rasa ⟦privativa⟧, varanda, terraço e churrasqueira",
       "Máquina de lavar e secar",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Três famílias pequenas que querem quartos equivalentes, ou grupos de até 9 pessoas. Silêncio das 20h às 8h e sem eventos. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal e 1 cama auxiliar", "Suíte 2: 1 cama de casal e 1 cama auxiliar", "Suíte 3: 1 cama de casal e 1 cama auxiliar"],
 loc_intro=KANUI_INTRO, loc=["Praia de Tatuamunha: ⟦X m⟧", "Santuário do Peixe-Boi: ⟦X km⟧"], chegar=KANUI_CHEGAR, extra_serv=OKA_SERV,
 faq=[("As suítes são iguais?", "Sim, as 3 têm cama de casal e cama auxiliar."),
      ("A hidromassagem é da casa?", "⟦Confirmar: o cadastro marca jacuzzi de uso comum⟧"),
      ("Tem máquina de lavar?", "Sim, de lavar e secar.")],
 pend=["Distância até a Praia de Tatuamunha", "Hidromassagem: da casa ou do condomínio", "Piscina privativa?", "O pino do mapa na Stays está ~6,5 km ao sul de Tatuamunha: conferir"],
 cad=["Corrigir o bairro \"Beverly Hills\" para Tatuamunha, Porto de Pedras", "Tirar \"Hidro\" do título se a hidromassagem for do condomínio", "Foto repetida na galeria"],
)

U["HS12J"] = dict(
 title="Casa triplex com hidro no Villa Kanui · 12 pessoas",
 p1="Casa triplex de 255 m² com piscina e hidromassagem no terraço para até 12 pessoas no Villa Kanui, em Tatuamunha, Porto de Pedras, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["Até 12 pessoas em 3 suítes",
       "Hidromassagem no terraço",
       "255 m² em 3 andares, com lavabo",
       "Piscina ⟦privativa⟧, varanda e churrasqueira",
       "Roupa de cama e banho, Wi-Fi e ar-condicionado inclusos"],
 ideal="Grupos de até 12 pessoas. Cada suíte recebe 4 pessoas com camas auxiliares. A casa tem escadas (3 andares) e câmeras de segurança nas áreas comuns internas. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal e 1 cama auxiliar de casal", "Suíte 2: 1 cama de casal e 1 cama auxiliar de casal", "Suíte 3: 1 cama de casal e 2 camas auxiliares de solteiro"],
 loc_intro=KANUI_INTRO, loc=["Praia de Tatuamunha: ⟦X m⟧", "Santuário do Peixe-Boi: ⟦X km⟧"], chegar=KANUI_CHEGAR, extra_serv=OKA_SERV,
 faq=[("Tem câmeras?", "Sim, nas áreas comuns internas. Quartos e banheiros não são monitorados ⟦confirmar⟧."),
      ("A hidromassagem é da casa?", "Sim, fica no terraço."),
      ("Tem estacionamento?", "⟦Confirmar⟧")],
 pend=["Distância até a praia", "Vagas", "Câmeras não ficam em quartos e banheiros"],
 cad=["Corrigir o bairro \"Beverly Hills\" para Tatuamunha, Porto de Pedras"],
)

VR_INTRO = "O Villas do Rio fica em Tatuamunha, Porto de Pedras, na Rota Ecológica dos Milagres, entre o rio e o mar."
VR_LOC = ["Praia de Tatuamunha: 300 m, cerca de 4 min a pé", "Praia de Porto da Rua: 1 km", "Santuário do Peixe-Boi: ⟦X km⟧"]
VR_CHEGAR = ["Aeroporto de Maceió: cerca de 108 km, ⟦cerca de X h de carro⟧", "Aeroporto do Recife: cerca de 187 km", "O carro é a melhor forma de circular pela região."]

U["HS05J"] = dict(
 title="Casa 3 suítes de casal no Villas do Rio · 6 pessoas",
 p1="Casa térrea com 3 suítes de casal, piscina e área gourmet para até 6 pessoas no Villas do Rio, a 300 m da Praia de Tatuamunha, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["3 suítes, todas com cama de casal",
       "300 m da Praia de Tatuamunha, cerca de 4 min a pé",
       "Área gourmet com churrasqueira e piscina ⟦privativa⟧",
       "Casa térrea, sem escadas, com lavabo",
       "Roupa de cama e banho, kit de amenities, Wi-Fi e TV inclusos"],
 ideal="Três casais, ou casal com filhos adultos, que querem uma suíte de casal para cada um. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal", "Suíte 2: 1 cama de casal", "Suíte 3: 1 cama de casal"],
 loc_intro=VR_INTRO, loc=VR_LOC, chegar=VR_CHEGAR, extra_serv=OKA_SERV,
 faq=[("A casa tem escadas?", "Não, é térrea."),
      ("Dá para ir a pé à praia?", "Sim, são 300 m."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["Piscina privativa?", "Metragem"],
 cad=["Trocar \"Villa Kanui\" por \"Villas do Rio\" no campo de transporte", "Tirar o código \"casa 01\" e o texto automático do Booking"],
)

U["HS35J"] = dict(
 title="Casa para família no Villas do Rio, Tatuamunha · 6 pessoas",
 p1="Casa térrea com 3 suítes, uma delas com 2 camas de solteiro, piscina e área gourmet para até 6 pessoas no Villas do Rio, a 300 m da Praia de Tatuamunha. Aluguel por temporada da Temporada MME.",
 dest=["Suíte com 2 camas de solteiro, boa para as crianças",
       "300 m da Praia de Tatuamunha, cerca de 4 min a pé",
       "Área gourmet com churrasqueira e piscina ⟦privativa⟧",
       "Casa térrea, sem escadas, com lavabo",
       "Roupa de cama e banho, artigos de praia, kit de primeiros socorros e Wi-Fi inclusos"],
 ideal="Família com 2 filhos e outro casal, ou dois casais com crianças. " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal", "Suíte 2: 2 camas de solteiro", "Suíte 3: 1 cama de casal"],
 loc_intro=VR_INTRO, loc=VR_LOC, chegar=VR_CHEGAR, extra_serv=OKA_SERV,
 faq=[("Tem quarto para crianças?", "Sim, uma suíte com 2 camas de solteiro."),
      ("A casa tem escadas?", "Não, é térrea."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["Piscina privativa?", "Metragem"],
 cad=["Trocar \"Villa Kanui\" por \"Villas do Rio\"", "Tirar o código \"casa 02\""],
)

U["HS37J"] = dict(
 title="Casa de 130 m² com 3 suítes no Villas do Rio · 6 pessoas",
 p1="Casa térrea de 130 m² com 3 suítes de casal, piscina e área gourmet para até 6 pessoas no Villas do Rio, a 300 m da Praia de Tatuamunha, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["130 m² em casa térrea, sem escadas",
       "3 suítes com cama de casal e lavabo",
       "300 m da Praia de Tatuamunha",
       "Área gourmet com churrasqueira e piscina ⟦privativa⟧",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Três casais ou família que quer espaço e suítes de casal. ⟦Diferencial próprio desta casa⟧ " + NOCRIB,
 quartos=["Suíte 1: 1 cama de casal", "Suíte 2: 1 cama de casal", "Suíte 3: 1 cama de casal"],
 loc_intro=VR_INTRO, loc=VR_LOC, chegar=VR_CHEGAR, extra_serv=OKA_SERV,
 faq=[("A casa é térrea?", "Sim."),
      ("Qual a metragem?", "130 m²."),
      ("A piscina é privativa?", "⟦Confirmar⟧")],
 pend=["O que esta casa tem de diferente das casas 01 e 02", "Piscina privativa?"],
 cad=["Trocar \"Villa Kanui\" por \"Villas do Rio\"", "Tirar o código \"casa 03\""],
)

NAAY_INTRO = "O Naay Villas Boutique fica em Tatuamunha, Porto de Pedras, na Rota Ecológica dos Milagres, perto do Rio Tatuamunha, onde é feita a observação do peixe-boi."
NAAY_LOC = ["Praia de Tatuamunha: ⟦100 m ou 150 m — padronizar⟧", "Ponte do Peixe-Boi: 500 m", "Farmácia: 750 m", "Restaurantes: 1 km", "Supermercado: 5,9 km", "Praia de Lages: cerca de 4,5 km"]
NAAY_CHEGAR = ["Aeroporto de Maceió: cerca de 120 km, ⟦cerca de X h de carro⟧", "O carro é a melhor forma de circular pela região."]
NAAY_NOTE = "Silêncio das 22h às 8h e sem eventos. "

U["HS18J"] = dict(
 title="Studio no Naay Villas, perto da praia · 4 pessoas",
 p1="Studio climatizado para até 4 pessoas no Naay Villas Boutique, perto da Praia de Tatuamunha e do passeio do peixe-boi, em Porto de Pedras, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["Praia de Tatuamunha a ⟦100 m⟧",
       "500 m da ponte de onde saem os passeios do peixe-boi",
       "Studio com cama de casal, sofá-cama e cama auxiliar",
       "Condomínio com piscina, academia e área de churrasco",
       "Roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Casais e famílias pequenas que passam o dia fora e querem uma base prática perto do mar. Todos dormem no mesmo ambiente. " + NAAY_NOTE + NOCRIB,
 quartos=["Ambiente único: 1 cama de casal, 1 sofá-cama ⟦para 1 ou 2 pessoas⟧ e 1 cama auxiliar"],
 loc_intro=NAAY_INTRO, loc=NAAY_LOC, chegar=NAAY_CHEGAR,
 faq=[("Cabem 4 adultos?", "Sim, no mesmo ambiente: cama de casal, sofá-cama e cama auxiliar."),
      ("Tem piscina?", "Sim, a do condomínio."),
      ("Tem supermercado perto?", "O mais próximo fica a 5,9 km; farmácia a 750 m.")],
 pend=["Sofá-cama para 1 ou 2 pessoas", "Distância até a praia (100 ou 150 m)", "Metragem real (todas as unidades mostram 117,98 m²)"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Etiqueta: Tatuamunha, Porto de Pedras", "Foto repetida na galeria"],
)

U["HS16J"] = dict(
 title="Apto 2 quartos no Naay Villas, Tatuamunha · 5 pessoas",
 p1="Apartamento com 2 quartos de casal e 2 banheiros para até 5 pessoas no Naay Villas Boutique, perto da Praia de Tatuamunha, em Porto de Pedras, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["2 quartos com cama de casal e ar-condicionado",
       "2 banheiros",
       "Praia de Tatuamunha a ⟦100 m⟧ e ponte do peixe-boi a 500 m",
       "Varanda com churrasqueira; condomínio com piscina e academia",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Dois casais ou família de até 5 pessoas. " + NAAY_NOTE + NOCRIB,
 quartos=["Quarto 1: 1 cama de casal", "Quarto 2: 1 cama de casal", "Sala: 1 sofá-cama de solteiro"],
 loc_intro=NAAY_INTRO, loc=NAAY_LOC, chegar=NAAY_CHEGAR,
 faq=[("Quantos quartos de casal?", "Dois."),
      ("Tem piscina?", "Sim, a do condomínio."),
      ("Tem supermercado perto?", "O mais próximo fica a 5,9 km.")],
 pend=["Distância até a praia", "Metragem real e andar"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Apagar \"Praia de São Miguel dos Milagres: cerca de 12 km\"; etiqueta Tatuamunha, Porto de Pedras", "Foto repetida na galeria"],
)

U["IM01J"] = dict(
 title="Duplex com rooftop no Naay Villas, Tatuamunha · 5 pessoas",
 p1="Apartamento duplex com rooftop para até 5 pessoas no Naay Villas Boutique, a 150 m da Praia de Tatuamunha e a 500 m da ponte do peixe-boi, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["150 m da Praia de Tatuamunha e 78 m do Rio Tatuamunha",
       "500 m da ponte de onde saem os passeios do peixe-boi",
       "Duplex com rooftop e cadeiras",
       "2 quartos e 2 banheiros; varanda com churrasqueira",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e TV inclusos"],
 ideal="Famílias com filhos que querem ver o peixe-boi e ir à praia a pé. O duplex tem escada interna. " + NAAY_NOTE + NOCRIB,
 quartos=["Quarto 1: 1 cama queen", "Quarto 2: 2 camas de solteiro", "Sala: 1 sofá-cama de solteiro"],
 loc_intro=NAAY_INTRO,
 loc=["Rio Tatuamunha: 78 m", "Praia de Tatuamunha: 150 m", "Ponte do Peixe-Boi: 500 m", "Farmácia: 750 m", "Restaurantes: 1 km", "Supermercado: 5,9 km"],
 chegar=NAAY_CHEGAR,
 faq=[("Dá para ir a pé ver o peixe-boi?", "A ponte de saída dos passeios fica a 500 m."),
      ("Tem supermercado perto?", "O mais próximo fica a 5,9 km; farmácia a 750 m."),
      ("Tem escada?", "Sim, é duplex.")],
 pend=["Metragem real"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Etiqueta Tatuamunha, Porto de Pedras", "Foto repetida na galeria"],
)

U["HS22J"] = dict(
 title="Duplex 2 camas king com rooftop no Naay Villas · 6 pessoas",
 p1="Duplex com 2 quartos de cama king e rooftop com espreguiçadeiras para até 6 pessoas no Naay Villas Boutique, perto da Praia de Tatuamunha, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["2 quartos com cama king e ar-condicionado",
       "Rooftop com espreguiçadeiras e cadeiras",
       "2 banheiros; varanda com churrasqueira",
       "Praia de Tatuamunha a ⟦100 m⟧ e ponte do peixe-boi a 500 m",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Dois casais que querem cama king, ou família de até 6 pessoas. O duplex tem escada interna. " + NAAY_NOTE + NOCRIB,
 quartos=["Quarto 1: 1 cama king", "Quarto 2: 1 cama king", "Sala: 1 sofá-cama ⟦de casal — confirmar⟧"],
 loc_intro=NAAY_INTRO, loc=NAAY_LOC, chegar=NAAY_CHEGAR,
 faq=[("As camas são king?", "Sim, nos dois quartos."),
      ("O sofá-cama é para quantas pessoas?", "⟦Confirmar⟧"),
      ("Tem escada?", "Sim, é duplex.")],
 pend=["Sofá-cama para 1 ou 2 pessoas (o texto atual diz as duas coisas)", "Distância até a praia"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Etiqueta Tatuamunha, Porto de Pedras"],
)

U["HS29J"] = dict(
 title="Duplex com jacuzzi no rooftop, Naay Villas · 6 pessoas",
 p1="Duplex com jacuzzi no rooftop e 2 quartos de cama king para até 6 pessoas no Naay Villas Boutique, perto da Praia de Tatuamunha, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["Jacuzzi ⟦privativa⟧ no rooftop",
       "2 quartos com cama king e ar-condicionado",
       "2 banheiros; varanda com churrasqueira",
       "Praia de Tatuamunha a ⟦100 m⟧ e ponte do peixe-boi a 500 m",
       "Roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Casais em viagem especial ou dois casais que querem uma área privativa para relaxar. O duplex tem escada interna. " + NAAY_NOTE + NOCRIB,
 quartos=["Quarto 1: 1 cama king", "Quarto 2: 1 cama king", "Sala: 1 sofá-cama de casal"],
 loc_intro=NAAY_INTRO, loc=NAAY_LOC, chegar=NAAY_CHEGAR,
 faq=[("A jacuzzi é só da unidade?", "⟦Confirmar⟧"),
      ("A jacuzzi é aquecida?", "⟦Confirmar⟧"),
      ("Tem escada?", "Sim, é duplex.")],
 pend=["Jacuzzi privativa e aquecida?", "Distância até a praia"],
 cad=["Desmarcar \"Piscina Privada\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"; marcar \"Jacuzzi privativa\"", "Fotos verticais geram barras brancas: usar horizontais", "Etiqueta Tatuamunha, Porto de Pedras"],
)

# ---------------- PATACHO ----------------
AZUK_INTRO = "O Azuk Patacho fica em Porto de Pedras, na Rota Ecológica dos Milagres, perto da Praia do Patacho, conhecida pelos coqueirais e pelas piscinas naturais na maré baixa."
AZUK_LOC = ["Praia do Patacho: ⟦X m⟧", "Praia de Lages: vizinha ao Patacho, acessível pela areia", "Santuário do Peixe-Boi, em Tatuamunha: ⟦X km⟧", "Beach club Sonhos do Patacho e restaurante Ninoan: ⟦X km⟧"]
AZUK_CHEGAR = ["Aeroporto de Maceió: cerca de 100 km, ⟦cerca de X h de carro⟧", "Aeroporto do Recife: cerca de 150 km", "Carro recomendado para a região; para trajetos curtos, use as bicicletas do condomínio."]

U["NF02J"] = dict(
 title="Studio no Azuk Patacho, perto da Praia do Patacho · 4 pessoas",
 p1="Studio térreo e sem degraus para até 4 pessoas no condomínio Azuk Patacho, perto da Praia do Patacho, em Porto de Pedras, na Rota dos Milagres. Aluguel por temporada da Temporada MME.",
 dest=["Unidade térrea, com ducha sem degraus e porta ampla",
       "Praia do Patacho a ⟦X m⟧",
       "Condomínio com piscina, academia, bicicletas e recepção 24 horas",
       "Carregador para carro elétrico no condomínio",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Casais, ou casal com 2 filhos, e quem prefere uma unidade sem escadas. Todos dormem no mesmo ambiente. Silêncio das 22h às 8h e sem eventos. " + NOCRIB,
 quartos=["Ambiente único: 1 cama queen e 1 sofá-cama de casal"],
 loc_intro=AZUK_INTRO, loc=AZUK_LOC, chegar=AZUK_CHEGAR,
 faq=[("Tem escadas?", "Não, a unidade é térrea."),
      ("Tem bicicleta?", "Sim, o condomínio oferece."),
      ("A que distância fica a praia?", "⟦Confirmar⟧")],
 pend=["Distância até a Praia do Patacho"],
 cad=["Desmarcar \"Piscina na Cobertura\", \"Vista para a Cidade\" e trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Cidade: Porto de Pedras", "Foto repetida na galeria"],
)

U["JI01J"] = dict(
 title="Apto 2 quartos no Azuk Patacho, Porto de Pedras · 6 pessoas",
 p1="Apartamento de 2 quartos com área externa e espreguiçadeiras para até 6 pessoas no condomínio Azuk Patacho, perto da Praia do Patacho, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["Área externa com espreguiçadeiras e mesa para refeições",
       "2 quartos (1 suíte) e 2 banheiros, um com bidê",
       "Praia do Patacho a ⟦X m⟧",
       "Condomínio com piscina com área rasa, academia, bicicletas e recepção 24 horas",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias de até 6 pessoas que querem ficar perto do Patacho com estrutura de condomínio. Silêncio das 22h às 8h e sem eventos. " + NOCRIB,
 quartos=["Suíte: 1 cama de casal", "Quarto 2: 2 camas de solteiro", "Sala: 1 sofá-cama de casal"],
 loc_intro=AZUK_INTRO, loc=AZUK_LOC, chegar=AZUK_CHEGAR,
 faq=[("Precisa de carro?", "Para conhecer a Rota, sim. Perto do Patacho dá para usar as bicicletas do condomínio."),
      ("Tem estacionamento?", "Sim, 1 vaga por unidade."),
      ("A que distância fica a praia?", "⟦Confirmar⟧")],
 pend=["Distância até a Praia do Patacho", "É casa ou apartamento? (cadastro diz \"CASA A02\")", "Bandeira Azul: só citar se a certificação estiver válida nesta temporada"],
 cad=["Cidade: Porto de Pedras", "Tirar \"restaurantes premiados\" ou citar o prêmio"],
)

U["MI02J"] = dict(
 title="Apto 82 m² com banheiro adaptado no Azuk Patacho · 6 pessoas",
 p1="Apartamento de 82 m² com suíte queen, quarto com 4 camas e banheiro adaptado para até 6 pessoas no condomínio Azuk Patacho, perto da Praia do Patacho, em Porto de Pedras. Aluguel por temporada da Temporada MME.",
 dest=["Banheiro com ducha adaptada e chuveiro acessível",
       "82 m², 2 quartos e 2 banheiros",
       "Quarto com 4 camas de solteiro",
       "Condomínio com piscina, academia, bicicletas e recepção 24 horas",
       "1 vaga de garagem gratuita; roupa de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias com até 4 filhos, grupos de amigos e hóspedes que precisam de banheiro adaptado. Sem eventos. Proibido fumar. " + NOCRIB,
 quartos=["Suíte: 1 cama queen", "Quarto 2: 2 camas de solteiro e 2 camas auxiliares de solteiro"],
 loc_intro=AZUK_INTRO, loc=AZUK_LOC, chegar=AZUK_CHEGAR,
 faq=[("É acessível para cadeira de rodas?", "O banheiro tem ducha adaptada. ⟦Confirmar o acesso até a unidade.⟧"),
      ("Pode fumar?", "Não."),
      ("Quantas camas tem?", "Uma queen e 4 de solteiro.")],
 pend=["Acesso sem degraus até a unidade", "Distância até a Praia do Patacho"],
 cad=["CORRIGIR JÁ nas Regras: \"Permitido fumar: sim\" e \"silêncio das 6h às 4h\"", "Trocar \"Academia (privativa)\" por \"Academia (área comum)\"", "Cidade: Porto de Pedras"],
)

U["NF04J"] = dict(
 title="Studio para casal no Villas Manatee, Patacho · 2 pessoas",
 p1="Studio para casal com cama queen e varanda no condomínio Villas Manatee Patacho, em Porto de Pedras, com piscina, hidromassagem e sauna. Aluguel por temporada da Temporada MME.",
 dest=["Exclusivo para 2 pessoas",
       "Cama queen e varanda ⟦com vista para a praia ou jardim⟧",
       "Condomínio com piscina, hidromassagem, sauna e academia compacta",
       "Praia do Patacho a ⟦X m⟧",
       "Enxoval de cama e banho, Wi-Fi e Smart TV inclusos"],
 ideal="Casais que querem um studio compacto perto do Patacho. Silêncio das 22h às 8h e sem eventos.",
 quartos=["Studio: 1 cama queen, ar-condicionado e banheiro privativo"],
 loc_intro="O Villas Manatee Patacho fica em Porto de Pedras, na Rota Ecológica dos Milagres.",
 loc=["Praia do Patacho: ⟦X m⟧", "Santuário do Peixe-Boi: ⟦X km⟧"],
 chegar=["Aeroporto de Maceió: ⟦X km, cerca de X h de carro⟧", "O carro é a melhor forma de circular pela região."],
 faq=[("Quantas pessoas cabem?", "Duas."),
      ("A que distância fica a praia?", "⟦Confirmar⟧"),
      ("Tem estacionamento?", "⟦Confirmar⟧")],
 pend=["Distância até a praia e o aeroporto", "Vista da varanda", "O condomínio tem spa? (texto diz sim, cadastro diz não)", "Vaga de garagem"],
 cad=["Desmarcar \"Quartos para famílias\"", "Galeria tem só 19 fotos"],
)

# ---------------- PIAÇABUÇU ----------------
U["II02J"] = dict(
 title="Casa com 11 suítes no Rio São Francisco · 21 pessoas",
 p1="Casa de 400 m² com 11 suítes, piscina e equipe de 6 funcionários para até 21 pessoas às margens do Rio São Francisco, em Piaçabuçu, Alagoas. Aluguel por temporada da Temporada MME.",
 dest=["11 suítes com ar-condicionado e 12 banheiros",
       "Equipe de 6 pessoas: 2 cozinheiras, 2 arrumadeiras, 1 garçom e 1 segurança",
       "Acesso ao rio com local para barco",
       "Piscina com área rasa, deck com espreguiçadeiras e churrasqueira",
       "Enxoval de hotel, toalhas de piscina, Wi-Fi e Smart TV inclusos"],
 ideal="Famílias grandes, grupos de amigos, celebrações e retiros de empresa de até 21 pessoas. Eventos precisam de consulta e aprovação prévia. " + NOCRIB,
 quartos=["10 suítes com 1 cama de casal", "1 suíte com 1 cama de solteiro"],
 loc_intro="A casa fica às margens do Rio São Francisco, em Piaçabuçu, no baixo São Francisco, em Alagoas.",
 loc=["Passeios de barco, lancha ou catamarã pelo rio a partir da região", "⟦2 ou 3 atrações da região com distância em km⟧"],
 chegar=["Aeroporto de Maceió: ⟦X km, cerca de X h de carro⟧", "Aeroporto de Aracaju: ⟦X km, cerca de X h de carro⟧",
         "Carro próprio ou alugado; para grupos grandes, transfer privativo (van ou micro-ônibus)", "Estacionamento privativo e gratuito ⟦X vagas⟧"],
 faq=[("Quantas pessoas cabem?", "Até 21."),
      ("A equipe está incluída na diária?", "⟦Confirmar⟧"),
      ("Posso fazer evento?", "Sim, mediante consulta e aprovação prévia."),
      ("Como chegar com um grupo grande?", "Recomendamos transfer privativo de van ou micro-ônibus.")],
 extra_serv="Nesta casa, a equipe de 6 funcionários sugere um cardápio personalizado (café da manhã, petiscos, almoço e jantar) e faz as compras e a organização da despensa. ⟦Equipe inclusa na diária ou paga à parte? Alimentos por conta do hóspede?⟧",
 pend=["Capacidade: 21 (ficha e camas) ou 24 (texto atual) — o texto novo usa 21", "Equipe inclusa ou paga à parte", "Distâncias dos aeroportos", "Vagas"],
 cad=["Trocar \"Lago\" por \"Rio\" nas comodidades e desmarcar \"Apartamento privado num edifício\"", "Conferir \"Academia (privativa)\"", "Tirar os parágrafos repetidos do texto atual", "Foto repetida na galeria"],
)

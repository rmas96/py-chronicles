DRUID_DIALOGUE = {
    "start": {
        "text": "Sinto os teus passos antes de te ver. Poucos forasteiros chegam tão longe na floresta sem se perderem.",
        "options": [
            {"text": "Quem são vocês?", "next": "who_are_you"},
            {"text": "Só estou de passagem.", "next": "just_passing"},
        ]
    },
    "who_are_you": {
        "text": "Somos os que ouvem a terra respirar. Chamam-nos druidas, mas isso é só uma palavra que os de fora usam.",
        "options": [
            {"text": "Ouvem a terra respirar?", "next": "explain_nature"},
            {"text": "Parece misticismo.", "next": "skeptic"},
        ]
    },
    "explain_nature": {
        "text": "As árvores sabem quando algo está errado muito antes de nós. Ultimamente, têm estado inquietas. Algo se move a norte que não devia.",
        "options": [
            {"text": "O que se move a norte?", "next": "hint_corrupted"},
        ]
    },
    "hint_corrupted": {
        "text": "Não sei ao certo. Um cheiro a podridão que não vem de nenhum animal que conheça. Se fores até lá, tem cuidado.",
        "options": []
    },
    "skeptic": {
        "text": "Achas que é misticismo até veres uma floresta inteira morrer em silêncio numa só noite. Já vi.",
        "options": []
    },
    "just_passing": {
        "text": "Ninguém apenas passa por aqui. A floresta escolhe quem entra. Volta quando tiveres perguntas a sério.",
        "options": []
    },
}


CORRUPTED_DIALOGUE = {
    "start": {
        "text": "*A figura vira-se lentamente, os olhos com um brilho estranho* ...Alguém. Há quanto tempo não via um rosto eu não conhecia?",
        "options": [
            {"text": "Estás bem?", "next": "ask_wellbeing"},
            {"text": "O que te aconteceu?", "next": "ask_what_happened"},
        ]
    },
    "ask_wellbeing": {
        "text": "Bem? *ri, sem alegria nenhuma* Sinto uma coisa a crescer dentro de mim desde que a névoa chegou às nossas terras. Ainda... ainda controlo os meus pensamentos. Por agora.",
        "options": [
            {"text": "Que névoa?", "next": "explain_mist"},
        ]
    },
    "ask_what_happened": {
        "text": "Não sei dizer ao certo. Foi gradual. Um sussurro à noite, depois dois. Agora ouço-o mesmo acordado.",
        "options": [
            {"text": "Consegues resistir-lhe?", "next": "resist"},
        ]
    },
    "explain_mist": {
        "text": "Veio das montanhas, há semanas. Quem a respira muda. Alguns dos meus... já não são eles próprios. Eu ainda luto.",
        "options": []
    },
    "resist": {
        "text": "Por agora. Não sei por quanto tempo mais. Se me vires outra vez e os meus olhos estiverem diferentes... foge.",
        "options": []
    },
}


EXILED_DIALOGUE = {
    "start": {
        "text": "*Um homem magro ergue a cabeça* Outro viajante. Não temos muito para oferecer, mas és bem-vindo a sentar-te.",
        "options": [
            {"text": "O que fazem aqui?", "next": "explain_camp"},
            {"text": "Aquela cidade ali é vossa?", "next": "ask_city"},
        ]
    },
    "explain_camp": {
        "text": "Sobrevivemos. É o que fazemos há anos. Antes disto, tínhamos um lar. Um bom lar.",
        "options": [
            {"text": "O que aconteceu ao vosso lar?", "next": "ask_city"},
        ]
    },
    "ask_city": {
        "text": "Foi nossa, sim. Fomos expulsos e as portas seladas atrás de nós. Ninguém entra, ninguém sai. Nem nós.",
        "options": [
            {"text": "Porque não tentam voltar?", "next": "explain_wall"},
        ]
    },
    "explain_wall": {
        "text": "A muralha é grossa demais para picaretas e o portão está trancado por dentro. Precisávamos de algo... mais decisivo. Estamos a reunir o que for preciso.",
        "options": [
            {"text": "Talvez eu possa ajudar.", "next": "offer_help"},
        ]
    },
    "offer_help": {
        "text": "*Os olhos dele acendem-se, pela primeira vez com esperança genuína* Se encontrares materiais que possam ajudar, traz-nos. Não te vamos esquecer isso.",
        "options": [
            {"text": "Dar recurso", "next": "give_resource"}
        ]
    },
    "give_resource": {
        "text": "Obrigado viajante! Não te vamos esquecer isto.",
        "options": [
            {"text": "De nada!", "next": "offer_help"}
        ]
    },
    "building_bomb": {
        "text": "Obrigado viajante! Não te vamos esquecer isto. Já temos recursos suficientes!",
        "options": [
            {"text": "O que vão fazer com eles?", "next": "explain_bomb"}
        ]
    },
    "explain_bomb": {
        "text": "Com o material que altruisticamente nos deste conseguimos contruir um explosivo que terá força suficiente para danificar a parede da cidade, e conseguiremos entrar.",
        "options": []
    },
    "travelling": {
        "text": "Estamos perto! Só nos falta usar o explosivo e estamos em casa!",
        "options": []
    },
}
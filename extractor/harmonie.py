# Rienecker + Dates from Steinman "From Abraham to Paul: A Biblical Chronology" + Correction

# Matthieu, Marc, Luc, Jean, Actes
harmonie=[
    {
        'titre': 'Prologue',
        'titre_short': 'prologue',
        'contenu': [
            {
                'titre': 'Introduction',
                'notes': [
                    "[Qui est Théophile ?](http://www.interbible.org/interBible/decouverte/comprendre/2013/clb_131011.html)"
                ],
                'contenu': [ None, [[1, 1, 1]], [[1, 1, 4]], [[1, 1, 5],[1,9,14]], None ]
            },
            {
                'titre': 'Généalogie',
                'contenu': [ [[1, 1, 17]], None, [[3, 23, 38]], None, None ]
            },
        ]
    },
    {
        'titre': 'Naissance et jeunesse de Jésus',
        'titre_short': 'jeunesse',
        'images': {
            'carte1.jpg': 'Carte 1'
        },
        'contenu': [
            {
                'titre': "Annonce par l'ange Gabriel de la naissance de Jean le Baptiste à Zacharie",
                'lieu': 'Jérusalem, Judée',
                'date': '-3',
                'contenu': [ None, None, [[1, 5, 25]], None, None ]
            },
            {
                'titre': "Annonce par l'ange Gabriel de la naissance de Jésus à Marie",
                'lieu': 'Nazareth, Galilée',
                'date': '-2',
                'contenu': [ None, None, [[1, 26, 38]], None, None ]
            },
            {
                'titre': 'Visite de Marie à Élisabeth',
                'lieu': 'Judée',
                'date': '-2',
                'contenu': [ None, None, [[1, 39, 56]], None, None ],
                'notes': ["Marie passe 3 mois en Judée"]
            },
            {
                'titre': 'Naissance de Jean le Baptiste',
                'date': '-3',
                'contenu': [ None, None, [[1, 57, 80]], None, None ]
            },
            {
                'titre': 'La naissance de Jésus annoncée à Joseph',
                'lieu': 'Nazareth, Galilée',
                'contenu': [ [[1, 18, 25]], None, None, None, None ]
            },
            {
                'titre': 'Naissance de Jésus',
                'date': '-2 vers le 1er Octobre',
                'lieu': 'Bethléem, Judée',
                'contenu': [ None, None, [[2, 1, 7]], None, None ],
                'notes': ['Jésus est né 5 mois et demi aprés Jean']
            },
            {
                'titre': 'Annonce des anges aux bergers',
                'date': '-2, début Octobre',
                'lieu': 'Près de Bethléem, Judée',
                'contenu': [ None, None, [[2, 8, 20]], None, None ]
            },
            {
                'titre': 'Circoncision de Jésus et présentation au temple de Bethléem. Purification de Marie.',
                'date': '-2, J+40 après naissance',
                'lieu': 'Bethléem ou Jérusalem, Judée',
                'notes': [
                    "Jésus est circoncis au 8e jour après sa naissance puis présenté au temple par ses parents après le 40e jour. ([Lév. 12:1-4](https://www.aelf.org/bible/Lv/12))"
                ],
                'contenu': [ None, None, [[2, 21, 38]], None, None ]
            },
            {
                'titre': 'Visite des mages',
                'date': '-2, 40/50 jours après naissance',
                'lieu': 'Bethléem, Judée',
                'contenu': [ [[2, 1, 12]], None, None, None, None ]
            },
            {
                'titre': 'Fuite en Égypte',
                'date': '-2',
                'lieu': 'Égypte', #TODO où la famille de Jésus a t'elle fui en Egypte ?
                'contenu': [ [[2, 13, 15]], None, None, None, None ]
            },
            {
                'titre': 'Meurtre des enfants de Bethléem par Hérode',
                # TODO quand cela a t'il eu lieu ?
                'contenu': [ [[2, 16, 18]], None, None, None, None ]
            },
            {
                'titre': "Retour à Nazareth par crainte d'Archélaüs",
                'date': '-1',
                'lieu': 'Nazareth, Galilée',
                'contenu': [ [[2, 19, 23]], None, [[2, 39, 40]], None, None ]
            },
            {
                'titre': 'Jésus au temple de Jérusalem à 12 ans',
                'date': '+10',
                'lieu': 'Jérusalem, Judée',
                'contenu': [ None, None, [[2, 41, 50]], None, None ]
            },
            {
                'titre': 'Jésus rentre à Nazareth (et devient charpentier);',
                'date': '+10',
                'lieu': 'Nazareth, Galilée',
                'contenu': [ None, None, [[2, 51, 52]], None, None ]
            },
        ]
    },
    {
        'titre': 'Debut du ministére avec Jean le Baptiste en Judée',
        'titre_short': 'debut',
        'images': {
            'carte2.jpg': 'Carte 2'
        },
        'contenu':[
            {
                'titre': 'Jean le Baptiste prépare son ministère',
                'contenu': [ [[3, 1, 12]], [[1, 2, 8]], [[3, 1, 18]], [[1, 6, 8]], None ],
                'date':  '+29, Mars-Juin',
                'lieu': 'Rives du Jourdain, en Judée ou en Pérée',
            },
            {
                'titre': 'Baptême de Jésus dans le Jourdain',
                'contenu': [ [[3, 13, 17]], [[1, 9, 11]], [[3, 21, 23]], None, None ],
                'date':  '+29, Juin/Juillet',
                'lieu': 'Rives du Jourdain, en Judée ou en Pérée',
            },
            {
                'titre': '40 jours de tentation',
                'contenu': [ [[4, 1, 11]], [[1, 12, 13]], [[4, 1, 13]], None, None ],
                'date':  '+29, Juillet-Septembre',
                'lieu': 'Désert de Judée',
                'images': {
                    "desert_de_judee.webp": "Vue du désert de Judée du mont Yair",
                },
                'notes':[
                    "Ce séjour fait écho aux quarante ans du peuple hébreu dans le désert pendant l’Exode, qui a connu dans sa longue traversée du désert la faim, la soif, l’épreuve et le doute. "
                ]
            },
        ]
    },
    {
        'titre': 'Jean le Baptiste à Béthanie',
        'titre_short': 'bethanie',
        'images': {
            'carte2.jpg': 'Carte 2'
        },
        'contenu':[
            {
                'titre': 'Prologue du témoignage de Jean le Baptiste envers Jésus',
                'contenu': [ None, None, None, [[1, 15, 18]], None ]
            },
            {
                'titre': 'J1: Témoignage de Jean le Baptiste',
                'contenu': [ None, None, None, [[1, 19, 28]], None ],
                'date':  '+29, Septembre-Novembre',
                'lieu': 'Béthanie en Pérée, au delà du Jourdain',
            },
            {
                'titre': 'J2: Jean identifie Jésus comme l\'agneau de Dieu',
                'contenu': [ None, None, None, [[1, 29, 34]], None ],
                'date':  '+29, Septembre-Novembre',
                'lieu': 'Béthanie en Pérée, au delà du Jourdain',
            },
            {
                'titre': 'J3: André suit Jésus et amène Simon-Pierre',
                'contenu': [ None, None, None, [[1, 35, 42]], None ],
                'date':  '+29, Septembre-Novembre',
                'lieu': 'Béthanie en Pérée, au delà du Jourdain',
            },
        ]
    },
    {
        'titre': 'Jésus en Galilée',
        'titre_short': 'galilee',
        'images': {
            'carte2.jpg': 'Carte 2'
        },
        'contenu':[
            {
                'titre': 'J4: Jésus retourne en Galilée et appelle Philippe qui améne Nathanaël',
                'contenu': [ None, None, None, [[1, 43, 51]], None ],
                'date':  '+29, Septembre-Novembre',
                'lieu': 'Béthanie en Pérée, au delà du Jourdain',
            },
            {
                'titre': 'J6: Noces de Cana',
                'contenu': [ None, None, None, [[2, 1, 11]], None ],
                'date':  '+29, Septembre-Novembre',
                'lieu': 'Cana, Galilée',
                'notes': ['Les noces durent trois jours. Le miracle se réalise le troisième jour']
            },
            {
                'titre': 'Jésus visite Capharnaüm',
                'contenu': [ None, None, None, [[2, 12, 12]], None ],
                'date':  '+29, Novembre-Décembre',
                'lieu': 'Capharnaüm, Galilée'
            },
        ]
    },
    {
        'titre': 'Jésus et Jean le Baptiste en Judée',
        'titre_short': 'judee',
        'images': {
            'carte2.jpg': 'Carte 2'
        },
        'contenu':[
            {
                'titre': 'Jésus va à Jérusalem pour la première Pâque de son ministère',
                'contenu': [ None, None, None, [[2, 13, 13]], None ],
                'date':  '+30, Mars/Avril',
                'lieu': 'Jérusalem, Judée',
                'notes': [
                    "Pessa'h, la Pâque juive, commémore la libération des esclaves israélites en Égypte antique"
                ]
            },
            {
                'titre': 'Il chasse les vendeurs et les changeurs du temple',
                'contenu': [ None, None, None, [[2, 14, 25]], None ],
                'date':  '+30, Mars/Avril',
                'lieu': 'Jérusalem, Judée',
            },
            {
                'titre': 'Entretien de nuit avec Nicodème, pharisien',
                'contenu': [ None, None, None, [[3, 1, 21]], None ],
                'date':  '+30, Avril',
                'lieu': 'Jérusalem, Judée',
            },
            {
                'titre':'Jésus quitte Jérusalem mais reste en Judée et baptise',
                'contenu': [ None, None, None, [[3, 22, 22]], None ],
                'date':  '+30, Avril-Octobre',
                'lieu': 'Judée',
            },
            {
                'titre':'Jean le Baptiste baptise à Aïnon (ou Ænon) ',
                'contenu': [ None, None, None, [[3, 23, 36]], None ],
                'date':  '+30, Avril-Octobre',
                'lieu': '[Aïnon, Judée](https://fr.wikipedia.org/wiki/A%C3%AFnon)',
            },
            {
                'titre':'Arrestation de Jean le Baptiste',
                'contenu': [ None, None, [[3,19,20]], None, None],
                'date':  '+30, Octobre',
            },
            {
                'titre':'Jésus quitte la Judée pour la Galilée',
                'contenu': [ [[4, 12, 12]], None, None, [[4, 1, 3]], None ],
                'date':  '+30, Novembre',
                'lieu': 'Judée',
            },
            {
                'titre':'Jésus passe par la Samarie : une femme de Sychar et plusieurs samaritains se convertissent',
                'contenu': [ None, None, None, [[4,4,42]], None ],
                'date':  '+30, Décembre',
                'lieu': 'Sychar, Samarie',
            },
        ]
    },
    {
        'titre': 'Jésus en Galilée',
        'titre_short': 'gallilee2',
        'images': {
            "carte3.jpg": "Carte 3",
        },
        'contenu':[
            {
                'titre':'Commencement de son ministère public en Galilée',
                'notes': ['Aprés que Jean eut été livré Marc 1:14'],
                'contenu': [ None, [[1,14,15]], [[4,14,30]], [[4,43,45]], None ],
                'date': '+31, Janvier',
                'lieu': 'Galilée',
            },
            {
                'titre':'Il s’établit à Capharnaüm où il enseigne',
                'contenu': [ [[4, 13, 17]], [[1, 21, 22]], [[4, 31, 32]], None, None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'La pêche miraculeuse ; l’appel de Simon, d’André, de Jacques et de Jean',
                'contenu': [ [[4,18,22]], [[1,16,20]], [[5,1,11]], None, None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Lac de Tibériade, près de Capharnaüm, Galilée'
            },
            {
                'titre':'Jésus parcourt la Galilée avec ses disciples',
                'contenu': [ [[4,23,25]], [[1,35,39]], [[4,42,44]], None, None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Galilée'
            },
            {
                'titre':'Jésus délivre un démoniaque',
                'contenu': [ None, [[1,23,28]], [[4,33,37]], None, None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Galilée'
            },
            {
                'titre':'Guérison de la belle-mère de Simon Pierre et d’autres malades',
                'contenu': [ [[8,14,17]], [[1,29,34]], [[4,38,41]], None, None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'Il visite Cana et guérit le fils d’un noble de Capharnaüm',
                'contenu': [ None, None, None, [[4,46,54]], None ],
                'date': '+31, Janvier-Mars',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'Il guérit un lépreux et fuyant la popularité, se retire au désert',
                'contenu': [ [[8,1,4]], [[1,40,45]], [[5,12,16]], None, None ],
                'date': '+31, Mars-Avril',
            },
            {
                'titre':'De retour à Capharnaüm, il guérit un paralytique qui lui est amené et descendu par le toit',
                'contenu': [ [[9,2,8]], [[2,1,12]], [[5,17,26]], None, None ],
                'date': '+31',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'L’appel de Matthieu, le festin et le discours dans sa maison — l’habit neuf et le vin nouveau',
                'contenu': [ [[9,9,13]], [[2,13,17]], [[5,27,32]], None, None ],
                'date': '+31',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'Réponse à ceux qui l’interrogent sur le jeûne',
                'contenu': [ [[9,14,17]], [[2,18,22]], [[5,33,39]], None, None ],
                'date': '+31',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre':'Passant par les champs, les disciples cueillent des épis le jour du sabbat',
                'contenu': [ [[12,1,8]], [[2,23,28]], [[6,1,5]], None, None ],
                'date': '+31, Avril-Mai',
                "note": '4 ou 5 mois, Tebeth to Nisan or Iyyar'
            },
            {
                'titre':'Jésus guérit un homme qui avait la main sèche ; les pharisiens et les hérodiens complotent contre Lui',
                'contenu': [ [[12,9,14]], [[3,1,6]], [[6,6,11]], None, None ],
                'date': '+31',
                'lieu': 'Galilée'
            },
            {
                'titre':'Il se retire près du lac et guérit plusieurs personnes',
                'contenu': [ [[12,15,21]], [[3,7,12]], [[6,17,19]], None, None ],
                'date': '+31',
                'lieu': 'Lac de Tibériade, Galilée'
            },
            {
                'titre':'Jésus choisit et nomme les douze apôtres',
                'contenu': [ None, [[3,13,19]], [[6,12,16]], None, None ],
                'date': '+31',
                'lieu': 'Galilée'
            },
            {
                'titre':'Le sermon sur la montagne',
                'contenu': [ [[5,1,48],[6,1,34],[7,1,29],[8,1,1]], None, [[6,20,49]], None, None ],
                'date': '+31',
                'lieu': 'Près de Capharnaüm, Galilée'
            },
            {
                'titre':'Guérison de l’esclave d’un centurion à Capharnaüm.',
                'contenu': [ [[8,5,13]], None, [[7,1,10]], None, None ],
                'lieu': 'Capharnaüm, Galilée',
                'date': '+31',
            },
            {
                'titre':"Résurrection du fils d'une veuve",
                'contenu': [ None, None, [[7,11,17]], None, None ],
                'date': '+31',
                'lieu': 'Naïn, Galilée',
                'images': {
                    'nain.jpg': 'Nain'
                }
            },
            {
                'titre':'Message de Jean-Baptiste à Jésus ; principe de changement de dispensation',
                'contenu': [ [[11,2,19]], None, [[7,18,35]], None, None ],
                'date': '+31',
                'lieu': 'Tibériade (Naïn ou environs), Galilée',
            },
            {
                'titre':'Reproches de Jésus à Chorazim, Bethsaïda, Capharnaüm et Il invite les âmes chargées',
                'contenu': [ [[11,20,30]], None, None, None, None ],
                'date': '+31',
            },
            {
                'titre':'La pécheresse pardonnée oint les pieds de Jésus chez Simon le pharisien',
                'contenu': [ None, None, [[7,36,50]], None, None ],
                'date': '+31',
                'lieu': 'Tibériade (Naïn ou environs), Galilée',
            },
            {
                'titre':'Il prêche de village en village en Galilée avec les 12 et des femmes pieuses',
                'contenu': [ None, None, [[8,1,3]], None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
            {
                'titre':'De retour à Capharnaüm, Il guérit un démoniaque aveugle et muet ; les pharisiens attribuent ce miracle à Béelzébul, blasphèment contre le Saint Esprit',
                'contenu': [ [[12,22,37]], [[3,22,30]], [[11,14,15],[11,17,23]], None, None ],
                'lieu': 'Capharnaüm, Galilée',
                'date': '+31',
            },
            {
                'titre':'Recherche d’un signe de sa part',
                'contenu': [ [[12,38,45]], None, [[11,16,16],[11,24,36]], None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
            {
                'titre':'Sa mère et ses frères le cherchent',
                'contenu': [ [[12,46,50]], [[3,20,21],[3,31,35]], [[8,19,21]], None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
            {
                'titre':'D’une barque Il énonce 7 paraboles',
                'contenu': [ [[13,1,53]], [[4,1,34]], [[8,4,18]], None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
            {
                'titre':'Jésus traverse le lac avec ses disciples et apaise la tempête',
                'contenu': [ [[8,18,27]], [[4,35,41]], [[8,22,25]], None, None ],
                'date': '+31',
                'lieu': 'Lac de Tibériade, Galilée',
            },
            {
                'titre':'Guérison de deux démoniaques',
                'contenu': [ [[8,28,34]], [[5,1,20]], [[8,26,40]], None, None ],
                'lieu': 'Gadara, Galilée',
                'date': '+31',
            },
            {
                'titre':'Retournant à l’ouest du lac, Il ressuscite la fille de Jaïrus et guérit une femme qui avait une perte de sang',
                'contenu': [ [[9,1,1],[9,18,26]], [[5,21,43]], [[8,41,56]], None, None ],
                'date': '+31',
                'lieu': 'Capharnaüm?, Galilée',
            },
            {
                'titre':'Il guérit deux aveugles et chasse un démon',
                'contenu': [ [[9,27,34]], None, None, None, None ],
                'date': '+31',
                'lieu': 'Capharnaüm?, Galilée',
            },
            {
                'titre':'Jésus revisite Nazareth ; incrédulité des habitants',
                'contenu': [ [[13,54,58]], [[6,1,6]], None, None, None ],
                'lieu': 'Nazareth, Galilée',
                'date': '+31',
            },
            {
                'titre': 'Enseigne en Galilée',
                'contenu': [ [[9,35,38]], [[6,6,6]], None, None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
            {
                'titre': 'Envoi des 12 disciples en mission',
                'contenu': [ [[10,1,42],[11,1,1]], [[6,7,13]], [[9,1,6]], None, None ],
                'date': '+31',
                'lieu': 'Galilée',
            },
        ]
    },
    {
        'titre': 'Jérusalem',
        'titre_short': 'jerusalem',
        'contenu':[
            {
                'titre':'Retour à Jérusalem pour la fête des Tabernacles. Il guérit un paralytique un jour de sabbat. Les pharisiens cherchent à le faire mourir',
                'contenu': [ None, None, None, [[5, 1, 47]], None ],
                'date':  '+31, Septembre-Octobre',
                'lieu': 'Jérusalem, Judée',
                'notes': [
                    "La fête des tabernacles est célébrée chaque année après le Grand Pardon, pendant laquelle les Juifs habitent des cabanes de branchages qui commémorent la traversée du désert sous la protection de Dieu."
                ]
            },
        ]
    },
    {
        'titre': 'Galilée',
        'titre_short': 'galilee3',
        'contenu': [
            {
                'titre': 'Execution de Jean le Baptiste',
                'contenu': [ [[14,1,12]], [[6,14,29]], [[3,19,20],[9,7,9]], None, None ],
                'date':  '+32, Décembre/Janvier',
                'lieu': 'Tibériade, Galilée',
            },
            {
                'titre': 'Retour des 12 ; Jésus se retire à l’autre rive et nourrit une foule de 5000 hommes plus les femmes et les enfants',
                'contenu': [ [[14,13,21]], [[6,30,44]], [[9,10,17]], [[6,1,15]], None ],
                'date':  '+32, Mars/Avril, vers la Pâque',
                'lieu': 'Capharnaüm?, rive NE de le Lac de Tibériade, Galilée',
            },
            {
                'titre': 'Envoi des disciples à Bethsaïda, de l’autre côté du lac, et de nuit Jésus vient à eux marchant sur l’eau',
                'contenu': [ [[14,22,33]], [[6,45,54]], None, [[6,16,21]], None ],
                'date':  '+32, Avril/Mai, vers la Pâque',
                'lieu': 'Galilée',
            },
            {
                'titre': 'La multitude nourrie miraculeusement cherche et trouve Jésus à Capharnaüm ; discours dans la synagogue et confession de Pierre',
                'contenu': [ None, None, None, [[6,22,71]], None ],
                'date':  '+32, Avril/Mai, vers la Pâque',
                'lieu': 'Capharnaüm, Galilée'
            },
            {
                'titre': 'Plusieurs guérisons dans la plaine de Génézareth',
                'contenu': [ [[14,34,36]], [[6,55,56]], None, None, None ],
                'date':  '+32, Avril/Mai, vers la Pâque',
                'lieu': 'Génézareth, Galilée',
                'images': {
                    'Génézareth.png': 'Emplacement de Génézareth',
                    'vue_de_génézareth.jpg': 'Vue du lac depuis Génézareth'
                }
            },
            {
                'titre': 'Les pharisiens et la tradition',
                'contenu': [ [[15,1,20]], [[7,1,23]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm ?, Galilée'

            },
            {
                'titre': 'Jésus se dirige vers Tyr et Sidon ; guérison de la fille de la femme cananéenne',
                'contenu': [ [[15,21,28]], [[7,24,30]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Phénicie, Décapole'
            },
            {
                'titre': 'Retour par la Décapole vers le Lac de Tibériade ; nombreuses guérisons ; multiplication des pains à une foule d’au moins 4000 hommes',
                'contenu': [ [[15,29,38]], [[7,31,37],[8,1,9]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Phénicie, Décapole'
            },
            {
                'titre': 'Jésus se rend à Dalmanutha',
                'contenu': [ [[15,39,39]], [[8,10,10]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': '[Magdala (Magadân)](https://fr.wikipedia.org/wiki/Magdala_(Isra%C3%ABl)), Galilée',
            },
            {
                'titre': 'Pharisiens et sadducéens cherchent un signe',
                'contenu': [ [[16,1,4]], [[8,11,12]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': '[Magdala (Magadân)](https://fr.wikipedia.org/wiki/Magdala_(Isra%C3%ABl)), Galilée',
            },
            {
                'titre': 'Quitte pharisiens et sadducéens jugés ; les 12 lents de cœur',
                'contenu': [ [[16,5,12]], [[8,13,21]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Lac de Tibériade, Galilée',
            },
            {
                'titre': 'Guérison d’un aveugle',
                'contenu': [ None, [[8,22,26]], None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Bethsaïde, Galilée',
                'images': {
                    'carte4.png': 'Carte 4',
                }
            },
            {
                'titre': 'Jésus sur le territoire de Césarée de Philippe ; la confession de Pierre',
                'contenu': [ [[16,13,20]], [[8,27,30]], [[9,18,21]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Césarée de Philippe, Galilée',
            },
            {
                'titre': 'Annonce Sa mort et Sa résurrection ; Pierre réprimandé',
                'contenu': [ [[16,21,28]], [[8,31,38],[9,1,1]], [[9,22,27]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Région de Césarée de Philippe, Galilée',
            },
            {
                'titre': 'La transfiguration',
                'contenu': [ [[17,1,13]], [[9,2,13]], [[9,28,36]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Mont Hermon?, Syrie',
            },
            {
                'titre': 'Le lendemain il chasse un démon',
                'contenu': [ [[17,14,21]], [[9,14,29]], [[9,37,43]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Région de Césarée de Philippe, Galilée',
            },
            {
                'titre': 'Jésus annonce à nouveau sa mort et sa résurrection',
                'contenu': [ [[17,22,23]], [[9,30,32]], [[9,44,45]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Galilée',
            },
            {
                'titre': 'Tribut payé miraculeusement',
                'contenu': [ [[17,24,27]], None, None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm, Galilée',
            },
            {
                'titre': 'Les petits enfants un modèle — Les offenses',
                'contenu': [ [[18,1,11]], [[9,33,48]], [[9,46,48]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm, Galilée',
            },
            {
                'titre': 'La brebis égarée',
                'contenu': [ [[18,12,14]], None, [[15,4,7]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm, Galilée',
            },
            {
                'titre': 'Parabole du débiteur et pardon',
                'contenu': [ [[18,15,35]], None, None, None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm, Galilée',
            },
            {
                'titre': 'Chacun salé de feu',
                'contenu': [ None, [[9,49,51]], None, None, None ]
            },
            {
                'titre': 'Celui qui n’est pas contre vous est pour vous',
                'contenu': [ None, None, [[9,49,50]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Capharnaüm, Galilée',
            },
            {
                'titre': 'Départ de la Galilée pour Jérusalem par la Samarie ; Il vient pour sauver et non pour détruire',
                'contenu': [ None, None, [[9,51,56]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Galilée -> Samarie',
            },
                        {
                'titre': 'Aucun lieu pour reposer sa tête — Laisser les morts ensevelir les morts — Ne pas regarder en arrière',
                'contenu': [ None, None, [[9,57,62]], None, None ],
                'date':  '+32, après la Pâque',
                'lieu': 'Galilée -> Samarie',
            },
            {
                'titre': 'Envoi des 70 — Jugement sur Chorazin, Tyr, Bethsaïda, Sidon — Celui qui méprise Christ méprise Celui qui L’a envoyé',
                'contenu': [ None, None, [[10,1,16]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Retour des 70 — Meilleure part, leurs noms sont écrits dans les cieux — Toutes choses livrées au Fils, bienheureux leurs yeux qui voient ce qu’ils voient',
                'contenu': [ None, None, [[10,17,24]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Question d’un docteur de la loi sur la vie éternelle — Histoire du Bon Samaritain',
                'contenu': [ None, None, [[10,25,37]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Béthanie, Judée',
            },
            {
                'titre': 'Jésus visite Marthe et Marie à Béthanie — Marie écoute Sa parole, Marthe sert',
                'contenu': [ None, None, [[10,38,42]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Béthanie, Judée',
            },
            {
                'titre': 'Il enseigne ses disciples à prier',
                'contenu': [ None, None, [[11,1,13]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Guérison d’un démoniaque muet — Blasphème contre le Saint Esprit — L’esprit immonde sorti — prend 7 autres de plus',
                'contenu': [ None, None, [[11,14,26]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Réception de la parole meilleure que la relation naturelle — Jugement de la génération par Jonas, Ninive, la reine de Shéba',
                'contenu': [ None, None, [[11,27,32]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Lumière sur le pied de lampe — Mais quel est l’œil qui la reçoit ?',
                'contenu': [ None, None, [[11,33,36]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Jugement des pharisiens, docteurs de la loi — Scribes Le pressent',
                'contenu': [ None, None, [[11,37,54]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Discours — Dieu doit être craint non pas l’homme — Toute chose sera connue',
                'contenu': [ None, None, [[12,1,7]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Disciples parlent par l’Esprit Saint — Parler contre l’Esprit Saint ne sera pas pardonné',
                'contenu': [ None, None, [[12,8,12]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Ne pas juger un conflit terrestre, fuir la convoitise, on n’est pas maître de sa vie',
                'contenu': [ None, None, [[12,13,21]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Ne pas être en souci, Dieu leur Père prend soin des disciples car ils Lui sont précieux — Le bon plaisir du Père est de leur donner le royaume',
                'contenu': [ None, None, [[12,22,34]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Attendre leur Seigneur jusqu’à ce qu’Il vienne ; alors l’amour du Christ les servira',
                'contenu': [ None, None, [[12,35,40]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Les serviteurs fidèles établis sur tous les biens du maître — Les infidèles jugés selon la connaissance de Sa volonté',
                'contenu': [ None, None, [[12,41,48]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Il n’apporte pas la paix ; discerner les temps ; se mettre d’accord avec la partie adverse de peur d’aller en prison',
                'contenu': [ None, None, [[12,49,59]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Ils doivent tous se repentir, ou bien seront détruits ; la patience de Dieu vis-à-vis de Son figuier est terminée',
                'contenu': [ None, None, [[13,1,9]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Guérison d’une femme infirme ; Il agit en grâce en Israël un jour de sabbat malgré l’hypocrisie',
                'contenu': [ None, None, [[13,10,17]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Royaume de Dieu semblable à un grain de moutarde, à du levain',
                'contenu': [ None, None, [[13,18,21]], None, None ],
                'date':  '+32, fête des Tabernacles',
                'lieu': 'Judée',
            },
            {
                'titre': 'Nombre des sauvés ; la nation rejette la porte étroite ; les derniers seront les premiers, les premiers, les derniers',
                'contenu': [ None, None, [[13,22,30]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Malgré les complots pour se débarrasser de Lui en Galilée Il doit mourir à Jérusalem au temps de Dieu quand Son œuvre sera faite',
                'contenu': [ None, None, [[13,31,33]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Plainte sur Jérusalem',
                'contenu': [ None, None, [[13,34,35]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Guérison d’un hydropique. Dieu doit être bon et travaille même un jour de sabbat',
                'contenu': [ None, None, [[14,1,6]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Paraboles des conviés — La grâce prend la dernière place et s’occupe de ceux qui ne peuvent pas rendre — Récompense en résurrection',
                'contenu': [ None, None, [[14,7,14]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Invitation au grand souper (caractère du Royaume) rejetée ; aller dans les rues puis dans les chemins ; les conviés sont rejetés',
                'contenu': [ None, None, [[14,15,24]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Renoncer aux relations et à la vie pour être Ses disciples ; calculer la dépense ; le sel doit garder sa saveur',
                'contenu': [ None, None, [[14,25,35]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Paraboles de la brebis égarée, de la drachme perdue et de l’enfant prodigue aux publicains — La grâce qui cherche, la grâce qui reçoit',
                'contenu': [ None, None, [[15,1,32]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'La grâce compte sur le futur en vue des choses présentes — Parabole de l’économe injuste',
                'contenu': [ None, None, [[16,1,18]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Les choses futures manifestées en contraste avec les choses présentes — Parabole du mauvais riche et de Lazare. Les juifs n’écouteront pas même si quelqu’un ressuscitait d’entre les morts',
                'contenu': [ None, None, [[16,19,31]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Offenses ; puissance de la foi ; serviteurs infidèles',
                'contenu': [ None, None, [[17,1,10]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Pérée',
            },
        ]
    },
    {
        'titre': 'Samarie',
        'date': "+32 Août/Septembre",
        'titre_short': 'samarie2',
        'contenu': [
            {
                'titre': 'Guérison de 10 lépreux sur la frontière samaritaine',
                'contenu': [ None, None, [[17,11,19]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Samarie',
            },
            {
                'titre': 'Parabole du juge inique',
                'contenu': [ None, None, [[17,20,37],[18,1,8]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Samarie',
            },
            {
                'titre': 'Parabole du pharisien et du publicain',
                'contenu': [ None, None, [[18,9,14]], None, None ],
                'date':  '+32, après la fête de l’Inauguration',
                'lieu': 'Samarie',
            },
        ]
    },
    {
        'titre': 'Judée',
        'titre_short': 'judee',
        'images': {
            'carte5.jpg': 'Carte 5'
        },
        'contenu': [
            {
                'titre': 'Voyage de Jésus pour la fête des Tabernacles',
                'contenu': [ None, None, None, [[7,1,10]], None ],
                'date': "+32 Septembre/Octobre",
                'lieu': 'Judée',
            },
            {
                'titre': 'Jésus quitte la fête et enseigne dans le temple',
                'contenu': [ None, None, None, [[7,11,14]], None ],
                'date': '+32',
                'lieu': 'Judée',
            },
            {
                'titre': 'Projets d’arrestation',
                'contenu': [ None, None, None, [[7,15,53]], None ],
                'date': '+32',
                'lieu': 'Judée',
            },
            {
                'titre': 'Femme adultère',
                'contenu': [ None, None, None, [[8,1,11]], None ],
                'date': '+32',
                'lieu': 'Judée',
            },
            {
                'titre': 'Jésus au temple se déclare la lumière du monde ; les Juifs cherchent à le lapider',
                'contenu': [ None, None, None, [[8,12,59]], None ],
                'date': '+32',
                'lieu': 'Judée',
            },
            {
                'titre': 'Guérison d’un aveugle-né',
                'contenu': [ None, None, None, [[9,1,41]], None ],
                'date': '+32',
                'lieu': 'Judée',
            },
            {
                'titre': 'Les pharisiens questionnent Jésus sur le divorce',
                'contenu': [ [[19,1,12]], [[10,1,12]], None, None, None ],
                'date': '+32',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Les parents amènent leurs enfants à Jésus',
                'contenu': [ [[19,13,15]], [[10,13,16]], [[18,15,17]], None, None ],
                'date': '+32',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Le jeune homme riche ; danger des richesses ; l’œuvre de salut est de Dieu et est impossible à l’homme ; tout quitter pour suivre Jésus',
                'contenu': [ [[19,16,30]], [[10,17,31]], [[18,18,30]], None, None ],
                'date': '+32',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Parabole des ouvriers de la vigne',
                'contenu': [ [[20,1,16]], None, None, None, None ],
                'date': '+32',
                'lieu': 'Pérée',
            },
            {
                'titre': 'Jésus annonce pour la 3ème fois Sa mort et Sa résurrection',
                'contenu': [ [[20,17,19]], [[10,32,34]], [[18,31,34]], None, None ],
                'date': '+32',
                'lieu': 'Pérée?',
            },
            {
                'titre': 'Demande des fils de Zébédée ; la place dans le royaume est pour ceux pour lesquels le Père l’a préparée ; la place d’abaissement des disciples',
                'contenu': [ [[20,20,28]], [[10,35,45]], None, None, None ],
                'date': '+32',
                'lieu': 'Pérée?',
            },
            {
                'titre': 'Guérison de 2 aveugles près de Jéricho ; Fils de David',
                'contenu': [ [[20,29,34]], [[10,46,52]], [[18,35,43],[19,1,1]], None, None ],
                'date': '+32',
                'lieu': 'Jéricho',
            },
            {
                'titre': 'Le publicain Zachée',
                'contenu': [ None, None, [[19,2,10]], None, None ],
                'date': '+32',
                'lieu': 'Jéricho',
            },
            {
                'titre': 'Parabole des 10 mines ; l’homme noble s’en va pour recevoir un royaume et au retour juge ses ennemis',
                'contenu': [ None, None, [[19,11,27]], None, None ],
                'date': '+32',
                'lieu': 'Jéricho',
            },
            {
                'titre': 'Parabole du Bon Berger',
                'contenu': [ None, None, None, [[10,1,21]], None ],
                'date': '+32',
            },
                {
                'titre': 'Jésus, à Jérusalem, pendant la fête de la Dédicace, déclare Son Unité avec le Père ; pour la 3ème fois les autorités cherchent à le lapider',
                'contenu': [ None, None, None, [[10,22,42]], None ],
                'date': "+32 Novembre/Décembre",
                'lieu': 'Jérusalem, Judée'
            },
        ]
    },
    {
        'titre': 'Pérée',
        'titre_short': 'bethanie2',
        'contenu': [
            {
                'titre': '2ème voyage de Jésus à Béthanie : Lazare malade',
                'contenu': [ None, None, None, [[11,1,16]], None ],
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'À Béthanie Jésus ressuscite Lazare',
                'contenu': [ None, None, None, [[11,17,46]], None ],
                'lieu': 'Béthanie, Judée'
            },
                        {
                'titre': 'Le sanhédrin décide de faire mourir Jésus',
                'contenu': [ None, None, None, [[11,47,53]], None ]
            },
            {
                'titre': 'Jesus se retire à Éphraïm',
                'contenu': [ None, None, None, [[11,54,54]], None ],
                'notes': ['Éphraïm correspond peut-être à Taïyibé en Samarie'],
                'lieu': 'Taïyibé, Samarie'
            },
        ]
    },
    {
        'titre': 'La quatrième Pâque',
        'titre_short': 'jerusalem2',
        'images': {
            'carte6.jpg': 'Carte 6'
        },
        'contenu': [
            {
                'titre': 'Jésus à Béthanie chez Simon le lépreux',
                'contenu': [ None, None, None, [[11,55,57]], None ],
                'date': 'Samedi 28 mars 33, 8 Nisan',
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'Des judéens viennent voir Jésus et Lazare à Béthanie',
                'contenu': [ None, None, None, [[12, 9, 11]], None ],
                'date': 'Samedi 28 mars 33, 8 Nisan',
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'Entrée triomphale de Jésus à Jérusalem sur un âne',
                'contenu': [ [[21,1,11]], [[11,1,10]], [[19,28,40]], [[12,12,19]], None ],
                'date': 'Dimanche 29 mars 33, 9 Nisan',
                'lieu': 'Béthanie -> Bethphagé -> Jérusalem, Judée'
            },
            {
                'titre': 'Pleurs sur Jérusalem',
                'contenu': [ None, None, [[19, 41, 44]], None, None ],
                'date': 'Dimanche 29 mars 33, 9 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Des grecs cherchent Jésus',
                'contenu': [ None, None, None, [[12, 20, 36]], None ],
                'date': 'Dimanche 29 mars 33, 9 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Jésus visite le temple et retourne dormir à Béthanie',
                'contenu': [ [[21,14,17]], [[11,11,11]], None, [[12, 37, 43]], None ],
                'date': 'Dimanche 29 mars 33, 9 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Le figuier stérile',
                'contenu': [ [[21,18,19]], [[11,12,14]], None, None, None ],
                'date': 'Lundi 30 mars 33, 10 Nisan',
                'lieu': 'Béthanie -> Jérusalem, Judée'
            },
            {
                'titre': 'Jésus chasse les marchands du temple',
                'contenu': [ [[21,12,13]], [[11,15,17]], [[19, 45, 46]], None, None ],
                'date': 'Lundi 30 mars 33, 10 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Les prêtres et les scribes veulent tuer Jésus',
                'contenu': [ None, [[11,18,18]], [[19, 47, 48]], None, None ],
                'date': 'Lundi 30 mars 33, 10 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Retour à Béthanie',
                'contenu': [ None, [[11,19,19]], None, None, None ],
                'date': 'Lundi 30 mars 33, 10 Nisan',
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'La foi véritable',
                'contenu': [ None, None, None, [[12, 44, 50]], None ],
                'date': 'Lundi 30 mars 33, 10 Nisan',
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'Enseignement du figuier',
                'contenu': [ [[21,20,22]], [[11,20,26]], None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Judée'
            },
            {
                'titre': 'Il enseigne au temple, Son autorité mise en question par le sanhédrin',
                'contenu': [ [[21,23,27]], [[11,27,33]], [[20,1,8]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Parabole des deux fils',
                'contenu': [ [[21,28,32]], None, None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Parabole des vignerons',
                'contenu': [ [[21, 33, 46]], [[12, 1, 12]], [[20, 9, 18]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Parabole des noces',
                'contenu': [ [[22, 1, 14]], None, None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Les pharisiens et les hérodiens lui posent des questions pièges sur le tribut dû à César',
                'contenu': [ [[22,15,22]], [[12,13,17]], [[20,19,26]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Les sadducéens le questionnent sur la résurrection',
                'contenu': [ [[22, 23, 33]], [[12, 18, 27]], [[20, 27, 39]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Il répond au sujet du plus grand commandement à un scribe',
                'contenu': [ [[22, 34, 40]], [[12, 28, 34]], None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Jésus demande aux pharisiens de qui le Messie est le fils.',
                'contenu': [ [[22, 41, 46]], [[12, 35, 37]], [[20, 40, 44]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Les sept reproches aux scribes et aux pharisiens',
                'contenu': [ [[23, 1, 36]], None, None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Mise en garde contre les scribes',
                'contenu': [ None, [[12,38,40]], [[20,45,47]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'L\'offrande de la veuve',
                'contenu': [ None, [[12,41,44]], [[21,1,4]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple,  Jérusalem, Judée'
            },
            {
                'titre': 'Lamentations sur Jérusalem',
                'contenu': [ [[23, 37, 39]], None, None, None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
            {
                'titre': 'Jésus annonce la destruction du temple',
                'contenu': [ [[24, 1, 2]], [[13, 1, 2]], [[21, 5, 6]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Mont des Oliviers, Jérusalem, Judée'
            },
            {
                'titre': 'Discours des oliviers',
                'contenu': [ [[24,3, 51],[25, 1, 46]], [[13, 3, 37]], [[21, 7, 36]], None, None ],
                'date': 'Mardi 31 mars 33, 11 Nisan',
                'lieu': 'Mont des oliviers, Jérusalem, Judée'
            },
            {
                'titre': 'Enseignements au temple',
                'contenu': [ None, None, [[21, 37, 38]], None, None ],
                'date': 'Mercredi 01 avril 33, 12 Nisan',
                'lieu': 'Temple, Jérusalem, Judée'
            },
                        {
                'titre': 'Jésus annonce sa crucifixition',
                'contenu': [ [[26, 1, 2]], None, None, None, None ],
                'date': 'Mercredi 01 avril 33, 12 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Les prêtres et les scribes complotent pour tuer Jésus',
                'contenu': [ [[26, 3, 5]], [[14, 1, 2]], [[22, 1, 2]], [[11, 45, 53]], None ],
                'date': 'Mercredi 01 avril 33, 12 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Jésus oint à Béthanie',
                'contenu': [ [[26, 6, 13]], [[14, 3, 9]], None, [[12, 1, 8]], None ],
                'date': 'Mercredi 01 avril 33, 12 Nisan',
                'lieu': 'Béthanie, Judée'
            },
            {
                'titre': 'Judas Iscarioth choisit de trahir Jésus',
                'contenu': [ [[26, 14, 16]], [[14, 10, 11]], [[22, 3, 6]], None, None ],
                'date': 'Mercredi 01 avril 33, 12 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Jésus envoie 2 disciples préparer le repas de la Pâque',
                'contenu': [ [[26, 17, 19]], [[14, 12, 16]], [[22, 7, 13]], None, None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '19h-21h: Le repas de la Pâque',
                'contenu': [ [[26, 20, 29]], [[14, 17, 25]], [[22, 14, 38]], [[13, 1, 35],[14, 1, 31],[15, 1, 27],[16, 1, 33],[17, 1, 26]], None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '21h-23h: Jésus prédit le reniement de Simon Pierre',
                'contenu': [ [[26, 30, 35]], [[14, 26, 31]], [[22,32,34]], [[13, 36, 38]], None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Mont des oliviers, Jérusalem, Judée'
            },
            {
                'titre': '21h-23h: Prières à Gethsémani',
                'contenu': [ [[26, 36, 46]], [[14, 32, 42]], [[22, 39, 46]], None, None ],
                'notes': ['Gethsémani pourrait être l\'oliveraie au pied du Mont des oliviers'],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Gethsémani, Mont des oliviers, Jérusalem, Judée'
            },
            {
                'titre': '23h: Jésus arrêté',
                'contenu': [ [[26, 47, 56]], [[14, 43, 52]], [[22, 47, 53]], [[18, 1, 12]], None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Mont des oliviers, Jérusalem, Judée'
            },
            {
                'titre': '23h-4h30: Jésus devant le grand prêtre Caiaphas',
                'contenu': [ [[26, 57, 68]], [[14, 53, 64]], [[22, 54, 54]], [[18, 13, 14],[18, 19, 24]], None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '23h-4h30: Simon Pierre renie Jésus',
                'contenu': [ [[26, 69, 75]], [[14, 66, 72]], [[22, 55, 62]], [[18, 15, 18],[18, 25, 27]], None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '23h-4h30: Jésus est houspillé par les gardes',
                'contenu': [ None, [[14, 65, 65]], [[22, 63, 65]], None, None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '23h-4h30: Jésus devant le Sanhédrin',
                'contenu': [ None, None, [[22, 66, 71]], None, None ],
                'date': 'Jeudi 2 avril 33, 13 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '4h: Jésus est amené devant Ponce Pilate, le gouverneur',
                'contenu': [ [[27, 1, 2]], [[15, 1, 1]], [[23, 1, 1]], [[18, 28, 28]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '4h30-6h: Judas Iscarioth se pend',
                'contenu': [ [[27, 3, 10]], None, None, None, [[1, 16, 19]] ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '4h30-6h: Jésus face à Pilate',
                'contenu': [ [[27, 11, 14]], [[15, 2, 5]], [[23, 2, 5]], [[18, 29, 38]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '4h30-6h: Jésus face à Hérode, roi de Judée',
                'contenu': [ None, None, [[23, 6, 12]], None, None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '6h: Barrabas le meurtrier libéré',
                'contenu': [ [[27, 15, 23]], [[15, 6, 14]], [[23, 13, 25]], [[18, 39, 40]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '6h: Pilate fait fouetter Jésus, cherche à le relâcher puis le livre',
                'contenu': [ [[27, 24, 31]], [[15, 15, 20]], None, [[19, 1, 16]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '8h: Jésus porte sa croix jusqu’à la porte de la ville où Simon de Cyrène s’en charge',
                'contenu': [ [[27, 32, 32]], [[15, 21, 22]], [[23, 26, 32]], [[19, 17, 17]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': '9h: Arrivé au Golgotha, Jésus refuse de boire du vin mélé de fiel',
                'contenu': [ [[27, 33, 34]], [[15, 23, 23]], None, None, None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Golgotha, Jérusalem, Judée'
            },
            {
                'titre': '9h-12h: Crucifixion au Golgotha',
                'contenu': [ [[27, 35, 44]], [[15, 24, 32]], [[23, 33, 43]], [[19, 18, 24]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Golgotha, Jérusalem, Judée'
            },
            {
                'titre': '12h-15h: L\'obscurité',
                'contenu': [ [[27, 45, 45]], [[15, 33, 33]], [[23, 44, 45]], None, None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Golgotha, Jérusalem, Judée'
            },
            {
                'titre': '15h: Décés de Jésus',
                'contenu': [ [[27, 46, 56]], [[15, 34, 41]], [[23, 46, 49]], [[19, 25, 37]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Golgotha, Jérusalem, Judée'
            },
            {
                'titre': '16h-17h: Mise au tombeau de Jésus',
                'contenu': [ [[27, 57, 61]], [[15, 42, 47]], [[23, 50, 56]], [[19, 38, 42]], None ],
                'date': 'Vendredi 3 avril 33, 14 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'La tombe est scellée puis gardée',
                'contenu': [ [[27, 62, 66]], None, None, None, None ],
                'date': 'Samedi 04 avril 33, 15 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            }
        ]
    },
    {
        'titre': 'La résurrection et les apparitions',
        'titre_short': 'resurrection',
        'contenu': [
            {
                'titre': 'La résurrection à l’aube',
                'contenu': [ [[28,2,4]], None, None, None, None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Les femmes viennent avec des aromates au sépulcre et le trouvent ouvert et vide.',
                'contenu': [ [[28,1,1]], [[16,1,4]], [[24,1,3]], [[20,1,2]], None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Les femmes restées au sépulcre voient deux anges qui leur annoncent la résurrection',
                'contenu': [ [[28, 5, 7]], [[16, 5, 7]], [[24, 4, 8]], None, None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Marie de Magdala revient au sépulcre, Jésus se révèle à elle',
                'contenu': [ None, [[16,9,11]], None, [[20,11,18]], None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Jésus rencontre les femmes (Marie de Magdala, Jeanne, Marie mère de Jacques) à leur retour',
                'contenu': [ [[28,8,10]], [[16,8,8]], [[24,9,11]], None, None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Le rapport des gardes',
                'contenu': [ [[28,11,15]], None, None, None, None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Pierre et Jean trouvent le sépulcre vide',
                'contenu': [ None, None, [[24,12,12]], [[20,3,10]], None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Porte de Damas, Jérusalem, Judée'
            },
            {
                'titre': 'Jésus apparaît et marche avec deux disciples sur la route d’Emmaüs',
                'contenu': [ None, [[16,12,13]], [[24,13,35]], None, None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Entre Jérusalem et Emmaüs, Judée'
            },
            {
                'titre': 'Jésus apparaît dans la soirée à dix apôtres',
                'contenu': [ None, None, [[24, 36, 49]], [[20, 19, 25]], None ],
                'date': 'Dimanche 05 avril 33, 16 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Jésus apparaît à nouveau aux onze apôtres réunis',
                'contenu': [ None, [[16, 14, 14]], None, [[20, 26, 29]], None ],
                'date': 'Dimanche 12 avril 33, 23 Nisan',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'Les onze s’en vont en Galilée à la montagne qu’il leur a indiquée. Jésus leur apparaît et leur commande d’évangéliser toutes les nations.',
                'contenu': [ [[28, 16, 20]], [[16, 15, 18]], None, None, None ],
                'lieu': 'Galilée'
            },
            {
                'titre': 'Jésus apparaît au bord du lac de Tibériade. Il confie à Pierre le soin des brebis et des agneaux',
                'contenu': [ None, None, None, [[21,1,14]], None ],
                'lieu': 'Galilée'
            },
            {
                'titre': 'La tâche de Simon Pierre',
                'contenu': [ None, None, None, [[21,15,24]], None ],
                'lieu': 'Galilée'
            },
        ]
    },
    {
        'titre': 'Ascension et Pentecôte',
        'titre_short': 'ascension',
        'contenu': [
            {
                'titre': 'Promesse de la venue du Saint Esprit',
                'contenu': [ None, None, None, None, [[1, 6, 8]]],
                'date': 'Jeudi 14 Mai 33',
                'lieu': 'Mont des Oliviers, Jérusalem, Judée'
            },
            {
                'titre': 'L\'ascension',
                'contenu': [ None, [[16, 19, 20]], [[24, 50, 53]], None, [[1, 9, 11]]],
                'date': 'Jeudi 14 Mai 33',
                'lieu': 'Mont des Oliviers, Jérusalem, Judée'
            },
            {
                'titre': 'Retour à Jérusalem et rassemblement',
                'contenu': [ None, None, None, None, [[1, 12, 26]]],
                'date': 'Mai 33',
                'lieu': 'Jérusalem, Judée'
            },
            {
                'titre': 'La Pentecôte et le discours de Pierre',
                'contenu': [ None, None, None, None, [[2, 1, 41]]],
                'notes': ['La pentecôte vient du grec pentêkostê qui signifie "cinquantième". La Pentecôte est en effet célébrée cinquante jour après Pâques'],
                'date': 'Dimanche 24 Mai 33',
                'lieu': 'Jérusalem, Judée'
            },
        ]
    },
    {
        'titre': 'Actes: Débuts et 1er voyage de Paul',
        'titre_short': 'apotres1',
        'contenu': [
            {
                'titre': 'Les débuts de l\'Église primitive ',
                'contenu': [ None, None, None, None, [[2, 42, 100]]],
            },
            {
                'titre': 'Le ministère de Pierre et de Jean à Jérusalem ',
                'contenu': [ None, None, None, None, [[3, 1, 100],[4,1,100],[5,1,100],[6,1,100],[7,1,100],[8,1,100]]],
            },
            {
                'titre': 'La conversion de Paul et son ministère',
                'contenu': [ None, None, None, None, [[9, 1, 100],[10,1,100],[11,1,100],[12,1,100]]],
            },
            {
                'titre': 'Le premier voyage missionnaire de Paul',
                'contenu': [ None, None, None, None, [[13, 1, 100],[14, 1, 100]]],
                'date': 'De mi 45 à fin 48',
            },
        ]
    },
    {
        'titre': 'Actes: Concile et 2ême voyage de Paul',
        'titre_short': 'apotres2',
        'contenu': [
            {
                'titre': 'Le Concile de Jérusalem',
                'contenu': [ None, None, None, None, [[15, 1, 100]]],
                'date': 'Avril/mai 49',
            },
            {
                'titre': 'Le deuxième voyage missionnaire de Paul ',
                'contenu': [ None, None, None, None, [[16, 1, 100], [17, 1, 100], [18, 1, 22]]],
                'date': 'Mai 49 à Novembre 51',
            },
        ]
    },
    {
        'titre': 'Actes: 3ême voyage de Paul et son arrestation',
        'titre_short': 'apotres3',
        'contenu': [
            {
                'titre': 'Le troisième voyage missionnaire de Paul ',
                'contenu': [ None, None, None, None, [[18, 23, 100], [19, 1, 100], [20, 1, 100], [21, 1, 11]]],
                'date': 'De 52 à mai 55',
            },
            {
                'titre': 'La judée, le voyage à Rome et l\'arrestation de Paul',
                'contenu': [ None, None, None, None, [[21, 12, 100], [22, 1, 100], [23, 1, 100], [24, 1, 100], [25, 1, 100], [26, 1, 100], [27, 1, 100], [28, 1, 100]]],
                'date': 'Juin 55 à mars 60',
            },
        ]
    },

]

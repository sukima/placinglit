import logging

from google.appengine.ext import db
from google.appengine.ext import webapp

# from classes import authors
from classes import placedlit


author_names = {
  'Sir Arthur Conan Doyle': 'Arthur Conan Doyle',
  'Harry Groome and others': 'Harry Groome',
  'Elizabeth McDonald (1910-1991)': 'Elizabeth McDonald',
  'Mary Wollstonecraft Shelley': 'Mary Shelley',
  'Margaret Eleanor Atwood': 'Margaret Atwood',
  'E-L Konigsburg': 'E. L. Konigsburg',
  'J.J. Hardie (1894-1951)': 'J.J. Hardie',
  'Elizabeth Von Armin': 'Elizabeth von Arnim',
  'Marta Chicote Juiz': 'Mart\xc3\xadn Chambi',
  'Vance Palmer (1885-1959)': 'Vance Palmer',
  '\xe9\x97\xab\xe7\xba\xa2 YAN Hong': 'Yan Hong',
  'Patrica Highsmith': 'Patricia Highsmith',
  'Louis Becke (1855-1913)': 'Louis Becke',
  'Sebasti\xef\xbf\xbd Juan Arb\xef\xbf\xbd': 'Sebasti\xc3\xa0 Juan Arb\xc3\xb3',
  'Ed Cahtterton': 'Ed Chatterton',
  'N\xef\xbf\xbdria Nardi': 'Maria Nardi',
  'STEPHENIE MEYER MEG CABOT': 'Stephenie Meyer',
  'Natsume Soseki': 'Natsume S\xc5\x8dseki',
  'Laura J. Moriarty': 'Laura Moriarty',
  'Bille Brown)': 'Bille Brown',
  'Gary D. Joiner, Cheryl H. White': 'Gary D. Joiner and Cheryl H. White',
  'Alfred Bernie Bell (Peter Bunkum)': 'Alfred Bernie Bell',
  'Benito P\xef\xbf\xbdrez Gald\xef\xbf\xbds': 'Benito P\xc3\xa9rez Gald\xc3\xb3s',
  'Rosa Navarro Dur\xef\xbf\xbdn': 'Rosa Navarro Dur\xc3\xa1n',
  'Sigurd Olson': 'Sigurd F. Olson',
  'V\xef\xbf\xbdctor Catal\xef\xbf\xbd': 'V\xc3\xadctor Catal\xc3\xa0',
  'Alexander MacDonald (1878-1939)': 'Alexander MacDonald',
  'Wallace Earle Stegner': 'Wallace Stegner',
  'Gonzalo M\xef\xbf\xbdrquez Cristo': 'Gonzalo M\xc3\xa1rquez Cristo',
  'John Watkins': 'Jonathan Watkins',
  'Mary Rold?an': 'Mary Rold\xc3\xa1n',
  'Alexander von Sch\xef\xbf\xbdnburg': 'Alexander von Schonburg',
  'Anon.': 'Anonymous',
  'Jaine & Raechel Faulkner': 'Jaime and Raechel Faulkner',
  'Dorothy Sayers': 'Dorothy L. Sayers',
  'Gary Crew & Gregory Rogers': 'Gary Crew Gregory Rogers',
  'Michael Gerard Bauer\xe2\x80\xa0': 'Michael Gerard Bauer',
  'Kath Walker/ Oodgeroo Noonuccal': 'Kath Walker',
  'Carlos- FUENTES': 'Carlos Fuentes',
  'Llosa Mario Vargas': 'Mario Vargas Llosa',
  'Fenimore Cooper James': 'James Fenimore Cooper',
  'Nancy Francis (1873-1954)': 'Nancy Francis',
  'Steele Rudd (Arthur Hoey David)': 'Steele Rudd',
  'Sembene Ousmane': 'Ousmane Semb\xc3\xa8ne',
  'Margery Forde & Michael Forde': 'Margery Forde and Michael Forde',
  'John Le Carre': 'John le Carr\xc3\xa9',
  'J.K. Rowling': 'J. K. Rowling',
  'Jaime & Raechel Faulkner': 'Jaime and Raechel Faulkner',
  'Carlos Ruiz Zafon': 'Carlos Ruiz Zaf\xc3\xb3n',
  'Joan Colebrook (n\xc3\x88e Heale) (1912-1991)': 'Joan Colebrook',
  'Edi\xef\xbf\xbd\xef\xbf\xbdes Gailivro': 'Edi\xc3\xa7\xc3\xb5es Gailivr',
  'SE Hinton': 'S. E. Hinton',
  'Billy Soo-Lee (copyright to: W.R. Soorley)': 'Billy Soo-Lee',
  'Joan Oliver (Pere Quart)': 'Joan Oliver',
  'John Lecarre': 'John le Carr\xc3\xa9',
  'Josep Aladern et. Al': 'Josep Aladern',
  'Tom Perotta': 'Tom Perrotta',
  'J. P. Salinger': 'J.D. Salinger',
  'Ion L. Idriess (1889-1979)': 'Ion L. Idriess',
  'Alfred J. Mac Adam': 'Alfred J. MacAdam',
  'Stephen Harris Morley King': 'Stephen King',
  'Plino Apuleyo Mendoza': 'Plinio Apuleyo Mendoza',
  'J.A. Barry (1850-1911)': 'J.A. Barry',
  'Elizabeth and Wandihnu Wymarra ; illustrated by Benjamin Hodges': 'Elizabeth and Wandihnu Wymarra',
  'Olivier Plaschka': 'Oliver Plaschka',
  'Mario Llosa Vargas': 'Mario Vargas Llosa',
  'Anita Bell (pseudonym AA Bell)': 'A.A. Bell',
  'Jonathon Coe': 'Jonathan Coe',
  "Ixion' nom de plume for Francis Kenna": 'Ixion',
  'Jason Miller': 'Jason Jack Miller',
  'Andri Snaer Magnason': 'Andri Sn\xc3\xa6r Magnason',
  'Ryszard Kapu?ci?ski': 'Ryszard Kapuscinski',
  "A.B. 'Banjo' Paterson (1864-1941)": "A.B. 'Banjo' Paterson",
  'Shipi Somaya Gowda': 'Shilpi Somaya Gowda',
  'Mark Twain (Samuel L. Clemens)': 'Mark Twain',
  'compiler, Brisbane City Council': 'Brisbane City Council',
  'Juan Jos\xef\xbf\xbd Arreola': 'Juan Jos\xc3\xa9 Arreola',
  'Gary Crew & Bruce Whatley': 'Gary Crew and Bruce Whatley',
  'S?seki Natsume': 'Natsume S\xc5\x8dseki',
  'Georg Seesslen': 'Georg See\xc3\x9flen',
  'Ritter Adler (Pseudonym)': 'Ritter Adler',
  'Louisa M. Alcott': 'Louisa May Alcott',
  'Shilip Somaya Gowda': 'Shilpi Somaya Gowda',
  'Lidi\xef\xbf\xbd\xef\xbf\xbd Korneevna Chukovska\xef\xbf\xbd\xef\xbf\xbd': 'Lydia Korneyevna Chukovskaya',
  'Angel Guimer\xef\xbf\xbd': '\xc3\x80ngel Guimer\xc3\xa0',
  'C?esar Vallejo': 'C\xc3\xa9sar Vallejo',
  'Francis Scott Key Fitzgerald': 'F. Scott Fitzgerald',
  'Frank Clune (1893-1971)': 'Frank Clune',
  'William Lane (John Miller) (1861-1917)': 'William Lane',
  'Nancy Mathes Horan': 'Nancy Horan',
  'Gabriel Garcia Marquez': 'Gabriel Garc\xc3\xada M\xc3\xa1rquez',
  'Ousmane Semb\xef\xbf\xbdne': 'Ousmane Semb\xc3\xa8ne',
  'Eckhard Nickel': 'Eckhart Nickel',
  'Emily Coungeau (1860-1936)': 'Emily Coungeau',
  'Merce Rodoreda': 'Merc\xc3\xa8 Rodoreda',
  'Julio Ram\xef\xbf\xbdn Ribeyro': 'Julio Ram\xc3\xb3n Ribeyro',
  'Maymie Ada Hamlyn-Harris (1890-1964)': 'Maymie Ada Hamlyn-Harris',
  'James L. A. Webb': 'James LA Webb',
  'Patricia- HIGHSMITH': 'Patricia Highsmith',
  'Mary House (1875-1950)': 'Mary House',
  'John le Carre': 'John le Carr\xc3\xa9',
  'Salvador Galm\xef\xbf\xbds': 'Salvador Galm\xc3\xa9s'}

titles = {
  'The Raven Saga Part 1: Raven': 'Raven',
  'Amy Foster Y Otros Relatos': 'Amy Foster',
  'Der Spion, Der Aus Der K\xef\xbf\xbdlte Kam': 'Der Spion, Der Aus Der Kulte Kam',
  'The Forever Love Series Box Set': 'The Forever Love',
  "The Reward' in Gemfields": 'The Reward',
  'Breaking Dawn: Special Edition': 'Breaking Dawn',
  'The Selected Works Of T.s. Spivet': 'Selected Works of T.S. Spivet',
  'The Host: A Novel': 'The Host',
  'Tempesta (Tempest)': 'Tempesta',
  'Nada: Una Novela': 'Nada',
  'Mercy Thompson 03. Spur Der Nacht': 'Mercy Thompson Spur Der Nacht',
  'Attack in the Library': 'Attack inthe Library',
  'Time Was Soft There: A Paris Sojourn at Shakespeare & Co.': 'Time Was Soft There',
  'Bis (biss) Zur Mittagsstunde': 'Biss Zur Mittagsstunde',
  'El Sue-o Del Celta': 'El Sueno del Celta',
  'Der Ewige G\xef\xbf\xbdrtner. Roman.': 'Der Ewige Gurtner',
  'Elizabeth Und Ihr Garten. Roman.': 'Elizabeth und Ihr Garten',
  "On the Northern Line' in Wildflowers of the Wallum": 'On the Northern Line',
  "Contaminated Food' located in: Short stories": 'Contaminated Food',
  'Palace Walk: The Cairo Trilogy': 'Palace Walk',
  'Faserland: Roman': 'Faserland',
  'The Talented Mr. Ripleyted Mr. Ripley': 'The Talented Mr. Ripley',
  'Dame, K\xef\xbf\xbdnig, As, Spion. Roman.': 'Dame, Kunig, As, Spion',
  'The Last Will & Testament of Senhor da Silva Ara\xc3\xbajo': 'The Last Will and Testament of Senhor da Silva Ara\xc3\xbajo',
  'Quien Mato A Palomino Molero?/who Killed Palomino Molero': 'Quien Mato A Palomino Molero?',
  'Cr\xc3\xadtica, personatges, confid\xc3\xa8ncies. Articles in\xc3\xa8dits i dispersos': 'Cr\xc3\xadtica, Personatges, Confid\xc3\xa8ncies',
  'PrairyErth: A Deep Map': 'Prairyerth',
  'Malfuria 02. Die H\xef\xbf\xbdterin Der Nebelsteine': 'Malfuria',
  'Bearn o la sala de les nines i Faust': 'Bearn o la sala de les nines',
  'El meu carrer, from Antologia po\xc3\xa8tica': 'El Meu Carrer',
  'The Selected Works Of T. S. Spivet': 'Selected Works of T.S. Spivet',
  'Victor Hugo Und Die Versuchung Des Unm\xef\xbf\xbdglichen': 'Victor Hugo Und Die Versuchung Des Unmglichen',
  'El Lenguaje De La Pasi\xef\xbf\xbdn': 'El Lenguaje De La Pasion',
  'Alpha & Omega': 'Alpha and Omega',
  'The Dead Years Volume 1': 'The Dead Years',
  'The Madonnas Of Echo Park: A Novel': 'The Madonnas of Echo Park',
  'La Orgia Perpetua/ The Perpetual Orgy:flaubert And Madame Bovary': 'La Orgia Perpetua',
  'Saga Crepusculo: Diarios / The Twilight Journals': 'Saga Crepusculo: Diarios',
  "Peregian Beach: Christmas Eve, Christmas Day 2003' in Coasters": 'Peregian Beach: Christmas Eve, Christmas Day 2003',
  'Zen And The Art Of Motorcycle Maintenance: An Inquiry Into Values': 'Zen and the Art of Motorcycle Maintenance',
  'Mercy Thompson, Tome 1': 'Mercy Thompson',
  'Fire (Elements of the Undead, #1)': 'Fire',
  'Ik, Jan Cremer': 'I Jan Cremer',
  'Twilight: Breaking Dawn': 'Twilight',
  'Twilight: Biss Zum Morgengrauen - Der Comic, Band 1': 'Twilight',
  "Cane Fires at Night' in Calendar Adam": 'Cane Fires at Night',
  'La Utopia Arcaica / The Archaic Utopia': 'La Utopia Arcaica',
  "The Flood' in The Australian Literary Review, vol. 6, no. 5, Jun. 2011, p. 21.": 'The Flood',
  "Romance - Old Style' in  Short stories": 'Romance - Old Style',
  'Air (Elements of the Undead, #2)': 'Air',
  'Der Nacht - Manager.': 'Der Nacht - Manager',
  'Lost Claus by Dan Fiorella': 'Lost Claus',
  'Halfkinds Volume 3: Alphas': 'Alphas',
  'Halfkinds Volume 2: Horus': 'Horus',
  'Conversacion En La Catedral: Bolsillo': 'Conversacion en la Catedral',
  "Twilight: The Graphic Novel Collector's Edition": 'Twilight',
  'Single Und Single.': 'Single Und Single',
  'Dietari. Roma 1930': 'Dietari',
  'The Twilight Saga Complete Collection': 'The Twilight Saga',
  'H\xef\xbf\xbdsitation': 'Hesitation',
  "Lena 1959' Die Liebe, der See und der Tod.": 'Lena 1959: Die Liebe, der See und der Tod',
  'One book many Brisbanes : fourth anthology of Brisbane stories': 'One Book Many Brisbanes',
  'The Lake, The River & The Other Lake': 'The Lake, the River and the Other Lake',
  'La Tia Julia Y El Escribidor/aunt Julia And The Scriptwriter': 'La Tia Julia Y El Escribidor',
  "The Working Man's Paradise: an Australian Labour novel": "The Working Man's Paradise",
  "Lot 17 Brisbane' in Short stories": 'Lot 17 Brisbane',
  "Daisy Madigan's Paradise: A Morgans Sisters Novella": "Daisy Madigan's Paradise",
  'Grab Onto Me Tightly As If I Knew The Way': 'Grab on to Me Tightly as If I Knew the Way',
  'Generation Golf 2.': 'Generation Golf Zwei',
  'Conversaci\xef\xbf\xbdn En La Catedral': 'Conversacion en la Catedral',
  "Orgia Perpetua. Flaubert Si 'doamna Bovary'": 'Orgia Perpetua',
  'Ein Blendender Spion. Roman.': 'Ein Blendender Spion',
  'Der Schneider Von Panama.': 'Der Schneider Von Panama',
  'Aunt Julia & The Scriptwriter': 'Aunt Julia and the Scriptwriter',
  'Amy Foster Y Otros Relatos Del Mar': 'Amy Foster',
  'War Of The End Of The World': 'The War of the End of the World',
  'Der Ewige G\xef\xbf\xbdrtner. 6 Cds.': 'Der Ewige Gurtner',
  "Patricia Briggs' Mercy Thompson": 'Mercy Thompson',
  'Crime: A Novel': 'Crime',
  'The Last Will And Testament Of Senhor Da Silva Ara\xef\xbf\xbdjo': 'The Last Will and Testament of Senhor da Silva Ara\xc3\xbajo',
  'La Hu\xef\xbf\xbdsped Hd 29': 'La Huesped',
  'The Sky Used to be Blue, Karma series #1': 'The Sky Used to be Blue',
  'I, Jan Cremer': 'I Jan Cremer',
  'Saga Fascination, Tome 3 : Hesitation': 'Saga Fascination',
  'O Sol Se Poe Em Sao Paulo': 'O Sol se p\xc3\xb5e em S\xc3\xa3o Paulo',
  'Contra Viento Y Marea, Ii:': 'Contra Viento Y Marea',
  "A flor d'oblit dins Obres Completes. Dietaris": "A Flor d'Oblit Dins Obres",
  'East Of The Mountains 18 C': 'East of the Mountains',
  'The Bible': 'Bible',
  'The Twilight Saga Collection': 'The Twilight Saga',
  'Twilight: Breaking Dawn Vol. 1 Of 2': 'Twilight',
  "Lena 1959' Die Liebe, der See und der Tod. ISBN 978-38442-1991-3": 'Lena 1959: Die Liebe, der See und der Tod',
  'Making Waves: Essays': 'Making Waves',
  'Twilight 2/hesitation': 'Twilight',
  'Mary Read: Sailor, Soldier, Pirate': 'Mary Read - Sailor, Soldier, Pirate',
  'THE COWCHIP CAFE available on Amazon.': 'The Cowchip Cafe',
  'La Ciudad Y Los Perros: Edicion Conmemorativa Del Cincuentenario': 'La Ciudad Y Los Perros',
  'Rockhound : an Annie Bryce mystery': 'Rockhound',
  'The Host 2': 'The Host',
  'The Host 1': 'The Host',
  'Mary Read: Sailor, Soldier, Pirate  Cherie Pugh': 'Mary Read - Sailor, Soldier, Pirate',
  'Last Of Mohicans': 'Last of the Mohicans',
  "Proserpine' located in Poems and Rhymes": 'Proserpine',
  'Twilight 12: Breaking Dawn Vol. 3 Of 4': 'Twilight',
  'Twilight, Tome 1': 'Twilight',
  'La Guerra Del Fin Del Mundo The War': 'La Guerra Del Fin Del Mundo',
  "Gotcha Merv' located in: Short stories": 'Gotcha Merv',
  'Eclipse - Portuguese Edition - Stephenie Meyer': 'Eclipse',
  'Crepusculo / Twilight': 'Crepusculo',
  'Faserland Textanalyse Und Interpretation Zu Christian Kracht': 'Faserland',
  'Lucky Stiff: A Lillian Byrd Crime Story': 'Lucky Stiff',
  'Les \xef\xbf\xbdmes Vagabondes': 'Les Ames Vagabondes',
  'Ciudad Y Los Perros': 'La Ciudad Y Los Perros',
  'Crepusculo: Un Amor Peligroso': 'Crepusculo',
  'De uitvreter | The Sponger': 'De Uitvreter',
  "Agent In Eigener Sache. Sonderausgabe. Smiley's Leute.": 'Agent in eigener Sache',
  'Halfkinds Volume 1: Contact': 'Contact',
  'Elizabeth Und Ihre Garten Projects': 'Elizabeth und Ihr Garten',
  'Los col\xe2\x80\xa2loquis de la insigne ciutat de Tortosa': 'Los colloquis de la insigne ciutat de Tortosa',
  'La Fiesta Del Chivo/the Feast Of The Goat': 'La Fiesta Del Chivo',
  'Johnno : a novel': 'Johnno',
  'Smileys People': "Smiley's People",
  'Elogio De La Madrastra': 'Elogio de la Madrasta',
  'Hail Tomorrow: a play in four acts': 'Hail Tomorrow',
  'Los Jefes / Los Cachorros/the Chiefs And The Cubs: Stories': 'Los Jefes',
  'Crep\xef\xbf\xbdsculo - Luz E Escurid\xef\xbf\xbdo': 'Crepusculo',
  'Seized: Book One of the Pipe Woman Chronicles': 'Seized',
  'Earth (Elements of the Undead, #3)': 'Earth',
  'Faserland. Roman.': 'Faserland',
  'Tristesse Royale. Das Popkulturelle Quintett.': 'Tristesse Royale',
  "Profiles of My Father' in The Bulletin, vol. 101 no. 5196, 29 Jan. 1980, p. 158.": 'Profiles of My Father',
  'The Detroit Electric Scheme: A Mystery': 'The Detroit Electric Scheme',
  'Huesped/ The Host': 'Huesped',
  'Saga Fascination - Twilight, Tome 1 : Fascination': 'Saga Fascination',
  'Ferien F\xef\xbf\xbdr Immer. Die Angenehmsten Orte Der Welt.': 'Ferien fur Immer',
  'Der Krieg Am Ende Der Welt.': 'Der Krieg Am Ende Der Welt',
  'Mercy Thompson 05. Zeichen Des Silbers': 'Mercy Thompson Zeichen Des Silbers',
  'Selected Works Of Ts Spivet': 'Selected Works of T.S. Spivet',
  'Das Ru\xef\xbf\xbdland- Haus. Roman.': 'Das Ruland Haus',
  'Intrigue in paradise : an Annie Bryce mystery': 'Intrigue in Paradise',
  'Luna Nueva /new Moon Movie Tie-in': 'Luna Nueva',
  'Shift!': 'Shift',
  'La Tentaci\xef\xbf\xbdn De Lo Imposible': 'La Tentacion De Lo Imposible',
  'Secret Daughter: A Novel': 'Secret Daughter',
  'Easy Street : A Lillian Byrd Crime Story': 'Easy Street',
  'The Twilight Saga Boxset': 'The Twilight Saga',
  "Yarnin' Up' in Only gammon : three plays from Kooemba Jdarra": "Yarnin' Up",
  'Malfuria - Die K\xef\xbf\xbdnigin Der Schattenstadt': 'Malfuria',
  'Saga Crepusculo: Guia Oficial Ilustrada': 'Saga Crepusculo: Diarios',
  'Eat Pray Love': 'Eat, Pray, Love',
  'Breaking Dawn. Stephenie Meyer': 'Breaking Dawn',
  'El Para\xef\xbf\xbdso En La Otra Esquina': 'El Paraiso en la Otra Esquina',
  'Mesopotamia. Ein Avant- Pop- Reader.': 'Mesopotamia',
  'The Twilight Saga White Collection': 'The Twilight Saga',
  'Wool 4: The Unraveling': 'Wool',
  'Mercy Thompson Series': 'Mercy Thompson',
  'Weihnachten. Gro\xef\xbf\xbddruck.': 'Weihnachten. Groudruck',
  'Los Cachorros; Los Jefes': 'Los Cachorros',
  'The Way To Paradise: A Novel': 'The Way To Paradise',
  'Header East Of The Mountai': 'Header East of the Mountain',
  'Crepusculo 1 / Twilight': 'Crepusculo',
  'Eclipse. Stephenie Meyer': 'Eclipse',
  'Die Uralte Metropole 01. Lycidas 1': 'Lycidas 1',
  'Der Ewige G\xef\xbf\xbdrtner.': 'Der Ewige Gurtner',
  'Der Heimliche Gef\xef\xbf\xbdhrte. Roman.': 'Der Heimliche Gefuhrte',
  'El saltamart\xc3\xad (1963)': 'El Saltamart\xc3\xad',
  'The Awakening And Selected Stories Of Kate Chopin': 'The Awakening',
  'La T\xef\xbf\xbda Julia Y El Escribidor': 'La Tia Julia Y El Escribidor',
  'Crosswind: Land, Sea, Sky Book 1': 'Crosswind',
  'Crist\xef\xbf\xbdbal Nonato. Novela.': 'Cristubal Nonato',
  'Frankenstein': 'Frankenstein or The Modern Prometheus',
  'Mercy Thompson Series Collection': 'Mercy Thompson',
  "The Outlaw and the Rider' in Australian Bush Ballads": 'The Outlaw and the Rider',
  'Traditional Chinese Edition Of Twilight': 'Twilight',
  'Affection : a novel': 'Affection',
  'I, Target (Part 1)': 'I, Target',
  "Inferno: A Poet's Novel": "Inferno (a poet's novel)",
  'Agent In Eigener Sache. Roman.': 'Agent in eigener Sache',
  "By Flood and by Torch' in Verse and Stories, p. 30": 'By Flood and By Torch',
  'Twilight 2/tentation': 'Twilight',
  'The Real Life Of Alejandro Mayta : A Novel': 'The Real Life of Alejandro Mayta',
  'Narraciones Y Novelas 1959-1967 / Short Stories And Novels 1959-1967': 'Narraciones Y Novelas 1959-1967',
  'Eine Kleine Stadt In Deutschland. Roman.': 'Eine Kleine Stadt In Deutschland',
  'Battlefield Eart': 'Battlefield Earth',
  'Crep\xef\xbf\xbdsculo': 'Crepusculo',
  'Ortsgesprach': 'Ortsgespr\xc3\xa4ch',
  'Homenots. Gaud\xc3\xad': 'Homenots',
  "Brisbane Inundated' in Scope, vol. 57, no. 1 Feb. 2011, p. 13.": 'Brisbane Inundated',
  'Orgia Perpetua, La': 'Orgia Perpetua',
  'The Bad Girl: A Novel': 'The Bad Girl',
  'Obra Reunida. Narrativa Breve/compiled Narrative Works: Narrativa Breve': 'Obra Reunida: Narrativa Breve',
  'Die Uralte Metropole 02. Lilith': 'Lilith',
  'Der Spion, Der Aus Der K\xef\xbf\xbdlte Kam. Gro\xef\xbf\xbddruck.': 'Der Spion, Der Aus Der Kulte Kam',
  'This book will save your life by A.M. Homes': 'This Book Will Save Your Life',
  'Further: Down The Path 2': 'Further',
  'Diccionario Del Amante De America Latina/ Dictionary Of The Lover Of Latin America': 'Diccionario Del Amante De America Latina',
  'Lituma En Los Andes/lituma In The Andes': 'Lituma En Los Andes',
  'Bis (biss) Zum Ersten Sonnenstrahl': 'Biss Zum Ersten Sonnenstrahl',
  "Beware of the Floods' in The Queenslander, 30 Jul. 1870, p. 6.": 'Beware of the Floods',
  'Amanecer': 'Breaking Dawn',
  'El Cuento Hispanoamericano Contempor\xef\xbf\xbdneo: Antolog\xef\xbf\xbda': 'El Cuento Hispanoamericano Contemporaneo',
  'Blood Meridian Or The Evening Redness In The West': 'Blood Meridian',
  'Verzauberter April. Gro\xef\xbf\xbddruck.': 'Verzauberter April',
  'El Paraiso En La Otra Esquina/the Way To Paradise': 'El Paraiso en la Otra Esquina',
  'D\xe2\x80\x99Al Pie de la encina. Historias tradicionales y recuerdos.': 'D\xe2\x80\x99Al Pie de la Encina',
  'Der Wachsame Tr\xef\xbf\xbdumer. Roman.': 'Der Wachsame Trumer',
  'Los Jefes / Los Cachorros/ The Chiefs And The Cubs': 'Los Jefes',
  'Eisprinzessin.': 'Eisprinzessin',
  'Der Spion, Der Aus Der K\xef\xbf\xbdlte Kam.': 'Der Spion, Der Aus Der Kulte Kam',
  'Der Ewige G\xef\xbf\xbdrtner': 'Der Ewige Gurtner',
  'Der Gelbe Bleistift.': 'Der Gelbe Bleistift',
  'The Twilight Collection': 'The Twilight Saga',
  'Call For The Dead.': 'Call For The Dead',
  'Crepuscle': 'Crepusculo',
  'Death In The Andes: A Novel': 'Death in the Andes',
  '\xe2\x80\x9cAls Llombards com a Casarsa. Imatges per a la Mediterr\xc3\xa0nia de Toni Catany\xe2\x80\x9d.': 'Als Llombards com a Casarsa. Imatges per a la Mediterr\xc3\xa0nia de Toni Catany',
  'Conversaciones En La Catedral': 'Conversacion en la Catedral',
  'Generation Golf. Eine Inspektion': 'Generation Golf: Eine Inspektion',
  "The Tower' in Polestar no. 18, 2009.": 'The Tower',
  "Men of the Carnarvon's' in Shadows in the mist : a collection of poems and short stories": "Men of the Carnarvon's",
  'Dame, K\xef\xbf\xbdnig, As, Spion': 'Dame, Kunig, As, Spion',
  'Amanecer = Breaking Dawn': 'Breaking Dawn',
  'Prairyerth (a Deep Map)': 'Prairyerth',
  "The Gray Years: a Mood' in The Queenslander, 17 July, 1897, p. 121.": 'The Gray Years: a Mood',
  "The Barron Falls, Q' in Rustling Leaves: Selected Poems": 'The Barron Falls, Q',
  "First Avenue' in Latecomers": 'First Avenue',
  'Outside - a post-apocalyptic novel': 'Outside',
  "The Gun Dealers' Daughter": "The Gun Dealer's Daughter",
  'Saga Fascination, Tome 4 : Revelation': 'Saga Fascination',
  'Twilight 13: Breaking Dawn Vol. 4 Of 4': 'Twilight',
  'Amanecer Mti / Breaking Dawn Mti': 'Breaking Dawn',
  "Floods' in The Brisbane Courier 8 February 1930  p. 22": 'Floods',
  'A Merced Del Viento. Relatos. Traducci\xef\xbf\xbdn De Helena Valent\xef\xbf\xbd.': 'A Merced del Viento',
  'A Hospedeira - Stephenie Meyer - Book In Portuguese': 'The Host',
  'La Ciudad Y Los Perros/the City And The Dogs': 'La Ciudad Y Los Perros',
  "Kay Thompson's Eloise": 'Eloise',
  'In Praise Of The Stepmother: A Novel': 'In Praise of the Stepmother',
  'The Journal of Lewis and Clarke to the Mouth of the Columbia River Beyond the Rocky Mountains in the Years 1804-5, & 6': 'The Journals Of Lewis And Clark',
  "Breaking Dawn Collector's Edition": 'Breaking Dawn',
  "Boat-ang mo'pul (in Wik Mungkan)= Two in a boat (in English)": "Boat-ang mo'pul",
  'Das Fest Des Ziegenbocks.': 'Das Fest Des Ziegenbocks',
  "Twilight Director's Notebook": 'Twilight',
  'Andes/andes': 'Andes',
  'La Tia Julia Y El Escribidor/ Aunt Julia And The Scriptwritter': 'La Tia Julia Y El Escribidor',
  "Lena 1959' Die Liebe, der See und der Tod. ISBN 978-3-8442-1991-3": 'Lena 1959: Die Liebe, der See und der Tod',
  'New Moon: The Graphic Novel, Vol. 2': 'New Moon',
  'New Moon: The Graphic Novel, Vol. 1': 'New Moon',
  'Los Jefes Los Cachorros': 'Los Jefes',
  'Travesuras De La Nina Mala / The Bad Girl': 'Travesuras De La Nina Mala',
  'The Wedding Of The Two-headed Woman: A Novel': 'The Wedding of the Two-Headed Woman',
  "The New Austrain' in Short stories": 'The New Austrain',
  "Smiley's People: A Novel": "Smiley's People",
  'Amanecer/breaking Dawn': 'Breaking Dawn',
  'Lob Der Stiefmutter. Roman.': 'Lob Der Stiefmutter',
  'Simplified Chinese Edition Of twilight: New Moon': 'Simplified Chinese Edition Of twilight',
  'Twilight Saga Eclipse Movie Comp': 'Twilight',
  'Nobels Testament;': 'Nobels Testament',
  'Tod Im Sch\xef\xbf\xbdrengarten': 'Tod im Sch\xc3\xa4rengarten',
  "Wild Fire' in Short stories": 'Wild Fire',
  'Mercy Thompson, Tome 5': 'Mercy Thompson Zeichen Des Silbers',
  'Selected Works Of T.s. Spivet, The': 'Selected Works of T.S. Spivet',
  'Der Nacht- Manager.': 'Der Nacht - Manager',
  'The Selected Works of T.S. Spivet': 'Selected Works of T.S. Spivet',
  'Plague Z, Part One': 'Plague Z',
  'Eine Art Held. Roman.': 'Eine Art Held',
  'The Host Vol. 2 Of 3': 'The Host',
  'Crepusculo - Twilight': 'Crepusculo',
  'Historia Secreta De Una Novela/the Secret History Of A Novel': 'Historia Secreta de una Novela',
  'Who Killed Palomino Molero': 'Who Killed Palomino Molero?',
  'Anleitung Zum Unschuldigsein. Das \xef\xbf\xbdbungsbuch F\xef\xbf\xbdr Ein Schlechtes Gewissen.': 'Anleitung Zum Unschuldigsein',
  "The Nigger Of The 'narcissus' -the Mirror Of The Sea": 'The Nigger of the Narcissus',
  'Jasminhof.': 'Jasminhof',
  "Las Guerras De Este Mundo / The Wars Of This World: Sociedad, Poder Y Ficcion En La Obra De Mario Vargas Llosa / Society, Power And Fiction In Mario Vargas Llosa's Work": 'Las Guerras De Este Mundo',
  'Down Amon The Dead Men': 'Down Among the Dead Men',
  'Twilight: The Graphic Novel, Vol. 1': 'Twilight',
  'Ciudad Y Los Perros, La Bol': 'La Ciudad Y Los Perros',
  'Historia De Mayta/ Real Life Of Alejandro Mayta': 'Historia de Mayta',
  'Amanhecer - Edicao Especial': 'Breaking Dawn',
  'Surrender or Starve: Travels in Ethiopia, Sudan, Somalia, and Eritrea': 'Surrender or Starve',
  'Un Homme accidentel by Philippe Besson (not translated into English yet)': 'Un Homme Accidentel',
  "Zane & Lucky's First Christmas": "Zane and Lucky's First Christmas",
  "Eclipse Collector's Edition": 'Eclipse',
  'Mi Primer Mario Vargas Llosa: Fonchito Y La Luna': 'Fonchito Y La Luna',
  "The Pub at Hannah Creek' in Random Rhymes: Poems from the Bush and Everyday Life": 'The Pub at Hannah Creek',
  "L'aroma d'ar\xc3\xa7 dins Obres Completes. Dietaris": "L'aroma d'ar\xc3\xa7 dins Obres Completes",
  "Prancer Muldoon the Stud' in Short stories": 'Prancer Muldoon the Stud',
  'El Sue\xef\xbf\xbdo Del Celta': 'El Sueno del Celta',
  'Lituma En Los Andes/spanish': 'Lituma En Los Andes',
  'Burke & Hare': 'Burke and Hare',
  'Breaking Dawn - Biss Zum Ende Der Nacht Teil 1. Filmausgabe': 'Breaking Dawn',
  'The Short Second Life Of Bree Tanner - An Eclipse Novella': 'The Short Second Life of Bree Tanner',
  'Lo somni. Orfeu i Tir\xc3\xa8sies visiten a Bernat': 'Lo somni',
  'Rassvet / Breaking Dawn': 'Rassvet',
  'Abraham Lincoln': 'Abraham Lincoln: The Prairie Years and The War Years',
  'Eclipse: The Twilight Saga Book 3': 'Eclipse',
  "Lena 1959' Die Liebe, der See und der Tod": 'Lena 1959: Die Liebe, der See und der Tod',
  'Qui A Tue Palomino Molero ?': 'Qui A Tue Palomino Molero?',
  'After the Fall (Broken Angel #2)': 'After the Fall',
  "On Whitsunday Passage'  in Chops and gravy : more bushies": 'On Whitsunday Passage',
  'Peratallada, from Antologia po\xc3\xa8tica': 'Peratallada',
  'El Paraiso En La Otra Esquina/ The Way To Paradise': 'El Paraiso en la Otra Esquina',
  'Das Gr\xef\xbf\xbdne Haus': 'Das Grune Haus',
  "Deep Into The Game: S.w. Tanpepper's Gameland": 'Deep into the Game',
  'Immorial': 'Immoral',
  'Todos Los Perros De Mi Vida/ All The Dogs Of My Life': 'Todos Los Perros De Mi Vida',
  'True Confections: A Novel': 'True Confections',
  'The Host. La Huesped': 'The Host',
  'Alpha & Omega, Tome 2': 'Alpha and Omega',
  'Alpha & Omega, Tome 1': 'Alpha and Omega',
  'The Enchanted April 1922': 'The Enchanted April',
  'El viol\xc3\xad d\xe2\x80\x99Auschwitz': "El Viol\xc3\xad d'Auschwitz",
  "Shark Bait' located in Short stories": 'Shark Bait',
  'Time Between Trains (Holy Walker)': 'Time Between Trains',
  'Die Libelle. Roman.': 'Die Libelle',
  'Contra Viento Y Marea / Making Waves': 'Contra Viento Y Marea',
  'The School of Arts: a play': 'The School of Arts',
  'New Moon. Stephenie Meyer': 'New Moon',
  'Loose ends : an Annie Bryce mystery': 'Loose Ends',
  'Mayne Inheritance: a play': 'Mayne inheritance',
  'La Verdad De Las Mentiras / The Truth About Lies': 'La Verdad De Las Mentiras',
  'New Moon: The Twilight Saga Book 2': 'New Moon',
  "Take Me Back' in Random Rhymes: Poems from the Bush and Everyday Life": 'Take Me Back',
  'Brindle royalist : a story of the plains': 'Brindle Royalist - A Story of the Australian Plains',
  'Ein Mord Erster Klasse.': 'Ein Mord Erster Klasse',
  'The Thousand Autumns Of Jacob De Zoet: A Novel': 'The Thousand Autumns of Jacob de Zoet',
  'untitled poem in Just Thoughts': 'Untitled',
  'Eloge De La Mar\xef\xbf\xbdtre': 'Eloge de la Martre',
  'Les Miserables': 'Les Mis\xc3\xa9rables',
  'Conversacion En La Catedral / Conversation In The Cathedral': 'Conversacion en la Catedral',
  'Wool 3': 'Wool',
  'Lucky Stiff!': 'Lucky Stiff',
  'Travesuras De La Nina Mala / Mischiefs Of The Bad Girl': 'Travesuras De La Nina Mala',
  'My \xef\xbf\xbdntonia': 'My Antonia',
  'Uralte Metropole 04. Somnia': 'Uralte Metropole',
  'Mart\xef\xbf\xbdn Chambi 1920-1950': 'Martin Chambi 1920-1950',
  'Zeit Der J\xef\xbf\xbdger': 'Zeit Der Jaeger',
  'The Bourne Identity: A Novel': 'The Bourne Identity',
  'Agent In Eigener Sache.': 'Agent in eigener Sache',
  'Blow-up, And Other Stories': 'Blow-up and Other Stories',
  'La F\xef\xbf\xbdte Au Bouc': 'La Fete Au Bouc',
  'Llibre d\xe2\x80\x99amic e amat': "Llibre d'amic e amat",
  'From The Mixed-up Files Of Mrs. Basil E. Frankweiler:35th Anniversary Edition': 'From the Mixed-Up Files of Mrs. Basil E. Frankweiler',
  'Twlight: Eclipse': 'Twilight',
  'Pantaleon Y Las Visitadoras/captain Pantoja And The Special Service': 'Pantaleon Y Las Visitadoras',
  'Freedom Or Death, The Life Of Gots\xef\xbf\xbd Delchev': 'Freedom or Death',
  'Bis (biss) Zum Morgengrauen': 'Biss Zum Morgengrauen',
  'Crepusculo. Un Amor Peligroso': 'Crepusculo',
  'Twilight: The Graphic Novel, Volume 1': 'Twilight',
  'Tagebuch Eines Sommers.': 'Tagebuch Eines Sommers',
  'Nostre Deu-vos-guard, a La Nova Cathalunya (11 febrer 1898, n\xc3\xbam. 1, p. 2)': 'Nostre Deu-vos-guard',
  'Twilight 10: Breaking Dawn Vol. 1 Of 4': 'Twilight',
  "Taming Patrick' in Short stories": 'Taming Patrick',
  'Twilight: The Graphic Novel, Vol. 2': 'Twilight',
  'Ring Of Daggers - A David Nelson Adventure': 'Ring Of Daggers',
  'Alg\xc3\xba que espera': "Suite de Parlav\xc3\xa0, seguit d'Alg\xc3\xba que espera",
  'Wool - Omnibus Edition': 'Wool',
  'Memory - Stadt Der Tr\xef\xbf\xbdume': 'Memory - Stadt Der Trume',
  'Frankenstein, Or, The Modern Prometheus': 'Frankenstein or The Modern Prometheus',
  'Verzauberter April.': 'Verzauberter April',
  'La Segunda Vida De Bree Tanner / The Short Second Life': 'La Segunda Vida De Bree Tanner',
  "S.W. Tanpepper's GAMELAND": 'Gameland',
  'Nada: A Novel': 'Nada',
  'Crepusculo 1 / Twilight 1': 'Crepusculo',
  'Absolute Freunde.': 'Absolute Freunde',
  'Faces in the Street: a story of Brisbane during the general strike of 1912': 'Faces in the Street',
  'Next: A Novel': 'Next',
  'Biss (biss) Zum Ende Der Nacht': 'Biss Zum Ende Der Nacht',
  'Ortsgespr\xef\xbf\xbdch': 'Ortsgespr\xc3\xa4ch',
  'La Civilizaci\xef\xbf\xbdn Del Espect\xef\xbf\xbdculo': 'La Civilizacion Del Espectaculo',
  'Conversacion En La Catedral ; La Orgia Perpetua ; Pantaleon Y Las Visitadoras': 'Conversacion en la Catedral',
  'El lledoner de la clastra': 'El Iledoner de la Clastra',
  'Crepusculo/ Twilight': 'Crepusculo',
  'Sables Y Utopias /essays By Vargas Llosa. His Vision About Latin America: Visiones De America Latina': 'Sables Y Utopias',
  'Bis (biss)zum Ende Der Nacht': 'Biss Zum Ende Der Nacht',
  'Tinker Tailor Soldier Spy: A Novel': 'Tinker, Tailor, Soldier, Spy',
  'The Plagiarist: A Novella': 'The Plagiarist',
  'The Raven Saga Part I: Raven': 'Raven',
  'Mercy Thompson: Moon Called': 'Mercy Thompson Moon Called',
  'Aunt Julia And The Scriptwriter: A Novel': 'Aunt Julia and the Scriptwriter',
  'Pursuit (Owen Hunter Series)': 'Pursuit',
  'Grandes Entrevistas De Com\xef\xbf\xbdn Presencia': 'Grandes Entrevistas De Coman Presencia',
  'Los Cachorros/los Jefes': 'Los Cachorros',
  'Die M\xef\xbf\xbdrderin.': 'Die Murderin',
  'The Wedding of the Two Headed Woman': 'The Wedding of the Two-Headed Woman',
  'La Letteratura \xef\xbf\xbd Fuoco. Contro Vento E Marea Vol. 2': 'La Letteratura a Fuoco',
  'Eclipsi': 'Eclipse',
  'Lo somni. Bernat parla de la seva innoc\xc3\xa8ncia': 'Lo somni',
  'Saga Fascination, Tome 1 : Fascination': 'Saga Fascination',
  'Ilustrado: A Novel': 'Ilustrado',
  '\xc2\xa0Terra baixa': 'Terra Baixa',
  'The Selected Works Of T. S. Spivet: A Novel': 'Selected Works of T.S. Spivet',
  'Contra Viento Y Marea, I:': 'Contra Viento Y Marea',
  'K\xc3\x89SEI SIRAT\xc3\x93': 'Kesei Sirato',
  'The Host Vol.1 Of 3': 'The Host',
  'Elizabeth Y Su Jardin Aleman / Elizabeth And Her German Garden': 'Elizabeth Y Su Jardin Aleman',
  'Les \xc3\x82mes Vagabondes': 'Les Ames Vagabondes',
  "Wobegong Shark' in Short stories": 'Wobegong Shark',
  'Lena 1959. Die Liebe, der See und der Tod': 'Lena 1959: Die Liebe, der See und der Tod',
  'Pedro Paramo': 'Pedro P\xc3\xa1ramo',
  'Overseas: stories': 'Overseas',
  "Twilight Collector's Edition": 'Twilight',
  'Amanhacer - Breaking Dawn - Portuguese Edition - Stephenie Meyer': 'Breaking Dawn',
  'Twilight. Stephenie Meyer': 'Twilight',
  "Brisbane Flood' in The Departure": 'Brisbane Flood',
  'El Sueno Del Celta / The Celtic Dream': 'El Sueno del Celta',
  'Vater. Roman. ( Die Frau In Der Literatur).': 'Vater',
  'Pantaleon Y Las Visitadoras / Captain Pantoja And The Special Service': 'Pantaleon Y Las Visitadoras',
  'The Host Vol. 3 Of 3': 'The Host',
  "New Moon Collector's Edition": 'New Moon',
  'Obras Completas Vi/ Complete Works Vi': 'Obras Completas VI',
  'Schatten Von Gestern.': 'Schatten Von Gestern',
  'Crepusculo, Un Amor Peligroso': 'Crepusculo',
  'Little House On The Prairie 75th Anniversary Edition': 'Little House on the Prairie',
  'La Tentacion De Lo Imposible/the Temptation Of The Impossible: Victor Hugo Y Los Miserables': 'La Tentacion De Lo Imposible',
  'Wool 5 - The Stranded': 'Wool',
  "The No 1 Ladies' Detective Agency": "The No. 1 Ladies' Detective Agency",
  "Deadman's Camp' in Steve Brown's Bunyip and Other Stories": "Deadman's Camp",
  'Cold, (Pamphlet Poets, Series 2, no. 5.)': 'Cold',
  'Twilight: The Complete Illustrated Movie Companion': 'Twilight',
  'Bestiari =': 'Bestiari',
  'New Moon Special Edition': 'New Moon',
  'Time Between Trains (Time Between Trains)': 'Time Between Trains',
  "Rock'NRoll in Locker Seventeen": "Rock'N Roll in Locker Seventeen",
  'Luna Nueva/ New Moon': 'Luna Nueva',
  'La Plaza Del Diamante/the Diamond Plaza': 'La pla\xc3\xa7a del Diamant',
  'Promise Me Anthology': 'Promise Me',
  'El Senor Skeffington/ Mr. Skeffington': 'El Senor Skeffington',
  'Lash (Broken Angel)': 'Lash',
  'First Shift - Legacy': 'Legacy',
  "The Blackall Ranges, Q' in Palm Fronds: Poems and Verse": 'The Blackall Ranges, Q',
  'Catch-22: 50th Anniversary Edition': 'Catch-22',
  'Eine Art Held.': 'Eine Art Held',
  'Corbeau, Tome 1': 'Corbeau',
  "Old Banana Town' in Lest We Forget: poems of the Dawson Valley": 'Old Banana Town',
  'Lo somni. Fragment del llibre quart': 'Lo somni',
  "Les Bonnes Nouvelles De L'am\xef\xbf\xbdrique Latine": "Les Bonnes Nouvelles De L'amrique Latine",
  'Blood Meridian: Or the Evening Redness in the West': 'Blood Meridian',
  'El Sueno Del Celta / The Dream Of The Celt': 'El Sueno del Celta',
  'Das B\xef\xbf\xbdse M\xef\xbf\xbddchen': 'Das Buse Mudchen',
  "Lena 1959' Die Liebe, der See und der Tod. ISBN 987-3-8442-1991-3": 'Lena 1959: Die Liebe, der See und der Tod',
  'Galatea 2.2 : A Novel': 'Galatea 2.2',
  'The Dream Of The Celt: A Novel': 'The Dream Of The Celt',
  'Conversation In The Cathedral': 'Conversacion en la Catedral',
  "Swann's Way: In Search of Lost Time, Volume 1": "Swann's Way: In Search of Lost Time",
  'Die Karte Meiner Tr\xef\xbf\xbdume': 'Die Karte Meiner Trume',
  'River Marked. By Patricia Briggs': 'River Marked',
  'Lob Der Stiefmutter.': 'Lob Der Stiefmutter',
  'Alpha & Omega, Call Of The Hunt': 'Alpha and Omega',
  'La Tia Julia Y El Escribidor/ Aunt Julia And The Scriptwriter': 'La Tia Julia Y El Escribidor',
  'Krieg Im Spiegel.': 'Krieg Im Spiegel',
  'Sallys Gl\xef\xbf\xbdck.': 'Sallys Glack',
  'Alias Grace : A Novel': 'Alias Grace',
  'Travessuras Da Menina Ma - Edicao De Bolso': 'Travessuras Da Menina Ma',
  'Twilight: Eclipse': 'Twilight',
  'Les Ames Vagabondes Fl': 'Les Ames Vagabondes',
  'Bis (biss) Zum Abendrot': 'Biss Zum Abendrot',
  'The Sun Also Rises, A Novel Of The Twenties': 'The Sun Also Rises',
  'Corbeau ; Int\xef\xbf\xbdgrale': 'Corbeau',
  'Wool 2': 'Wool',
  "Acacia Ridge' in My People": 'Acacia Ridge',
  'King Of Swords: Assassin Series #1': 'King of Swords',
  "Dead Snake Attacks' located in Short stories": 'Dead Snake Attacks',
  'Los Jefes-los Cachorros': 'Los Jefes',
  "In Memory of Bauhinia Shire 11/11/1879-14/3/2008' in Shadows in the mist : a collection of poems and short stories": 'In Memory of Bauhinia Shire',
  'This Book Will Save Your Life by A.M. Homes': 'This Book Will Save Your Life',
  'La Fiesta Del Chivo 1': 'La Fiesta Del Chivo',
  "Moving of 'Winnie'": 'Moving of Winnie',
  'Saga Fascination, Tome 2 : Tentation': 'Saga Fascination',
  'Twilight: New Moon': 'Twilight',
  'The Enchanted April: Intermediate': 'The Enchanted April',
  'Jet Ii - Betrayal': 'Betrayal',
  'P\xef\xbf\xbdikesevariutus': 'Pikesevariutus',
  'The Short Second Life Of Bree Tanner: An Eclipse Novella': 'The Short Second Life of Bree Tanner',
  'Bis (biss) Zum Abendrot: Eclipse': 'Biss Zum Abendrot',
  "Meditation 6: The River at Brisbane' in Southerly, vol. 52, no. 1, March 1992, p. 58": 'Meditation 6: The River at Brisbane',
  'The Feast Of The Goat: A Novel': 'The Feast of the Goat',
  'La Casa Verde/ The Green House': 'La Casa Verde',
  'Malfuria 01': 'Malfuria',
  'Lituma En Los Andes / Death In The Andes': 'Lituma En Los Andes',
  "Atherton' in The Musings of a Mountain Maid": 'Atherton in The Musings of a Mountain Maid',
  'The Daughter: a Novel': 'The Daughter',
  'La vaca cega (The blind cow)': 'La vaca cega',
  'Fortunata and Jacinta: Two Stories of Married Women': 'Fortunata and Jacinta',
  'Deception : a techno-thriller novel': 'Deception'}


class UpdateAuthorsHandler(webapp.RequestHandler):
  def get(self):
    updated_scenes = list()
    for key, value in author_names.iteritems():
      try:
        query = db.GqlQuery('SELECT __key__ from PlacedLit WHERE author = :1',
                            key)
        for scene_key in query.run():
          self.response.out.write('{}:{}<br/>'.format(key, value))
          place = placedlit.PlacedLit.get(scene_key)
          place.author = value
          updated_scenes.append(place)
          # place.put()
      except UnicodeError:
        self.response.out.write('{}:{}<br/>'.format(key, value))
        # logging.info('%s:%s', key, value)
    db.put(updated_scenes)


class UpdateTitlesHandler(webapp.RequestHandler):
  def get(self):
    # updated_scenes = list()
    for key, value in titles.iteritems():
      try:
        query = db.GqlQuery('SELECT __key__ from PlacedLit WHERE title = :1',
                            unicode(key))
        for scene_key in query.run():
          self.response.out.write('{}:{}<br/>'.format(key, value))
          place = placedlit.PlacedLit.get(scene_key)
          place.title = value
          # updated_scenes.append(place)
          place.put()
      except UnicodeError:
        self.response.out.write('{}:{}<br/>'.format(key, value))
        # logging.info('%s:%s', key, value)


urls = [
  ('/update_authors', UpdateAuthorsHandler),
  ('/update_titles', UpdateTitlesHandler),
]

app = webapp.WSGIApplication(urls, debug="True")

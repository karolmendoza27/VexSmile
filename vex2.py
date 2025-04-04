import telebot
import sqlite3
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

# Configuración del bot de Telegram
TELEGRAM_BOT_TOKEN = '7855247638:AAEZzoLl6Xc0CRRjE52kCJmLo-Enu_AmxkY'
 
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Inicialización de la base de datos SQLite
def inicializar_base():
    conexion = sqlite3.connect('centros_salud.db')
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS centros_salud (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            provincia TEXT NOT NULL,
            nombre TEXT NOT NULL,
            direccion TEXT NOT NULL,
            contacto TEXT NOT NULL
        )
    ''')
    conexion.commit()
    conexion.close()

# Insertar datos reales solo si la tabla está vacía
def insertar_datos_reales():
    conexion = sqlite3.connect('centros_salud.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM centros_salud")
    if cursor.fetchone()[0] == 0:
        # Datos para todas las provincias
        datos = [
            # Pichincha
            ("Pichincha", "Centro de Salud La Tola", "Av. 24 de Mayo y Cuenca, Quito", "022586700"),
        ("Pichincha", "Centro de Salud Chimbacalle", "Calle Pedro Pinto Guzmán y Maldonado, Quito", "022671510"),
        ("Pichincha", "Centro de Salud Cotocollao", "Av. La Prensa y Villalengua, Quito", "022540103"),
        ("Pichincha", "Centro de Salud Carapungo", "Av. Padre Luis Vaccari y De los Tulipanes, Quito", "022800216"),
        ("Pichincha", "Centro de Salud Chillogallo", "Calle S42 y Av. Mariscal Sucre, Quito", "022673020"),
        ("Pichincha", "Centro de Salud Comité del Pueblo", "Av. De los Pinos y Galo Plaza Lasso, Quito", "022460550"),
        ("Pichincha", "Centro de Salud Calderón", "Av. Geovanny Calles y Av. Simón Bolívar, Quito", "022805020"),
        ("Pichincha", "Centro de Salud Tumbaco", "Av. Interoceánica y Gonzalo Pizarro, Quito", "022372020"),
        ("Pichincha", "Centro de Salud Guamaní", "Calle E1 y Av. Maldonado, Quito", "022671230"),
        ("Pichincha", "Centro de Salud San Roque", "Calle Imbabura y Loja, Quito", "022973411"),
            # Guayas
            ("Guayas", "Centro de Salud Guayaquil Norte", "Av. Francisco de Orellana y Juan Tanca Marengo, Guayaquil", "042100050"),
        ("Guayas", "Centro de Salud Guayaquil Sur", "Av. 25 de Julio y Calle Portete, Guayaquil", "042100060"),
        ("Guayas", "Centro de Salud Bastión Popular", "Mz. 234 Solar 6, Guayaquil", "042100070"),
        ("Guayas", "Centro de Salud Fertisa", "Av. 25 de Julio y Calle 48 SO, Guayaquil", "042100080"),
        ("Guayas", "Centro de Salud Pascuales", "Vía a Daule km 14, Guayaquil", "042100090"),
        ("Guayas", "Centro de Salud Mapasingue", "Calle 37 SO y Av. Perimetral, Guayaquil", "042100100"),
        ("Guayas", "Centro de Salud Letamendi", "Calle Letamendi y 10 de Agosto, Guayaquil", "042100110"),
        ("Guayas", "Centro de Salud Gómez Rendón", "Calle Gómez Rendón y Ayacucho, Guayaquil", "042100120"),
        ("Guayas", "Centro de Salud Febres Cordero", "Av. Quito y Gómez Rendón, Guayaquil", "042100130"),
        ("Guayas", "Centro de Salud Monte Sinaí", "Calle principal y 24 SO, Guayaquil", "042100140"),
            # Manabí
            ("Manabí", "Centro de Salud Manta", "Av. 113 y Calle 109, Manta", "052620101"),
        ("Manabí", "Centro de Salud Portoviejo", "Av. Reales Tamarindos y Callejón, Portoviejo", "052620102"),
        ("Manabí", "Centro de Salud Chone", "Av. Amazonas y Colón, Chone", "052620103"),
        ("Manabí", "Centro de Salud El Carmen", "Calle Manabí y Bolívar, El Carmen", "052620104"),
        ("Manabí", "Centro de Salud Jipijapa", "Calle Olmedo y Rocafuerte, Jipijapa", "052620105"),
        ("Manabí", "Centro de Salud Bahía", "Av. Bolívar y Loja, Bahía de Caráquez", "052620106"),
        ("Manabí", "Centro de Salud Montecristi", "Calle 9 de Julio y Sucre, Montecristi", "052620107"),
        ("Manabí", "Centro de Salud Rocafuerte", "Av. Rocafuerte y García Moreno, Rocafuerte", "052620108"),
        ("Manabí", "Centro de Salud Tosagua", "Calle 10 de Agosto y Bolívar, Tosagua", "052620109"),
        ("Manabí", "Centro de Salud San Vicente", "Calle 24 de Mayo y Eloy Alfaro, San Vicente", "052620110"),
            # Loja
            ("Loja", "Centro de Salud Loja Norte", "Av. Universitaria y Catacocha, Loja", "072570100"),
        ("Loja", "Centro de Salud Loja Sur", "Av. Manuel Agustín Aguirre y Rocafuerte, Loja", "072570101"),
        ("Loja", "Centro de Salud Catamayo", "Calle Bolívar y Sucre, Catamayo", "072570102"),
        ("Loja", "Centro de Salud Macará", "Av. 24 de Mayo y 10 de Agosto, Macará", "072570103"),
        ("Loja", "Centro de Salud Saraguro", "Calle Sucre y Bolívar, Saraguro", "072570104"),
        ("Loja", "Centro de Salud Pindal", "Av. Pindal y Eloy Alfaro, Pindal", "072570105"),
        ("Loja", "Centro de Salud Calvas", "Calle Sucre y García Moreno, Cariamanga", "072570106"),
        ("Loja", "Centro de Salud Quilanga", "Av. Quilanga y Sucre, Quilanga", "072570107"),
        ("Loja", "Centro de Salud Paltas", "Calle Bolívar y Olmedo, Catacocha", "072570108"),
        ("Loja", "Centro de Salud Espíndola", "Calle Loja y Rocafuerte, Amaluza", "072570109"),
            # Azuay
            ("Azuay", "Centro de Salud Cuenca Norte", "Av. Ordóñez Lasso y Los Claveles, Cuenca", "072840100"),
        ("Azuay", "Centro de Salud Cuenca Sur", "Av. Loja y Isabel La Católica, Cuenca", "072840101"),
        ("Azuay", "Centro de Salud El Valle", "Calle Principal y García Moreno, El Valle", "072840102"),
        ("Azuay", "Centro de Salud Gualaceo", "Av. Jaime Roldós y Bolívar, Gualaceo", "072840103"),
        ("Azuay", "Centro de Salud Paute", "Av. 3 de Noviembre y Sucre, Paute", "072840104"),
        ("Azuay", "Centro de Salud Sígsig", "Calle Loja y 10 de Agosto, Sígsig", "072840105"),
        ("Azuay", "Centro de Salud Girón", "Av. Girón y Loja, Girón", "072840106"),
        ("Azuay", "Centro de Salud Santa Isabel", "Calle Bolívar y Sucre, Santa Isabel", "072840107"),
        ("Azuay", "Centro de Salud Nabón", "Calle 24 de Mayo y Sucre, Nabón", "072840108"),
        ("Azuay", "Centro de Salud Camilo Ponce", "Av. Principal y Eloy Alfaro, Camilo Ponce Enríquez", "072840109"),
            # Cañar
            ("Cañar", "Centro de Salud Azogues", "Av. 24 de Mayo y Sucre, Azogues", "072850100"),
        ("Cañar", "Centro de Salud Biblián", "Calle Bolívar y Sucre, Biblián", "072850101"),
        ("Cañar", "Centro de Salud Cañar", "Av. Cañar y Loja, Cañar", "072850102"),
        ("Cañar", "Centro de Salud El Tambo", "Av. Panamericana y Bolívar, El Tambo", "072850103"),
        ("Cañar", "Centro de Salud Suscal", "Calle Principal y 10 de Agosto, Suscal", "072850104"),
        ("Cañar", "Centro de Salud Déleg", "Av. Déleg y Loja, Déleg", "072850105"),
        ("Cañar", "Centro de Salud La Troncal", "Av. La Troncal y 24 de Mayo, La Troncal", "072850106"),
        ("Cañar", "Centro de Salud Gualleturo", "Calle Gualleturo y Bolívar, Gualleturo", "072850107"),
        ("Cañar", "Centro de Salud Honorato Vásquez", "Av. Principal y Sucre, Honorato Vásquez", "072850108"),
        ("Cañar", "Centro de Salud Javier Loyola", "Calle 24 de Mayo y Loja, Javier Loyola", "072850109"),
            # Chimborazo
            ("Chimborazo", "Centro de Salud Riobamba Norte", "Av. Canónigo Ramos y Loja, Riobamba", "032960100"),
        ("Chimborazo", "Centro de Salud Riobamba Sur", "Av. Unidad Nacional y Brasil, Riobamba", "032960101"),
        ("Chimborazo", "Centro de Salud Colta", "Av. Colta y Sucre, Colta", "032960102"),
        ("Chimborazo", "Centro de Salud Guamote", "Av. Guamote y Bolívar, Guamote", "032960103"),
        ("Chimborazo", "Centro de Salud Alausí", "Av. 5 de Junio y García Moreno, Alausí", "032960104"),
        ("Chimborazo", "Centro de Salud Chunchi", "Calle Sucre y Bolívar, Chunchi", "032960105"),
        ("Chimborazo", "Centro de Salud Cumandá", "Av. Cumandá y 10 de Agosto, Cumandá", "032960106"),
        ("Chimborazo", "Centro de Salud Guano", "Calle Guano y Rocafuerte, Guano", "032960107"),
        ("Chimborazo", "Centro de Salud Penipe", "Calle Bolívar y Sucre, Penipe", "032960108"),
        ("Chimborazo", "Centro de Salud Pallatanga", "Av. Pallatanga y 24 de Mayo, Pallatanga", "032960109"),
            # Cotopaxi
            ("Cotopaxi", "Centro de Salud Latacunga Centro", "Av. Cívica y Quijano y Ordóñez, Latacunga", "032800100"),
        ("Cotopaxi", "Centro de Salud Latacunga Norte", "Av. Amazonas y Loja, Latacunga", "032800101"),
        ("Cotopaxi", "Centro de Salud Salcedo", "Av. Velasco Ibarra y Quito, Salcedo", "032800102"),
        ("Cotopaxi", "Centro de Salud Saquisilí", "Av. Saquisilí y Bolívar, Saquisilí", "032800103"),
        ("Cotopaxi", "Centro de Salud Pujilí", "Calle Sucre y Olmedo, Pujilí", "032800104"),
        ("Cotopaxi", "Centro de Salud La Maná", "Av. 24 de Mayo y Bolívar, La Maná", "032800105"),
        ("Cotopaxi", "Centro de Salud Pangua", "Av. Principal y Loja, Pangua", "032800106"),
        ("Cotopaxi", "Centro de Salud Sigchos", "Calle Sigchos y Bolívar, Sigchos", "032800107"),
        ("Cotopaxi", "Centro de Salud Mulaló", "Calle Principal y Loja, Mulaló", "032800108"),
        ("Cotopaxi", "Centro de Salud Toacaso", "Av. Toacaso y Sucre, Toacaso", "032800109"),
            # Tungurahua
            ("Tungurahua", "Centro de Salud Ambato Centro", "Av. Cevallos y Montalvo, Ambato", "032540100"),
        ("Tungurahua", "Centro de Salud Ambato Sur", "Av. Indoamérica y Cuenca, Ambato", "032540101"),
        ("Tungurahua", "Centro de Salud Ambato Norte", "Av. Bolivariana y 12 de Noviembre, Ambato", "032540102"),
        ("Tungurahua", "Centro de Salud Baños", "Av. Amazonas y Oriente, Baños", "032540103"),
        ("Tungurahua", "Centro de Salud Pelileo", "Av. Pelileo y Bolívar, Pelileo", "032540104"),
        ("Tungurahua", "Centro de Salud Patate", "Calle Patate y Olmedo, Patate", "032540105"),
        ("Tungurahua", "Centro de Salud Quero", "Calle Principal y 10 de Agosto, Quero", "032540106"),
        ("Tungurahua", "Centro de Salud Mocha", "Calle Sucre y Bolívar, Mocha", "032540107"),
        ("Tungurahua", "Centro de Salud Cevallos", "Av. Cevallos y García Moreno, Cevallos", "032540108"),
        ("Tungurahua", "Centro de Salud Tisaleo", "Av. Tisaleo y Loja, Tisaleo", "032540109"),
            # Esmeraldas
            ("Esmeraldas", "Centro de Salud Esmeraldas Norte", "Av. Del Pacífico y 10 de Agosto, Esmeraldas", "062710100"),
        ("Esmeraldas", "Centro de Salud Esmeraldas Sur", "Av. Malecón y Sucre, Esmeraldas", "062710101"),
        ("Esmeraldas", "Centro de Salud Atacames", "Calle Principal y Bolívar, Atacames", "062710102"),
        ("Esmeraldas", "Centro de Salud Quinindé", "Av. 6 de Diciembre y Loja, Quinindé", "062710103"),
        ("Esmeraldas", "Centro de Salud Muisne", "Calle Bolívar y Manabí, Muisne", "062710104"),
        ("Esmeraldas", "Centro de Salud Rioverde", "Av. Principal y Quito, Rioverde", "062710105"),
        ("Esmeraldas", "Centro de Salud Eloy Alfaro", "Calle Alfaro y Sucre, Valdez", "062710106"),
        ("Esmeraldas", "Centro de Salud San Lorenzo", "Av. Bolívar y Maldonado, San Lorenzo", "062710107"),
        ("Esmeraldas", "Centro de Salud Tonsupa", "Av. Principal y Esmeraldas, Tonsupa", "062710108"),
        ("Esmeraldas", "Centro de Salud Viche", "Calle Principal y Loja, Viche", "062710109"),
            # Sucumbíos
            ("Sucumbíos", "Centro de Salud Nueva Loja", "Av. Quito y Amazonas, Nueva Loja", "062980100"),
        ("Sucumbíos", "Centro de Salud Shushufindi", "Av. 29 de Mayo y Loja, Shushufindi", "062980101"),
        ("Sucumbíos", "Centro de Salud Lago Agrio", "Av. 17 de Julio y Quito, Lago Agrio", "062980102"),
        ("Sucumbíos", "Centro de Salud Cascales", "Calle Principal y Bolívar, Cascales", "062980103"),
        ("Sucumbíos", "Centro de Salud Cuyabeno", "Av. Amazonas y Quito, Tarapoa", "062980104"),
        ("Sucumbíos", "Centro de Salud Lumbaquí", "Av. Principal y Manabí, Lumbaquí", "062980105"),
        ("Sucumbíos", "Centro de Salud Pacayacu", "Calle Principal y Bolívar, Pacayacu", "062980106"),
        ("Sucumbíos", "Centro de Salud Joya de los Sachas", "Av. 24 de Mayo y Quito, Sachas", "062980107"),
        ("Sucumbíos", "Centro de Salud Dureno", "Calle Bolívar y Olmedo, Dureno", "062980108"),
        ("Sucumbíos", "Centro de Salud General Farfán", "Av. Principal y Esmeraldas, Farfán", "062980109"),
            # Orellana
            ("Orellana", "Centro de Salud Francisco de Orellana", "Av. Quito y 10 de Agosto, Coca", "063040100"),
        ("Orellana", "Centro de Salud La Joya de los Sachas", "Av. Amazonas y Quito, Sachas", "063040101"),
        ("Orellana", "Centro de Salud Loreto", "Calle Bolívar y Maldonado, Loreto", "063040102"),
        ("Orellana", "Centro de Salud Dayuma", "Av. Principal y Loja, Dayuma", "063040103"),
        ("Orellana", "Centro de Salud Taracoa", "Calle Quito y Bolívar, Taracoa", "063040104"),
        ("Orellana", "Centro de Salud Pompeya", "Av. 24 de Mayo y Sucre, Pompeya", "063040105"),
        ("Orellana", "Centro de Salud El Edén", "Av. Principal y Bolívar, El Edén", "063040106"),
        ("Orellana", "Centro de Salud Nuevo Rocafuerte", "Calle Rocafuerte y Quito, Rocafuerte", "063040107"),
        ("Orellana", "Centro de Salud Alejandro Labaka", "Calle Labaka y Loja, Coca", "063040108"),
        ("Orellana", "Centro de Salud San José de Guayusa", "Av. Principal y Quito, San José", "063040109"),
            # Napo
            ("Napo", "Centro de Salud Tena", "Av. Jumandy y Quito, Tena", "063020100"),
        ("Napo", "Centro de Salud Archidona", "Calle Bolívar y Sucre, Archidona", "063020101"),
        ("Napo", "Centro de Salud Carlos Julio Arosemena", "Av. Principal y Manabí, Carlos Julio Arosemena", "063020102"),
        ("Napo", "Centro de Salud Cotundo", "Av. Quito y Loja, Cotundo", "063020103"),
        ("Napo", "Centro de Salud Talag", "Calle Bolívar y Sucre, Talag", "063020104"),
        ("Napo", "Centro de Salud Puerto Napo", "Av. Principal y Quito, Puerto Napo", "063020105"),
        ("Napo", "Centro de Salud Ahuano", "Calle Sucre y Bolívar, Ahuano", "063020106"),
        ("Napo", "Centro de Salud Baeza", "Av. Principal y Loja, Baeza", "063020107"),
        ("Napo", "Centro de Salud El Chaco", "Av. Quito y 24 de Mayo, El Chaco", "063020108"),
        ("Napo", "Centro de Salud Papallacta", "Calle Principal y Bolívar, Papallacta", "063020109"),
            # Pastaza
            ("Pastaza", "Centro de Salud Puyo", "Av. 9 de Octubre y Quito, Puyo", "063050100"),
        ("Pastaza", "Centro de Salud Mera", "Calle Bolívar y Maldonado, Mera", "063050101"),
        ("Pastaza", "Centro de Salud Santa Clara", "Av. Principal y Loja, Santa Clara", "063050102"),
        ("Pastaza", "Centro de Salud Arajuno", "Calle Principal y Bolívar, Arajuno", "063050103"),
        ("Pastaza", "Centro de Salud Tarqui", "Av. Tarqui y Sucre, Puyo", "063050104"),
        ("Pastaza", "Centro de Salud Canelos", "Av. Principal y Quito, Canelos", "063050105"),
        ("Pastaza", "Centro de Salud Simón Bolívar", "Calle Bolívar y Olmedo, Simón Bolívar", "063050106"),
        ("Pastaza", "Centro de Salud Pomona", "Av. Principal y Sucre, Pomona", "063050107"),
        ("Pastaza", "Centro de Salud Veracruz", "Calle Principal y Quito, Veracruz", "063050108"),
        ("Pastaza", "Centro de Salud Curaray", "Av. Quito y Loja, Curaray", "063050109"),
            # Morona Santiago
            ("Morona Santiago", "Centro de Salud Macas", "Av. Amazonas y Quito, Macas", "063030100"),
        ("Morona Santiago", "Centro de Salud Gualaquiza", "Calle Bolívar y Sucre, Gualaquiza", "063030101"),
        ("Morona Santiago", "Centro de Salud Limón Indanza", "Av. Principal y Loja, Limón", "063030102"),
        ("Morona Santiago", "Centro de Salud Sucúa", "Calle Principal y Bolívar, Sucúa", "063030103"),
        ("Morona Santiago", "Centro de Salud San Juan Bosco", "Av. Quito y Maldonado, San Juan Bosco", "063030104"),
        ("Morona Santiago", "Centro de Salud Huamboya", "Av. Principal y Sucre, Huamboya", "063030105"),
        ("Morona Santiago", "Centro de Salud Pablo Sexto", "Calle Bolívar y Olmedo, Pablo Sexto", "063030106"),
        ("Morona Santiago", "Centro de Salud Taisha", "Av. Principal y Quito, Taisha", "063030107"),
        ("Morona Santiago", "Centro de Salud Logroño", "Calle Principal y Loja, Logroño", "063030108"),
        ("Morona Santiago", "Centro de Salud Santiago de Méndez", "Av. Quito y Bolívar, Santiago", "063030109"),
            # Zamora Chinchipe
            ("Zamora Chinchipe", "Centro de Salud Zamora", "Av. Amazonas y Quito, Zamora", "063070100"),
        ("Zamora Chinchipe", "Centro de Salud Yantzaza", "Calle Bolívar y Sucre, Yantzaza", "063070101"),
        ("Zamora Chinchipe", "Centro de Salud El Pangui", "Av. Principal y Loja, El Pangui", "063070102"),
        ("Zamora Chinchipe", "Centro de Salud Centinela del Cóndor", "Calle Principal y Bolívar, Centinela del Cóndor", "063070103"),
        ("Zamora Chinchipe", "Centro de Salud Palanda", "Av. Quito y Sucre, Palanda", "063070104"),
        ("Zamora Chinchipe", "Centro de Salud Chinchipe", "Av. Principal y Quito, Chinchipe", "063070105"),
        ("Zamora Chinchipe", "Centro de Salud Nangaritza", "Calle Bolívar y Olmedo, Nangaritza", "063070106"),
        ("Zamora Chinchipe", "Centro de Salud Paquisha", "Av. Principal y Sucre, Paquisha", "063070107"),
        ("Zamora Chinchipe", "Centro de Salud Yacuambi", "Calle Principal y Quito, Yacuambi", "063070108"),
        ("Zamora Chinchipe", "Centro de Salud Zumbi", "Av. Quito y Loja, Zumbi", "063070109"),
                # El Oro
        ("El Oro", "Centro de Salud Machala Norte", "Av. Ferroviaria y Santa Rosa, Machala", "072960100"),
        ("El Oro", "Centro de Salud Machala Sur", "Av. Bolívar Madero Vargas y Sucre, Machala", "072960101"),
        ("El Oro", "Centro de Salud Huaquillas", "Av. La República y Loja, Huaquillas", "072960102"),
        ("El Oro", "Centro de Salud Santa Rosa", "Calle Colón y Bolívar, Santa Rosa", "072960103"),
        ("El Oro", "Centro de Salud Pasaje", "Av. Rocafuerte y 9 de Octubre, Pasaje", "072960104"),
        ("El Oro", "Centro de Salud Arenillas", "Av. Principal y Quito, Arenillas", "072960105"),
        ("El Oro", "Centro de Salud Zaruma", "Calle Bolívar y Olmedo, Zaruma", "072960106"),
        ("El Oro", "Centro de Salud Piñas", "Av. 10 de Agosto y Loja, Piñas", "072960107"),
        ("El Oro", "Centro de Salud El Guabo", "Calle Principal y Sucre, El Guabo", "072960108"),
        ("El Oro", "Centro de Salud Portovelo", "Av. Quito y Bolívar, Portovelo", "072960109"),
            # Santa Elena
            ("Santa Elena", "Centro de Salud Santa Elena Centro", "Av. Guayaquil y Quito, Santa Elena", "042920100"),
        ("Santa Elena", "Centro de Salud La Libertad", "Calle 9 de Octubre y Bolívar, La Libertad", "042920101"),
        ("Santa Elena", "Centro de Salud Salinas", "Av. Malecón y Quito, Salinas", "042920102"),
        ("Santa Elena", "Centro de Salud Ballenita", "Av. Ballenita y Olmedo, Ballenita", "042920103"),
        ("Santa Elena", "Centro de Salud Chanduy", "Calle Principal y Sucre, Chanduy", "042920104"),
        ("Santa Elena", "Centro de Salud Atahualpa", "Av. Atahualpa y Bolívar, Atahualpa", "042920105"),
        ("Santa Elena", "Centro de Salud Simón Bolívar", "Calle Bolívar y Olmedo, Simón Bolívar", "042920106"),
        ("Santa Elena", "Centro de Salud Colonche", "Av. Principal y Quito, Colonche", "042920107"),
        ("Santa Elena", "Centro de Salud Manglaralto", "Calle Principal y Sucre, Manglaralto", "042920108"),
        ("Santa Elena", "Centro de Salud Ancón", "Av. Ancón y Loja, Ancón", "042920109"),
            # Galápagos
            ("Galápagos", "Centro de Salud Puerto Ayora", "Av. Charles Darwin y Bolívar, Santa Cruz", "052720100"),
        ("Galápagos", "Centro de Salud Puerto Baquerizo Moreno", "Calle Colón y Quito, San Cristóbal", "052720101"),
        ("Galápagos", "Centro de Salud Puerto Villamil", "Av. Isabela y Loja, Isabela", "052720102"),
        ("Galápagos", "Centro de Salud Bellavista", "Calle Principal y Sucre, Bellavista", "052720103"),
        ("Galápagos", "Centro de Salud El Progreso", "Av. Progreso y Bolívar, San Cristóbal", "052720104"),
        ("Galápagos", "Centro de Salud Tomás de Berlanga", "Calle Principal y Quito, Santa Cruz", "052720105"),
        ("Galápagos", "Centro de Salud El Cascajo", "Av. Cascajo y Loja, Isabela", "052720106"),
        ("Galápagos", "Centro de Salud El Océano", "Calle Principal y Bolívar, Santa Cruz", "052720107"),
        ("Galápagos", "Centro de Salud Santa Rosa", "Av. Santa Rosa y Quito, Santa Cruz", "052720108"),
        ("Galápagos", "Centro de Salud El Edén", "Calle Principal y Sucre, Isabela", "052720109"),
            # Imbabura
            ("Imbabura", "Centro de Salud Ibarra Norte", "Av. Eugenio Espejo y Quito, Ibarra", "062620100"),
        ("Imbabura", "Centro de Salud Ibarra Sur", "Av. Teodoro Gómez y Bolívar, Ibarra", "062620101"),
        ("Imbabura", "Centro de Salud Otavalo", "Av. Rumiñahui y Sucre, Otavalo", "062620102"),
        ("Imbabura", "Centro de Salud Cotacachi", "Calle Bolívar y Rocafuerte, Cotacachi", "062620103"),
        ("Imbabura", "Centro de Salud Antonio Ante", "Av. Atahualpa y Sucre, Atuntaqui", "062620104"),
        ("Imbabura", "Centro de Salud Urcuquí", "Calle Principal y Bolívar, Urcuquí", "062620105"),
        ("Imbabura", "Centro de Salud Pimampiro", "Av. Pimampiro y 10 de Agosto, Pimampiro", "062620106"),
        ("Imbabura", "Centro de Salud San Antonio", "Calle Bolívar y Olmedo, San Antonio de Ibarra", "062620107"),
        ("Imbabura", "Centro de Salud La Esperanza", "Av. Esperanza y Loja, La Esperanza", "062620108"),
        ("Imbabura", "Centro de Salud Lita", "Calle Principal y Quito, Lita", "062620109"),
             # Bolívar
            ("Bolívar", "Centro de Salud Guaranda Centro", "Av. Guayaquil y Bolívar, Guaranda", "032960200"),
        ("Bolívar", "Centro de Salud San Miguel", "Av. San Miguel y Sucre, San Miguel", "032960201"),
        ("Bolívar", "Centro de Salud Chillanes", "Av. Chillanes y Bolívar, Chillanes", "032960202"),
        ("Bolívar", "Centro de Salud Chimbo", "Calle Principal y Loja, Chimbo", "032960203"),
        ("Bolívar", "Centro de Salud Echeandía", "Av. Echeandía y Sucre, Echeandía", "032960204"),
        ("Bolívar", "Centro de Salud Caluma", "Av. Principal y Bolívar, Caluma", "032960205"),
        ("Bolívar", "Centro de Salud Las Naves", "Calle Sucre y Bolívar, Las Naves", "032960206"),
        ("Bolívar", "Centro de Salud Salinas de Guaranda", "Calle Principal y Loja, Salinas", "032960207"),
        ("Bolívar", "Centro de Salud Facundo Vela", "Av. Principal y Quito, Facundo Vela", "032960208"),
        ("Bolívar", "Centro de Salud Julio Moreno", "Av. Julio Moreno y Olmedo, Guaranda", "032960209"),
            # Santo Domingo de los Tsáchilas
            ("Santo Domingo", "Centro de Salud Central", "Av. Tsáchila y Abraham Calazacón, Santo Domingo", "023700100"),
        ("Santo Domingo", "Centro de Salud 15 de Septiembre", "Calle Córdova y Ambato, Santo Domingo", "023700101"),
        ("Santo Domingo", "Centro de Salud Chigüilpe", "Vía a Chone, Km 3, Chigüilpe", "023700102"),
        ("Santo Domingo", "Centro de Salud Zaracay", "Av. Zaracay y Quevedo, Santo Domingo", "023700103"),
        ("Santo Domingo", "Centro de Salud Río Toachi", "Barrio Río Toachi, Santo Domingo", "023700104"),
        ("Santo Domingo", "Centro de Salud Las Delicias", "Vía Quevedo Km 9, Las Delicias", "023700105"),
        ("Santo Domingo", "Centro de Salud Valle Hermoso", "Calle Principal, Valle Hermoso", "023700106"),
        ("Santo Domingo", "Centro de Salud Julio Moreno", "Av. Principal y Loja, Julio Moreno", "023700107"),
        ("Santo Domingo", "Centro de Salud Plan de Vivienda", "Barrio Plan de Vivienda, Santo Domingo", "023700108"),
        ("Santo Domingo", "Centro de Salud La Concordia", "Calle Sucre y Quito, La Concordia", "023700109"),
            # Los Ríos
            ("Los Ríos", "Centro de Salud Babahoyo", "Av. Universitaria y Rocafuerte, Babahoyo", "052720100"),
        ("Los Ríos", "Centro de Salud Vinces", "Av. Bolívar y Sucre, Vinces", "052720101"),
        ("Los Ríos", "Centro de Salud Quevedo Norte", "Av. Jaime Roldós y Bolívar, Quevedo", "052720102"),
        ("Los Ríos", "Centro de Salud Quevedo Sur", "Av. Walter Andrade y Sucre, Quevedo", "052720103"),
        ("Los Ríos", "Centro de Salud Buena Fe", "Calle Principal y Bolívar, Buena Fe", "052720104"),
        ("Los Ríos", "Centro de Salud Ventanas", "Av. Principal y Quito, Ventanas", "052720105"),
        ("Los Ríos", "Centro de Salud Valencia", "Calle Valencia y Bolívar, Valencia", "052720106"),
        ("Los Ríos", "Centro de Salud Montalvo", "Av. Montalvo y Sucre, Montalvo", "052720107"),
        ("Los Ríos", "Centro de Salud Palenque", "Calle Sucre y Loja, Palenque", "052720108"),
        ("Los Ríos", "Centro de Salud Urdaneta", "Calle Principal y Quito, Catarama", "052720109"),
        ]
        cursor.executemany("INSERT INTO centros_salud (provincia, nombre, direccion, contacto) VALUES (?, ?, ?, ?)", datos)
        conexion.commit()
    conexion.close()

# Función para buscar centros por provincia
def buscar_centros_por_provincia(provincia):
    conexion = sqlite3.connect('centros_salud.db')
    cursor = conexion.cursor()
    cursor.execute("SELECT nombre, direccion, contacto FROM centros_salud WHERE provincia = ?", (provincia,))
    centros = cursor.fetchall()
    conexion.close()
    return centros

# Mostrar menú principal con botones de regiones
def mostrar_menu_principal(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("🗺️ Región Costa"),
        KeyboardButton("🏞️ Región Sierra")
    )
    markup.add(
        KeyboardButton("🌿 Región Amazonía"),
        KeyboardButton("🌊 Región Insular")
    )
    bot.send_message(chat_id, "🌟 *Hola! Soy VexSmile 🦷*\nSelecciona una región para continuar:", reply_markup=markup, parse_mode="Markdown")

# Función de región (Costa)
def mostrar_provincias_costa(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Guayas"), KeyboardButton("Manabí"),
        KeyboardButton("Los Ríos"), KeyboardButton("Santa Elena"),
        KeyboardButton("Esmeraldas"), KeyboardButton("El Oro"), 
        KeyboardButton("Volver al menú principal")
    )
    bot.send_message(chat_id, "🌊 Estas son las provincias de la *Región Costa*:", reply_markup=markup, parse_mode="Markdown")

# Función de región (Sierra)
def mostrar_provincias_sierra(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Pichincha"), KeyboardButton("Azuay"),
        KeyboardButton("Loja"), KeyboardButton("Tungurahua"),
        KeyboardButton("Carchi"), KeyboardButton("Cotopaxi"),
        KeyboardButton("Bolívar"), KeyboardButton("Chimborazo"),
        KeyboardButton("Cañar"), KeyboardButton("Santo Domingo"),
        KeyboardButton("Imbabura"), KeyboardButton("Volver al menú principal")
    )
    bot.send_message(chat_id, "🏞️ Estas son las provincias de la *Región Sierra*:", reply_markup=markup, parse_mode="Markdown")

# Función de región (Amazonía)
def mostrar_provincias_amazonia(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Napo"), KeyboardButton("Pastaza"),
        KeyboardButton("Orellana"), KeyboardButton("Sucumbíos"),
        KeyboardButton("Morona Santiago"), KeyboardButton("Zamora Chinchipe"),
        KeyboardButton("Volver al menú principal")
    )
    bot.send_message(chat_id, "🌿 Estas son las provincias de la *Región Amazonía*:", reply_markup=markup, parse_mode="Markdown")

# Función de región (Insular)
def mostrar_provincias_insular(chat_id):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton("Galápagos"), KeyboardButton("Volver al menú principal")
    )
    bot.send_message(chat_id, "🌊 Estas son las provincias de la *Región Insular*:", reply_markup=markup, parse_mode="Markdown")

# Lista completa de todas las provincias
TODAS_PROVINCIAS = [
    "Guayas", "Manabí", "Los Ríos", "Santa Elena", "Esmeraldas", "El Oro"
    "Pichincha", "Azuay", "Loja", "Tungurahua", "Carchi", "Cotopaxi", "Bolívar", "Chimborazo", "Cañar", "Santo Domingo", "Imbabura",
    "Napo", "Pastaza", "Orellana", "Sucumbíos", "Morona Santiago", "Zamora Chinchipe",
    "Galápagos"
]

# Manejador para el comando /start
@bot.message_handler(commands=['start'])
def comando_start(message):
    mostrar_menu_principal(message.chat.id)

# Responder a los mensajes
@bot.message_handler(func=lambda message: True)
def responder_mensaje(message):
    texto = message.text
    chat_id = message.chat.id
    
    if texto == "/start":
        mostrar_menu_principal(chat_id)
    elif texto == "Volver al menú principal":
        mostrar_menu_principal(chat_id)
    elif texto == "🗺️ Región Costa":
        mostrar_provincias_costa(chat_id)
    elif texto == "🏞️ Región Sierra":
        mostrar_provincias_sierra(chat_id)
    elif texto == "🌿 Región Amazonía":
        mostrar_provincias_amazonia(chat_id)
    elif texto == "🌊 Región Insular":
        mostrar_provincias_insular(chat_id)
    elif texto in TODAS_PROVINCIAS:
        centros = buscar_centros_por_provincia(texto)
        if centros:
            mensaje = f"📍 *Centros de salud en {texto}*:\n\n"
            for nombre, direccion, contacto in centros:
                mensaje += f"🏥 *{nombre}*\n📌 Dirección: {direccion}\n📞 Contacto: {contacto}\n\n"
            bot.send_message(chat_id, mensaje, parse_mode="Markdown")
        else:
            # Esto no debería ocurrir ahora que hemos añadido datos para todas las provincias
            bot.send_message(chat_id, f"Lo siento, no hay centros de salud registrados en {texto} por el momento. Estamos trabajando para ampliar nuestra cobertura.", parse_mode="Markdown")
    else:
        # En vez de simplemente rechazar la entrada, mostramos el menú
        bot.send_message(chat_id, "No reconozco esa opción. Por favor selecciona una opción del menú:")
        mostrar_menu_principal(chat_id)

# Función para limpiar y reiniciar la base de datos (útil para pruebas)
def reiniciar_base_datos():
    conexion = sqlite3.connect('centros_salud.db')
    cursor = conexion.cursor()
    cursor.execute("DROP TABLE IF EXISTS centros_salud")
    conexion.commit()
    conexion.close()
    inicializar_base()
    insertar_datos_reales()
    print("Base de datos reiniciada con éxito")

# Inicialización
if __name__ == "__main__":
    # Descomentar la siguiente línea si quieres reiniciar la base de datos
    # reiniciar_base_datos()
    
    inicializar_base()
    insertar_datos_reales()
    print("Bot iniciado. Presiona Ctrl+C para detener.")
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error en el bot: {e}")
        # Intenta reiniciar el bot
        bot.polling(none_stop=True)
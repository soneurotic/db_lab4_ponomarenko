import psycopg2
import matplotlib.pyplot as plt
from textwrap import wrap

username = 'postgres'
password = 'postgres'
database = 'lab_3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT has.character_name, weapon.max_atk FROM has
LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name
'''
query_2 = '''
SELECT weapon_type, COUNT(weapon_type) FROM is_at 
	LEFT JOIN character ON is_at.character_name = character.character_name
	LEFT JOIN has ON character.character_name = has.character_name
		WHERE is_at.level > 40
			GROUP BY weapon_type
'''

query_3 = '''
SELECT is_at.character_name, is_at.base_atk, weapon.max_atk FROM is_at 
	LEFT JOIN character ON is_at.character_name = character.character_name
	LEFT JOIN has ON character.character_name = has.character_name
	LEFT JOIN weapon ON has.weapon_name = weapon.weapon_name
		ORDER BY base_atk + max_atk
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    print("Database opened successfully")
    cur = conn.cursor()

    # # Запит 1
    # cur.execute(query_1)
    # characters = []
    # atk = []
    #
    # for row in cur:
    #     characters.append(row[0])
    #     atk.append(row[1])
    # x_range = range(len(characters))

    # plt.bar(x_range, atk, width=0.5)
    # plt.title('Максимальна атака зброї, якою споряджені персонажі')
    # plt.xlabel('Персонажі')
    # plt.xticks(x_range, characters)
    # plt.ylabel('Атака, од.')
    # plt.show()

    # Запит 2
    # cur.execute(query_2)
    #
    # weapon_type = []
    # freq = []
    #
    # for row in cur:
    #     weapon_type.append(row[0])
    #     freq.append(row[1])
    #
    # plt.pie(freq, labels=weapon_type, autopct='%1.1f%%')
    # plt.title("\n".join(wrap('Частка використання зброї, що припадає на кожен тип зброї '
    #                          'використовуваний персонажами, що мають рівень вище 40', 60)))
    # plt.show()

    # Запит 3
    # cur.execute(query_3)
    # char_names = []
    # base_max = []
    #
    # for row in cur:
    #     char_names.append(row[0])
    #     base_max.append((row[1], row[2]))
    #
    # plt.plot(char_base:=[el[0] for el in base_max], max_atk:=[el[1] for el in base_max], marker='o', linestyle='-', color='b')
    # plt.xlabel('base_atk')
    # plt.ylabel('max_atk')
    # plt.title('Базова атака персонажа + максимальна атака зброї')
    #
    # for name, val in zip(char_names, base_max):
    #     plt.annotate(name, val, textcoords="offset points", xytext=(0, 5), ha='center')
    #
    # plt.show()
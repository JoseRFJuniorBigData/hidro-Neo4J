import csv

input_csv_path = r"D:\PROJECTS\hidro-Neo4J\siga-empreendimentos-geracao.csv"
output_cypher_path = r"D:\PROJECTS\hidro-Neo4J\siga-empreendimentos-geracao_saida2.cypher"

with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_csv:
    csvreader = csv.reader(input_csv, delimiter=',')
    headers = next(csvreader)

    with open(output_cypher_path, 'w', newline='', encoding='utf-8') as output_cypher:
        output_cypher.write(":begin\n")

        for row in csvreader:
            labels = headers[0].split(".")
            create_command = f"CREATE (n:{':'.join(labels)})"
            properties = []
            for i in range(1, len(headers)):
                properties.append(f"{headers[i]}: '{row[i]}'")
            if properties:
                create_command += " SET " + ", ".join(properties)
            output_cypher.write(create_command + ";\n")

        output_cypher.write(":commit\n")

print("Conversão concluída!")

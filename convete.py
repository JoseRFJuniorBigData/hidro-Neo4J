import csv

input_csv_path = "D:\PROJECTS\hidro-Neo4J\siga-empreendimentos-geracao.csv"
output_csv_path = "D:\PROJECTS\hidro-Neo4J\siga-empreendimentos-geracao_saida2.csv"

# Abrir o arquivo de entrada CSV
with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_csv:
    csvreader = csv.reader(input_csv, delimiter=';')
    headers = next(csvreader)  # Lê a primeira linha (cabeçalho)

    # Criar o arquivo de saída CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        csvwriter = csv.writer(output_csv, delimiter=';')
        csvwriter.writerow(["query"])  # Escreve o cabeçalho no arquivo de saída

        # Processar cada linha do CSV de entrada
        for row in csvreader:
            labels = headers[0].split(":")
            create_command = f"CREATE (n:{':'.join(labels)})"
            properties = []
            for i in range(1, len(headers)):
                properties.append(f"{headers[i]}: '{row[i]}'")
            if properties:
                create_command += " SET " + ", ".join(properties)
            csvwriter.writerow([create_command])  # Escreve o comando CREATE no arquivo de saída

print("Conversão concluída!")

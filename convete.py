import csv

input_csv_path = "caminho/para/seu/arquivo.csv"
output_csv_path = "caminho/para/saida.csv"

# Abrir o arquivo de entrada CSV
with open(input_csv_path, 'r', newline='', encoding='utf-8') as input_csv:
    csvreader = csv.reader(input_csv, delimiter=';')
    headers = next(csvreader)  # Lê a primeira linha (cabeçalho)

    # Criar o arquivo de saída CSV
    with open(output_csv_path, 'w', newline='', encoding='utf-8') as output_csv:
        csvwriter = csv.writer(output_csv, delimiter=';')
        csvwriter.writerow(headers)  # Escreve o cabeçalho no arquivo de saída

        # Processar cada linha do CSV de entrada
        for row in csvreader:
            create_command = f"CREATE (:{headers[0]} {{"
            for i in range(1, len(headers)):
                create_command += f"{headers[i]}: '{row[i]}'"
                if i < len(headers) - 1:
                    create_command += ", "
            create_command += "})"

            csvwriter.writerow([create_command])  # Escreve o comando CREATE no arquivo de saída

print("Conversão concluída!")

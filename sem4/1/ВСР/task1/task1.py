# Программа берет данные их json и сохраняет их в csv


def main():
    json_name = 'MOCK_DATA.json'
    csv_name = 'csv_data.csv'
    # Синтаксис исключений
    try:
        import json
        # Использование менеджера контекста
        with open(json_name, 'r') as js_file:
            js_dicts = json.loads(''.join(js_file.readlines()))
    except (ImportError, FileNotFoundError) as errors:
        print(errors)

    try:
        import csv
        with open(csv_name, 'w') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(js_dicts[0].keys())
            for dict_item in js_dicts:
                csv_writer.writerow(dict_item.values())
    except (ImportError, FileNotFoundError) as errors:
        print(errors)

    print(js_dicts)

main()
# io_handler.py

def read_graph(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            NV, NE = map(int, file.readline().split())
            file.readline()  # Пропуск пустой строки

            edges = []
            for _ in range(NE):
                u, v = map(int, file.readline().split())
                edges.append((u, v))

            file.readline()  # Пропуск пустой строки

            node_rules = []
            for i in range(NV):
                rule = file.readline().strip().split()
                node_rules.append(rule)

            edge_rules = []
            for i in range(NE):
                rule = file.readline().strip().split()
                edge_rules.append(rule)

    except FileNotFoundError:
        raise Exception("Файл не найден. Проверьте путь к файлу.")
    except ValueError as e:
        raise Exception(f"Ошибка формата файла: {str(e)}. Проверьте количество узлов и рёбер.")
    except Exception as e:
        raise Exception(f"Ошибка при чтении графа: {str(e)}")

    return NV, NE, edges, node_rules, edge_rules

def save_attributes_to_file(output_file, node_attributes, edge_attributes, edges):
    try:
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write("Атрибуты узлов:\n")
            for i, attr in enumerate(node_attributes):
                file.write(f"Узел {i + 1}: {attr}\n")

            file.write("\nАтрибуты рёбер:\n")
            for i, attr in enumerate(edge_attributes):
                u, v = edges[i]
                file.write(f"Ребро {i + 1} (из {u} в {v}): {attr}\n")
    except Exception as e:
        raise Exception(f"Ошибка при сохранении данных в файл: {str(e)}")

# main.py

from io_handler import read_graph, save_attributes_to_file
from graph import Graph

if __name__ == '__main__':
    input_file = 'input.txt'  # Имя файла с входными данными
    output_file = 'output.txt'  # Имя файла для вывода

    try:
        # Чтение графа из файла
        NV, NE, edges, node_rules, edge_rules = read_graph(input_file)

        # Создание графа и вычисление атрибутов
        graph = Graph(NV, NE, edges, node_rules, edge_rules)
        node_attrs, edge_attrs = graph.compute_attributes()

        # Сохранение результата в файл
        save_attributes_to_file(output_file, node_attrs, edge_attrs, edges)

        print("Программа успешно завершена.")
    except Exception as e:
        print(f"Ошибка: {str(e)}")

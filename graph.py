# graph.py

class Graph:
    def __init__(self, NV, NE, edges, node_rules, edge_rules):
        self.NV = NV  # Количество узлов
        self.NE = NE  # Количество рёбер
        self.edges = edges  # Рёбра графа
        self.node_attributes = [None] * NV  # Атрибуты узлов
        self.edge_attributes = [None] * NE  # Атрибуты рёбер
        self.node_rules = node_rules  # Правила для узлов
        self.edge_rules = edge_rules  # Правила для рёбер

    def get_attribute(self, element_type, index, visited):
        current_key = (element_type, index)
        if current_key in visited:
            raise Exception(f"Обнаружено зацикливание при вычислении атрибута {element_type} {index + 1}")

        visited.add(current_key)

        attributes = self.node_attributes if element_type == 'v' else self.edge_attributes
        if attributes[index] is not None:
            visited.remove(current_key)
            return attributes[index]

        rule = self.node_rules[index] if element_type == 'v' else self.edge_rules[index]

        try:
            if len(rule) == 1:
                if rule[0] == 'min' and element_type == 'v':
                    incoming_edges = [i for i, (start, end) in enumerate(self.edges) if end == index + 1]
                    if incoming_edges:
                        attributes[index] = min(self.get_attribute('e', edge_idx, visited) for edge_idx in incoming_edges)
                    else:
                        attributes[index] = float('inf')
                elif rule[0] == '*' and element_type == 'e':
                    start_node = self.edges[index][0] - 1
                    incoming_edges = [i for i, (start, end) in enumerate(self.edges) if end == start_node + 1]
                    left_node_attr = self.get_attribute('v', start_node, visited)
                    edge_product = 1
                    for edge_idx in incoming_edges:
                        edge_product *= self.get_attribute('e', edge_idx, visited)
                    attributes[index] = left_node_attr * edge_product
                else:
                    attributes[index] = float(rule[0])
            elif rule[0] == 'v':
                node_index = int(rule[1]) - 1
                attributes[index] = self.get_attribute('v', node_index, visited)
            elif rule[0] == 'e':
                edge_index = int(rule[1]) - 1
                attributes[index] = self.get_attribute('e', edge_index, visited)
        except Exception as e:
            raise Exception(f"Ошибка при вычислении атрибута {element_type} {index + 1}: {str(e)}")

        visited.remove(current_key)
        return attributes[index]

    def compute_attributes(self):
        visited = set()
        for i in range(self.NV):
            self.get_attribute('v', i, visited)
        for i in range(self.NE):
            self.get_attribute('e', i, visited)

        return self.node_attributes, self.edge_attributes

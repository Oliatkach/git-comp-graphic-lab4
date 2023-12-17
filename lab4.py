import matplotlib.pyplot as plt
from scipy.spatial import Voronoi, voronoi_plot_2d
import numpy as np

# Зчитування датасету з файлу
def read_dataset(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        points = [tuple(map(int, line.split())) for line in lines]
    return np.array(points)

# Знаходження зв'язаних областей та їхніх центрів ваги
def find_connected_regions(points):
    # Ваш код для знаходження зв'язаних областей тут
    # Приклад: розділити точки на дві групи, наприклад, за X-координатою
    group1 = points[points[:, 0] < np.mean(points[:, 0])]
    group2 = points[points[:, 0] >= np.mean(points[:, 0])]
    centers_of_mass = [np.mean(group1, axis=0), np.mean(group2, axis=0)]
    
    return centers_of_mass

# Будування діаграми Вороного
def build_voronoi_diagram(points):
    vor = Voronoi(points)
    return vor

# Відображення результатів
def plot_results(points, centers_of_mass, vor):
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Відображення центрів ваги
    for center in centers_of_mass:
        plt.scatter(center[0], center[1], s=50, color='red', marker='o')
    
    # Відображення діаграми Вороного
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, line_alpha=0.6, point_size=0)
    
    # Відображення точок вихідного датасету
    plt.scatter(points[:, 0], points[:, 1], s=5, color='black', alpha=0.1)
    
    # Встановлення розмірів вікна
    plt.xlim(0, 960)
    plt.ylim(0, 540)
    
    # Відображення графіку
    plt.show()

# Запис результатів у файл
def save_results(centers_of_mass, vor, output_file):
    fig, ax = plt.subplots(figsize=(12, 7))
    
    # Відображення центрів ваги
    for center in centers_of_mass:
        plt.scatter(center[0], center[1], s=50, color='red', marker='o')
    
    # Відображення діаграми Вороного
    voronoi_plot_2d(vor, ax=ax, show_vertices=False, line_colors='blue', line_width=2, line_alpha=0.6, point_size=0)
    
    # Встановлення розмірів вікна
    plt.xlim(0, 960)
    plt.ylim(0, 540)
    
    # Збереження результатів у файл
    plt.savefig(output_file)

if __name__ == "__main__":
    # Зчитування датасету з файлу
    dataset = read_dataset("DS2.txt")
    
    # Знаходження зв'язаних областей та їхніх центрів ваги
    centers_of_mass = find_connected_regions(dataset)
    
    # Будування діаграми Вороного
    voronoi = build_voronoi_diagram(dataset)
    
    # Відображення результатів
    plot_results(dataset, centers_of_mass, voronoi)
    
    # Запис результатів у файл (замість "output.png" вкажіть власний шлях та ім'я файлу)
    save_results(centers_of_mass, voronoi, "result.png")
import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV-файла
data = pd.read_csv("sales_data_region.csv")

# Просмотр первых строк данных
print("Данные о продажах по регионам за 1 квартал 2023 года:")
print(data.head())

# Фильтрация данных за 1 квартал 2023 года
quarter_data = data[(data['date'] >= '2023-01-01') & (data['date'] <= '2023-03-31')]

# Агрегирование данных: общие продажи по регионам
sales_by_region = quarter_data.groupby('region')['sales'].sum()

# Вывод на экран суммы продаж по регионам
print("\nСумма продаж по регионам за 1 квартал 2023 года:")
print(sales_by_region)

# Построение диаграммы
sales_by_region.plot(kind='bar', color='lightgreen')
plt.title('Total Sales by Region (Q1 2023)')
plt.ylabel('Sales (in $)')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.tight_layout()

# Сохранение диаграммы в файл
plt.savefig("sales_by_region.png")

# Показ диаграммы
plt.show()

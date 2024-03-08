def aggregate_purchase_data(data, category_mapping):
    aggregated_data = defaultdict(int)
    for purchase, count in data.items():
        categories = purchase.split(';')
        for category in categories:
            category = category.strip('_')
            mapped_category = category_mapping.get(category, category)
            aggregated_data[mapped_category] += count
    return aggregated_data




def aggregate_purchase_data(data, category_mapping):
    aggregated_purchase = defaultdict(int)
    for purchase, count in data.items():
        categories = purchase.split(';')
        for category in categories:
            category = category.strip('_')

            mapped_category = category_mapping.get(category, category)
            aggregated_purchase[mapped_category] += count
    return aggregated_purchase




def calculate_percentages(aggregated_purchase):
    total_count = sum(aggregated_purchase.values())
    percentages = {category: (count / total_count) * 100 for category, count in aggregated_purchase.items()}
    return percentages


def print_age_percentages(percentages):
    for age_group, percentage in percentages.items():
        print(f"{age_group}: {percentage:.2f}%")
        
        

def calculate_sales(sales_data):
    total_sales = sum(sales_data.values())
    percentages = {meal_type: (sales / total_sales) * 100 for meal_type, sales in sales_data.items()}
    return sales



def promotions_source_data(data, category_mapping):
    aggregated_data = defaultdict(int)
    for purchase, count in data.items():
        categories = purchase.split(';')
        for category in categories:
            category = category.strip('_')

            mapped_category = category_mapping.get(category, category)
            aggregated_data[mapped_category] += count
    return aggregated_data





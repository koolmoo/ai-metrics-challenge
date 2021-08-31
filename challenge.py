def sum_calories(items):
    return sum(item['calories'] for item in items)

def sum_cost(items):
    return sum(item['cost'] for item in items)

def optimize_food(calorie_max, budget, menu, current_list):
    total_calories = sum_calories(current_list)
    total_cost = sum_cost(current_list)
    solutions = []

    for item in menu:
        if total_calories + item['calories'] < calorie_max and total_cost + item['cost'] < budget:
            solutions.append(optimize_food(calorie_max, budget, menu, current_list + [item]))
        else:
            solutions.append(current_list)

    return max(solutions, key=lambda x: (sum_cost(x), sum_calories(x)), default=[])

def main():
    menu = [
        {'name': 'Cheese Pizza Slice', 'calories': 700, 'cost': 4},
        {'name': 'House Salad', 'calories': 100, 'cost': 8.5},
        {'name': 'Grilled Shrimp', 'calories': 400, 'cost': 15},
        {'name': 'Beef Brisket', 'calories': 400, 'cost': 12},
        {'name': 'Bottled Water', 'calories': 0, 'cost': 1},
        {'name': 'Soda', 'calories': 100, 'cost': 1}
    ]
    print(optimize_food(1000, 10, menu, []))

if __name__ == '__main__':
    main()
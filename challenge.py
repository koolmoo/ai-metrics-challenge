import itertools
import math

def sum_calories(items):
    return sum(item['calories'] for item in items)

def sum_cost(items):
    return sum(item['cost'] for item in items)

def safe_divide(x, y):
    try:
        return int(x // y)
    except ZeroDivisionError:
        return math.inf

def optimize_food(calorie_max, calorie_min, budget, menu, current_list):
    total_calories = sum_calories(current_list)
    total_cost = sum_cost(current_list)
    solutions = []

    for item in menu:
        if total_calories + item['calories'] < calorie_max and total_cost + item['cost'] < budget:
            solutions.append(optimize_food(calorie_max, calorie_min, budget, menu, current_list + [item]))
        else:
            solutions.append(current_list)

    solutions = [s for s in solutions if sum_calories(s) > calorie_min]
    return max(solutions, key=lambda x: (sum_cost(x), sum_calories(x)), default=[])
    
def optimize_food_iterative(calorie_max, calorie_min, budget, menu):
    max_counts = [min(safe_divide(calorie_max, item['calories']), safe_divide(budget, item['cost'])) for item in menu]
    count_ranges = [list(range(count + 1)) for count in max_counts]
    solutions = []

    for combo in itertools.product(*count_ranges):
        total_calories = 0
        total_cost = 0
        for i, item in enumerate(menu):
            total_calories += combo[i] * item['calories']
            total_cost += combo[i] * item['cost']
        if total_cost < budget and total_calories > calorie_min and total_calories < calorie_max:
            solutions.append((combo, total_cost, total_calories))

    return max(solutions, key=lambda x: (x[1], x[2]), default=None)

def print_solution(solution):
    if len(solution) > 0:
        print('Recursive solution:')
        print(', '.join([item['name'] for item in solution]))
        print(f'Total cost: ${sum_cost(solution)}')
        print(f'Total calories: {sum_calories(solution)}')
    else:
        print('There is no solution')

def print_solution_iterative(solution, menu):
    if solution is not None:
        print('Iterative solution:')
        for i, item in enumerate(menu):
            if solution[0][i] > 0:
                print(f"{solution[0][i]} {item['name']}")
        print(f'Total cost: ${solution[1]}')
        print(f'Total calories: {solution[2]}')
    else:
        print('There is no solution')

def main():
    menu = [
        {'name': 'Cheese Pizza Slice', 'calories': 700, 'cost': 4},
        {'name': 'House Salad', 'calories': 100, 'cost': 8.5},
        {'name': 'Grilled Shrimp', 'calories': 400, 'cost': 15},
        {'name': 'Beef Brisket', 'calories': 400, 'cost': 12},
        {'name': 'Bottled Water', 'calories': 0, 'cost': 1},
        {'name': 'Soda', 'calories': 100, 'cost': 1}
    ]
    solution = optimize_food(1000, 200, 10, menu, [])
    print_solution(solution)
    solution = optimize_food_iterative(1000, 200, 10, menu)
    print_solution_iterative(solution, menu)

if __name__ == '__main__':
    main()

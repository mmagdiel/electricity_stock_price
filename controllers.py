import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from models import Coordinates 
from solution import calculate_intersection, transform_df
from data import file_name, index, generation_cost, generation_offer, demand_cost, demand_offer
from data import cumulative_label, price_label, type_label, offer_label, generation, demand
from data import increasing_label, decreasing_label, solution_x, solution_y, title, description

def calculation_hour(file_name: str, with_plots: bool) -> Coordinates:
    hour = file_name[2:5]
    df = pd.read_excel(file_name, index_col=0)

    generation_sorted = df.sort_values(generation_cost)
    demand_sorted = df.sort_values(demand_cost, ascending=False)

    x = generation_sorted[generation_offer].cumsum()
    y = generation_sorted[generation_cost]

    w = demand_sorted[demand_offer].cumsum()
    z = demand_sorted[demand_cost]

    df_generation = transform_df(generation_sorted, generation, generation_offer, [demand_offer, demand_cost], {generation_cost: price_label}, {generation_offer: offer_label})
    df_demand = transform_df(demand_sorted, demand, demand_offer, [generation_offer, generation_cost], {demand_cost: price_label}, {demand_offer: offer_label})

    df_both = pd.concat([df_generation, df_demand], axis=0)
    df_both_sorted = df_both.sort_values(cumulative_label)

    solution = calculate_intersection(df_both_sorted)

    line_x = np.arange(x.count())
    line_x.fill(solution[1])
    line_y = np.arange(y.count())
    line_y.fill(solution[0])

    if with_plots:
        plt.step(x, y, label=f'{increasing_label} en {hour}')
        plt.step(w, z, label=f'{decreasing_label} en {hour}') 
        plt.plot(solution[0], solution[1], 'o--', color='grey', alpha=0.1)
        plt.plot(x, line_x, 'o--', color='silver', alpha=0.3, label=f'{solution_x} en {solution[1]}')
        plt.plot(line_y, y, 'o--', color='darkgray', alpha=0.3, label=f'{solution_y} en {solution[0]}')

        plt.grid(axis='x', color='0.95')
        plt.legend(title=description)
        plt.title(f'{title} para {hour}')
        plt.show()

    return solution

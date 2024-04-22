from helpers import get_point_by_row, get_line_equation, get_determinant, get_pairs, get_intersection_lines
from data import file_name, index, generation_cost, generation_offer, demand_cost, demand_offer
from data import cumulative_label, price_label, type_label, offer_label, generation, demand

def transform_df(df, df_type, cumulative_col, drop_columns, column_cost, column_offer): 
    df = df.drop(columns=drop_columns)
    df[type_label] = df_type
    df[cumulative_label] = df[cumulative_col].cumsum()
    df.rename(columns = column_cost, inplace = True)
    df.rename(columns = column_offer, inplace = True)
    return df 

def calculate_intersection(df): 
    # Initial condition
    last_demand = 100000000
    last_generation = 0
    last_price_demand = 100000000
    last_price_generation = 0
    is_not_negative = True
    has_change_signature = False
    only_once = True

    for index, row  in df.iterrows():
        has_last_demand = row[type_label] == demand
        has_last_generation = row[cumulative_label] > last_generation and row[type_label] == generation
        last_demand = row[cumulative_label] if has_last_demand else last_demand
        last_generation = row[cumulative_label] if has_last_generation else last_generation

        last_price_demand = row[price_label] if has_last_demand else last_price_demand
        last_price_generation = row[price_label] if has_last_generation else last_price_generation

        is_not_negative = last_price_demand - last_price_generation > 0
        has_change_signature = has_change_signature if has_change_signature else has_change_signature ^ (not is_not_negative)

        if has_change_signature and only_once:
            before_list_current = df.loc[(df[type_label].isin([row[type_label]])) & (df[cumulative_label] < row[cumulative_label])]
            before_list_another = df.loc[(~df[type_label].isin([row[type_label]])) & (df[cumulative_label] < row[cumulative_label])]
            after_list_another = df.loc[(~df[type_label].isin([row[type_label]])) & (df[cumulative_label] > row[cumulative_label])]
            before_row_current = before_list_current.iloc[-1]
            before_row_another = before_list_another.iloc[-1]
            after_row_another = before_list_another.iloc[-2]
            
            before_point_current = get_point_by_row(before_row_current)
            after_point_current = get_point_by_row(row, -row[offer_label])
            before_point_another = get_point_by_row(before_row_another)
            after_point_another = get_point_by_row(after_row_another,  0, before_row_another[price_label] - after_row_another[price_label])

            line_current = get_line_equation(before_point_current, after_point_current)
            line_another = get_line_equation(before_point_another, after_point_another)
            solution = get_intersection_lines(line_current, line_another)
            return solution
            


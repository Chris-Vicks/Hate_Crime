import pandas as pd

def calculate_and_print_victim_counts(dataset):
    victim_counts = dataset['VICTIM_COUNT'].value_counts()
    print(victim_counts)
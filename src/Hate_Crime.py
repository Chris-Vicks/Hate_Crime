import sys
import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


class HateCrimeAnalyzer:
    def __init__(self, data_path):
        self.data = pd.read_csv(data_path)
        self.data.fillna(0, inplace=True)

    # def sum_offenses_by_year(self):
    #     """Summarizes the number of offenses by year.

    #     Returns:
    #         DataFrame containing the summed data.
    #     """
    #     summed_data = self.data.groupby(['DATA_YEAR', 'OFFENSE_NAME'])['INCIDENT_ID'].count().reset_index()
    #     summed_data.rename(columns={'INCIDENT_ID': 'Number of Offenses'}, inplace=True)
    #     return summed_data

    def calculate_and_print_victim_counts(self):
        victim_counts = self.data['VICTIM_COUNT'].value_counts()
        print(victim_counts)

    def map_to_severity(self, offense_type):
            violent_lst = ["Simple Assault", "Intimidation", "Aggravated Assault", "Robbery",\
                          "Burglary/Breaking & Entering","Destruction/Damage/Vandalism of Property;Intimidation",\
                          "Burglary/Breaking & Entering;Destruction/Damage/Vandalism of Property",\
                            "Aggravated Assault;Simple Assault", "Arson","Destruction/Damage/Vandalism of Property;Simple Assault",\
                            "Intimidation;Simple Assault","Murder and Nonnegligent Manslaughter",\
                            "Aggravated Assault;Destruction/Damage/Vandalism of Property","Rape",\
                            "Arson;Destruction/Damage/Vandalism of Property","Destruction/Damage/Vandalism of Property;Not Specified",\
                            "Arson;Intimidation","Aggravated Assault;Intimidation","Weapon Law Violations",\
                            "Aggravated Assault;Murder and Nonnegligent Manslaughter","Kidnapping/Abduction;Robbery","Fondling",\
                            "Pornography/Obscene Material","Robbery;Simple Assault","Sexual Assault With An Object","Kidnapping/Abduction",\
                            "Arson;Burglary/Breaking & Entering","Sodomy","Rape;Robbery","Destruction/Damage/Vandalism of Property;Intimidation;Not Specified",\
                            "Arson;Burglary/Breaking & Entering;Destruction/Damage/Vandalism of Property",\
                            "Burglary/Breaking & Entering;Simple Assault","Aggravated Assault;Destruction/Damage/Vandalism of Property;Intimidation",\
                            "Burglary/Breaking & Entering;Intimidation","Aggravated Assault;Not Specified",\
                            "Intimidation;Weapon Law Violations","Kidnapping/Abduction;Rape","Pornography/Obscene Material;Simple Assault",\
                            "Statutory Rape","All Other Larceny;Simple Assault","Aggravated Assault;Pocket-picking",\
                            "Aggravated Assault;Drug/Narcotic Violations","Aggravated Assault;All Other Larceny","Aggravated Assault;Arson",\
                            "Arson;Destruction/Damage/Vandalism of Property;Intimidation","Robbery;Sexual Assault With An Object",\
                            "Shoplifting;Simple Assault","Destruction/Damage/Vandalism of Property;Robbery",\
                            "Aggravated Assault;Weapon Law Violations","Aggravated Assault;Burglary/Breaking & Entering",\
                            "Aggravated Assault;Intimidation;Simple Assault","Aggravated Assault;Robbery",\
                            "Destruction/Damage/Vandalism of Property;Intimidation;Robbery;Simple Assault",\
                            "Intimidation;Not Specified","Arson;Destruction/Damage/Vandalism of Property;Not Specified" ]
            
            if offense_type in violent_lst:
                return 'Violent'
            elif offense_type == "Not Specified":
                return 'Non-Violent'
            else:
                return "Non-Violent"
        

    def remove_columns(self, columns):
        self.data.drop(columns=columns, inplace=True)
        print("Columns successfully removed.")

    def process_data(self, columns_to_remove):
        # Remove specified columns
        self.remove_columns(columns_to_remove)

        #create severity column
        self.data['SEVERITY'] = self.data['OFFENSE_NAME'].apply(self.map_to_severity)

if __name__ == "__main__":
    data_path = "C:/Users/chris/Documents/Galvanize/daimil10/Final_Project/Hate_Crime/data/Hate_crime1/combined_data.csv"
    output_path = "C:/Users/chris/Documents/Galvanize/daimil10/Final_Project/Hate_Crime/data/Hate_crime1/combined_data_processed_data.csv"  # Specify your desired output path
    
    data_processor = HateCrimeAnalyzer(data_path)
    data_processor.data['SEVERITY'] = data_processor.data['OFFENSE_NAME'].apply(data_processor.map_to_severity)

    columns_to_remove = [
        "ORI", "PUB_AGENCY_UNIT","PUB_AGENCY_NAME","STATE_ABBR","LOCATION_NAME","OFFENSE_NAME","VICTIM_TYPES","TOTAL_INDIVIDUAL_VICTIMS", "AGENCY_TYPE_NAME", "DIVISION_NAME", 
        "REGION_NAME", "ADULT_VICTIM_COUNT", "JUVENILE_VICTIM_COUNT", 
        "ADULT_OFFENDER_COUNT", "JUVENILE_OFFENDER_COUNT", "OFFENDER_ETHNICITY", 
        "MULTIPLE_OFFENSE", "MULTIPLE_BIAS","INCIDENT_ID","DATA_YEAR","STATE_NAME","POPULATION_GROUP_CODE","Unnamed: 0","INCIDENT_DATE"
    ] 

    data_processor.remove_columns(columns_to_remove)
    
    


    print(data_processor.data.head())
    # Call the sum_offenses_by_year function
    #summed_offenses = data_processor.sum_offenses_by_year()
    
    # print(summed_offenses)
    # # Call the calculate_and_print_victim_counts function
    # data_processor.calculate_and_print_victim_counts()

    data_processor.data.to_csv(output_path, index=False)


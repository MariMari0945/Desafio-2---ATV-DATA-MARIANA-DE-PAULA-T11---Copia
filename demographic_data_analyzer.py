import pandas as pd

def demographic_data_analyzer():
    # Load the data
    df = pd.read_csv("data/adult.data.csv")

    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # 2. What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # 3. What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4. Percentage of people with advanced education (Bachelors, Masters, or Doctorate) making more than 50K
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[advanced_education & (df['salary'] == '>50K')].shape[0] / df[advanced_education].shape[0]) * 100, 1)

    # 5. Percentage of people without advanced education making more than 50K
    lower_education = ~advanced_education
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # 6. Minimum number of hours a person works per week
    min_work_hours = df['hours-per-week'].min()

    # 7. Percentage of the people who work the minimum number of hours per week having a salary of >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours].shape[0]
    rich_percentage = round((df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')].shape[0] / num_min_workers) * 100, 1)

    # 8. Country with the highest percentage of people that earn >50K
    country_earnings = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_totals = df['native-country'].value_counts()
    highest_earning_country_percentage = round((country_earnings / country_totals * 100).max(), 1)
    highest_earning_country = (country_earnings / country_totals * 100).idxmax()

    # 9. Identify the most popular occupation for those who earn >50K in India
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

# Execute and print the result for testing
result = demographic_data_analyzer()
for key, value in result.items():
    print(f"{key}: {value}")

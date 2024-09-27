# Importa a biblioteca pandas
import pandas as pd

# Cria uma função para a análise do dataset
def demographic_data_analyzer():
    df = pd.read_csv('data/adult.data.csv')
    
    # Quantidade de pessoas de cada raça
    race_count = df['race'].value_counts()
    
    # Idade média dos homens
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    
    # Porcentagem de pessoas com Bacharelado
    percentage_bachelors = (df[df['education'] == 'Bachelors'].shape[0] / df.shape[0]) * 100
    
    # Porcentagem de pessoas com ensino superior avançado que ganham >50K
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    higher_education_rich = (higher_education[higher_education['salary'] == '>50K'].shape[0] / higher_education.shape[0]) * 100
    
    # Porcentagem de pessoas sem ensino superior avançado que ganham >50K
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education_rich = (lower_education[lower_education['salary'] == '>50K'].shape[0] / lower_education.shape[0]) * 100
    
    # Número mínimo de horas trabalhadas por semana
    min_work_hours = df['hours-per-week'].min()
    
    # Porcentagem das pessoas que trabalham o número mínimo de horas e ganham >50K
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = (num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100
    
    # País com maior porcentagem de pessoas que ganham >50K
    country_earning_rich = df[df['salary'] == '>50K']['native-country'].value_counts(normalize=True) * 100
    highest_earning_country = country_earning_rich.idxmax()
    highest_earning_country_percentage = country_earning_rich.max()
    
    # Ocupação mais popular para pessoas que ganham >50K na Índia
    top_IN_occupation = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()
    
    # Retorna as variáveis esperadas
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


# Executa e printa o reusltado teste
result = demographic_data_analyzer()
for key, value in result.items():
    print(f"{key}: {value}")

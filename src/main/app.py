from typing import Union

from fastapi import FastAPI

from src.main.data import read_dataset
from src.main.util import filter_not_null_keys

app = FastAPI()

dataset = read_dataset()


@app.get("/survey_data")
async def survey_data(
    sort: Union[str, None] = None,
    fields: Union[str, None] = None,
    # Attributes
    timestamp: Union[str, None] = None,
    employment_type: Union[str, None] = None,
    company_name: Union[str, None] = None,
    location_country: Union[str, None] = None,
    location_city: Union[str, None] = None,
    company_industry: Union[str, None] = None,
    company_type: Union[str, None] = None,
    job_title: Union[str, None] = None,
    job_ladder: Union[str, None] = None,
    job_level: Union[str, None] = None,
    hrs_per_week_req: Union[str, None] = None,
    hrs_per_week_act: Union[str, None] = None,
    health_insurance_offered: Union[str, None] = None,
    annual_vacations: Union[str, None] = None,
    gender: Union[str, None] = None,
    experience_industry: Union[str, None] = None,
    experience_currenty_company: Union[str, None] = None,
    education_level: Union[str, None] = None,
    salary_base_2018: Union[str, None] = None,
    company_size: Union[str, None] = None,
    bonus_2018: Union[str, None] = None,
    stock_options_2018: Union[str, None] = None,
    question_happiness: Union[str, None] = None,
    question_inidustry_direction: Union[str, None] = None,
    question_top_skills: Union[str, None] = None,
    question_bootcamp: Union[str, None] = None
):
    selection_tuple = None

    select_cols_values = {
        "timestamp": timestamp,
        "employment_type": employment_type,
        "company_name": company_name,
        "location_country": location_country,
        "location_city": location_city,
        "company_industry": company_industry,
        "company_type": company_type,
        "job_title": job_title,
        "job_ladder": job_ladder,
        "job_level": job_level,
        "hrs_per_week_req": hrs_per_week_req,
        "hrs_per_week_act": hrs_per_week_act,
        "health_insurance_offered": health_insurance_offered,
        "annual_vacations": annual_vacations,
        "gender": gender,
        "experience_industry": experience_industry,
        "experience_currenty_company": experience_currenty_company,
        "education_level": education_level,
        "salary_base_2018": salary_base_2018,
        "company_size": company_size,
        "bonus_2018": bonus_2018,
        "stock_options_2018": stock_options_2018,
        "question_happiness": question_happiness,
        "question_inidustry_direction": question_inidustry_direction,
        "question_top_skills": question_top_skills,
        "question_bootcamp": question_bootcamp
    }
        
    select_cols_values = dict(filter(filter_not_null_keys, select_cols_values.items()))
    
    if (select_cols_values):
        selection_tuple = (dataset[list(select_cols_values.items())[0][0]] == 
                        list(select_cols_values.items())[0][1])
        for t in select_cols_values.items():
            selection_tuple = selection_tuple | (dataset[t[0]] == t[1])


    result_dataset = dataset
    
    if (selection_tuple):
        result_dataset = result_dataset[selection_tuple]

    if (fields):
        selection_cols = fields.split(",") if "," in fields else [fields]
        result_dataset = result_dataset[selection_cols]

    if (sort):
        sort_cols = sort.split(",") if "," in sort else sort
        result_dataset = result_dataset.sort_values(by=sort_cols, ascending=True)

    return result_dataset.fillna("nan").to_dict(orient="records")
        
    
    
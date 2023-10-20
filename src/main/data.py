import pandas as pd

dataset_path = "data/salary_survey.csv"

dataset_headers_mapping = {
    "Timestamp": "timestamp",
    "Employment Type": "employment_type",
    "Company Name": "company_name",
    "Primary Location (Country)": "location_country",
    "Primary Location (City)": "location_city",
    "Industry in Company": "company_industry",
    "Public or Private Company": "company_type",
    "Job Title In Company": "job_title",
    "Job Ladder": "job_ladder",
    "Job Level": "job_level",
    "Required Hours Per Week": "hrs_per_week_req",
    "Actual Hours Per Week	": "hrs_per_week_act",
    "Health Insurance Offered": "health_insurance_offered",
    "Annual Vacation (in Weeks)": "annual_vacations",
    "Gender": "gender",
    # --- #
    "Years Experience in Industry": "experience_industry",
    "Years of Experience in Current Company": "experience_currenty_company",
    "Highest Level of Formal Education Completed": "education_level",
    "Total Base Salary in 2018 (in USD)": "salary_base_2018",
    "Company Size - # Employees": "company_size",
    "Total Bonus in 2018 (cumulative annual value in USD)": "bonus_2018",
    "Total Stock Options/Equity in 2018 (cumulative annual value in USD)": "stock_options_2018",
    # --- #
    "Are you happy at your current position?": "question_happiness",
    "Do you plan to resign in the next 12 months?": "question_resign",
    "What are your thoughts about the direction of your industry?": "question_inidustry_direction",
    "Final Question: What are the top skills (you define what that means) that you believe will be necessary for job growth in your industry over the next 10 years?": "question_top_skills",
    "Have you ever done a bootcamp? If so was it worth it?": "question_bootcamp",
}

def read_dataset():
    dataset = pd.read_csv(dataset_path)
    dataset = dataset.rename(columns=dataset_headers_mapping)

    return dataset
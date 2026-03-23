Use the app using this link: https://ai-data-analyst-pro.streamlit.app

AI Data Analyst Pro
AI Data Analyst Pro is an end-to-end data analysis application that simplifies the journey from raw datasets to actionable insights. Built using Python and Streamlit, the tool enables users to upload data, explore it, and generate insights through an interactive interface without requiring advanced technical skills.

FEATURES
Upload and preview datasets (CSV/Excel)
Automated Exploratory Data Analysis (EDA)
Data cleaning and dataset merging
Ask questions about data using AI (natural language queries)
Export processed data and results
Interactive and user-friendly Streamlit interface

WORKFLOW
Upload dataset
Preview and inspect data structure
Perform automated EDA (summary statistics, distributions, missing values)
Clean and merge datasets
Ask questions about the data using AI
Export results

TECH STACK
Python (Pandas, NumPy)
Streamlit (Frontend & App Deployment)
SQLite (Data storage)
OpenAI API (AI-powered insights)
Matplotlib / Seaborn (Visualizations)

Project Structure
ai-data-analyst-pro/
│
├── app.py
├── pages/
│   ├── 1_Upload.py
│   ├── 2_EDA.py
│   ├── 3_Clean_and_Merge.py
│   ├── 4_Ask_Data.py
│   └── 5_Export.py
│
├── utils/
│   ├── cleaning.py
│   ├── eda.py
│   ├── llm.py
│   └── merge.py
│
├── data.db
└── requirements.txt


Clone the repository and run locally:

git clone https://github.com/your-username/ai-data-analyst-pro.git  
cd ai-data-analyst-pro  

python -m venv venv  
source venv/bin/activate  

pip install -r requirements.txt  
streamlit run app.py  

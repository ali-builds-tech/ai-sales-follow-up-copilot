AI Sales Follow-Up Copilot — Project Progress



Last Updated: 20 September 2026





1\. Project Goal



Build a practical AI-assisted sales follow-up system that helps businesses identify which leads should be contacted first, understand lead priority, and generate actionable follow-up recommendations.



The project is designed as a real-world business automation/product concept rather than a simple tutorial project.





2\. Current Project Structure



ai-sales-follow-up-copilot/

│

├── data/

│   ├── leads.csv

│   └── scored\_leads.csv

│

├── src/

│   ├── main.py

│   ├── dashboard.py

│   ├── dashboard\_backup.py

│   ├── dashboard\_backup\_2.py

│   ├── dashboard\_backup\_3.py

│   └── # AI Sales Follow-Up Copilot — Prog.txt

│

├── venv/

└── PROJECT\_PROGRESS.md





3\. Completed Components



Data Layer



\- \[x] Created data/leads.csv

\- \[x] Lead dataset contains business and sales-related information.

\- \[x] Created data/scored\_leads.csv

\- \[x] Verified scored lead output is generated correctly.



Lead Scoring Workflow



\- \[x] Python workflow created in src/main.py

\- \[x] Lead scoring implemented

\- \[x] Priority classification implemented

\- \[x] Days since last contact calculated

\- \[x] Lead reasoning generated

\- \[x] Follow-up recommendations generated

\- \[x] Follow-up messages generated

\- \[x] Scored results exported to CSV

\- \[x] Workflow successfully tested from the terminal



Dashboard



\- \[x] Streamlit dashboard created in src/dashboard.py

\- \[x] Priority filters implemented

\- \[x] Industry filters implemented

\- \[x] Lead overview created

\- \[x] Priority chart added

\- \[x] Industry chart added

\- \[x] Action Summary added

\- \[x] Sales Opportunities table added

\- \[x] Lead Details section added

\- \[x] Lead Score displayed

\- \[x] Lead Priority displayed

\- \[x] Days Since Contact displayed

\- \[x] Lead Reason displayed

\- \[x] Recommended Action displayed

\- \[x] Follow-Up Message displayed

\- \[x] CSV download implemented

\- \[x] Empty-filter behavior tested

\- \[x] High-priority leads tested

\- \[x] Medium-priority leads tested

\- \[x] Low-priority leads tested

\- \[x] Industry filtering tested

\- \[x] Dashboard successfully launched and verified





4\. Current Workflow



Raw Leads

&#x20;  ↓

leads.csv

&#x20;  ↓

Python Lead Scoring

&#x20;  ↓

Lead Score

&#x20;  ↓

Priority Classification

&#x20;  ↓

Lead Reason

&#x20;  ↓

Follow-Up Recommendation

&#x20;  ↓

Follow-Up Message

&#x20;  ↓

scored\_leads.csv

&#x20;  ↓

Streamlit Dashboard

&#x20;  ↓

Salesperson identifies which leads need attention

&#x20;  ↓

Salesperson takes the recommended action





5\. Verified Current Output



The current scored\_leads.csv contains 15 leads.



Priority distribution:



\- High Priority: 3

\- Medium Priority: 3

\- Low Priority: 9



Current follow-up actions:



\- Contact Today: 3

\- Follow Up Soon: 0

\- Monitor: 9



Examples from the verified dataset:



\- Global Logistics — Lead Score: 85.00 — High — 34 days since contact

\- TechVision Solutions — Lead Score: 69.33 — High — 21 days since contact

\- BuildPro Contractors — Lead Score: 65.00 — High — 31 days since contact

\- Smart Auto Parts — Lead Score: 47.81 — Medium — 29 days since contact

\- Health Plus Clinic — Lead Score: 42.29 — Medium — 24 days since contact

\- Prime Estate Group — Lead Score: 40.29 — Medium — 13 days since contact

\- Style House — Lead Score: 28.98 — Low — 7 days since contact



The exact values should always be taken from the latest generated data/scored\_leads.csv.





6\. Dashboard Verification



The final dashboard was successfully launched using:



venv\\Scripts\\python.exe -m streamlit run src\\dashboard.py



The dashboard currently displays:



\- Total Leads

\- High Priority

\- Medium Priority

\- Low Priority

\- Leads by Priority chart

\- Leads by Industry chart

\- Contact Today count

\- Follow Up Soon count

\- Monitor count

\- Sales Opportunities table

\- Lead Details

\- Lead Score

\- Priority

\- Days Since Contact

\- Lead Reason

\- Recommended Action

\- Follow-Up Message

\- CSV download



Verified example:



Global Logistics



\- Industry: Logistics

\- City: Lahore

\- Employees: 75

\- Monthly Revenue: 4,200,000

\- Lead Score: 85.0

\- Priority: High

\- Days Since Contact: 34

\- Lead Reason: High revenue, Large company, Long time since contact

\- Recommended Action: Contact today



The dashboard is currently functioning as expected.





7\. Business Problem Solved



Many small and medium-sized businesses have leads but do not know:



\- Which lead should be contacted first?

\- Which leads are becoming cold?

\- Which leads deserve immediate attention?

\- What should the salesperson do next?

\- Which leads have been ignored for too long?



The Copilot converts raw lead information into prioritized and actionable sales follow-up information.





8\. Product Direction



The long-term goal is to turn this portfolio project into a practical business automation product.



Potential target users:



\- Small businesses

\- Sales teams

\- Agencies

\- Local service businesses

\- B2B companies

\- Lead-generation agencies

\- Freelancers managing client leads



Potential value proposition:



"Stop guessing


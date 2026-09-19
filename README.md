AI Sales Follow-Up Copilot



Turn raw sales leads into prioritized follow-up actions and actionable sales intelligence.



Problem



Sales teams often have many leads but limited time to decide:



\- Which leads should be contacted first?

\- Which leads are becoming cold?

\- Why is a lead considered important?

\- What action should the salesperson take?

\- What message should be sent?



Without a structured process, valuable leads can be missed and follow-ups can become inconsistent.



Solution



AI Sales Follow-Up Copilot analyzes sales leads and converts raw lead data into practical follow-up intelligence.



The system:



1\. Reads raw lead data from a CSV file.

2\. Calculates a lead score.

3\. Assigns a priority level.

4\. Explains why the lead received that priority.

5\. Recommends the next sales action.

6\. Generates a follow-up message.

7\. Presents the results through an interactive Streamlit dashboard.



Workflow



Raw Sales Leads

&#x20;      ↓

&#x20;  Lead Scoring

&#x20;      ↓

&#x20;Priority Classification

&#x20;      ↓

&#x20;   Lead Reason

&#x20;      ↓

&#x20;Follow-Up Recommendation

&#x20;      ↓

&#x20;Follow-Up Message

&#x20;      ↓

&#x20;Streamlit Sales Dashboard



Current Verified Results



The current example dataset contains 15 sales leads.



Priority| Leads

High| 3

Medium| 3

Low| 9



Recommended actions:



Action| Leads

Contact Today| 3

Schedule Follow-Up| 3

Monitor| 9



Example



Global Logistics



\- Lead Score: 85.00

\- Priority: High

\- Days Since Contact: 34

\- Reason: High revenue, large company, long time since contact

\- Recommended Action: Contact today



This demonstrates how the system converts raw lead information into a clear sales action.



Dashboard Features



The Streamlit dashboard currently provides:



\- Total lead count

\- High / Medium / Low priority metrics

\- Priority filtering

\- Industry filtering

\- Lead overview charts

\- Sales opportunities table

\- Individual lead details

\- Lead score

\- Priority

\- Days since contact

\- Reason behind lead priority

\- Recommended follow-up action

\- Generated follow-up message

\- CSV download



Sales Intelligence Logic



The system uses available lead information such as:



\- Company size

\- Monthly revenue

\- Website status

\- Time since last contact



These signals are combined to calculate a lead score and classify leads into:



High → Contact Today



Medium → Schedule Follow-Up



Low → Monitor and Follow Up Later



The goal is not to replace a salesperson's judgment. The system acts as a decision-support tool that helps salespeople focus their time.



Technology Stack



\- Python

\- Pandas

\- Streamlit

\- Git

\- GitHub



Project Structure



ai-sales-follow-up-copilot/

│

├── data/

│   ├── leads.csv

│   └── scored\_leads.csv

│

├── src/

│   ├── main.py

│   ├── dashboard.py

│   └── dashboard\_backup\*.py

│

├── PROJECT\_PROGRESS.md

├── README.md

├── .gitignore

└── venv/



Run Locally



Clone the repository:



git clone https://github.com/ali-builds-tech/ai-sales-follow-up-copilot.git



Move into the project:



cd ai-sales-follow-up-copilot



Run the Streamlit dashboard:



venv\\Scripts\\python.exe -m streamlit run src\\dashboard.py



The dashboard will open in your browser.



Input Data



The system currently uses a CSV dataset containing sales lead information such as:



\- Lead ID

\- Business name

\- Industry

\- City

\- Email

\- Phone

\- Number of employees

\- Monthly revenue

\- Last contact date

\- Website status



Generated Output



The scoring workflow generates:



"data/scored\_leads.csv"



The output contains additional sales intelligence including:



\- Lead Score

\- Priority

\- Lead Reason

\- Follow-Up Recommendation

\- Follow-Up Message



Target Users



The concept is designed for:



\- Small sales teams

\- Sales representatives

\- Lead-generation agencies

\- B2B businesses

\- Service businesses

\- Freelancers building sales automation systems



Business Value



The system is designed to help salespeople:



\- Identify important leads faster

\- Reduce manual lead analysis

\- Prioritize follow-ups

\- Understand why a lead deserves attention

\- Generate consistent follow-up messages

\- Spend more time selling and less time organizing leads



Future Development



Planned improvements include:



\- CRM integration

\- Automated email follow-ups

\- Real-time lead updates

\- More advanced predictive scoring

\- Lead history tracking

\- Follow-up scheduling

\- Production database support

\- Authentication and user management

\- Model-based sales prediction

\- Automation workflows



A future n8n no-code version may be developed as a separate project and is not part of this current Python MVP.



Testing \& Verification



The current dashboard has been manually tested for:



\- High-priority leads

\- Medium-priority leads

\- Low-priority leads

\- Industry filtering

\- Multiple filter combinations

\- Empty filter results

\- Lead details

\- Follow-up recommendations

\- Follow-up messages

\- CSV download



The current MVP is working locally.



Current Project Status



MVP: Working



Completed:



\- Lead dataset

\- Lead scoring

\- Priority classification

\- Lead reasoning

\- Follow-up recommendations

\- Follow-up message generation

\- Streamlit dashboard

\- Filtering

\- Lead details

\- CSV export

\- Git version control

\- GitHub repository



Next stage:



Deploy the Streamlit dashboard and prepare the project for portfolio/demo presentation.



Development Philosophy



The project follows:



Learn → Build → Test → Break → Debug → Measure → Explain → Improve



The focus is on building practical AI systems that solve real business problems rather than creating projects only for tutorials.



Current Limitations



This is an MVP and should not be considered a production sales platform.



Current limitations include:



\- Small example dataset

\- CSV-based storage

\- No CRM integration

\- No automatic email or messaging

\- No automated scheduling

\- No authentication

\- No production monitoring

\- No autonomous sales decisions



Project Vision



The long-term goal is to evolve the project from a simple lead-scoring dashboard into a practical AI sales assistant that helps businesses identify opportunities, understand lead behavior, prioritize actions, and automate repetitive follow-up work.



Author



Ali Hussnain



GitHub:



https://github.com/ali-builds-tech



License



No open-source license has been added yet.


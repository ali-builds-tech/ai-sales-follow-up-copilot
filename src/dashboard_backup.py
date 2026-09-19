import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Sales Follow-Up Copilot",
    page_icon="📈",
    layout="wide"
)

st.title("AI Sales Follow-Up Copilot")
st.write("Find the leads that need attention and decide what to do next.")

df = pd.read_csv(
    "data/scored_leads.csv",
    dtype={"Phone": str}
)

st.sidebar.header("Filters")

priority = st.sidebar.multiselect(
    "Priority",
    ["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)

industry_list = sorted(df["Industry"].unique())

industry = st.sidebar.multiselect(
    "Industry",
    industry_list,
    default=industry_list
)

leads = df[
    df["Priority"].isin(priority)
    & df["Industry"].isin(industry)
]

st.subheader("Sales Overview")

total = len(leads)
contact_today = (leads["Follow_Up_Recommendation"] == "Contact today").sum()
scheduled = (leads["Follow_Up_Recommendation"] == "Schedule follow-up").sum()
monitor = (leads["Follow_Up_Recommendation"] == "Monitor and follow up later").sum()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", total)
col2.metric("Contact Today", contact_today)
col3.metric("Schedule Follow-Up", scheduled)
col4.metric("Monitor Later", monitor)

st.divider()

st.subheader("Leads")

table = leads[
    [
        "Business_Name",
        "Industry",
        "City",
        "Lead_Score",
        "Priority",
        "Days_Since_Contact",
        "Follow_Up_Recommendation"
    ]
]

st.dataframe(
    table,
    width="stretch",
    hide_index=True
)

st.divider()

if not leads.empty:

    st.subheader("Selected Lead")

    selected = st.selectbox(
        "Select a business",
        leads["Business_Name"].tolist()
    )

    lead = leads[
        leads["Business_Name"] == selected
    ].iloc[0]

    left, right = st.columns(2)

    with left:
        st.write("### Business")
        st.write(f"*{lead['Business_Name']}*")
        st.write(f"Industry: {lead['Industry']}")
        st.write(f"City: {lead['City']}")
        st.write(f"Employees: {lead['Employees']}")
        st.write(f"Monthly Revenue: {lead['Monthly_Revenue']}")

    with right:
        st.write("### Sales Information")
        st.metric("Lead Score", lead["Lead_Score"])
        st.write(f"Priority: {lead['Priority']}")
        st.write(f"Days Since Contact: {lead['Days_Since_Contact']}")
        st.write(f"Why follow up: {lead['Lead_Reason']}")
        st.write(f"Next step: {lead['Follow_Up_Recommendation']}")

    st.write("### Follow-Up Message")

    st.text_area(
        "Suggested message",
        lead["Follow_Up_Message"],
        height=180
    )

    st.download_button(
        "Download Lead Data",
        leads.to_csv(index=False),
        "sales_follow_up_leads.csv",
        "text/csv"
    )

else:
    st.warning("No leads match the selected filters.")
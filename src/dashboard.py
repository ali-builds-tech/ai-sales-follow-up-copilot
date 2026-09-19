import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Sales Follow-Up Copilot",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv("data/scored_leads.csv", dtype={"Phone": str})

st.title("AI Sales Follow-Up Copilot")

st.write(
    "Turn raw leads into prioritized sales actions. "
    "Find the leads that need attention and decide what to do next."
)

st.divider()

st.sidebar.header("Lead Filters")

priority_filter = st.sidebar.multiselect(
    "Priority",
    ["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)

industry_filter = st.sidebar.multiselect(
    "Industry",
    sorted(df["Industry"].unique()),
    default=sorted(df["Industry"].unique())
)

filtered_df = df[
    (df["Priority"].isin(priority_filter)) &
    (df["Industry"].isin(industry_filter))
]

total_leads = len(filtered_df)
high_leads = len(filtered_df[filtered_df["Priority"] == "High"])
medium_leads = len(filtered_df[filtered_df["Priority"] == "Medium"])
low_leads = len(filtered_df[filtered_df["Priority"] == "Low"])

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Leads", total_leads)
col2.metric("High Priority", high_leads)
col3.metric("Medium Priority", medium_leads)
col4.metric("Low Priority", low_leads)

st.divider()

st.subheader("Lead Overview")

if total_leads > 0:

    col1, col2 = st.columns(2)

    with col1:
        st.write("Leads by Priority")

        priority_chart = (
            filtered_df["Priority"]
            .value_counts()
            .reindex(["High", "Medium", "Low"], fill_value=0)
        )

        st.bar_chart(priority_chart)

    with col2:
        st.write("Leads by Industry")

        industry_chart = filtered_df["Industry"].value_counts()

        st.bar_chart(industry_chart)

    st.divider()

    st.subheader("Action Summary")

    contact_today = len(
        filtered_df[
            filtered_df["Follow_Up_Recommendation"] == "Contact today"
        ]
    )

    follow_up_soon = len(
        filtered_df[
            filtered_df["Follow_Up_Recommendation"] == "Follow up soon"
        ]
    )

    monitor_later = len(
        filtered_df[
            filtered_df["Follow_Up_Recommendation"]
            == "Monitor and follow up later"
        ]
    )

    col1, col2, col3 = st.columns(3)

    col1.metric("Contact Today", contact_today)
    col2.metric("Follow Up Soon", follow_up_soon)
    col3.metric("Monitor", monitor_later)

else:
    st.info("Select different filters to see available leads.")

st.divider()

st.subheader("Sales Opportunities")

if total_leads > 0:

    display_df = filtered_df[
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
        display_df,
        use_container_width=True,
        hide_index=True
    )

else:
    st.warning("No leads match the selected filters.")

st.divider()

st.subheader("Lead Details")

if total_leads > 0:

    selected_business = st.selectbox(
        "Select a lead",
        filtered_df["Business_Name"].tolist()
    )

    lead = filtered_df[
        filtered_df["Business_Name"] == selected_business
    ].iloc[0]

    col1, col2 = st.columns(2)

    with col1:
        st.write("### Business")
        st.write("Business:", lead["Business_Name"])
        st.write("Industry:", lead["Industry"])
        st.write("City:", lead["City"])
        st.write("Employees:", lead["Employees"])
        st.write("Monthly Revenue:", lead["Monthly_Revenue"])

    with col2:
        st.write("### Sales Intelligence")
        st.metric("Lead Score", lead["Lead_Score"])
        st.write("Priority:", lead["Priority"])
        st.write("Days Since Contact:", lead["Days_Since_Contact"])
        st.write("Why this lead:", lead["Lead_Reason"])
        st.write(
            "Recommended Action:",
            lead["Follow_Up_Recommendation"]
        )

    st.write("### Follow-Up Message")

    st.text_area(
        "Ready-to-use message",
        lead["Follow_Up_Message"],
        height=180
    )

    st.download_button(
        "Download Lead Data",
        data=filtered_df.to_csv(index=False),
        file_name="sales_follow_up_leads.csv",
        mime="text/csv"
    )

else:
    st.info("Select different filters to view lead details.")
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Sales Follow-Up Copilot",
    page_icon="📊",
    layout="wide"
)

df = pd.read_csv(
    "data/scored_leads.csv",
    dtype={"Phone": str}
)

st.title("AI Sales Follow-Up Copilot")

st.markdown(
    """
    ### Turn raw leads into prioritized sales actions

    Find the leads that need attention, understand why they matter,
    and know what to do next.
    """
)

st.divider()

st.sidebar.header("Lead Filters")

priority_filter = st.sidebar.multiselect(
    "Priority",
    options=["High", "Medium", "Low"],
    default=["High", "Medium", "Low"]
)

industry_filter = st.sidebar.multiselect(
    "Industry",
    options=sorted(df["Industry"].unique()),
    default=sorted(df["Industry"].unique())
)

filtered_df = df[
    df["Priority"].isin(priority_filter)
    & df["Industry"].isin(industry_filter)
]

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Leads", len(filtered_df))

with col2:
    st.metric(
        "High Priority",
        (filtered_df["Priority"] == "High").sum()
    )

with col3:
    st.metric(
        "Medium Priority",
        (filtered_df["Priority"] == "Medium").sum()
    )

with col4:
    st.metric(
        "Low Priority",
        (filtered_df["Priority"] == "Low").sum()
    )

st.divider()

st.subheader("Lead Overview")

if len(filtered_df) > 0:

    chart_col1, chart_col2 = st.columns(2)

    with chart_col1:
        st.write("*Leads by Priority*")

        priority_counts = (
            filtered_df["Priority"]
            .value_counts()
            .reindex(["High", "Medium", "Low"], fill_value=0)
        )

        st.bar_chart(priority_counts)

    with chart_col2:
        st.write("*Leads by Industry*")

        industry_counts = (
            filtered_df["Industry"]
            .value_counts()
            .sort_values(ascending=False)
        )

        st.bar_chart(industry_counts)

else:
    st.info("Select different filters to view the charts.")

st.divider()

st.subheader("Sales Opportunities")

if len(filtered_df) > 0:

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

if len(filtered_df) > 0:

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
        st.write(f"*Business:* {lead['Business_Name']}")
        st.write(f"*Industry:* {lead['Industry']}")
        st.write(f"*City:* {lead['City']}")
        st.write(f"*Employees:* {lead['Employees']}")
        st.write(f"*Monthly Revenue:* {lead['Monthly_Revenue']}")

    with col2:
        st.write("### Sales Intelligence")
        st.metric("Lead Score", lead["Lead_Score"])
        st.write(f"*Priority:* {lead['Priority']}")
        st.write(
            f"*Days Since Contact:* {lead['Days_Since_Contact']}"
        )
        st.write(f"*Why this lead:* {lead['Lead_Reason']}")
        st.write(
            f"*Recommended Action:* "
            f"{lead['Follow_Up_Recommendation']}"
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
    st.info("Select different filters to view available leads.")
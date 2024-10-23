import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Set the layout to wide mode
st.set_page_config(layout="wide")

# Custom CSS to style the page
st.markdown("""
    <style>
             .stAppHeader {
        background-color: #09355D; /* Change this to your preferred color */
        color: white;
        top:0;
        font-size: 24px;
        text-align: center;
        padding: 40px;
        
    }  
            
              .stSidebar{
            background-color:#ffffff;
            color:white;
            margin-top:90px;
            border-radius:10px;
            font-size: 24px;
            text-align: center;
            border: 1px solid #e0e0e0;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
                       
            
            }
            .stSidebar title{
            color:white;
            }

    # /* Top Navigation Bar */
    # .nav-bar {
    #     background-color: #002C61;
    #     padding: 15px;
    #     color: white;
    #     display: flex;
    #     justify-content: space-between;
    #     align-items: center;
    # }

    # .nav-bar img {
    #     height: 40px;
    # }

    # .nav-right {
    #     display: flex;
    #     align-items: center;
    # }

    # .nav-right img {
    #     border-radius: 50%;
    #     height: 30px;
    #     margin-left: 15px;
    # }

    /* Search bar and filter section */
    .filter-section {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 20px;
    }

    .filter-item {
        margin-right: 20px;
        flex-grow: 1;
    }

    /* Section Styling */
    .section-header {
        font-size: 18px;
        margin-bottom: 10px;
        font-weight: bold;
    }

    </style>
""", unsafe_allow_html=True)




# # Top Navigation Bar
# st.markdown("""
#     <div class="nav-bar">
#         <div>
#             <img src="https://upload.wikimedia.org/wikipedia/commons/5/5f/Nissan_2020_logo.svg" alt="Nissan Logo">
#         </div>
#         <div class="nav-right">
#             <span style="margin-right: 15px;">John Doe</span>
#             <img src="https://www.w3schools.com/howto/img_avatar.png" alt="User Avatar">
#         </div>
#     </div>
# """, unsafe_allow_html=True)

# Title
st.title("Supplier 360° Analysis")

# Filters Section
st.markdown("""
    <div class="filter-section">
        <div class="filter-item">
            <input type="text" placeholder="Search supplier.." style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
        </div>
        <div class="filter-item">
            <select style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
                <option>Select Facility</option>
                <option>SP</option>
                <option>CP</option>
                <option>DP</option>
            </select>
        </div>
        <div class="filter-item">
            <select style="width: 100%; padding: 10px; border-radius: 5px; border: 1px solid #ccc;">
                <option>Select Month</option>
                <option>January</option>
                <option>February</option>
                <option>March</option>
                <option>April</option>
                <option>May</option>
                <option>Jun</option>
                <option>Jul</option>
                
            </select>
        </div>
    </div>
""", unsafe_allow_html=True)

# Dummy Data for Charts
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
performance_data = {
    "Months": months,
    "Impact Score": [50, 60, 55, 70, 80, 75, 90],
    "FIN - Impact": [40, 50, 60, 70, 65, 55, 85],
    "OPS - Impact": [30, 35, 45, 55, 60, 65, 80]
}
ran_shipment_data = {
    "Months": months,
    "Shipment": [200, 300, 400, 350, 375, 450, 500]
}
trend_data = pd.DataFrame({
    "Months": months,
    "Downtime": [12, 16, 8, 18, 20, 14, 24],
    "PPOF": [3, 4, 6, 5, 7, 5, 9],
    "RDR": [5, 6, 5, 8, 9, 7, 10],
    "AETC": [2, 3, 4, 4, 5, 6, 6]
})
financial_data = {
    "Months": months,
    "Cost (in Million $)": [2.5, 3.0, 3.2, 3.5, 4.0, 7.5, 5.0]
}

# Supplier Performance and RAN Shipment side by side
col1, col2 = st.columns(2)

# Supplier Performance Chart
with col1:
    with st.expander("Supplier Performance", expanded=True):
        sort_option = st.selectbox("Sort By:", ["2024", "2023", "2022"], key="supplier_performance_sort")
        fig1 = go.Figure()
        fig1.add_trace(go.Bar(
            x=months, y=performance_data["Impact Score"],
            name="Impact Score",
            marker=dict(
                color="rgb(102,178,255)",
                line=dict(color="rgba(58, 128, 255, 1.0)", width=2),
                opacity=0.9
            )
        ))
        fig1.add_trace(go.Bar(
            x=months, y=performance_data["FIN - Impact"],
            name="FIN - Impact",
            marker=dict(
                color="rgb(255, 128, 128)",
                line=dict(color="rgba(255, 58, 58, 1.0)", width=2),
                opacity=0.9
            )
        ))
        fig1.add_trace(go.Bar(
            x=months, y=performance_data["OPS - Impact"],
            name="OPS - Impact",
            marker=dict(
                color="rgb(128, 255, 128)",
                line=dict(color="rgba(58, 255, 58, 1.0)", width=2),
                opacity=0.9
            )
        ))
        fig1.update_layout(
            barmode='group',
            title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True),
            margin=dict(l=0, r=0, t=40, b=0),
            title_font_size=20,
            title_x=0.5,
            showlegend=True,
            hovermode="closest",
            bargap=0.2,
            bargroupgap=0.1,
            annotations=[
                dict(x=1.30, y=0.55, xref="paper", yref="paper", text="Impact Score < 0.50", showarrow=False,
                     font=dict(color="blue")),
                dict(x=1.30, y=0.48, xref="paper", yref="paper", text="FIN - Impact < 0.50", showarrow=False,
                     font=dict(color="red")),
                dict(x=1.30, y=0.40, xref="paper", yref="paper", text="OPS - Impact < 0.50", showarrow=False,
                     font=dict(color="green"))
            ],
            height=250
        )
        st.plotly_chart(fig1, use_container_width=True)

# RAN Shipment Chart
with col2:
    with st.expander("RAN Shipment", expanded=True):
        sort_option = st.selectbox("Sort By:", ["2024", "2023", "2022"], key="ran_shipment_sort")
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=months, y=ran_shipment_data["Shipment"],
            marker=dict(
                color="rgba(186, 104, 200, 0.7)",
                line=dict(color="rgba(147, 112, 219, 1)", width=2)
            )
        ))
        fig2.update_layout(
            title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True),
            margin=dict(l=0, r=0, t=40, b=0),
            title_font_size=20,
            title_x=0.5,
            showlegend=False,
            hovermode="closest",
            height=250
        )
        st.plotly_chart(fig2, use_container_width=True)
        
        



# Trend Analysis and Financial Impact side by side
col3, col4 = st.columns(2)

# Trend Analysis Chart
with col3:
    with st.expander("Trend Analysis", expanded=True):
        sort_option = st.selectbox("Sort By:", ["2024", "2023", "2022"], key="trend_analysis_sort")
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=trend_data["Months"], y=trend_data["Downtime"], mode='lines+markers',
                                  name="Downtime", line=dict(color="green", width=2)))
        fig3.add_trace(go.Scatter(x=trend_data["Months"], y=trend_data["PPOF"], mode='lines+markers',
                                  name="PPOF", line=dict(color="blue", width=2)))
        fig3.add_trace(go.Scatter(x=trend_data["Months"], y=trend_data["RDR"], mode='lines+markers',
                                  name="RDR", line=dict(color="red", width=2)))
        fig3.add_trace(go.Scatter(x=trend_data["Months"], y=trend_data["AETC"], mode='lines+markers',
                                  name="AETC", line=dict(color="purple", width=2)))
        fig3.update_layout(
            title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True),
            margin=dict(l=0, r=0, t=40, b=0),
            title_font_size=20,
            title_x=0.5,
            hovermode="closest",
            height=250
        )
        st.plotly_chart(fig3, use_container_width=True)

# Financial Impact Chart
with col4:
    with st.expander("Financial Impact", expanded=True):
        sort_option = st.selectbox("Sort By:", ["2024", "2023", "2022"], key="financial_impact_sort")
        fig4 = go.Figure()
        fig4.add_trace(go.Scatter(
            x=months, y=financial_data["Cost (in Million $)"], mode='lines+markers',
            line=dict(color="blue", width=3), marker=dict(size=8, color="rgba(58, 128, 255, 1.0)")
        ))
        fig4.update_layout(
            title="",
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            xaxis=dict(showgrid=False),
            yaxis=dict(showgrid=True),
            margin=dict(l=0, r=0, t=40, b=0),
            title_font_size=20,
            title_x=0.5,
            hovermode="closest",
            height=250
        )
        st.plotly_chart(fig4, use_container_width=True)









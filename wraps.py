import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(layout="wide")

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

    .section-header {
        font-size: 18px;
        margin-bottom: 10px;
        font-weight: bold;
    }

    .metric-box {
        padding: 15px;
        margin: 10px;
        border-radius: 10px;
        background-color: #f9f9f9;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }

    .metric-value {
        font-size: 24px;
        font-weight: bold;
        color: #2c3e50;
    }

    .metric-label {
        font-size: 14px;
        color: #7f8c8d;
    }

    .action-btn {
        padding: 6px 12px;
        background-color: #f0f0f0;
        border: 1px solid #ccc;
        border-radius: 5px;
        cursor: pointer;
        color: #333;
    }

    .action-btn:hover {
        background-color: #e0e0e0;
    }

    .pagination {
        display: flex;
        justify-content: flex-end;
        margin-top: 5px;
        margin-bottom: 5px;
    }

    .pagination a {
        color: #333;
        float: none;
        display: inline-block;
        padding: 5px 10px;
        margin: 0 2px;
        text-decoration: none;
        transition: background-color .3s, transform .2s;
        border: 1px solid #ddd;
        border-radius: 4px;
        font-size: 10px;
    }

    .pagination a.active {
        background-color: #007BFF;
        color: white;
        border: 1px solid #007BFF;
    }

    .pagination a:hover:not(.active) {
        background-color: #f0f0f0;
        transform: scale(1.05);
    }
    .card {
        background-color: #f8f9fa;
        padding: 20px;
        margin: 10px 0;
        border-radius: 10px;
        box-shadow: 0 6px 10px rgba(0,0,0,0.1);
        max-width: 100%;  /* Ensure card doesn't exceed parent width */
        overflow-x: auto; 
        overflow-y:auto;
        
    }
    .card-header {
        font-size: 18px;
            
        
        color: #333;
        margin-bottom: 10px;
    }
    .action-btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 8px 16px;
        text-align: center;
        text-decoration: none;
        font-size: 12px;
        cursor: pointer;
        border-radius: 4px;
    }
    table {
        width: 100%;
        border-collapse: collapse;
        margin: 5px 0;
        font-size: 14px;
    }
    th, td {
        padding: 8px 12px;
        border-bottom: 1px solid #ddd;
        border-collapse: collapse;
        text-align:center;
    }
    th {
        background-color: #f2f2f2;
    }
    .css-1d391kg, .css-1v3fvcr, .css-1lcbmhc {  
        width: 200px;  /* Set the width of the sidebar */
    }

    /* Optional: adjust the width of the main content area */
    .css-1g3uw71 {
        margin-left: 120px; /* Adjust margin based on sidebar width */
    }
    .custom-button {
        display: inline-block;
        background-color: #4CAF50; /* Green background */
        color: white; /* White text */
        padding: 10px 20px; /* Padding */
        text-align: center; /* Center text */
        text-decoration: none; /* Remove underline */
        margin: 4px 2px; /* Margin */
        border: none; /* Remove border */
        border-radius: 5px; /* Rounded corners */
        cursor: pointer; /* Pointer cursor on hover */
        width: 100%; /* Full width */
        transition: background-color 0.3s; /* Transition effect */
    }

    .custom-button:hover {
        background-color: #45a049; /* Darker green on hover */
    }
    </style>
""", unsafe_allow_html=True)



# # sidebar
# # Function to switch between pages
# def navigate_to(page_name):
#     st.session_state.page = page_name
#     st.experimental_rerun()  # Rerun the app to reflect the changes

# # Set default page if it doesn't exist
# if 'page' not in st.session_state:
#     st.session_state.page = 'Home'

# with st.sidebar:
#     # Navigation buttons
#     st.markdown('<a class="custom-button" href="supplier.py" onclick="window.location.reload();">Dashboard</a>', unsafe_allow_html=True)
#     st.markdown('<a class="custom-button" href="vin_management.py" onclick="window.location.reload();">Vin Management</a>', unsafe_allow_html=True)

# # Display content based on the current page
# if st.session_state.page == 'Dashboard':
#     st.title("Dashboard")
#     # Dashboard content goes here
#     st.write("This is the Dashboard page.")
# elif st.session_state.page == 'Vin Management':
#     import pages.vin_management as vin_management
#     vin_management.run()
#     # st.title("Vin Management")
#     # # Vin Management content goes here
#     # st.write("This is the Vin Management page.")
# else:
#     st.title("Home")
#     st.write("This is the Home page.")


# st.markdown("""
#     <div class="nissan-image">
#         <div>
#             <img src="assets/nissan.png" alt="Nissan Logo">
#         </div>
       
#     </div>
# """, unsafe_allow_html=True)

# st.markdown("""
#     <div class="stAppHeader">
#         <div class="nissan-image">
#             <img src="assets/nissan.png" alt="Nissan Logo">
#         </div>
#         <h1>Your App Title</h1>
#     </div>
# """, unsafe_allow_html=True)

st.title("WRAPS - Warranty Dashboard")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    country = st.multiselect('Country', ['All', 'USA', 'JPN', 'CAN'], default='USA')
with col2:
    supplier_name = st.multiselect('Supplier Name', ['All',  'AUTOLIV SAFETY', 'HITACHI', 'KI (USA)','PK USA INC'], default='All')
with col3:
    parts_name = st.multiselect('Parts Name', ['All', 'CENTER BEARING BRACKET', 'HEATER UNIT', 'BRAKE TUBE', 'BATTERY','AIR/FUEL RATIO SENSOR','INVERTER','CABIN SEAL','BRAKE SWITCH'], default='All')
with col4:
    vehicle_model = st.multiselect('Vehicle Model', ['All', 'QX55 / NEDM', 'ARMADA', 'ROGUE', 'ALTIMA SEDAN','QX60','SENTRA','KICKS','FRONTIER','TITAN','ARIYA','LEAF'], default='All')
with col5:
    date_range = st.selectbox('Date Range Selector', ['Last 7 Days', 'Last 30 Days', 'Last 90 Days', 'Custom'], index=1)

metric_col1, metric_col2, metric_col3, metric_col4, metric_col5 = st.columns(5)

with metric_col1:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Total Claim Count</div>
        <div class="metric-value">354</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col2:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Total Claim Amount</div>
        <div class="metric-value">$10,298</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col3:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Total Recovery Amount</div>
        <div class="metric-value">$6,458.87</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col4:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Total Parts Amount</div>
        <div class="metric-value">$27,000</div>
    </div>
    """, unsafe_allow_html=True)

with metric_col5:
    st.markdown("""
    <div class="metric-box">
        <div class="metric-label">Total Labour Amount</div>
        <div class="metric-value">$358.43</div>
    </div>
    """, unsafe_allow_html=True)

col1, col2 = st.columns(2)

# with col1:
#     with st.expander("Claim Volume Analysis", expanded=True):
#         report_frequency = st.selectbox('Report Frequency:', ['Monthly', 'Quarterly', 'Yearly'], key='report_frequency_claim_volume')
#         months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
#         total_count = [254, 325, 300, 280, 305, 290, 310]
#         mis_3 = [220, 300, 280, 260, 285, 270, 295]
#         mis_6 = [180, 250, 240, 230, 245, 230, 250]
#         fig = go.Figure()
#         fig.add_trace(go.Bar(x=months, y=total_count, name="Total Count", marker=dict(color="rgba(102, 178, 255, 0.9)", line=dict(color="rgba(58, 128, 255, 1.0)", width=2), opacity=0.9)))
#         fig.add_trace(go.Bar(x=months, y=mis_3, name="3 MIS", marker=dict(color="rgba(46, 204, 113, 0.9)", line=dict(color="rgba(39, 174, 96, 1.0)", width=2), opacity=0.9)))
#         fig.add_trace(go.Bar(x=months, y=mis_6, name="6 MIS", marker=dict(color="rgba(241, 196, 15, 0.9)", line=dict(color="rgba(241, 196, 15, 1.0)", width=2), opacity=0.9)))
#         fig.update_layout(title='', barmode='group', plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", xaxis=dict(showgrid=False), yaxis=dict(showgrid=True), margin=dict(l=0, r=0, t=40, b=0), title_font_size=20, title_x=0.5, showlegend=True, hovermode="x unified", bargap=0.2, bargroupgap=0.1)
#         st.plotly_chart(fig, use_container_width=True)

with col1:
    with st.expander("Claim Volume Analysis", expanded=True):
        report_frequency = st.selectbox('Report Frequency:', ['Monthly', 'Quarterly', 'Yearly'], key='report_frequency_claim_volume')
        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul"]
        total_count = [254, 325, 300, 280, 305, 290, 310]
        mis_3 = [220, 300, 280, 260, 285, 270, 295]
        mis_6 = [180, 250, 240, 230, 245, 230, 250]
        
        # Create the Plotly figure
        fig = go.Figure()
        fig.add_trace(go.Bar(x=months, y=total_count, name="Total Count", 
                             marker=dict(color="rgba(102, 178, 255, 0.9)", 
                                         line=dict(color="rgba(58, 128, 255, 1.0)", width=2), 
                                         opacity=0.9)))
        fig.add_trace(go.Bar(x=months, y=mis_3, name="3 MIS", 
                             marker=dict(color="rgba(46, 204, 113, 0.9)", 
                                         line=dict(color="rgba(39, 174, 96, 1.0)", width=2), 
                                         opacity=0.9)))
        fig.add_trace(go.Bar(x=months, y=mis_6, name="6 MIS", 
                             marker=dict(color="rgba(241, 196, 15, 0.9)", 
                                         line=dict(color="rgba(241, 196, 15, 1.0)", width=2), 
                                         opacity=0.9)))
        
        # Update the layout to reduce height
        fig.update_layout(
            title='',
            barmode='group',
            plot_bgcolor="rgba(0,0,0,0)", 
            paper_bgcolor="rgba(0,0,0,0)", 
            xaxis=dict(showgrid=False), 
            yaxis=dict(showgrid=True), 
            margin=dict(l=0, r=0, t=40, b=0),
            title_font_size=20, 
            title_x=0.5, 
            showlegend=True, 
            hovermode="x unified", 
            bargap=0.2, 
            bargroupgap=0.1,
            height=250  # Set custom height here
        )
        
        # Display the chart in Streamlit
        st.plotly_chart(fig, use_container_width=True)


# with col2:
#     with st.expander("Claim Hotspot Region Analysis", expanded=True):
#         year = st.selectbox("Select Year:", ["2024", "2023", "2022"], key="claim_hotspot")
#         map_data = pd.DataFrame({'lat': [37.77, 38.64, 40.71, 34.05, 41.88], 'lon': [-122.41, -90.19, -74.01, -118.24, -87.63]})
#         st.map(map_data)
with col2:
    with st.expander("Claim Hotspot Region Analysis", expanded=True):
        year = st.selectbox("Select Year:", ["2024", "2023", "2022"], key="claim_hotspot")
        map_data = pd.DataFrame({'lat': [37.77, 38.64, 40.71, 34.05, 41.88], 'lon': [-122.41, -90.19, -74.01, -118.24, -87.63]})
        st.map(map_data, height=250)  # Adjust the height value as needed

col3, col4 = st.columns(2)

with col3:
    with st.expander("Top Supplier by Claims", expanded=True):
        supplier_data = pd.DataFrame({"Supplier": ["DECOSTAR INDUSTRIES INC.", "ABC Inoac", "ABC TECHNOLOGIES", "Hella Automotive", "Mitta"], "Claim Count": [55, 43, 38, 25, 12]})
        fig2 = go.Figure(go.Pie(labels=supplier_data["Supplier"], values=supplier_data["Claim Count"], hole=0.5, marker=dict(colors=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A']), textinfo='percent', hoverinfo='label+percent+value', textfont=dict(size=12)))
        fig2.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=40, b=0), height=250, width=300)
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown("""
        <div class="pagination">
            <a href="#">&laquo;</a>
            <a href="#" class="active">1</a>
            <a href="#">2</a>
            <a href="#">3</a>
            <a href="#">4</a>
            <a href="#">...</a>
            <a href="#">10</a>
            <a href="#">&raquo;</a>
        </div>
        """, unsafe_allow_html=True)

with col4:
    with st.expander("Top Issue Category by Claims", expanded=True):
        issue_data = pd.DataFrame({"Issue Category": ["Die Pusher Fails", "Process Failure", "No Labels", "Insert Direction", "Mitta"], "Issue Count": [55, 42, 37, 23, 15]})
        fig3 = go.Figure(go.Pie(labels=issue_data["Issue Category"], values=issue_data["Issue Count"], hole=0.5, marker=dict(colors=['#FF6692', '#19D3F3', '#FF97FF', '#FECB52', '#FFA15A']), textinfo='percent', hoverinfo='label+percent+value', textfont=dict(size=12)))
        fig3.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", margin=dict(l=0, r=0, t=40, b=0), height=250, width=300)
        st.plotly_chart(fig3, use_container_width=True)
        st.markdown("""
        <div class="pagination">
            <a href="#">&laquo;</a>
            <a href="#" class="active">1</a>
            <a href="#">2</a>
            <a href="#">3</a>
            <a href="#">4</a>
            <a href="#">...</a>
            <a href="#">10</a>
            <a href="#">&raquo;</a>
        </div>
        """, unsafe_allow_html=True)

col5, col6 = st.columns(2)

with col5:
    with st.expander("Top Issue Parts", expanded=True):
        parts_data = pd.DataFrame({"Parts": ["AC", "Fuel Pump", "Safety Bags", "Headlight", "Engine"], "Issue Percentage": [95, 86, 64, 52, 78]})
        fig4 = go.Figure(go.Bar(y=parts_data["Parts"], x=parts_data["Issue Percentage"], orientation='h', marker=dict(color='rgba(44, 160, 44, 0.7)', line=dict(color='rgba(44, 160, 44, 1.0)', width=2)), text=parts_data["Issue Percentage"]))
        fig4.update_traces(marker=dict(line=dict(width=2)), textposition='auto')
        fig4.update_layout(xaxis_title="Issue Percentage", yaxis_title="Parts", bargap=0.5, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", hovermode="closest", margin=dict(l=0, r=0, t=40, b=0),height=250)
        st.plotly_chart(fig4, use_container_width=True)
        st.markdown("""
        <div class="pagination">
            <a href="#">&laquo;</a>
            <a href="#" class="active">1</a>
            <a href="#">2</a>
            <a href="#">3</a>
            <a href="#">4</a>
            <a href="#">...</a>
            <a href="#">10</a>
            <a href="#">&raquo;</a>
        </div>
        """, unsafe_allow_html=True)

with col6:
    with st.expander("Top Issue Models", expanded=True):
        models_data = pd.DataFrame({"Model": ["Altima", "Path Finder", "Maxima", "Leaf", "Sunny"], "Issue Percentage": [95, 86, 64, 52, 78]})
        fig5 = go.Figure(go.Bar(y=models_data["Model"], x=models_data["Issue Percentage"], orientation='h', marker=dict(color='rgba(255, 159, 64, 0.7)', line=dict(color='rgba(255, 159, 64, 1.0)', width=2)), text=models_data["Issue Percentage"]))
        fig5.update_traces(marker=dict(line=dict(width=2)), textposition='auto')
        fig5.update_layout(xaxis_title="Issue Percentage", yaxis_title="Models", bargap=0.5, plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)", hovermode="closest", margin=dict(l=0, r=0, t=40, b=0),height=250)
        st.plotly_chart(fig5, use_container_width=True)
        st.markdown("""
        <div class="pagination">
            <a href="#">&laquo;</a>
            <a href="#" class="active">1</a>
            <a href="#">2</a>
            <a href="#">3</a>
            <a href="#">4</a>
            <a href="#">...</a>
            <a href="#">10</a>
            <a href="#">&raquo;</a>
        </div>
        """, unsafe_allow_html=True)

# with st.expander("Warranty Claim Summary", expanded=True):
#     claim_summary = pd.DataFrame({
#         "VIN Number": ["JN1BV7AR1EM696855"] * 5,
#         "Model Name": ["Altima"] * 5,
#         "Model Year": [2020] * 5,
#         "State": ["TN"] * 5,
#         "Claim Number": ["53135102"] * 5,
#         "Claim Open Date": ["Nov 29, 2021"] * 5,
#         "Claim Inservice Date": ["Mar 29, 2022"] * 5,
#         "Part Name": ["Fuel Pump"] * 5,
#         "Supplier Name": ["Decostar"] * 5,
#         "Issue Category": ["Filter Issue"] * 5,
#         "Action": ['<button class="action-btn">View</button>'] * 5
#     })
#     st.markdown(claim_summary.to_html(escape=False), unsafe_allow_html=True)

# with st.expander("Warranty Claim Summary", expanded=True):
#     claim_summary = pd.DataFrame({
#         "VIN Number": ["JN1BV7AR1EM696855"] * 5,
#         "Model Name": ["Altima"] * 5,
#         "Model Year": [2020] * 5,
#         "State": ["TN"] * 5,
#         "Claim Number": ["53135102"] * 5,
#         "Claim Open Date": ["Nov 29, 2021"] * 5,
#         "Claim Inservice Date": ["Mar 29, 2022"] * 5,
#         "Part Name": ["Fuel Pump"] * 5,
#         "Supplier Name": ["Decostar"] * 5,
#         "Issue Category": ["Filter Issue"] * 5,
#         "Action": ['<button class="action-btn">View</button>'] * 5
#     })
#     st.markdown(claim_summary.to_html(escape=False), unsafe_allow_html=True)





# ----------------------------------------------------------------------------------------------------
# with st.container():
#     st.markdown("""
#     <div class="card">
#         <div class="card-header">Warranty Claim Summary</div>
#     """, unsafe_allow_html=True)

#     # Sample DataFrame with claims data
#     claim_summary = pd.DataFrame({
#         "VIN Number": ["JN1BV7AR1EM696855"] * 5,
#         "Model Name": ["Altima"] * 5,
#         "Model Year": [2020] * 5,
#         "State": ["TN"] * 5,
#         "Claim Number": ["53135102"] * 5,
#         "Claim Open Date": ["Nov 29, 2021"] * 5,
#         "Claim Inservice Date": ["Mar 29, 2022"] * 5,
#         "Part Name": ["Fuel Pump"] * 5,
#         "Supplier Name": ["Decostar"] * 5,
#         "Issue Category": ["Filter Issue"] * 5,
#         "Action": ['<button class="action-btn">View</button>'] * 5
#     })

#     # Display the table inside the card
#     st.markdown(claim_summary.to_html(escape=False, index=False), unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)




claim_summary = pd.DataFrame({
    "VIN Number": ["JN1BV7AR1EM696855"] * 5,
    "Model Name": ["Altima"] * 5,
    "Model Year": [2020] * 5,
    "State": ["TN"] * 5,
    "Claim Number": ["53135102"] * 5,
    "Claim Open Date": ["Nov 29, 2021"] * 5,
    "Claim Inservice Date": ["Mar 29, 2022"] * 5,
    "Part Name": ["Fuel Pump"] * 5,
    "Supplier Name": ["Decostar"] * 5,
    "Issue Category": ["Filter Issue"] * 5,
    "Action": ['<button class="action-btn">View</button>'] * 5
})

# Create the card layout
card_html = """
<div class="card">
    <div class="card-header">Warranty Claim Summary</div>
    {table}
</div>
"""

# Insert the DataFrame table into the card
table_html = claim_summary.to_html(escape=False, index=False)

# Display the card with the table inside
st.markdown(card_html.format(table=table_html), unsafe_allow_html=True)
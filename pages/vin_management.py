import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide")

# CSS Styling for appealing UI
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
    /* General Page Styling */
    .search-bar {
        width: 35%;
        padding: 12px;
        border-radius: 8px;
        border: 1px solid #ccc;
        font-size: 14px;
        margin-bottom: 20px;
        margin-right: 20px;
    
    }

    .controls-section {
        display: flex;
        align-items: center;
        gap: 10px;
    }

    .control-item button {
        background-color: #002C61;
        border: none;
        padding: 8px 16px;
        border-radius: 8px;
        color: white;
        cursor: pointer;
        font-size: 14px;
        transition: background-color 0.3s ease;
    }

    .control-item button:hover {
        background-color: #004A9F;
    }

    /* Styling for VIN Summary Section */
    .vin-summary-content {
        
        padding: 0px;
       
        display: grid;
        grid-template-columns: repeat(4, 1fr);
        gap: 12px;
        margin-bottom: 10px;
    }

    .vin-item {
        background-color: #f4f4f4;
        padding: 15px;
        border-radius: 8px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.1);
        text-align: left;
    }

    /* Styling for the Claim Summary Table */
    .claim-summary {
        width: 100%;
        border-collapse: collapse;
        margin-top: 10px;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.1);
    }

    .claim-summary th {
        background-color: #002C61;
        color: white;
        padding: 12px;
        text-align: left;
    }

    .claim-summary td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
        background-color: #f9f9f9;
    }

    .claim-summary tr:nth-child(even) td {
        background-color: #f3f6fa;
    }

    .claim-summary tr:hover td {
        background-color: #e1edff;
        color: #002C61;
        font-weight: bold;
    }

    .claim-summary-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #fff;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        margin-top: 10px;
    }

    /* Styling for Intelligence Analysis */
    .intelligence-bar {
        background-color: #DAA520;
        border-radius: 8px;
        padding: 12px;
        color: white;
        font-weight: bold;
        font-size: 18px;
        text-align: left;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }

    .intelligence-checkbox {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        padding: 12px;
        margin-top:10px;
        margin-bottom: 10px;
        background-color: #f7f7f7;
        border-radius: 8px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }

    .run-button {
        background-color: #DAA520;
        position: absolute;
        right:0;
        
        align-items: center;
        color: white;
        padding: 12px;
        border: none;
        border-radius: 8px;
        cursor: pointer;
        width: 25%;
        margin-bottom: 20px;
        font-size: 16px;
        font-weight: bold;
        transition: background-color 0.3s ease;
    }

    .run-button:hover {
        background-color: #004A9F;
    }

    .details-box {
        background-color: #f7f7f7;
        border-radius: 8px;
        padding: 15px;
        margin-top: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }

    /* Custom styles for expander headers */
    .expander-header {
        background-color: #002C61;
        color: white;
        padding: 15px;
        border-radius: 10px;
        font-size: 18px;
        margin-bottom: 10px;
        cursor: pointer;
    }

    /* Styling for the Part Summary Table */
    .part-summary {
        width: 100%;
        border-collapse: collapse;
        margin-top: 60px;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
    }

    .part-summary th {
        background-color: #002C61;
        color: white;
        padding: 12px;
        text-align: left;
    }

    .part-summary td {
        padding: 12px;
        border-bottom: 1px solid #ddd;
        background-color: #f9f9f9;
    }

    .part-summary tr:nth-child(even) td {
        background-color: #f3f6fa;
    }

    .part-summary tr:hover td {
        background-color: #e1edff;
        color: #002C61;
        font-weight: bold;
    }

    .part-summary th:nth-child(1),
    .part-summary td:nth-child(1) {
        text-align: center;
    }

    .part-summary td a {
        color: #0066cc;
        text-decoration: none;
    }

    .part-summary td a:hover {
        text-decoration: underline;
    }

    </style>
""", unsafe_allow_html=True)

# VIN Summary Section
st.markdown("""
    <h2 style='text-align: left;'>VIN Analysis</h2>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center;">
        <input type="text" class="search-bar" placeholder="Search VIN">
    </div>
""", unsafe_allow_html=True)


with st.expander("VIN Summary", expanded=True):
    st.markdown("""
        <div class="vin-summary-content">
            <div class="vin-item">
                <strong>VIN Number:</strong><br>224567894
            </div>
            <div class="vin-item">
                <strong>Model Year:</strong><br>2020
            </div>
            <div class="vin-item">
                <strong>Color:</strong><br>Blue
            </div>
            <div class="vin-item">
                <strong>Country:</strong><br>United States
            </div>
            <div class="vin-item">
                <strong>Engine Model Code:</strong><br>VQ37
            </div>
            <div class="vin-item">
                <strong>Engine Serial Number:</strong><br>246897457
            </div>
            <div class="vin-item">
                <strong>Miles Driven:</strong><br>24
            </div>
            <div class="vin-item">
                <strong>KM Driven:</strong><br>40
            </div>
        </div>
    """, unsafe_allow_html=True)


# Claim Summary Section with Expander and Checkboxes
with st.expander("Claim Summary", expanded=True):
    st.markdown("""
        <div class="expander-box">
            <table class="claim-summary">
                <thead>
                    <tr>
                        <th></th> <!-- For checkbox -->
                        <th>Claim Number</th>
                        <th>Claim Open Date</th>
                        <th>Part Name</th>
                        <th>Issue Category</th>
                        <th>Supplier Name</th>
                        <th>Action</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>53135105</td>
                        <td>Aug 13, 2024</td>
                        <td>Fuel Tank</td>
                        <td>Filter Issue</td>
                        <td>Decostar</td>
                        <td><button>View</button></td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>46893086</td>
                        <td>Aug 13, 2024</td>
                        <td>Front Wheel</td>
                        <td>Front Wheel Alignment</td>
                        <td>ABC Corp</td>
                        <td><button>View</button></td>
                    </tr>
                    <tr>
                        <td><input type="checkbox"></td>
                        <td>46893237</td>
                        <td>Aug 13, 2024</td>
                        <td>Engine</td>
                        <td>Oil Leak Issue</td>
                        <td>Nissan</td>
                        <td><button>View</button></td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)
# Parts Summary Section
with st.expander("Parts Summary", expanded=True):
    # Intelligence Analysis Section with Gold Bar
    st.markdown("""
        <div class="intelligence-bar">Intelligence Analysis</div>
    """, unsafe_allow_html=True)

    # Intelligence Analysis Section content
    st.markdown("""
        <div class="expander-box">
            <div class="intelligence-checkbox">
                <input type="checkbox" checked> Summarization: Summarizing Vehicle information & Parts issues related complaints from customer or service advisor and dealer or technician comments
            </div>
            <div class="intelligence-checkbox">
                <input type="checkbox" checked> RCA Classification (Root Cause Category): Identifying Root Cause Category for each part based on customer complaints and dealer comments
            </div>
            <button class="run-button">Run</button>
        </div>
    """, unsafe_allow_html=True)


    st.markdown("""
        <div class="expander-box">
            <table class="part-summary">
                <thead>
                    <tr>
                        <th>#</th>
                        <th>Claim Number</th>
                        <th>Part Name</th>
                        <th>Customer/Service Advisor Complaint</th>
                        <th>Dealer/Technician Comments</th>
                        <th>Issue Summary</th>
                        <th>Root Cause Category</th>
                        <th>RCA Source System</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>01</td>
                        <td>53135105</td>
                        <td>Fuel Tank</td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>Filter design issue</td>
                        <td>DRIVE</td>
                    </tr>
                    <tr>
                        <td>02</td>
                        <td>46893086</td>
                        <td>Front Wheel</td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>Filter design issue</td>
                        <td>DRIVE</td>
                    </tr>
                    <tr>
                        <td>03</td>
                        <td>46893237</td>
                        <td>Engine</td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>filter issue in fuel pumping system which leads... <a href="#">View More</a></td>
                        <td>Filter design issue</td>
                        <td>DRIVE</td>
                    </tr>
                </tbody>
            </table>
        </div>
    """, unsafe_allow_html=True)
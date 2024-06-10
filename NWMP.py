import pandas as pd
import streamlit as st

# Load the main data
df = pd.read_excel('2023 Data.xlsx')

# Title and Header
st.title('2023 NWMP Data')
st.header('State-wise Data')

# Dropdown for selecting state-wise data
file_name = st.selectbox(label='Choose State Data', options=[
    'ANDHRA PRADESH.xlsx', 'ARUNACHAL PRADESH.xlsx', 'ASSAM.xlsx', 'BIHAR.xlsx',
    'CHHATTISGARH.xlsx', 'DAMAN AND DIU, DADRA AND NAGAR HAVELI.xlsx', 'DELHI.xlsx',
    'GOA.xlsx', 'GUJARAT.xlsx', 'HARYANA.xlsx', 'HIMACHAL PRADESH.xlsx',
    'JAMMU & KASHMIR.xlsx', 'JHARKHAND.xlsx', 'KARNATAKA.xlsx', 'KERALA.xlsx',
    'LAKSHADWEP.xlsx', 'MADHYA PRADESH.xlsx', 'MAHARASHTRA.xlsx', 'MANIPUR.xlsx',
    'MEGHALAYA.xlsx', 'MIZORAM.xlsx', 'NAGALAND.xlsx', 'ODISHA.xlsx',
    'PUDUCHERRY.xlsx', 'PUNJAB.xlsx', 'RAJASTHAN.xlsx', 'SIKKIM.xlsx',
    'TAMIL NADU.xlsx', 'TELANGANA.xlsx', 'TRIPURA.xlsx', 'UTTAR PRADESH.xlsx',
    'UTTARAKHAND.xlsx', 'WEST BENGAL.xlsx'])

# Read selected state-wise data
state_by_data = pd.read_excel(file_name)

# Display the selected state name within the header
#st.header(f'2023 Data Status - {file_name.split(".")[0]}')

# Display state-wise data
st.dataframe(state_by_data)

st.header(f'2023 DATA STATUS - {file_name.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = state_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)

    # Filter the DataFrame to get rows where Min Dissolved Oxygen (mg/L) equals Minimum_DO
    monitoring_location_min_DO = state_by_data.loc[state_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)
    

with col2:
    Maximum_BOD = state_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = state_by_data.loc[state_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col3, col4 = st.columns(2)
with col3:
    Minimum_pH = state_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = state_by_data.loc[state_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col4:
    Maximum_pH = state_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = state_by_data.loc[state_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)


col5, col6 = st.columns(2)
with col5:
    Maximum_FC = state_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = state_by_data.loc[state_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)


with col6:
    Maximum_Arsenic = state_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = state_by_data.loc[state_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)


st.header('Water Body Wise Data')

# Dropdown for selecting water body-wise data
file_name2 = st.selectbox(label='Choose Water Body Data', options=[
    'RIVER.xlsx', 'LAKE.xlsx', 'CANAL.xlsx', 'DRAIN.xlsx', 'GROUND WATER.xlsx',
    'MARINE.xlsx', 'BEACH.xlsx', 'TANK.xlsx', 'RESERVOIR.xlsx', 'STP.xlsx',
    'WETLAND.xlsx', 'SEA.xlsx', 'CREEK.xlsx', 'POND.xlsx',
    'WATER TREATMENT PLANT (RAW WATER).xlsx', 'COSTAL.xlsx'])
water_body_by_data = pd.read_excel(file_name2)
st.dataframe(water_body_by_data)

st.header(f'2023 DATA STATUS - {file_name2.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = water_body_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)
    monitoring_location_min_DO = water_body_by_data.loc[water_body_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)



with col2:
    Maximum_BOD = water_body_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = water_body_by_data.loc[water_body_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col3, col4 = st.columns(2)
with col3:
    Minimum_pH = water_body_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = water_body_by_data.loc[water_body_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col4:
    Maximum_pH = water_body_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = water_body_by_data.loc[water_body_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)

col5, col6 = st.columns(2)
with col5:
    Maximum_FC = water_body_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = water_body_by_data.loc[water_body_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)

with col6:
    Maximum_Arsenic = water_body_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = water_body_by_data.loc[water_body_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)


st.header('River Wise Data')

file_name3 = st.selectbox(label='Choose River Data', options=[
    'GODAVARI.xlsx', 'KRISHNA.xlsx', 'BRAHMAPUTRA.xlsx', 'GANGA.xlsx', 'MAHANANDA.xlsx', 
    'MAHANADI.xlsx', 'YAMUNA.xlsx', 'MAHI.xlsx', 'TAPI.xlsx', 'GHAGGAR.xlsx','BEAS.xlsx', 'SATLUJ.xlsx', 
    'SUBARNAREKHA.xlsx', 'CAUVERY.xlsx', 'BAITARNI.xlsx', 'BRAHMANI.xlsx', 'PENNAR.xlsx', 'CHAMBAL.xlsx', 
    'SABARMATI.xlsx'])
River_by_data = pd.read_excel(file_name3)
st.dataframe(River_by_data)

st.header(f'2023 DATA STATUS - {file_name3.split(".")[0]}')

# Compute metrics based on the selected state-wise data
col1, col2 = st.columns(2)
with col1:
    Minimum_DO = River_by_data['Min Dissolved Oxygen (mg/L)'].min()
    st.metric(label='Minimum Dissolved Oxygen (mg/L)', value=Minimum_DO)
    monitoring_location_min_DO = River_by_data.loc[River_by_data['Min Dissolved Oxygen (mg/L)'] == Minimum_DO, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_DO)
    



with col2:
    Maximum_BOD = River_by_data['Max BOD (mg/L)'].max()
    st.metric(label='Maximum BOD (mg/L)', value=Maximum_BOD)
    monitoring_location_max_BOD = River_by_data.loc[River_by_data['Max BOD (mg/L)'] == Maximum_BOD, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_BOD)

col3, col4 = st.columns(2)
with col3:
    Minimum_pH = River_by_data['Min pH'].min()
    st.metric(label='Minimum pH', value=Minimum_pH)
    monitoring_location_min_pH = River_by_data.loc[River_by_data['Min pH'] == Minimum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_min_pH)

with col4:
    Maximum_pH = River_by_data['Max pH'].max()
    st.metric(label='Maximum pH', value=Maximum_pH)
    monitoring_location_max_pH = River_by_data.loc[River_by_data['Max pH'] == Maximum_pH, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_pH)

col5, col6 = st.columns(2)
with col5:
    Maximum_FC = River_by_data['Max Fecal Coliform  (MPN/100ml)'].max()
    st.metric(label='Max Fecal Coliform  (MPN/100ml)', value=Maximum_FC)
    monitoring_location_max_FC = River_by_data.loc[River_by_data['Max Fecal Coliform  (MPN/100ml)'] == Maximum_FC, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_FC)

with col6:
    Maximum_Arsenic = River_by_data['Max Arsenic (mg/L)'].max()
    st.metric(label='Maximum Arsenic', value=Maximum_Arsenic)
    monitoring_location_max_Ar = River_by_data.loc[River_by_data['Max Arsenic (mg/L)'] == Maximum_Arsenic, 'Monitoring Location'].iloc[0]
    st.write("Location:",monitoring_location_max_Ar)


st.header("Maximum BOD (mg/L) Over Monitoring Location")
st.line_chart(River_by_data.set_index('Monitoring Location')[['Max BOD (mg/L)']].assign(Standard_Line=3))

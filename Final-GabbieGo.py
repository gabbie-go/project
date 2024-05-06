#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Name: Gabbie Go
CS230: Section 2
Data: Georgia Bridges
Description:
This program looks at various aspects of the data, usually grouped by county or 
bridge ownership. The queries at the bottom of the program helped me build 
meaningful graphs. The charts showed bridges conditions and their average age, 
and also county traffic. 

"""

import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt 

filepath = '/Users/gabbie/Desktop/spyder/python_project/Georgia_Bridges_10000_sample.csv'
df = pd.read_csv(filepath)


st.title('Bridges in Georgia')
    
tab1, tab2, tab3 = st.tabs(["Home", "Widgets", "Vizualisations" ])


with st.sidebar:
    st.subheader("A few quick questions about bridges!")
    add_radio = st.radio(
        "Do you like bridges?",
        ("Yes", "No")
    )
    bridge = st.text_input("Favourite bridge?", "")
    st.write("Your favourite bridge is:", bridge)

with tab1:
    st.title(''':blue[Welcome to my analysis of bridges in Georgia!]''')
    st.write("Please visit the other tabs to look at insights on the data")
    st.balloons()
    def map():    
        st.subheader("Georgia State Map")
        st.write("This is a map of Georgia State and counties included in this dataset!")
    
        # Define latitude and longitude coordinates for specific locations in Georgia
        locations = {
            'Appling County':{'lat':31.7122, 'lon':-82.2583},
            'Atkinson County':{'lat':31.2932, 'lon':-82.8641},
            'Bacon County':{'lat':31.5412, 'lon':-82.4319},
            'Baker County':{'lat':31.2816, 'lon':-84.4803},
            'Baldwin County':{'lat':33.0338, 'lon':-83.2934},
            'Banks County':{'lat':34.3785, 'lon':-83.4644},
            'Barrow County':{'lat':34.0143, 'lon':-83.6987},
            'Bartow County':{'lat':34.2660, 'lon':-84.8151},
            'Ben Hill County':{'lat':31.7664, 'lon':-83.2078},
            'Berrien County':{'lat':31.3119, 'lon':-83.2078},
            'Bibb County':{'lat':32.7866, 'lon':-83.7199},
            'Bleckley County':{'lat':32.4088, 'lon':-83.3789},
            'Brantley County':{'lat':31.1511, 'lon':-81.9971},
            'Brooks County':{'lat':30.8730, 'lon':-83.5497},
            'Bryan County':{'lat':32.0237, 'lon':-81.4718},
            'Bulloch County':{'lat':32.3596, 'lon':-81.7787},
            'Burke County':{'lat':33.0888, 'lon':-81.9535},
            'Butts County':{'lat':33.2691, 'lon':-83.9533},
            'Calhoun County':{'lat':31.5622, 'lon':-84.6479},
            'Camden County':{'lat':30.8983, 'lon':-81.6035},
            'Candler County':{'lat':32.4242, 'lon':-82.0843},
            'Carroll County':{'lat':33.5642, 'lon':-85.0649},
            'Catoosa County':{'lat':34.8982, 'lon':-85.1479},
            'Charlton County':{'lat':30.7917, 'lon':-82.0843},
            'Chatham County':{'lat':31.9994, 'lon':-81.1196},
            'Chattahoochee County':{'lat':32.2952, 'lon':-84.8151},
            'Chattooga County':{'lat':34.4633, 'lon':-85.3136},
            'Cherokee County':{'lat':34.2515, 'lon':-84.4803},
            'Clarke County':{'lat':33.9519, 'lon':-83.3576},
            'Clay County':{'lat':31.6448, 'lon':-85.0026},
            'Clayton County':{'lat':33.5572, 'lon':-84.3752},
            'Clinch County':{'lat':30.9717, 'lon':-82.8210},
            'Cobb County':{'lat':33.8999, 'lon':-84.5641},
            'Coffee County':{'lat':31.5182, 'lon':-82.8210},
            'Colquitt County':{'lat':31.2073, 'lon':-83.8473},
            'Columbia County':{'lat':33.5099, 'lon':-82.2583},
            'Cook County':{'lat':31.1428, 'lon':-83.4644},
            'Coweta County':{'lat':33.3717, 'lon':-84.7316},
            'Crawford County':{'lat':32.7091, 'lon':-83.9744},
            'Crisp County':{'lat':31.8876, 'lon':-83.8049},
            'Dade County':{'lat':34.9109, 'lon':-85.4788},
            'Dawson County':{'lat':34.4129, 'lon':-84.1435},
            'Decatur County':{'lat':30.8720, 'lon':-84.5222},
            'DeKalb County':{'lat':33.7956, 'lon':-84.2279},
            'Dodge County':{'lat':32.1287, 'lon':-83.2078},
            'Dooly County':{'lat':32.1593, 'lon':-83.8049},
            'Dougherty County':{'lat':31.5439, 'lon':-84.2279},
            'Douglas County':{'lat':33.7290, 'lon':-84.7316},
            'Early County':{'lat':31.3901, 'lon':-84.8985},
            'Echols County':{'lat':30.7503, 'lon':-82.9502},
            'Effingham County':{'lat':32.3781, 'lon':-81.3839},
            'Elbert County':{'lat':34.0795, 'lon':-82.8641},
            'Emanuel County':{'lat':32.5727, 'lon':-82.3018},
            'Evans County':{'lat':32.1427, 'lon':-81.9098},
            'Fannin County':{'lat':34.8580, 'lon':-84.2279},
            'Fayette County':{'lat':33.4502, 'lon':-84.4803},
            'Floyd County':{'lat':34.2829, 'lon':-85.2308},
            'Forsyth County':{'lat':34.2359, 'lon':-84.1435},
            'Franklin County':{'lat':34.3646, 'lon':-83.2078},
            'Fulton County':{'lat':33.8034, 'lon':-84.3963},
            'Gilmer County':{'lat':34.6935, 'lon':-84.4803},
            'Glascock County':{'lat':33.2423, 'lon':-82.6267},
            'Glynn County':{'lat':31.2624, 'lon':-81.6035},
            'Gordon County':{'lat':34.4892, 'lon':-84.856},
            'Grady County':{'lat':30.9050, 'lon':-84.2279},
            'Greene County':{'lat':33.5187, 'lon':-83.1649},
            'Gwinnett County':{'lat':33.9191, 'lon':-84.0167},
            'Habersham County':{'lat':34.6479, 'lon':-83.5497},
            'Hall County':{'lat':34.3078, 'lon':-83.8049},
            'Hancock County':{'lat':33.2883, 'lon':-83.0361},
            'Haralson County':{'lat':33.7923, 'lon':-85.1894},
            'Harris County':{'lat':32.7033, 'lon':-84.8568},
            'Hart County':{'lat':34.3500, 'lon':-82.9502},
            'Heard County':{'lat':33.2990, 'lon':-85.1479},
            'Henry County':{'lat':33.4348, 'lon':-84.1435},
            'Houston County':{'lat':32.4220, 'lon':-83.6348},
            'Irwin County':{'lat':31.5893, 'lon':-83.2934},
            'Jackson County':{'lat':34.1175, 'lon':-83.5497},
            'Jasper County':{'lat':33.3247, 'lon':-83.7199},
            'Jeff Davis County':{'lat':31.8235, 'lon':-82.6051},
            'Jefferson County':{'lat':33.0741, 'lon':-82.4319},
            'Jenkins County':{'lat':32.7781, 'lon':-81.9971},
            'Johnson County':{'lat':32.7308, 'lon':-82.6915},
            'Jones County':{'lat':33.0003, 'lon':-83.5070},
            'Lamar County':{'lat':33.0766, 'lon':-84.1435},
            'Lanier County':{'lat':31.0291, 'lon':-83.0361},
            'Laurens County':{'lat':32.4330, 'lon':-82.9932},
            'Lee County':{'lat':31.8128, 'lon':-84.1435},
            'Liberty County':{'lat':31.8430, 'lon':-81.4718},
            'Lincoln County':{'lat':33.7875, 'lon':-82.4319},
            'Long County':{'lat':31.7756, 'lon':-81.8224},
            'Lowndes County':{'lat':30.8600, 'lon':-83.2934},
            'Lumpkin County':{'lat':34.5814, 'lon':-83.9744},
            'Macon County':{'lat':32.3524, 'lon':-84.0590},
            'Madison County':{'lat':34.0990, 'lon':-83.2078},
            'Marion County':{'lat':32.3281, 'lon':-84.5222},
            'McDuffie County':{'lat':33.5259, 'lon':-82.5186},
            'McIntosh County':{'lat':31.4748, 'lon':-81.3839},
            'Meriwether County':{'lat':33.0561, 'lon':-84.6897},
            'Miller County':{'lat':31.2008, 'lon':-84.7316},
            'Mitchell County':{'lat':31.2230, 'lon':-84.1857},
            'Monroe County':{'lat':32.9747, 'lon':-83.8897},
            'Montgomery County':{'lat':32.1802, 'lon':-82.5186},
            'Morgan County':{'lat':33.5794, 'lon':-83.4644},
            'Murray County':{'lat':34.7928, 'lon':-84.7316},
            'Muscogee County':{'lat':32.4794, 'lon':-84.8985},
            'Newton County':{'lat':33.5544, 'lon':-83.8473},
            'Oconee County':{'lat':33.8232, 'lon':-83.4430},
            'Oglethorpe County':{'lat':33.9120, 'lon':-83.0361},
            'Paulding County':{'lat':33.9142, 'lon':-84.8985},
            'Peach County':{'lat':32.5893, 'lon':-83.8261},
            'Pickens County':{'lat':34.4497, 'lon':-84.4593},
            'Pierce County':{'lat':31.3438, 'lon':-82.1714},
            'Pike County':{'lat':33.0882, 'lon':-84.3963},
            'Polk County':{'lat':34.0132, 'lon':-85.1479},
            'Pulaski County':{'lat':32.2326, 'lon':-83.4644},
            'Putnam County':{'lat':33.3070, 'lon':-83.3789},
            'Quitman County':{'lat':31.8486, 'lon':-84.9818},
            'Rabun County':{'lat':34.9027, 'lon':-83.3789},
            'Randolph County':{'lat':31.7913, 'lon':-84.6897},
            'Richmond County':{'lat':33.3205, 'lon':-82.0843},
            'Rockdale County':{'lat':33.6752, 'lon':-84.0379},
            'Schley County':{'lat':32.2736, 'lon':-84.3121},
            'Screven County':{'lat':32.7075, 'lon':-81.6035},
            'Seminole County':{'lat':30.9331, 'lon':-84.8985},
            'Spalding County':{'lat':33.2637, 'lon':-84.3121},
            'Stephens County':{'lat':34.5459, 'lon':-83.2934},
            'Stewart County':{'lat':32.1141, 'lon':-84.8151},
            'Sumter County':{'lat':31.9982, 'lon':-84.2279},
            'Talbot County':{'lat':32.6891, 'lon':-84.5222},
            'Taliaferro County':{'lat':33.5698, 'lon':-82.8856},
            'Tattnall County':{'lat':32.0635, 'lon':-82.0843},
            'Taylor County':{'lat':32.5407, 'lon':-84.2279},
            'Telfair County':{'lat':31.8908, 'lon':-82.9932},
            'Terrell County':{'lat':31.7370, 'lon':-84.4803},
            'Thomas County':{'lat':30.8417, 'lon':-83.8473},
            'Tift County':{'lat':31.4206, 'lon':-83.5497},
            'Toombs County':{'lat':32.0795, 'lon':-82.3452},
            'Towns County':{'lat':34.9208, 'lon':-83.7199},
            'Treutlen County':{'lat':32.3870, 'lon':-82.5835},
            'Troup County':{'lat':33.0699, 'lon':-85.0233},
            'Turner County':{'lat':31.6977, 'lon':-83.6348},
            'Twiggs County':{'lat':32.6836, 'lon':-83.4644},
            'Union County':{'lat':34.8458, 'lon':-83.9744},
            'Upson County':{'lat':32.9048, 'lon':-84.3121},
            'Walker County':{'lat':34.6858, 'lon':-85.3550},
            'Walton County':{'lat':33.7709, 'lon':-83.7199},
            'Ware County':{'lat':31.1344, 'lon':-82.4753},
            'Warren County':{'lat':33.4470, 'lon':-82.6915},
            'Washington County':{'lat':32.9627, 'lon':-82.8210},
            'Wayne County':{'lat':31.5092, 'lon':-81.9098},
            'Webster County':{'lat':32.0130, 'lon':-84.5641},
            'Wheeler County':{'lat':32.1000, 'lon':-82.6915},
            'White County':{'lat':34.6568, 'lon':-83.7199},
            'Whitfield County':{'lat':34.8034, 'lon':-84.9818},
            'Wilcox County':{'lat':31.9612, 'lon':-83.4644},
            'Wilkes County':{'lat':33.8083, 'lon':-82.7779},
            'Wilkinson County':{'lat':32.8025, 'lon':-83.1649},
            'Worth County':{'lat':31.5282, 'lon':-83.8897}
        }
    
        # Create a DataFrame from the locations dictionary
        dframe = pd.DataFrame(locations).T
        st.map(dframe)
    
    map()


with tab2:
    def year_built():
        st.subheader("Bridges Built per Year")
        slider_range = st.slider("Please pick a year to see how many bridges were built then", min_value=1885, max_value=2022, value=1954)
        bridge_count = {1960: 333, 1965: 244, 1980: 237, 1970: 199, 1950: 195,1955: 191, 1990: 187,
                        1959: 181, 1976: 173, 1964: 170, 1988: 169, 1963: 169, 1958: 168, 1966: 164,
                        1962: 159, 1987: 158, 1984: 157, 1974: 156, 1968: 156, 1969: 155, 1991: 150,
                        1995: 150, 1992: 146, 1977: 145, 1993: 145, 1979: 141, 1986: 139, 1967: 139,
                        1985: 138, 1996: 134, 1978: 133, 1989: 133, 1961: 128, 1975: 122, 1994: 119, 
                        1971: 117, 2005: 115, 1956: 113, 1999: 113, 1940: 108, 2006: 106, 1957: 106,
                        1972: 105, 1973: 104, 2008: 101, 2007: 99, 1983: 99, 1954: 98, 1997: 98, 1982: 98,
                        2000: 94, 1998: 93, 2003: 91, 2009: 89, 2001: 89, 2010: 88, 2004: 88, 1981: 86,
                        1952: 78, 2002: 77, 1938: 77, 2019: 75, 2015: 74, 1948: 70, 2017: 69, 1949: 68,
                        2021: 66, 2012: 63, 2018: 61, 2011: 61, 2016: 60, 2014: 60, 1935: 57, 1936: 57,
                        1953: 55, 2013: 53, 2020: 53, 1937: 51, 1928: 46, 1931: 43, 1939: 43, 1941: 42,
                        1932: 41, 1951: 41, 1930: 39, 1933: 35, 1947: 30, 1934: 27, 1927: 27, 1942: 26,
                        1929: 24, 1926: 23, 1945: 21, 1946: 17, 1943: 12, 1944: 12, 1920: 12, 1921: 10,
                        1922: 10, 1923: 9, 1925: 7, 2022: 6, 1924: 6, 1918: 5, 1914: 4, 1911: 3, 1915: 2,
                        1912: 2, 1916: 2, 1897: 1, 1919: 1, 1906: 1, 1900: 1, 1891: 1, 1910: 1, 1885: 1
    }
        if slider_range not in bridge_count:
            st.write('No bridges were built in', slider_range)
        else:
            st.write(f'There were {bridge_count[slider_range]} bridges built in {slider_range}')
        
    year_built()
    
    st.divider()
    
    def bridge_county():
        st.subheader("Bridge Owners")
        options = st.multiselect(
        "Please choose an owner",
        ['County Highway Agency','State Highway Agency','City or Municipal Highway Agency',
        'Army','U.S. Forest Service','State Park, Forest, or Reservation Agency','Railroad',
        'Other Public Entity (i.e. Airport or Transit Authority)','National Park Service',
        'Navy/Marines','Town or Township Highway Agency', 'Corps of Engineers (Civil)',
        'Other State Agencies','Private (Other Than Railroad)','Tennessee Valley Authority'])
        owners = {
        'County Highway Agency': 4720,
        'State Highway Agency': 4557,
        'City or Municipal Highway Agency': 534,
        'Army': 95,
        'U.S. Forest Service': 37,
        'State Park, Forest, or Reservation Agency': 13,
        'Railroad': 13,
        'Other Public Entity (i.e. Airport or Transit Authority)': 8,
        'National Park Service': 5,
        'Navy/Marines': 4,
        'Town or Township Highway Agency': 4,
        'Corps of Engineers (Civil)': 4,
        'Other State Agencies': 2,
        'Private (Other Than Railroad)': 2,
        'Tennessee Valley Authority': 1
    }
        total_bridges = sum(owners.get(option, 0) for option in options)
    
        st.write(f"Selected owners: {', '.join(options)}")
        st.write(f"Total bridges owned: {total_bridges}")
       
        for option in options:
            if option in owners:
                st.write(f"{option} owns {owners[option]} bridges")
        
    
    bridge_county()
        
    st.divider()
    
    def lanes():
        st.subheader("Lane Count")
        number = st.number_input("Please insert a whole number from 1-17", value=None, placeholder="Type a number...")
        lanes = {2: 7913, 4: 674, 1: 431, 3: 313, 5: 278, 6: 175, 8: 74, 7: 61, 10: 34, 
                 9: 15, 12: 13, 13: 6, 14: 5, 11: 5, 15: 1, 17: 1, 16: 1}
        
        if number not in lanes:
            st.write(f"There are no bridges with {number} lanes")
        else:
            count = lanes[number]
            st.write(f"There are {count} bridges with {number} lanes")
            
            
    lanes()

    
with tab3:   
    def traffic_plot():
        county_traffic = {
            'Appling County': {'traffic':1613.40,'bridges':47},
            'Atkinson County': {'traffic':1773.28,'bridges':43},
            'Bacon County': {'traffic':1997.46,'bridges':26},
            'Baker County': {'traffic':1077.50,'bridges':16},
            'Baldwin County': {'traffic':4056.17,'bridges':41},
            'Banks County': {'traffic':6852.95,'bridges':61},
            'Barrow County': {'traffic':4778.98,'bridges':49},
            'Bartow County': {'traffic':16160.84,'bridges':148},
            'Ben Hill County': {'traffic':1235.88,'bridges':34},
            'Berrien County': {'traffic':1654.35,'bridges':51},
            'Bibb County': {'traffic':22207.59,'bridges':143},
            'Bleckley County': {'traffic':2164.44,'bridges':18},
            'Brantley County': {'traffic':2012.58,'bridges':31},
            'Brooks County': {'traffic':1619.33,'bridges':66},
            'Bryan County': {'traffic':16337.04,'bridges':54},
            'Bulloch County': {'traffic':4632.99,'bridges':80},
            'Burke County': {'traffic':2118.42,'bridges':59},
            'Butts County': {'traffic':2159.62,'bridges':24},
            'Calhoun County': {'traffic':778.40,'bridges':25},
            'Camden County': {'traffic':11180.77,'bridges':61},
            'Candler County': {'traffic':4832.05,'bridges':39},
            'Carroll County': {'traffic':6037.45,'bridges':123},
            'Catoosa County': {'traffic':16756.03,'bridges':63},
            'Charlton County': {'traffic':2078.44,'bridges':45},
            'Chatham County': {'traffic':23680.07,'bridges':175},
            'Chattahoochee County': {'traffic':1631.16,'bridges':43},
            'Chattooga County': {'traffic':1681.24,'bridges':79},
            'Cherokee County': {'traffic':13562.55,'bridges':117},
            'Clarke County': {'traffic':18629.68,'bridges':63},
            'Clay County': {'traffic':606.15,'bridges':13},
            'Clayton County': {'traffic':28573.89,'bridges':113},
            'Clinch County': {'traffic':1130.35,'bridges':55},
            'Cobb County': {'traffic':26292.62,'bridges':273},
            'Coffee County': {'traffic':1931.01,'bridges':79},
            'Colquitt County': {'traffic':1585.39,'bridges':115},
            'Columbia County': {'traffic':7839.77,'bridges':44},
            'Cook County': {'traffic':4241.91,'bridges':47},
            'Coweta County': {'traffic':8670.01,'bridges':115},
            'Crawford County': {'traffic':4420.31,'bridges':26},
            'Crisp County': {'traffic':5577.67,'bridges':60},
            'Dade County': {'traffic':12707.20,'bridges':50},
            'Dawson County': {'traffic':2145.32,'bridges':31},
            'DeKalb County': {'traffic':38478.53,'bridges':262},
            'Decatur County': {'traffic':3597.72,'bridges':57},
            'Dodge County': {'traffic':1145.80,'bridges':44},
            'Dooly County': {'traffic':2755.33,'bridges':45},
            'Dougherty County': {'traffic':16510.60,'bridges':67},
            'Douglas County': {'traffic':11519.38,'bridges':64},
            'Early County': {'traffic':869.12,'bridges':57},
            'Echols County': {'traffic':746.07,'bridges':28},
            'Effingham County': {'traffic':6542.20,'bridges':49},
            'Elbert County': {'traffic':1000.75,'bridges':60},
            'Emanuel County': {'traffic':2998.31,'bridges':77},
            'Evans County': {'traffic':2377.96,'bridges':27},
            'Fannin County': {'traffic':2412.96,'bridges':75},
            'Fayette County': {'traffic':7701.78,'bridges':51},
            'Floyd County': {'traffic':6721.20,'bridges':133},
            'Forsyth County': {'traffic':10325.66,'bridges':67},
            'Franklin County': {'traffic':4263.56,'bridges':73},
            'Fulton County': {'traffic':32745.81,'bridges':530},
            'Gilmer County': {'traffic':2783.46,'bridges':67},
            'Glascock County': {'traffic':515.33,'bridges':15},
            'Glynn County': {'traffic':15585.82,'bridges':55},
            'Gordon County': {'traffic':6865.24,'bridges':82},
            'Grady County': {'traffic':2528.41,'bridges':70},
            'Greene County': {'traffic':4898.12,'bridges':42},
            'Gwinnett County': {'traffic':22003.15,'bridges':197},
            'Habersham County': {'traffic':3833.71,'bridges':75},
            'Hall County': {'traffic':9225.14,'bridges':97},
            'Hancock County': {'traffic':565.83,'bridges':36},
            'Haralson County': {'traffic':4434.38,'bridges':64},
            'Harris County': {'traffic':4697.58,'bridges':65},
            'Hart County': {'traffic':1483.60,'bridges':43},
            'Heard County': {'traffic':1189.24,'bridges':42},
            'Henry County': {'traffic':22453.16,'bridges':98},
            'Houston County': {'traffic':10678.70,'bridges':77},
            'Irwin County': {'traffic':958.86,'bridges':44},
            'Jackson County': {'traffic':6581.66,'bridges':85},
            'Jasper County': {'traffic':628.63,'bridges':49},
            'Jeff Davis County': {'traffic':2307.61,'bridges':41},
            'Jefferson County': {'traffic':2233.16,'bridges':45},
            'Jenkins County': {'traffic':1866.32,'bridges':38},
            'Johnson County': {'traffic':1010.56,'bridges':34},
            'Jones County': {'traffic':3447.06,'bridges':35},
            'Lamar County': {'traffic':6292.02,'bridges':46},
            'Lanier County': {'traffic':2001.54,'bridges':13},
            'Laurens County': {'traffic':4015.30,'bridges':115},
            'Lee County': {'traffic':2560.74,'bridges':27},
            'Liberty County': {'traffic':8061.67,'bridges':66},
            'Lincoln County': {'traffic':1065.42,'bridges':24},
            'Long County': {'traffic':5135.48,'bridges':31},
            'Lowndes County': {'traffic':8081.46,'bridges':89},
            'Lumpkin County': {'traffic':2393.65,'bridges':37},
            'Macon County': {'traffic':1502.22,'bridges':50},
            'Madison County': {'traffic':1858.36,'bridges':58},
            'Marion County': {'traffic':610.31,'bridges':32},
            'McDuffie County': {'traffic':3324.14,'bridges':29},
            'McIntosh County': {'traffic':13156.14,'bridges':44},
            'Meriwether County': {'traffic':1883.16,'bridges':86},
            'Miller County': {'traffic':858.07,'bridges':29},
            'Mitchell County': {'traffic':1986.88,'bridges':73},
            'Monroe County': {'traffic':10611.19,'bridges':59},
            'Montgomery County': {'traffic':1246.79,'bridges':28},
            'Morgan County': {'traffic':5959.58,'bridges':72},
            'Murray County': {'traffic':2039.60,'bridges':50},
            'Muscogee County': {'traffic':13981.58,'bridges':139},
            'Newton County': {'traffic':8810.08,'bridges':65},
            'Oconee County': {'traffic':6443.33,'bridges':42},
            'Oglethorpe County': {'traffic':724.32,'bridges':37},
            'Paulding County': {'traffic':6062.98,'bridges':56},
            'Peach County': {'traffic':3979.58,'bridges':24},
            'Pickens County': {'traffic':3285.75,'bridges':40},
            'Pierce County': {'traffic':1905.51,'bridges':49},
            'Pike County': {'traffic':1770.80,'bridges':25},
            'Polk County': {'traffic':4575.82,'bridges':79},
            'Pulaski County': {'traffic':1520.43,'bridges':23},
            'Putnam County': {'traffic':2463.50,'bridges':34},
            'Quitman County': {'traffic':658.12,'bridges':16},
            'Rabun County': {'traffic':1921.09,'bridges':74},
            'Randolph County': {'traffic':889.14,'bridges':29},
            'Richmond County': {'traffic':15382.90,'bridges':121},
            'Rockdale County': {'traffic':9367.79,'bridges':29},
            'Schley County': {'traffic':802.67,'bridges':15},
            'Screven County': {'traffic':1224.60,'bridges':50},
            'Seminole County': {'traffic':938.30,'bridges':27},
            'Spalding County': {'traffic':7578.18,'bridges':66},
            'Stephens County': {'traffic':2412.74,'bridges':50},
            'Stewart County': {'traffic':914.12,'bridges':34},
            'Sumter County': {'traffic':2619.49,'bridges':59},
            'Talbot County': {'traffic':1000.19,'bridges':52},
            'Taliaferro County': {'traffic':3454.20,'bridges':25},
            'Tattnall County': {'traffic':1351.56,'bridges':45},
            'Taylor County': {'traffic':1869.02,'bridges':41},
            'Telfair County': {'traffic':1048.40,'bridges':50},
            'Terrell County': {'traffic':903.85,'bridges':39},
            'Thomas County': {'traffic':1928.20,'bridges':122},
            'Tift County': {'traffic':4642.50,'bridges':64},
            'Toombs County': {'traffic':1714.04,'bridges':47},
            'Towns County': {'traffic':1988.67,'bridges':27},
            'Treutlen County': {'traffic':4426.90,'bridges':42},
            'Troup County': {'traffic':8989.97,'bridges':125},
            'Turner County': {'traffic':1387.07,'bridges':41},
            'Twiggs County': {'traffic':6265.71,'bridges':35},
            'Union County': {'traffic':2221.27,'bridges':59},
            'Upson County': {'traffic':966.67,'bridges':39},
            'Walker County': {'traffic':2362.10,'bridges':100},
            'Walton County': {'traffic':5206.53,'bridges':72},
            'Ware County': {'traffic':3683.83,'bridges':60},
            'Warren County': {'traffic':3376.00,'bridges':40},
            'Washington County': {'traffic':1211.04,'bridges':48},
            'Wayne County': {'traffic':2799.64,'bridges':56},
            'Webster County': {'traffic':816.00,'bridges':20},
            'Wheeler County': {'traffic':1158.40,'bridges':35},
            'White County': {'traffic':2682.25,'bridges':59},
            'Whitfield County': {'traffic':11564.49,'bridges':86},
            'Wilcox County': {'traffic':823.00,'bridges':40},
            'Wilkes County': {'traffic':877.66,'bridges':47},
            'Wilkinson County': {'traffic':1867.77,'bridges':47},
            'Worth County': {'traffic':1227.30,'bridges':89},
            }

        st.subheader('Traffic Analysis')
        st.write('Scatter plot of Average Daily Traffic vs. Bridges in County')

        counties = list(county_traffic.keys())
        
        selected_counties = st.multiselect("Select Counties", counties)
        
        if not selected_counties:
            st.warning("Please select one or more county.")
            return
        
        filtered_traffic = {county: county_traffic[county] for county in selected_counties}
        
        traffic_values = [filtered_traffic[county]['traffic'] for county in selected_counties]
        bridge_values = [filtered_traffic[county]['bridges'] for county in selected_counties]
        
        font = {'fontname':'Tahoma'}
        plt.scatter(bridge_values, traffic_values, label='Counties', color='blue')

        fig, ax = plt.subplots(figsize=(10, 8))
        ax.scatter(bridge_values, traffic_values, label='Counties', color='blue', alpha=0.7)
        
        ax.set_title("Average Bridge Traffic by County",**font, weight='bold')
        ax.set_xlabel("Bridges in County",**font)
        ax.set_ylabel("Average Daily Traffic",**font)
        ax.grid(True)
        
        for i, txt in enumerate(selected_counties):
            ax.annotate(txt, (bridge_values[i], traffic_values[i]), fontsize=9)
        
        ax.legend()
        
        st.pyplot(fig)
        
    traffic_plot()
        
    with st.expander("See explanation"):
        st.write('''
            The scatter plot above shows the average bridge traffic in each county. 
            There is no correlation between number of bridges and the traffic they recieve.
        ''')
        
    st.divider()
    
    def condition_bar():
        st.subheader('Condition Analysis')
        st.write('Bar Graph Showing Average Age of Bridges Within Each Category')
        
        fig = plt.figure()
        font = {'fontname':'Tahoma'}
        plt.style.use('seaborn-v0_8-whitegrid')
        categories = {'Poor':62.99,'Fair':58.91,'Good':41.21}
        condition_labels = list(categories.keys())
        ages = list(categories.values())
        
        plt.bar(condition_labels, ages, color='skyblue')
        plt.title("Bridge Condition by Age",**font, weight='bold')
        plt.xlabel("Condition",**font)
        plt.ylabel("Bridge Age (yr)",**font)
        plt.show()
        st.pyplot(fig)
        return fig

    condition_bar()
    
    with st.expander("See explanation"):
        st.write('''
            The bar chart demonstrates that on average the bridges in better 
            condition are younger. However, the data is quite spread out and some 
            older bridges have maintained their good condition. The data might 
            be skewed as there are 7471 bridges classified as good, 2338 as fair, 
            and only 191 as poor.
        ''')
    
            
#Calculations
def traffic_sort():
    sorted_df = df.sort_values(by='3 - County Name')
    selected_df = sorted_df.loc[:, ['3 - County Name', '29 - Average Daily Traffic']]
    grouped_df = selected_df.groupby('3 - County Name').mean().round(2)
    print(grouped_df)
    
#traffic_sort()

def county_bridges():    
    sorted_county = df.sort_values(by='3 - County Name')
    county_counts = sorted_county['3 - County Name'].value_counts()
    county_counts_df = county_counts.reset_index()
    county_counts_df.columns = ['County Name', 'Bridge Count']
    sorted_county_counts_df = county_counts_df.sort_values(by='County Name')
    print(sorted_county_counts_df)
    
#county_bridges()

def county_precipitation():
    sorted_df = df.sort_values(by='3 - County Name')
    selected_df = sorted_df.loc[:, ['3 - County Name', 'Total Precipitation']]
    grouped_df = selected_df.groupby('3 - County Name').mean().round(2)
    print(grouped_df)
 
#county_precipitation()

def condition_year():
    sorted_df = df.sort_values(by='CAT10 - Bridge Condition')
    selected_df = sorted_df.loc[:, ['CAT10 - Bridge Condition', 'Bridge Age (yr)']]
    grouped_df = selected_df.groupby('CAT10 - Bridge Condition').mean().round(2)
    print(grouped_df)
    
condition_year()

def counts():
    year = df['27 - Year Built'].value_counts()
    county = df['3 - County Name'].value_counts()
    owner = df['22 - Owner Agency'].value_counts()
    lanes = df['28A - Lanes On the Structure'].value_counts()
    condition = df['CAT10 - Bridge Condition'].value_counts()
    print(owner)

counts()


#Extra Sources
#https://matplotlib.org/stable/users/explain/quick_start.html#a-simple-example
#https://docs.streamlit.io/develop
   
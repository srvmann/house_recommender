import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import seaborn as sns
import pickle


st.set_page_config(page_title = "Viz_demo")

# lat_long_data is used
new_df = pd.read_csv('Datasets/lat_long_included .csv')

# geo map
st.title('Geo map Sector Wise')
group_df = new_df.groupby('sector')[['price','price_per_sqft','built_up_area','latitude','longitude']].mean()

fig = px.scatter_map(group_df, lat="latitude", lon="longitude", color="price_per_sqft", size='built_up_area',
                        color_continuous_scale=px.colors.cyclical.IceFire, zoom=10,
                        map_style="open-street-map",width = 1200,height = 700,
                        hover_name = group_df.index)

st.plotly_chart(fig,use_container_width = True)
st.subheader("Insights from the Map Visualization")
st.write("""
1. Price Distribution:
   - Blue dots represent areas with lower prices (around 5k-10k per square foot).
   - Yellow to red dots represent areas with higher prices (up to 30k+ per square foot).
   - The darker red clusters suggest premium or high-demand areas.

2. Clustering:
   - Higher-priced properties (yellow/red) are concentrated in specific areas, indicating prime locations or upscale neighborhoods.
   - Lower-priced properties (blue) are more widespread, potentially in less developed or suburban areas.

3. Geographic Trends:
   - The central areas of Gurugram show a higher concentration of high-priced properties, suggesting better 
     infrastructure or proximity to commercial hubs. 
   - Outskirts, such as near Manesar, generally display lower price points.

4. Utility:
   - This map can help identify affordable vs. premium property zones.
   - Useful for analyzing location-based trends in property prices, assisting buyers, sellers, 
     or real estate developers.
""")


#wordcloud for amenities (the scrapped data is used)
# using the trained feature text file(on jupyter file)
feature_text = pickle.load(open('Recommender_files/feature_text.pkl','rb'))
st.title('Word_Cloud')

# Generate the word cloud
wordcloud = WordCloud(
    width=800,
    height=800,
    background_color='white',
    stopwords=set(['s']),  # Add stopwords here if needed
    min_font_size=10
).generate(feature_text)

# Plot the word cloud
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.tight_layout(pad=0)

# Display in Streamlit
st.pyplot(plt)

st.subheader("Insights from Word Cloud of Property Amenities")
st.write("""
1. Most Prominent Features:
   - Maintenance Staff, Security, and Visitor Parking are the top features,highlighting their importance.
   - Other notable amenities include Water Storage,Intercom Facility,and Vaastu Compliant.

2. Lifestyle and Wellness:
   - Features like Fitness Centre,GYM Club,and FengShui suggest a focus on enhancing lifestyle.

3. Safety and Environmental Considerations:
   - Amenities such as Fire Alarm,Rain Water Harvesting,and Waste Disposal emphasize safety and eco-friendliness.

4. Diverse Offerings:
   - The variety of amenities caters to different preferences, making the properties attractive to a broader audience.
""")


# area vs price scatter plot
st.title('Scatter plot of Area VS Price')

property_type = st.selectbox("Select Property Type",['flat','house'])

if property_type == 'house':
    fig1 = px.scatter(new_df[new_df['property_type'] == 'house'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    # Show the plot
    st.plotly_chart(fig1,use_container_width = True)
else:
    fig1 = px.scatter(new_df[new_df['property_type'] == 'flat'], x="built_up_area", y="price", color="bedRoom", title="Area Vs Price")
    # Show the plot
    st.plotly_chart(fig1,use_container_width = True)

### Insights from Scatterplots: Area vs. Price
st.subheader("Insights from Scatterplots: Area vs. Price {flats and house}")
st.write("""
1. FLATS :-
    * The price generally increases as the built-up area increases, which is an expected trend.
    * Most data points are concentrated in areas with smaller built-up areas (less than 4,000 sq ft) and lower prices.
    * Properties with more bedrooms (darker shades) appear to have higher prices, though they are fewer in number.
    
2. HOUSE :-
    * This plot also represent the same relationship, but with higher price ranges reaching up to 30 million.
    * Larger built-up areas and properties with more bedrooms dominate the higher price segment.
    
3. COMMON FOUNDINGS : -
    1. Built-up Area vs Price Relationship: The price of properties generally increases with an increase in 
                                            built-up area. This is evident from the upward trend in the scatterplots.
    2. Bedroom Count: Properties with a higher number of bedrooms (indicated by darker color shades) tend 
                      to have higher prices.
    3. Concentration: Most properties are clustered in the lower price range with smaller built-up areas
                      (less than 4,000 sq ft specially for flats). 
    
""")


# bhk pie chart
st.title('BHK Pie Chart')

sector_options = new_df['sector'].unique().tolist()
sector_options.insert(0,'Overall')

selected_sector = st.selectbox('Select Sector',sector_options)

if selected_sector == 'Overall':
    fig2 = px.pie(new_df, names='bedRoom')
    st.plotly_chart(fig2,use_container_width = True)
else:
    fig2 = px.pie(new_df[new_df['sector'] == selected_sector], names='bedRoom', title='Total Bill Amount by Day')
    st.plotly_chart(fig2, use_container_width=True)

# side by side boxplot of bedroom price
st.title('Side by Side BHK-Price-Comaprison')

temp_df = new_df[new_df['bedRoom'] <= 4]

st.subheader("Insights from BHK Plot")
st.write("""
This is just basic visual representation of number of bedrooms in terms of percentage.Overall and sectorwise as well
""")



# Create side-by-side boxplots of the total bill amounts by day
fig3 = px.box(temp_df, x='bedRoom', y='price', title='BHK Price Range')
st.plotly_chart(fig3, use_container_width=True)
import streamlit as st

st.subheader("Insights from BHK Price Range Box Plot")
st.write("""
1. Price Range by Bedroom Count:
   - 1 BHK: The price range is relatively narrow, with most properties priced lower. Few outliers exist in the higher
            price range.
   - 2 BHK: Prices start to vary more, showing a moderate range with a few outliers.
   - 3 BHK: The price range widens significantly, indicating higher variance. Some properties are priced much higher
            than the majority.
   - 4 BHK: The widest range of prices is observed here. This category has the highest median price and several
            outliers in the premium range.

2. Price Trends:
   - As the number of bedrooms increases, the median price generally rises.
   - Properties with more bedrooms (3 BHK and 4 BHK) show greater variability, reflecting higher demand and 
     luxury pricing.

3. Outliers:
   - There are extreme price points in all categories, particularly in the 4 BHK segment, which could represent 
     luxury or premium properties.
   - The lower BHK categories have fewer high-value outliers, indicating budget housing.

4. Utility:
   - This chart helps identify the typical price range for properties with varying bedroom counts, which can 
     assist buyers and sellers in decision-making.
""")



# Figure 4 price of flats vs house
st.title('Side by Side Comparison of Flat VS House')

fig4, ax = plt.subplots(figsize=(10, 4))

# Plot house prices
sns.kdeplot(new_df[new_df['property_type'] == 'house']['price'], label='House', ax=ax, fill=True)

# Plot flat prices
sns.kdeplot(new_df[new_df['property_type'] == 'flat']['price'], label='Flat', ax=ax, fill=True)

# Add legend and labels
ax.legend(title="Property Type")
ax.set_title("Price Distribution: Flats vs Houses")
ax.set_xlabel("Price")
ax.set_ylabel("Density")

# Display in Streamlit
st.pyplot(fig4)

st.subheader("Insights from the distribution Visualization]")
st.write("""
1. Price Range and Density:
    Flats (orange line): Most flats are priced lower, concentrated within a narrow range. The high peak indicates
                         that the majority of flat prices are similar, likely clustered around the median.
                         
    Houses (blue line):  The price distribution for houses is more spread out, with a broader curve, indicating higher
                         price variability.

2. Overlapping Region:
    The overlapping region near the peak suggests that there are some price ranges where houses and flats are priced 
    similarly.

3. Outliers:
    Houses extend to much higher prices compared to flats, indicating the presence of luxury or premium houses in
    the dataset.

4. Implication:
    Flats tend to be more affordable and uniform in pricing, whereas houses are more expensive and show greater 
    variation.
""")
import streamlit as st

st.set_page_config(
    page_title = "Home_Page",
    page_icon  = "Home"
)

st.write("Welcome User 🙏🏻")

st.subheader("To Property Recommendation System! 🏡")

st.write('''
        This project is designed to analyze real estate data{of gurugram only} and provide insights to help users make informed decisions. 

            Here's what it does:

            A) Data Analysis: Explore property trends using visualizations like scatter plots for Area vs Price and word clouds to highlight commonly offered amenities in the property.
           
            B) Comparison: Compare flats and houses side by side to find what suits you best according to the price.
            
            C) Price Prediction: Get accurate price estimates based on user inputs, including property type, sector,bedrooms,balconies,built-up area, furnishing type, and more.
           
            D) Property Recommendations:
               1) By Location:   Discover apartments within a specified radius of your chosen location.
               2) By Similarity: Select an apartment, and we'll recommend similar ones.
            
            
            Dive into the world of data-driven property recommendations and make smarter choices today! 🌟🌟
''')

st.subheader("*** This recommendation project is only for Gurugram area properties ***")

(st.sidebar.success("Select a demo above."))


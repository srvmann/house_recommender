
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title = "Recommendations")

loc_df      = pickle.load(open('Recommender_files/location_df.pkl','rb'))
cosine_sim1 = pickle.load(open('Recommender_files/cosine_sim1.pkl','rb'))
cosine_sim2 = pickle.load(open('Recommender_files/cosine_sim2.pkl','rb'))
cosine_sim3 = pickle.load(open('Recommender_files/cosine_sim3.pkl','rb'))

# recommendation_function
def recommend_properties_with_scores(property_name, top_n=247):
    cosine_sim_matrix = 30 * cosine_sim1 + 20 * cosine_sim2 + 8 * cosine_sim3
    # cosine_sim_matrix = cosine_sim3

    # Get the similarity scores for the property using its name as the index
    sim_scores = list(enumerate(cosine_sim_matrix[loc_df.index.get_loc(property_name)]))

    # Sort properties based on the similarity scores
    sorted_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    # Get the indices and scores of the top_n most similar properties
    top_indices = [i[0] for i in sorted_scores[1:top_n + 1]]
    top_scores = [i[1] for i in sorted_scores[1:top_n + 1]]

    # Retrieve the names of the top properties using the indices
    top_properties = loc_df.index[top_indices].tolist()

    # Create a dataframe with the results
    recommendations_df = pd.DataFrame({
        'PropertyName': top_properties,
        'SimilarityScore': top_scores
    })

    return recommendations_df


# Test the recommender function using a property name
# recommend_properties_with_scores('Ireo Victory Valley')


st.title("Select Location and Radius")
selected_loc = st.selectbox("Location",sorted(loc_df.columns.to_list()))

radius = st.number_input("Radius in Kms")

if st.button('Search'):

    st.subheader("Results ")
    st.text(f"The top 10 nearest apartments from {selected_loc} within the {int(radius)} kms are:- [societyname no.of kms]")
    result = loc_df[loc_df[selected_loc] < radius * 1000][selected_loc].sort_values().head(10)

    for key,value in result.items():
        st.text(str(key) +' '+ str(round(value / 1000)) + 'Kms')

st.title("Recommend Apartments")
selected_apartment = st.selectbox("Select an apartment",sorted(loc_df.index.to_list()))

if st.button("Recommend"):
    rec_df = recommend_properties_with_scores(selected_apartment)

    # displaying the recommended apartments by the upper function
    st.text("Top 10 recommended property on the bases of choosen property {on similarity bases}.")
    st.dataframe(rec_df['PropertyName'].head(10))

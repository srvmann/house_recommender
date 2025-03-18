# Real Estate Insights & Recommendations 🏡📊  

This project is designed to analyze real estate data (specific to Gurugram) and provide actionable insights to help users make informed decisions.  

## Features ✨  

### 🛠️ **Data Analysis**
- Explore property trends using interactive visualizations.  
- Gain insights through scatter plots (e.g., Area vs. Price) and word clouds that highlight frequently offered amenities in properties.  

### 🔍 **Property Comparison**
- Compare flats and houses side by side.  
- Find what suits your preferences and budget.  

### 🧮 **Price Prediction**
- Predict property prices accurately based on user inputs like:  
  - Property Type (Flat/House)  
  - Sector  
  - Number of Bedrooms  
  - Balconies  
  - Built-Up Area  
  - Furnishing Type  
  - And more!  

### 🏠 **Property Recommendations**
1. **By Location**: Discover properties within a specific radius of your chosen location.  
2. **By Similarity**: Select an apartment and receive recommendations for similar properties.  

## How It Works 🔧
1. **Upload Your Data**:  
   - Use your real estate dataset (Gurugram-specific) to power the analysis.  
2. **Visualize Trends**:  
   - Generate interactive charts and word clouds to uncover valuable insights.  
3. **Predict Prices**:  
   - Input key details about a property and get an estimated price instantly.  
4. **Get Recommendations**:  
   - Find properties near you or similar to your favorite choices.  

## Tech Stack 💻  
- **Python**: Backend development and analysis  
- **Streamlit**: User-friendly web interface  
- **scikit-learn**: Machine learning for price predictions  
- **PyPDF2, python-docx**: Document processing  
- **Matplotlib, Seaborn**: Data visualization  

## Getting Started 🚀  
Follow these steps to set up and run the project locally:  

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/your-username/real_estate_recommender.git
   cd real_estate_recommender
   ```  

2. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the App**  
   ```bash
   streamlit run Home.py
   ```  

4. **Access the Application**  
   Open your browser and navigate to `http://localhost:8501`.  

## File Structure 📂  
- **`Home.py`**: Main application file.  
- **`pickled_files/`**: Stores the trained machine learning models and encoders.  
- **`data/`**: Placeholder for the real estate dataset.  

## Future Enhancements 🔮  
- Add support for more locations beyond Gurugram.  
- Incorporate additional property features for more detailed analysis.  
- Provide detailed neighborhood insights.  

## Contributing 🤝  
Contributions are welcome! If you'd like to enhance the project, please fork the repository and submit a pull request.  

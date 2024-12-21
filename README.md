# Movie Recommendation System 🎥

This is a **Movie Recommendation System** built using **Streamlit**, **Pandas**, and the **TMDb API**. It allows users to select a movie and get five similar movie recommendations along with their posters.

## Features
- **Movie Recommendations**: Get top 5 movies similar to the one you select.
- **Poster Display**: View the posters of the recommended movies.
- **Interactive Interface**: Built with an easy-to-use Streamlit interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SimpleCyber/Movie-Recommendation-system.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Movie-Recommendation-system
   ```
3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Download the necessary `.pkl` files (`movies_dict.pkl` and `similarity.pkl`) and place them in the root directory.

## Usage

1. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
2. Open your browser and go to the URL displayed in the terminal (default: `http://localhost:8501`).
3. Select a movie from the dropdown and click "Recommend" to view recommendations.

## Output Example

<img src="https://github.com/SimpleCyber/Movie-Recommendation-system/blob/main/output.png" alt="Output Example" width="800">

## API Key
Make sure to replace the TMDb API key (`1f4efd04a20fb47cd4021f041fac3679`) with your own key in the `ferch_poster` function for uninterrupted functionality.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements.

---

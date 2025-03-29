# Movie Recommendation System

## 📌 Project Description
The **Movie Recommendation System** suggests movies based on user input using content-based filtering. It analyzes genres, actors, and storylines to find the most relevant recommendations. The system uses **TF-IDF vectorization** and **cosine similarity** to compare movie descriptions and generate personalized recommendations.

## 🚀 Features
- 🎬 **Personalized Movie Suggestions**: Recommends five similar movies based on the user's choice.
- 📊 **Content-Based Filtering**: Uses movie genres and descriptions for similarity analysis.
- 🛠 **Machine Learning Techniques**: Implements **CountVectorizer** and **Cosine Similarity** for feature extraction.
- 🏗 **Efficient Data Handling**: Processes and organizes movie data using **Pandas** and **NumPy**.
- 🔎 **Interactive CLI Interface**: Users can input a movie title and instantly receive recommendations.

## 📂 Tech Stack
- **Programming Language**: Python 🐍
- **Libraries Used**:
  - `pandas` for data manipulation
  - `numpy` for numerical operations
  - `sklearn` for vectorization and similarity calculations

## 📖 How It Works
1. Loads a **CSV dataset** containing movie details.
2. Combines genres and movie overviews to create a feature set (**tags** column).
3. Converts text data into numerical vectors using **CountVectorizer**.
4. Computes the similarity between movies using **cosine similarity**.
5. Accepts a movie title as input and recommends the **top 5 most similar movies**.

## 📦 Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   cd movie-recommendation-system
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the script**
   ```bash
   python movie_recommender.py
   ```

## 🎯 Usage
1. Run the script in the terminal.
2. Enter a movie name when prompted.
3. The system will display **five recommended movies** similar to the input movie.

## 📌 Example Output
```
Enter the movie you want to watch: Inception
Recommended Movies:
1. Interstellar
2. The Prestige
3. Memento
4. The Dark Knight
5. Shutter Island
```

## 🤝 Contributing
Feel free to fork this repository and contribute improvements. Pull requests are welcome!
---
⚡ *Happy Coding!* 🎥🍿


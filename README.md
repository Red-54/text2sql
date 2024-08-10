# Text2SQL with Gemini and Streamlit

This project demonstrates a basic implementation of a natural language to SQL query translator using Google's Gemini API and Streamlit for the frontend. 

**Note:** This is a work in progress and currently has limitations in handling complex databases and queries. 

## Features

- Translates natural language questions into SQL queries.
- Executes queries on a SQLite database (`student.db`).
- Provides a user-friendly interface with Streamlit.

## Limitations (Current Version)

- Requires manual definition of the database schema in the prompt.
- Doesn't support multiple interconnected tables.
- Lacks comprehensive error handling.
- May struggle with complex SQL queries.

## Future Improvements

- [ ] Automatically extract database schema to eliminate manual input.
- [ ] Support multi-table queries and relationships.
- [ ] Implement robust error handling for invalid queries or data.
- [ ] Enhance query understanding for more complex SQL structures.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-username/text2sql.git
   cd text2sql 
   ```

2. **Set up a Virtual Environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate 
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up Google Gemini API Key:**
   - Create a `.env` file in the root directory.
   - Add your Google Gemini API key:
     ```
     GOOGLE_API_KEY=your_google_api_key_here
     ```

5. **Run the Streamlit App:**
   ```bash
   streamlit run app.py 
   ```

## Usage

1. **Access the app in your browser (usually at `http://localhost:8501`).**
2. **Type your natural language question in the input field.**
3. **Click "Ask the question".**
4. **The generated SQL query and the result from the database will be displayed.**

## Example

**Database (`student.db`):**
- Table name: `STUDENT`
- Columns: `NAME`, `CLASS`, `SECTION`, `MARKS`

**Question:** 
"Tell me all the students studying in Data Science class?"

**Output:**

- **Generated SQL:** 
  ```sql
  SELECT * FROM STUDENT where CLASS="Data Science"
  ```

- **Results:** 
  (The data retrieved from the `student.db` database will be shown).

## Contributing

Contributions are welcome! Please open an issue to discuss potential improvements or submit a pull request with your changes.

## License

This project is licensed under the MIT License.

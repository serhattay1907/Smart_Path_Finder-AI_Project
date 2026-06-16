# 📍 Smart Path Finder:

This project is a web-based pathfinding application that calculates the **shortest and most efficient route** between key locations in Muğla Center. It provides real-time navigation data, including total distance, estimated walking time, and step count.

Powered by **Dijkstra's Algorithm** on the backend and **Leaflet.js** on the frontend. 🚀

## 🌟 Features

* **Shortest Path Calculation:** Implements Dijkstra's algorithm to find the optimal route between nodes.
* **Real-World Distances:** Uses the Haversine formula to calculate accurate distances based on GPS coordinates.
* **Interactive Map:** Fully interactive map interface built with Leaflet.js, allowing users to select start and end points via clicks.
* **Detailed Analytics:** Displays total distance (meters), estimated duration (minutes), and step count.
* **Responsive Design:** Modern and user-friendly interface.

## 🛠️ Tech Stack

* **Backend:** Python (Flask)
* **Algorithm:** Dijkstra & Haversine Formula
* **Frontend:** HTML5, CSS3, JavaScript
* **Map Library:** Leaflet.js
* **Data Structure:** JSON (Graph & Coordinate data)

## ⚙️ Installation & Usage

Follow these steps to run the project locally:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/yourusername/smart-path-finder-mugla.git](https://github.com/yourusername/smart-path-finder-mugla.git)
    cd smart-path-finder-mugla
    ```

2.  **Install dependencies:**
    ```bash
    pip install flask
    ```

3.  **Run the application:**
    ```bash
    python app.py
    ```

4.  **Open in Browser:**
    Click the link shown in the terminal (usually `http://127.0.0.1:5000`).

## 📂 Project Structure

```text
├── app.py              # Flask server & main backend logic
├── dijkstra.py         # Shortest path algorithm implementation
├── graph-data.json     # Nodes, edges, and coordinate data
├── index.html          # Main frontend interface & map logic
├── style.css           # Styling files
├── script.js           # External scripts (if applicable)
└── README.md           # Project documentation

🤝 Contributing
Contributions are welcome! If you have suggestions or want to add new locations to the map, feel free to open a Pull Request.

👤 Author
SERHAT TAY

📝 License
This project is open-source and available for educational purposes.

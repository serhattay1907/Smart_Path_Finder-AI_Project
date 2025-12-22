from flask import Flask, render_template, request
import json
import math
from dijkstra import find_shortest_path

# HTML dosyasını yan klasörde (aynı dizinde) ara
app = Flask(__name__, template_folder='.')

# Haversine Formülü: Koordinatlar arası gerçek metre hesabı
def calculate_distance(coord1, coord2):
    R = 6371000 # Dünya yarıçapı (metre)
    phi1, phi2 = math.radians(coord1[0]), math.radians(coord2[0])
    delta_phi = math.radians(coord2[0] - coord1[0])
    delta_lambda = math.radians(coord2[1] - coord1[1])
    
    a = math.sin(delta_phi/2)**2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda/2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    return R * c 

def load_data():
    with open('graph-data.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    nodes = data['nodes']
    coords = data['coordinates']
    raw_edges = data['edges']
    
    graph_dict = {}
    for node in nodes:
        graph_dict[node] = {}
        
    # JSON'daki weight:0 değerlerini gerçek mesafe ile güncelle
    for start_node, neighbors in raw_edges.items():
        for item in neighbors:
            end_node = item['node']
            c1 = coords.get(start_node)
            c2 = coords.get(end_node)
            
            if c1 and c2:
                dist = calculate_distance(c1, c2)
                graph_dict[start_node][end_node] = dist
            else:
                graph_dict[start_node][end_node] = 1 # Hata önleyici

    formatted_coords = {}
    for k, v in coords.items():
        formatted_coords[k] = {'lat': v[0], 'lon': v[1]}
        
    return formatted_coords, graph_dict

# Verileri yükleme
formatted_coords, graph_with_weights = load_data()

@app.route('/', methods=['GET', 'POST'])
def home():
    path = None
    total_distance = 0
    time_min = 0
    steps = 0
    error_message = None
    s_start = ""
    s_end = ""

    if request.method == 'POST':
        s_start = request.form.get('start_node')
        s_end = request.form.get('end_node')
        
        if s_start and s_end:
            if s_start in graph_with_weights and s_end in graph_with_weights:
                result_path, dist_meters = find_shortest_path(graph_with_weights, s_start, s_end)
                
                if result_path:
                    path = result_path
                    total_distance = round(dist_meters, 2)
                    time_min = round(total_distance / 80) # 80m/dk yürüme hızı
                    
                    steps = len(path) - 1 if len(path) > 1 else 0
                    
                else:
                    error_message = "Rota bulunamadı."
            else:
                error_message = "Geçersiz nokta seçimi."
    
    return render_template('index.html', 
                           nodes=formatted_coords,
                           path=path,
                           distance=total_distance,
                           time=time_min,
                           steps=steps, 
                           error=error_message,
                           s_start=s_start,
                           s_end=s_end)

if __name__ == '__main__':
    app.run(debug=True)
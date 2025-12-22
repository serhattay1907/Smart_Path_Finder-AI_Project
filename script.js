document.addEventListener('DOMContentLoaded', function() {
    
    // 1. HARİTAYI BAŞLAT (Muğla Merkezli)
    var map = L.map('map').setView([37.21530878688118, 28.363719614751343], 30);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    // 2. GLOBAL VERİLERİ OKU (Index.html içindeki script taginden gelir)
    var nodes = window.appData.nodes;
    var path = window.appData.path;

    // 3. İŞARETLEYİCİLERİ EKLE
    for (var nodeName in nodes) {
        var lat = nodes[nodeName].lat;
        var lon = nodes[nodeName].lon;

        if (lat && lon) {
            var marker = L.marker([lat, lon]).addTo(map);

            // İsimleri sürekli göster
            marker.bindTooltip(nodeName, {
                permanent: true,
                direction: 'top',
                className: 'node-label'
            });

            // Tıklama Olayı 
            marker.on('click', function(e) {
                // Tooltip içeriğinden ismi alıyoruz
                var clickedName = this.getTooltip().getContent();
                handleMapClick(clickedName);
            });
        }
    }

    // 4. SEÇİM MANTIĞI (BAŞLANGIÇ -> HEDEF -> BAŞA DÖN)
    var selectionStep = 1;
    
    function handleMapClick(nodeName) {
        var startInput = document.getElementById('start_input');
        var endInput = document.getElementById('end_input');

        if (selectionStep === 1) {
            startInput.value = nodeName;
            endInput.value = ""; 
            selectionStep = 2;
        } else {
            endInput.value = nodeName;
            selectionStep = 1;
        }
    }

    // 5. YOL ÇİZİMİ
    if (path && path.length > 0) {
        var pathCoords = [];
        for (var i = 0; i < path.length; i++) {
            var pName = path[i];
            if (nodes[pName]) {
                pathCoords.push([nodes[pName].lat, nodes[pName].lon]);
            }
        }

        if (pathCoords.length > 0) {
            var polyline = L.polyline(pathCoords, {
                color: '#e74c3c', // Kırmızı
                weight: 6,
                opacity: 0.8,
                dashArray: '10, 10', // Kesikli çizgi efekti
                lineCap: 'round'
            }).addTo(map);

            map.fitBounds(polyline.getBounds(), {padding: [50, 50]});
        }
    }
});
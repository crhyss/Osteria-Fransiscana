mapboxgl.accessToken = 'pk.eyJ1IjoiY3JhdXoiLCJhIjoiY2w0dzZjZWk5MjV4eTNqczg2bmIwazNoMCJ9.VaYyChMCUOnf5dJjUhDwDg';
let map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-70.70447896746107, -33.592399939493966],
    zoom: 12
});
var img = document.getElementById("img1");
map.on('load', () => {
    map.loadImage(
        'https://docs.mapbox.com/mapbox-gl-js/assets/custom_marker.png',
        (error, image) => {
            if (error) throw error;
            map.addImage('custom-marker', image);
            map.addSource('points', {
                'type': 'geojson',
                'data': {
                    'type': 'FeatureCollection',
                    'features': [
                        {
                            'type': 'Feature',
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [
                                    -70.70606863980281,-33.59867197873413
                                ]
                            },
                            'properties': {
                                'title': 'Osteria Fransciscana'
                            }
                        },
                        {
                            'type': 'Feature',
                            'geometry': {
                                'type': 'Point',
                                'coordinates': [-70.70665938466453,-33.59528862035967]
                            },
                            'properties': {
                                'title': 'Osteria Fransciscana'
                            }
                        }
                    ]
                }
            });

            map.addLayer({
                'id': 'points',
                'type': 'symbol',
                'source': 'points',
                'layout': {
                    'icon-image': 'custom-marker',
                    'text-field': ['get', 'title'],
                    'text-font': [
                        'Open Sans Semibold',
                        'Arial Unicode MS Bold'
                    ],
                    'text-offset': [0, 1.25],
                    'text-anchor': 'top'
                }
            });
        }
    );
});
map.addControl(
    new MapboxDirections({
        accessToken: mapboxgl.accessToken
    }),
    'top-left'
);
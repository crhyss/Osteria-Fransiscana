<script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.6/dist/umd/popper.min.js" integrity="sha384-oBqDVmMz9ATKxIep9tiCxS/Z9fNfEXiDAYTujMAeBAsjFuCZSmKbSSUnQlmh/jp3" crossorigin="anonymous"></script>,
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.min.js" integrity="sha384-7VPbUDkoPSGFnVtYi0QogXtr74QeVeeIs99Qfg5YCF+TidwNdjvaKZX19NZ/e6oz" crossorigin="anonymous"></script>

mapboxgl.accessToken = '{{mapbox_access_token}}';
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/streets-v11',
    center: [-70.70447896746107,-33.592399939493966],
    zoom: 12
});
var geojson={
    type:'Restaurantes',
        feacture:[{
            type:'Restaurant',
            ubicacion:{
                type: 'Point',
                coordenadas:[-70.70447896746107,-33.592399939493966]
            },
            propietario:{
                title:'mapbox',
                descripcion:'Osteria Fransciscana'
            }
        },
        {
            type:'Restaurant2',
            ubicacion:{
                type: 'Point',
                coordenadas:[-70.70623849299018,-33.59525973732504]
            },
            propietario:{
                title:'mapbox',
                descripcion:'Osteria Fransciscana'
            }
        }]
}
for (const feature of geojson.features) {
    // create a HTML element for each feature
    const el = document.createElement('div');
    el.className = 'marker';
  
    // make a marker for each feature and add to the map
    new mapboxgl.Marker(el).setLngLat(feature.geometry.coordinates).addTo(map);
  }

  
var wms_layers = [];


        var lyr_OSMStandard_0 = new ol.layer.Tile({
            'title': 'OSM Standard',
            'type': 'base',
            'opacity': 1.000000,
            
            
            source: new ol.source.XYZ({
    attributions: ' &middot; <a href="https://www.openstreetmap.org/copyright">© OpenStreetMap contributors, CC-BY-SA</a>',
                url: 'http://tile.openstreetmap.org/{z}/{x}/{y}.png'
            })
        });
var format_all_files_head_1 = new ol.format.GeoJSON();
var features_all_files_head_1 = format_all_files_head_1.readFeatures(json_all_files_head_1, 
            {dataProjection: 'EPSG:4326', featureProjection: 'EPSG:3857'});
var jsonSource_all_files_head_1 = new ol.source.Vector({
    attributions: ' ',
});
jsonSource_all_files_head_1.addFeatures(features_all_files_head_1);
var lyr_all_files_head_1 = new ol.layer.Vector({
                declutter: true,
                source:jsonSource_all_files_head_1, 
                style: style_all_files_head_1,
                interactive: true,
    title: 'all_files_head<br />\
    <img src="styles/legend/all_files_head_1_0.png" /> Accipiter<br />\
    <img src="styles/legend/all_files_head_1_1.png" /> Accipiter brevipes<br />\
    <img src="styles/legend/all_files_head_1_2.png" /> Alces alces<br />\
    <img src="styles/legend/all_files_head_1_3.png" /> Anser albifrons<br />\
    <img src="styles/legend/all_files_head_1_4.png" /> Cathartes aura<br />\
    <img src="styles/legend/all_files_head_1_5.png" /> Chondestes grammacus<br />\
    <img src="styles/legend/all_files_head_1_6.png" /> Cygnus cygnus<br />\
    <img src="styles/legend/all_files_head_1_7.png" /> Falco peregrinus<br />\
    <img src="styles/legend/all_files_head_1_8.png" /> Gavia adamsii<br />\
    <img src="styles/legend/all_files_head_1_9.png" /> Grus grus<br />\
    <img src="styles/legend/all_files_head_1_10.png" /> <br />'
        });

lyr_OSMStandard_0.setVisible(true);lyr_all_files_head_1.setVisible(true);
var layersList = [lyr_OSMStandard_0,lyr_all_files_head_1];
lyr_all_files_head_1.set('fieldAliases', {'field_1': 'field_1', 'study_id': 'study_id', 'individual_id': 'individual_id', 'taxon_canonical_name': 'taxonName', 'sex': 'sex', 'timestamp': 'timestamp', 'location_lat': 'latitude', 'location_long': 'longitude', });
lyr_all_files_head_1.set('fieldImages', {'field_1': 'Range', 'study_id': 'Range', 'individual_id': 'Range', 'taxon_canonical_name': 'TextEdit', 'sex': 'TextEdit', 'timestamp': 'TextEdit', 'location_lat': 'TextEdit', 'location_long': 'TextEdit', });
lyr_all_files_head_1.set('fieldLabels', {'field_1': 'no label', 'study_id': 'no label', 'individual_id': 'no label', 'taxon_canonical_name': 'header label', 'sex': 'no label', 'timestamp': 'no label', 'location_lat': 'no label', 'location_long': 'no label', });
lyr_all_files_head_1.on('precompose', function(evt) {
    evt.context.globalCompositeOperation = 'normal';
});
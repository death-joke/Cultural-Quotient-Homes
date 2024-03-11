import React from 'react';
import { MapContainer, TileLayer, GeoJSON, Popup, Marker } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css';
import L from 'leaflet';
import 'leaflet-defaulticon-compatibility';

const MapView = () => {
    const position = [51.505, -0.09];
    let geojsonFeature: GeoJSON.Feature = {
        type: "Feature",
        geometry: {
          type: "Point",
          coordinates: [125.6, 10.1]
        },
        properties: {
          name: "Dinagat Islands"
        }
      };
      let geojsonFeature2: GeoJSON.Feature = {
        type: "Feature",
        properties: {
          name: "A polygon"
        },
        geometry: {
          type: "Polygon",
          coordinates: [
            [ // This array represents the exterior of the polygon
              [100.0, 0.0],
              [101.0, 0.0],
              [101.0, 1.0],
              [100.0, 1.0],
              [100.0, 0.0] // The first and last coordinate must be the same to close the polygon
            ]
            // Additional arrays would represent holes in the polygon
          ]
        }
      };
    return (
        <MapContainer center={[51.505, -0.09]} zoom={13} scrollWheelZoom={true}   style={{height: "100vh"}}>
  <TileLayer
    attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
    url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
  />
  <Marker position={[51.505, -0.09]}>
    <Popup>
      A pretty CSS3 popup. <br /> Easily customizable.
    </Popup> 
  </Marker>
    <GeoJSON data={geojsonFeature} />
    <GeoJSON data={geojsonFeature2} pathOptions={{color: 'red'}}  />
    
</MapContainer> );
};

export default MapView;
import React, { useEffect, useState }  from 'react';
import { MapContainer, TileLayer, GeoJSON, Popup, Marker } from 'react-leaflet';
import 'leaflet/dist/leaflet.css';
import 'leaflet-defaulticon-compatibility/dist/leaflet-defaulticon-compatibility.css';
import L from 'leaflet';
import 'leaflet-defaulticon-compatibility';
//result.geojson
const MapView = () => {
  const position = [51.505, -0.09];
  const [geojsonData, setGeojsonData] = useState(null);
const [scaleMode, setScaleMode] = useState('dvf')
const [atualScale, setatualScale] = useState([0, 0, 0])
const [dvfSCale, setdvfSCale] = useState([75000, 200000, 500000])
const [schoolSCale, setschoolSCale] = useState([1, 5, 15])
const [museumSCale, setmuseumSCale] = useState([0, 1, 2])
const [bibliothequeSCale, setbibliothequeSCale] = useState([1,2 ,3])
const [monumentSCale, setmonumentSCale] = useState([1, 2, 3])
const [cinemaSCale, setcinemaSCale] = useState([1, 2, 3])
const [culurelpointSCale, setculurelpointSCale] = useState([1, 2, 3])





  useEffect(() => {
      // Load GeoJSON data from a file in the public directory
      fetch('/light_result.geojson')
          .then(response => response.json())
          .then(data => setGeojsonData(data));  

    
  }, []);

  const getScaleColor=(feature:any)=>{
    switch (scaleMode) {
        case 'dvf':  
            return getDVFColor(feature.properties['Valeur foncière moyenne']);          
            break;
        case 'school':
            return getSchoolColor(feature.properties['Nombre d\'établissements scolaires']);
            break;
        case 'museum':
            return getMuseumColor(feature.properties['Nombre de musées']);
            break;
        case 'bibliotheque':
            return getBibliothequeColor(feature.properties['Nombre de bibliotheques']);
            break;
        case 'monument':
            return getMonumentColor(feature.properties['Nombre de monuments']);
            break;
        case 'cinema':
            return getCinemaColor(feature.properties['Nombre de cinemas']);
        break;
        case 'culurel-point': 
        //to get the number of cultural points, we need to sum the number of museums, bibliotheques, monuments and cinemas
        const culurelpoint = parseInt(feature.properties['Nombre de musées']) + parseInt(feature.properties['Nombre de bibliotheques']) + parseInt(feature.properties['Nombre de monuments']) + parseInt(feature.properties['Nombre de cinemas']);
        return getCulurelpointColor(culurelpoint.toString());
        break  
        default:
            break;
    }
  }

  const getDVFColor = (value:string) => {
      const baseColor = ['green', 'yellow','orange' ,'red'];
        const scale = dvfSCale;
        //convert value to a number
        const val = parseFloat(value);
        //if the value is not a number, return grey
        if (isNaN(val)) {
            return `rgb(128,128,128) `;
        }
        //if the value is lower than the first scale, return the first color
        if (val < scale[0]) {
            return `rgb(0,128,0)`;
        }else if (val < scale[1]) {
            return `rgb(255,255,0)`;
        }else if (val < scale[2]) {
            return `rgb(255,165,0)`;
        }else{
            return `rgb(255,0,0)`;
        }
        // //if the value is higher than the last scale, return the last color
        // if (val > scale[2]) {
        //     return `rgb(255,0,0)`;
        // }
        // //if the value is between the first and the second scale, return the second color
        // if (val < scale[1]) {
        //     return `rgb(255,255,0)`;
        // }
        // //if the value is between the second and the third scale, return the third color
        // if (val < scale[2]) {
        //     return `rgb(255,165,0)`;
        // }
};
  const getSchoolColor = (value:string) => {
    const baseColor = ['green', 'yellow','orange' ,'red'];
      const scale = schoolSCale;
      //convert value to a number
      const val = parseFloat(value);
      //if the value is not a number, return grey
      if (isNaN(val)) {
          return `rgb(128,128,128) `;
      }
      //if the value is lower than the first scale, return the first color
      if (val < scale[0]) {
          return `rgb(0,128,0)`;
      }else if (val < scale[1]) {
          return `rgb(255,255,0)`;
      }else if (val < scale[2]) {
          return `rgb(255,165,0)`;
      }else{
          return `rgb(255,0,0)`;
      }
      // //if the value is higher than the last scale, return the last color
      // if (val > scale[2]) {
      //     return `rgb(255,0,0)`;
      // }
      // //if the value is between the first and the second scale, return the second color
      // if (val < scale[1]) {
      //     return `rgb(255,255,0)`;
      // }
      // //if the value is between the second and the third scale, return the third color
      // if (val < scale[2]) {
      //     return `rgb(255,165,0)`;
      // }
};
const getMuseumColor = (value:string) => {
    const baseColor = ['green', 'yellow','orange' ,'red'];
      const scale = museumSCale;
      //convert value to a number
      const val = parseFloat(value);
      //if the value is not a number, return grey
      if (isNaN(val)) {
          return `rgb(128,128,128) `;
      }
      //if the value is lower than the first scale, return the first color
      if (val < scale[0]) {
          return `rgb(0,128,0)`;
      }else if (val < scale[1]) {
          return `rgb(255,255,0)`;
      }else if (val < scale[2]) {
          return `rgb(255,165,0)`;
      }else{
          return `rgb(255,0,0)`;
      }
};
    const getBibliothequeColor = (value:string) => {
        const baseColor = ['green', 'yellow','orange' ,'red'];
          const scale = bibliothequeSCale;
          //convert value to a number
          const val = parseFloat(value);
          //if the value is not a number, return grey
          if (isNaN(val)) {
              return `rgb(128,128,128) `;
          }
          //if the value is lower than the first scale, return the first color
          if (val < scale[0]) {
              return `rgb(0,128,0)`;
          }else if (val < scale[1]) {
              return `rgb(255,255,0)`;
          }else if (val < scale[2]) {
              return `rgb(255,165,0)`;
          }else{
              return `rgb(255,0,0)`;
          }
};
const getMonumentColor = (value:string) => {
    const baseColor = ['green', 'yellow','orange' ,'red'];
      const scale = monumentSCale;
      //convert value to a number
      const val = parseFloat(value);
      //if the value is not a number, return grey
      if (isNaN(val)) {
          return `rgb(128,128,128) `;
      }
      //if the value is lower than the first scale, return the first color
      if (val < scale[0]) {
          return `rgb(0,128,0)`;
      }else if (val < scale[1]) {
          return `rgb(255,255,0)`;
      }else if (val < scale[2]) {
          return `rgb(255,165,0)`;
      }else{
          return `rgb(255,0,0)`;
      }
}
const getCinemaColor = (value:string) => {
    const baseColor = ['green', 'yellow','orange' ,'red'];
      const scale = cinemaSCale;
      //convert value to a number
      const val = parseFloat(value);
      //if the value is not a number, return grey
      if (isNaN(val)) {
          return `rgb(128,128,128) `;
      }
      //if the value is lower than the first scale, return the first color
      if (val < scale[0]) {
          return `rgb(0,128,0)`;
      }else if (val < scale[1]) {
          return `rgb(255,255,0)`;
      }else if (val < scale[2]) {
          return `rgb(255,165,0)`;
      }else{
          return `rgb(255,0,0)`;
      }
}
const getCulurelpointColor = (value:string) => {
    const baseColor = ['green', 'yellow','orange' ,'red'];
      const scale = culurelpointSCale;
      //convert value to a number
      const val = parseFloat(value);
      //if the value is not a number, return grey
      if (isNaN(val)) {
          return `rgb(128,128,128) `;
      }
      //if the value is lower than the first scale, return the first color
      if (val < scale[0]) {
          return `rgb(0,128,0)`;
      }else if (val < scale[1]) {
          return `rgb(255,255,0)`;
      }else if (val < scale[2]) {
          return `rgb(255,165,0)`;
      }else{
          return `rgb(255,0,0)`;
      }
}

const style = (feature: any) => {
    return {
        color:getScaleColor(feature),
    };
};

return (
    <div>
        <MapContainer center={[46, 1.43]} zoom={5} style={{ height: "100vh", width: "100%" }} id='Map'>
                <TileLayer
                        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
                        attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
                />
                {geojsonData && <GeoJSON data={geojsonData} style={style} />}
                    <Marker position={[48.8566, 2.3522]}>
                            <Popup>
                                    Paris
                            </Popup>
                    </Marker>
                    <Marker position={[43.7102, 7.2620]}>
                            <Popup>
                                    Nice
                            </Popup>
                    </Marker>
                    <Marker position={[43.6047, 1.4442]}>
                            <Popup>
                                    Toulouse
                            </Popup>
                    </Marker>
                    <Marker position={[47.2184, -1.5536]}>
                            <Popup>
                                    Nantes
                            </Popup>
                    </Marker>
                    <Marker position={[48.1173, -1.6778]}>
                            <Popup>
                                    Rennes
                            </Popup>
                    </Marker>
                    <Marker position={[44.8378, -0.5792]}>
                            <Popup>
                                    Bordeaux
                            </Popup>
                    </Marker>
                    <Marker position={[48.5734, 7.7521]}>
                            <Popup>
                                    Strasbourg
                            </Popup>
                    </Marker>
                    <Marker position={[50.6293, 3.0573]}>
                            <Popup>
                                    Lille
                            </Popup>
                    </Marker>
                    <Marker position={[43.1242, 5.9280]}>
                            <Popup>
                                    Marseille
                            </Popup>
                    </Marker>
                    <Marker position={[45.7640, 4.8357]}>
                            <Popup>
                                    Lyon
                            </Popup>
                    </Marker>
            
        </MapContainer>
            <div className="card" id='Menu'>
                    <div className="card-body button-container">
                            <h5 className="card-title">Scale mode</h5>

                            <div className='row row justify-content-between'>
                         
                            <div className='col-5'
                            >
                                     <div className='row'>
                                            <button  className={`btn ${scaleMode === 'dvf' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => 
                                            {setScaleMode('dvf')
                                    setatualScale(dvfSCale)}}>property value</button></div>
                            <div className='row'>

                            
                            <button className={`btn ${scaleMode === 'school' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => {setScaleMode('school')
                    setatualScale(schoolSCale)
                    }}>School</button>
                            </div>
                            <div className='row'>
                            <button className={`btn ${scaleMode === 'museum' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => {setScaleMode('museum')
                    setatualScale(museumSCale)
                            }}>Museum</button>
                            </div>
                            <div className='row'>
                            <button className={`btn ${scaleMode === 'bibliotheque' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => {setScaleMode('bibliotheque')
                    setatualScale(bibliothequeSCale)
                    }}>Bibliotheque</button>
                            </div>
                            <div className='row'>
                            <button className={`btn ${scaleMode === 'monument' ? 'btn-primary' : 'btn-outline-primary'}`}  onClick={() => {setScaleMode('monument')
                    setatualScale(monumentSCale)            
                    }}>Monument</button>
                            </div>
                            <div className='row'>
                            <button className={`btn ${scaleMode === 'cinema' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() => {setScaleMode('cinema')
                    setatualScale(cinemaSCale)            
                    }}>Cinema</button>
                            </div>
                            <div className='row'>
                            <button className={`btn ${scaleMode === 'culurel-point' ? 'btn-primary' : 'btn-outline-primary'}`} onClick={() =>{ setScaleMode('culurel-point')
                    setatualScale(culurelpointSCale)
                    }}>Culurel-point</button>
                            </div>               
                            </div>
                            <div className='col-5'>                  
                                    <h5 className="card-title">Legend</h5>
                                    <h6>{scaleMode==='dvf'?"Mean property value":`Number of ${scaleMode}`}</h6>
                                    <h6>{}</h6>
                                    <div className='row'>
                                            <div className="col-2" style={{backgroundColor: 'green', width: '20px', height: '20px'}}></div>
                                            <div className="col-8">{`< ${atualScale[0]}`}</div>
                                    </div>
                                    <div className='row'>
                                            <div className="col-2" style={{backgroundColor: 'yellow', width: '20px', height: '20px'}}></div>
                                            <div className="col-8">
                                                    {`< ${atualScale[1]}`}
                                            </div>
                                    </div>
                                    <div className='row'>
                                            <div className="col-2" style={{backgroundColor: 'orange', width: '20px', height: '20px'}}></div>
                                            <div className="col-8">
                                                    {`< ${atualScale[2]}`}
                                            </div>
                                    </div>  
                                    <div className='row'>
                                            <div className="col-2" style={{backgroundColor: 'red', width: '20px', height: '20px'}}></div>
                                            <div className="col-8">
                                                    {`> ${atualScale[2]}`}
                                            </div>
                                    </div>
                                    <div className='row'>
                                            <div className="col-2" style={{backgroundColor: 'gray', width: '20px', height: '20px'}}></div>
                                            <div className="col-8">No data</div>
                                    </div>
                            </div>
                            </div>

                            
                            
                            
                    </div>
            </div>
            {/* <div id='Menu'>
                    <h2>Scale mode</h2>
                            <button  className="btn btn-outline-primary" onClick={() => setScaleMode('dvf')}>DVF</button>
                            <button className="btn btn-outline-primary" onClick={() => setScaleMode('school')}>School</button>
                            <button className="btn btn-outline-primary" onClick={() => setScaleMode('museum')}>Museum</button>
                            <button className="btn btn-outline-primary" onClick={() => setScaleMode('bibliotheque')}>Bibliotheque</button>
                            <button className="btn btn-outline-primary"  onClick={() => setScaleMode('monument')}>Monument</button>
                            <button className="btn btn-outline-primary" onClick={() => setScaleMode('cinema')}>Cinema</button>
                            <button className="btn btn-outline-primary" onClick={() => setScaleMode('culurel-point')}>Culurel-point</button>

                    </div>*/}
        </div> 
);
};

export default MapView;
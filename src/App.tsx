import React from 'react';
import { ScenaryControllerState } from './Materials/ScenaryControllerState';
import { FistJob } from './Pages/FistJob';
import { GlobalStyle } from './Styles/global';

function App() {

  const scenary = new ScenaryControllerState();

  scenary.start();

  return <>
    <GlobalStyle/>
    {/* <FistJob/> */}
    <h1>Iniciando..</h1>
  </>
}

export default App;

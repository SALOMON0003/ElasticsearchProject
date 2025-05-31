import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import axios from 'axios'
import {Routes, Route} from 'react-router-dom'
import Search from './pages/Search'

function App() {
  return (
      <Routes>
        <Route path="/" element={<Search />} />
      </Routes>
  );
}

export default App

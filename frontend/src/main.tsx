import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import Exemple from './pages/lessons/exemple/exemple'

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />
    },
    {
        path: "/lessons/exemple",
        element: <Exemple />
    }
])

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)

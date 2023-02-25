import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import { createBrowserRouter, RouterProvider } from 'react-router-dom'
import LessonsExemple from './pages/lessons/exemple'
import QuestionaireExemple from './pages/questionaire/exemple'

const router = createBrowserRouter([
    {
        path: "/",
        element: <App />
    },
    {
        path: "/lessons/exemple",
        element: <LessonsExemple />
    },
    {
        path: "/exercises/questionaire/exemple",
        element: <QuestionaireExemple />
    }
])

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>,
)

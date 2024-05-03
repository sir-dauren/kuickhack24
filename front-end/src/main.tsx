import ReactDOM from 'react-dom/client'
import './index.scss'
import { BrowserRouter } from 'react-router-dom'
import AuthProvider from './provider/AuthProvider/AuthProvider.tsx'
import App from './App'

ReactDOM.createRoot(document.getElementById('root')!).render(
  <BrowserRouter>
    <AuthProvider>
      <App/>
    </AuthProvider>
  </BrowserRouter>
)

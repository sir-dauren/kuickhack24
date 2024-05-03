import {FC} from 'react'
import { Route, Routes } from 'react-router-dom'
import Home from './pages/Home/Home'
import { useAuth } from './hooks/useAuth'
import Auth from './pages/Auth/Auth'


const App: FC = () => {
      const {isAuth} = useAuth()

      return (
           <div>
                  <Routes>                  
                        {isAuth ? (
                              <Route path='/' element={<Home/>} />
                        ) : (
                              <Route path='*' element={<Auth/>} />
                        )}
                        
                        
                  </Routes>
           </div>
      )
}

export default App
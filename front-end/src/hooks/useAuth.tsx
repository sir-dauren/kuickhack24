import {useContext} from 'react'
import { AuthContext } from '../provider/AuthProvider/AuthProvider'

export const useAuth = () => useContext(AuthContext)
import axios from 'axios'
import { $URL } from './url'

export const $axios = axios.create({
      baseURL: $URL,
      headers: {
            'Content-Type': 'application/json',
            'Authorization':  localStorage.getItem('access_token') 
                                    ? `Bearer ${localStorage.getItem('access_token')}` : null
        }
})
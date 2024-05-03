import { FC, useState, createContext} from 'react';
import AuthContextProps from './AuthProviderInterface';

export const AuthContext = createContext<AuthContextProps>({} as AuthContextProps);

const AuthProvider: FC = ({ children }) => {
    const [isAuth, setIsAuth] = useState<boolean>( localStorage.getItem('access_token')? true : false );

    return (
        <AuthContext.Provider value={{isAuth, setIsAuth}}>
            {children}
        </AuthContext.Provider>
    )
}

export default AuthProvider
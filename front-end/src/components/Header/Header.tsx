import { FC, useState } from 'react'
import styles from './Header.module.scss'
import { HiMenuAlt1 } from "react-icons/hi";
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../../hooks/useAuth';
import { FaUserCircle } from "react-icons/fa";
import UserWindow from '../UserWindow/UserWindow';


const Header: FC = () => {
      const [showUserWindow, setShowUserWindow] = useState<boolean>(false)
      const navigate = useNavigate()
      const {setIsAuth} = useAuth()
      
      const logout = () => {
            localStorage.clear()
            setIsAuth(false)
            navigate('/')
      }

      return (
            <>
                  <header className={styles.header}>
                        <div className={styles.header__right}>
                              <a className={styles.link__menu}>
                                    <HiMenuAlt1 />
                              </a>
                              <Link to='/index' className={styles.link}>Главная</Link>  
                              <Link to='/contacts' className={styles.link}>Контакты</Link>        
                        </div>
                        <div className={styles.header__right}>
                              <a onClick={logout} className={styles.link}>Выйти</a>        
                              <a className={styles.link__user} onClick={() => setShowUserWindow(true)}>
                                    <FaUserCircle />
                              </a>
                        </div>
                  </header>
                  {showUserWindow? 
                        (<UserWindow closeWindow={setShowUserWindow}/>) : ""}
            </>
      )
}

export default Header
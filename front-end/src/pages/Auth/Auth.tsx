import {FC, useEffect, useState} from 'react'
import styles from './Auth.module.scss'
import { useAuth } from '../../hooks/useAuth';
import { useNavigate } from 'react-router-dom';
import Button from '../../components/ui/Button/Button';
import { $axios } from '../../api';
import Message from '../../components/ui/Message/Message';


const Auth: FC = () => {
  const navigate = useNavigate()
  const {isAuth, setIsAuth} = useAuth()
  const [pageType, setPageType] = useState<string>('Регистрация');
  const [errorMessage, setErrorMessage] = useState<string>('')
  const [form, setForm] = useState({})


  useEffect(() => {
    isAuth ? navigate('/') : navigate
    document.title = pageType
    
    if (pageType == 'Регистрация') {
      setForm({
        'username': '',
        'email': '',
        'password': '',
        'password_confirmation': '',
      })
    } else {
      setForm({
        'email': '',
        'password': '',
      })
    }
  }, [pageType])

  const getComponentName = (key: string): string => {
    switch (key) {
      case 'username':
        return 'Имя пользователя'
      case 'email':
        return 'Почта'
      case 'password':
        return 'Пароль'
      case 'password_confirmation':
        return 'Подтверждение пароля'
      default:
        return ''
    }
  }

  const auth = (e) => {
    e.preventDefault()
    
    $axios.post(pageType == 'Регистрация' 
                  ? '/auth/sign-up/' : '/auth/sign-in/', form)
          .then(res => {
              console.log(res)
              localStorage.setItem('access_token', res.data.access_token)
              // localStorage.setItem('refresh_token', res.data.refresh_token)

              setIsAuth(true)
              window.location.reload()
              navigate('/')
          })
          .catch(e => {
            setErrorMessage(e.response.data.message)
          })
  }

  return (
    <div className={styles.auth}>
      {errorMessage && <Message text={errorMessage} />}
      <form className={styles.form} method="post" onSubmit={auth}>
        <h1>{pageType}</h1>

        {Object.keys(form).map((key, index) => (
          <div className={styles.form__component} key={key}>
            <label>{getComponentName(key)}:</label>
            <input
              key={index}
              type={key == 'password' || key == 'password_confirmation' ? 'password' : 'text'}
              name={key}
              value={form[key]}
              onChange={(e) => setForm({ ...form, [key]: e.target.value })}
            />
          </div>
        ))}

        <Button onClick={auth}>Продолжить</Button>

        <div className={styles.form__change__type}>
          {pageType == 'Регистрация' ? (
            <>
              <p>У вас уже есть аккаунт?</p> 
              <a onClick={() => setPageType('Вход')}>Вход</a>
            </>
          ) : (
            <>
              <p>У вас нет аккаунта?</p>
              <a onClick={() => setPageType('Регистрация')}>Регистрация</a>
            </>
          )}
        </div>
      </form>
    </div>
  )
}

export default Auth
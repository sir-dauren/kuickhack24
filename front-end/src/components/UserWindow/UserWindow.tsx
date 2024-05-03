import { FC, useEffect, useState } from 'react'
import styles from './UserWindow.module.scss'
import Button from '../ui/Button/Button'
import { $axios } from '../../api'

const UserWindow:FC = ({closeWindow}) => {
  const [form, setForm] = useState({})

  const handleKeyPress = (event: any) => {
    if (event.key === 'Escape') {
      closeWindow(false);
    }
  };


  useEffect(() => {
    getProfileData()

    setForm({
      'username': '',
      'email': '',
      'monthly_salary': '',
    })
    document.addEventListener('keydown', handleKeyPress);

    return () => {
      document.removeEventListener('keydown', handleKeyPress);
    };
  }, [])

  const getProfileData = () => {
    $axios.get('/auth/profile/')
      .then(res => {
        console.log(res)

        setForm({
          'username': res.data.user.username,
          'email': res.data.user.email,
          'monthly_salary': '',
        })
      })
      .catch(err => {
        console.log(err)
      })
  }

  const getComponentName = (key: string): string => {
    switch (key) {
      case 'username':
        return 'Имя пользователя'
      case 'email':
        return 'Почта'
      case 'monthly_salary':
        return 'Средний доход в месяц'
      default:
        return ''
    }
  }

  return (
    <div className={styles.user__window}>
      <div className={styles.user__window__back}  onClick={() => closeWindow(false)}></div>
      <div className={styles.user__window__item}>
            <h2>Изменить профиль</h2>
            
            {Object.keys(form).map((key, index) => (
              <div className={styles.user__window__component} key={key}>
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

            <button>Сохранить</button>
      </div>
    </div>
  )
}

export default UserWindow

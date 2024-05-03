import {FC} from 'react'
import styles from './Loader.module.scss'

const Loader:FC = () => {
  return (
      <div className={styles.pre_loader}>
            <div className={styles.loader}></div>
      </div>
  )
}

export default Loader
import { FC, useState } from 'react'
import styles from './CreateForm.module.scss'
import { $axios } from '../../api';
import Message from '../ui/Message/Message';
import Loader from '../ui/Loader/Loader';

const CreateForm: FC = ({ getDocuments }) => {
      const [errorMessage, setErrorMessage] = useState<string>('')
      const [showLoader, setShowLoader] = useState<boolean>(false)
      const [showForm, setShowForm] = useState<boolean>(true)
      
      const handleFileChange = async (e: React.ChangeEvent<HTMLInputElement>) => {
            const file = e.target.files && e.target.files[0];
            if (file) {
                  const formData = new FormData();
                  formData.append('document', file);
                  setShowLoader(true)
                  setShowForm(false)
            
                  $axios.post('/documents/create/', formData, {
                  headers: {
                        'Content-Type': 'multipart/form-data',
                  }
                  })  
                        .then(res => {
                              console.log(res)
                              getDocuments()

                              setShowLoader(false)
                              setShowForm(true)
                        })
                        .catch(err => {
                              setErrorMessage(err.response.data.message)
                              
                              setShowLoader(false)
                              setShowForm(true)
                        })
            }
      };

      return (
            <div className={styles.form}>
                  {errorMessage && <Message text={errorMessage} />}
                  
                  {showForm ? (
                        <input
                              type='file'
                              onChange={handleFileChange}
                        />
                  ): ""}

                  {showLoader ? <Loader /> : ''}
            </div>
      )
}

export default CreateForm
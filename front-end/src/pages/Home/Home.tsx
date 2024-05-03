import {FC, useEffect, useState} from 'react'
import Header from '../../components/Header/Header'
import CreateForm from '../../components/CreateForm/CreateForm'
import styles from './Home.module.scss'
import { $axios } from '../../api'
import Message from '../../components/ui/Message/Message'
import { $URL } from '../../url'

interface Document {
  id: number;
  text: string;
  file: string;
  created: string;
}

const Home: FC = () => {
  const [errorMessage, setErrorMessage] = useState<string>('')
  const [documents, setDocuments] = useState<Document[]>([])

  useEffect(() => {
    document.title = 'Дом'
    getAllDocuments()
  }, [])

  const getAllDocuments = () => {
    $axios.get('/documents/')
        .then(res => {
          console.log(res)
          setDocuments(res.data.content)
        })
  }

  const formatedData = (timestamp: string): string => {
    const date = new Date(timestamp)
    const mounth = date.getMonth() + 1
    const day = date.getDate()
    const year = date.getFullYear()
    const hours = date.getHours()
    const minutes = date.getMinutes()

    return `${mounth}.${day}.${year} ${hours}:${minutes < 10 ? '0' : ''}${minutes}`
  }

  const deleteDocument = (id) => {
      if (confirm("Вы действительно хотите удалить этот документ?")) {
        $axios.delete(`/documents/${id}/`)
          .then(res => {
            console.log(res)
            getAllDocuments()
          })
          .catch(e => {
            setErrorMessage(e.response.data.message)
          })
      }
  }

  return (
    <div className={styles.home}>
      {errorMessage && <Message text={errorMessage} />}

      <Header />

      <h1>Документы</h1>
      <div className={styles.filters}>
        <span>Документы</span>
        <span>Изображения</span>
      </div>

      <CreateForm getDocuments={getAllDocuments} />

      <div className={styles.document_list}>
        {documents.map(doc => 
          <div className={styles.document} key={doc.id}>
            <div>
              {/* <iframe src={`http://127.0.0.1:8000${doc.file}`}></iframe> */}
              <img src={`${$URL}${doc.file}`} alt='' />
              {/* <a>{doc.text ? doc.text : formatedData(doc.created)}</a> */}
              <a dangerouslySetInnerHTML={{ __html: doc.text  }}></a>
            </div>
            <p>
              <a onClick={() => {deleteDocument(doc.id)}}>Удалить</a>
            </p>
          </div>
        )}
      </div>
    </div>
  )
}

export default Home
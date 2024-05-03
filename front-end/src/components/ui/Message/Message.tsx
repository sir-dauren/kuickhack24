import { FC, useEffect, useState } from "react";
import styles from './Message.module.scss'
import { IoIosNotifications } from "react-icons/io";

const Message:FC = ({text}) => {
    const [messageText, setMessageText] = useState("")

    useEffect(() => {
        setMessageText(text)

        setTimeout(() => {
            setMessageText("")
        }, 3000)
    }, [])

    return (
        <>
            {messageText ? (
                <div className={styles.message}><IoIosNotifications /> {messageText}</div>
            ) : ""}
        </>
    )
}

export default Message
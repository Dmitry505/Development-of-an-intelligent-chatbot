import { FC } from "react";
import styles from "./ai-content.module.scss";

interface Message {
    text: string;
    isUser: boolean;
}
type AiContentPropsType = {
    messages: Message[];
};

export const AiContent: FC<AiContentPropsType> = ({ messages }) => {
    return (
        <div className={styles.aiContent}>
            {messages?.map((message: Message, index: number) => (
                <div
                    key={index}
                    className={`${styles.message} ${
                        message.isUser ? styles.userMessage : styles.botMessage
                    }`}
                >
                    {message.text}
                </div>
            ))}
        </div>
    );
};

import { FC, useState } from "react";
import styles from "./query-input.module.scss";
import ArrowUpwardIcon from "@mui/icons-material/ArrowUpward";
import { client } from "../../constants";
import { CircularProgress } from "@mui/material";

type QueryInputPropsType = {
    addMessage: (message: string, isUser: boolean) => void;
};
export const QueryInput: FC<QueryInputPropsType> = ({ addMessage }) => {
    const [query, setQuery] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!query) return;

        addMessage(query, true);

        try {
            setQuery("");
            setIsLoading(true);
            const response = await client.get(`/user_message/${query}`);
            const botMessage =
                response.data?.text || "Ответ от сервера отсутствует";
            addMessage(botMessage, false);
        } catch (error) {
            console.error("Ошибка:", error);
            addMessage("Произошла ошибка при обработке запроса", false);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <form className={styles.query} onSubmit={handleSubmit}>
            <input
                className={styles.queryInput}
                placeholder="Создай запрос..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button
                disabled={isLoading}
                className={styles.queryButton}
                type="submit"
            >
                {isLoading ? (
                    <CircularProgress size={24} style={{ color: "white" }} />
                ) : (
                    <ArrowUpwardIcon className={styles.queryArrow} />
                )}
            </button>
        </form>
    );
};

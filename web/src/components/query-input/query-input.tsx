import { useState } from 'react';
import styles from './query-input.module.scss';
import ArrowUpwardIcon from '@mui/icons-material/ArrowUpward';
import axios from 'axios';

export const QueryInput = () => {
    const [query, setQuery] = useState('');

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        if (!query) return;

        try {
            const response = await axios.post('api', {
                query,
            });

            console.log(response.data); 
        } catch (error) {
            console.error('Ошибка:', error);

        }
        setQuery(''); 

    };

    return (
        <form className={styles.query} onSubmit={handleSubmit}>
            <input
                className={styles.queryInput}
                placeholder="Создай запрос..."
                value={query}
                onChange={(e) => setQuery(e.target.value)}
            />
            <button className={styles.queryButton} type="submit">
                <ArrowUpwardIcon className={styles.queryArrow} />
            </button>
        </form>
    );
};
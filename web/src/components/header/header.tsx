import styles from "./header.module.scss";
export const Header = () => {
    return (
        <div className={styles.header}>
            <h1 className={styles.title}>ПФМИШНЫЙ ГПТ</h1>
            <img width={30} height={30} src="./chill.jpeg" />
        </div>
    );
};

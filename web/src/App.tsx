import "./App.css";
import { useState } from "react";
import { AiContent } from "./components/ai-content";
import { Header } from "./components/header";
import { QueryInput } from "./components/query-input";

function App() {
    const [messages, setMessages] = useState<
        { text: string; isUser: boolean }[]
    >([]);

    const addMessage = (text: string, isUser: boolean) => {
        setMessages((prev) => [...prev, { text, isUser }]);
    };

    return (
        <div className="root">
            <Header />
            <AiContent messages={messages} />
            <QueryInput addMessage={addMessage} />
        </div>
    );
}

export default App;

import './App.css'
import { AiContent } from './components/ai-content'
import { Header } from './components/header'
import { QueryInput } from './components/query-input'

function App() {

  return (
    <div className='root'>
        
      <Header/>
      <AiContent/>
      <QueryInput/>
    </div>
  )
}

export default App

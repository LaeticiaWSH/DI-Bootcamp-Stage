import React from 'react';
import './vote.css'

class Vote extends React.Component {
    constructor(props){
        super(props);
        this.state = {
            php : "Php",
            phpCount : 0 ,
            python: "Python",
            pythonCount: 0,
            javascript: "Javascript",
            javascriptCount: 0,
            java: "Java",
            javaCount: 0

        }
    }
    countphp = () => {
        this.setState({phpCount :this.state.phpCount + 1})
    }
    countpython = () => {
        this.setState({ pythonCount: this.state.pythonCount + 1 })
    }
    countjavascript = () => {
        this.setState({ javascriptCount: this.state.javascriptCount + 1 })
    }
    countjava = () => {
        this.setState({ javaCount: this.state.javaCount + 1 })
    }
    render() {
        return(
            <>
                <p id='php'>{this.state.phpCount}  {this.state.php} 
                <button onClick={this.countphp}>Click Here</button></p >
                <p id='py'>{this.state.pythonCount}  {this.state.python}
                <button onClick={this.countpython}>Click Here</button></p>
                <p id='j'>{this.state.javascriptCount}  {this.state.javascript}
                <button onClick={this.countjavascript}>Click Here</button></p>
                <p id='java'>{this.state.javaCount}  {this.state.java}
                <button onClick={this.countjava}>Click Here</button></p>
            </>
        )
    }

}

export default Vote
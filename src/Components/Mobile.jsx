import React from 'react';
import '../Styles/Mobile.scss';
import mc_icon from '../Images/mc-icon.png';
import Chart from './Chart.jsx';

class Mobile extends React.Component {
    constructor (props) {
        super(props);

        this.state = {
            online: false,
            players: 0,
            maxPlayers: 0,
            users: [],
            showReport: false
        };

        this.getUsers = this.getUsers.bind(this);
        this.toggleReportView = this.toggleReportView.bind(this);
    }

    componentDidMount() {
        this.getUsers();
        this.intervalId = setInterval(() => this.getUsers(), 5000);
    }

    componentWillUnmount() {
        clearInterval(this.intervalId);
    }

    getUsers() {
        fetch("https://api.mcsrvstat.us/2/3.132.110.119")
            .then(res =>res.json())
            .then(
                (result) => {
                    if (result.players.online > 0) {
                        this.setState({
                            online: result.online,
                            players: result.players.online,
                            maxPlayers: result.players.max,
                            users: result.players.list
                        });
                    } else {
                        this.setState({
                            online: result.online,
                            players: result.players.online,
                            maxPlayers: result.players.max,
                        });
                    }
                }, (error) => {
                    console.error("Error loading API");
                }
            );
    }

    toggleReportView() {
        let newState = !this.state.showReport;
        this.setState({showReport: newState});
    }
    
    render() {
        const playersTable = this.state.users.map((name, i) =>
            <li key={i}>{name}</li>
        );

        return (
            <div className="mobile-app">
                <div className="header">
                    <div className="header-subgroup">
                        <img classname="header-icon" src={mc_icon} alt="icon" />
                        <div className="header-text">
                            <h1 className="header-1">BU Minecraft</h1>
                            <h3>3.132.110.119</h3>
                        </div>
                    </div>
                </div>
                <div className="server-status">
                    <h2 className="online-status">{this.state.players}/{this.state.maxPlayers}</h2>
                </div>
                <ul className="player-list">
                    {playersTable}
                </ul>
                <div className="usage-report">
                    <div className="usage-toggle" onClick={this.toggleReportView}>
                        <label>Show/Hide April cost report</label>
                    </div>
                    <div className="usage-image">
                        { this.state.showReport ? <Chart /> : null }
                    </div>
                </div>
            </div>
        );
    }
}

export default Mobile;
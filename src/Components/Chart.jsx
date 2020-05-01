import React from 'react';
import usage_costs from '../Images/usage_costs.png';
// import './Chart.scss';

class Chart extends React.Component {
  render() {
    return (
      <div className='Graphs'>
          <img src={usage_costs} alt="cost-report" className="image" />
      </div>
    );
  }
}

export default Chart;
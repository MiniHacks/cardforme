import React from 'react';
import { Pie } from 'react-chartjs-2';
import { Box, useColorModeValue } from '@chakra-ui/react';

type SpendingData = {
  dining: number;
  flights: number;
  car_rental: number;
  gas: number;
  entertainment: number;
  hotel: number;
  other: number;
};

type SpendingPieChartProps = {
  data: SpendingData;
};

const SpendingPieChart: React.FC<SpendingPieChartProps> = ({ data }) => {
  const chartData = {
    labels: ['Dining', 'Flights', 'Car Rental', 'Gas', 'Entertainment', 'Hotel', 'Other'],
    datasets: [
      {
        data: [
          data.dining,
          data.flights,
          data.car_rental,
          data.gas,
          data.entertainment,
          data.hotel,
          data.other,
        ],
        backgroundColor: [
          '#FF6384',
          '#36A2EB',
          '#FFCE56',
          '#FF5733',
          '#33FF57',
          '#8533FF',
          '#33FFF3',
        ],
      },
    ],
  };

  const chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
  };

  const bgColor = useColorModeValue('white', 'gray.800');

  return (
    <Box bg={bgColor} p={4} borderRadius="md" shadow="md" width="100%" height="400px">
      <Pie data={chartData} options={chartOptions} />
    </Box>
  );
};

export default SpendingPieChart;

export const pieChartOptions = {
  labels: [
    "Restaurants and Dining",
    "Groceries",
    "Gas",
    "Retail",
    "Entertainment",
    "Car Rental",
    "Hotel",
    "Other",
  ],
  colors: [
    "#7B55D7",
    "#D45909",
    "#D8056B",
    "#DD6CA2",
    "#E1E9F8",
    "#851E97",
    "#391435",
    "#D8716E",
  ],
  chart: {
    width: "50px",
  },
  states: {
    hover: {
      filter: {
        type: "none",
      },
    },
  },
  legend: {
    show: false,
  },
  dataLabels: {
    enabled: false,
  },
  hover: { mode: null },
  plotOptions: {
    donut: {
      expandOnClick: true,
      donut: {
        labels: {
          show: true,
        },
      },
    },
  },
  fill: {
    colors: [
      "#7B55D7",
      "#D45909",
      "#D8056B",
      "#DD6CA2",
      "#8F96CD",
      "#851E97",
      "#391435",
      "#D8716E",
    ],
  },
  tooltip: {
    enabled: true,
    theme: "dark",
  },
};

export const pieChartData = [44, 55, 13, 43, 22, 13, 22, 13];

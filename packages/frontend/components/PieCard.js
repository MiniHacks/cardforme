import { Box, Flex, Text, Select, useColorModeValue } from "@chakra-ui/react";
// Custom components

import { pieChartData, pieChartOptions } from "./charts";
import PieChart from "./PieChart";

export default function Conversion(props) {
  const { ...rest } = props;

  // Chakra Color Mode
  const textColor = useColorModeValue("secondaryGray.900", "white");
  const cardColor = useColorModeValue("white", "navy.700");
  const cardShadow = useColorModeValue(
    "0px 18px 40px rgba(112, 144, 176, 0.12)",
    "unset"
  );
  return (
    <Box p={"20px"} align={"center"} direction={"column"} w={"100%"} {...rest}>
      <Flex
        px={{ base: "0px", "2xl": "10px" }}
        justifyContent={"space-between"}
        alignItems={"center"}
        w={"100%"}
        mb={"8px"}
      />

      <PieChart
        h={"100px"}
        w={"100px"}
        chartData={pieChartData}
        chartOptions={pieChartOptions}
      />
    </Box>
  );
}

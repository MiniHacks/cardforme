import type { NextPage } from "next";
import { Box, Heading, HStack, VStack } from "@chakra-ui/react";
import PageLayout from "../components/Layout/PageLayout";
import Head from 'next/head';
import React from "react";

const Home: NextPage = () => {

  const gradientStyle = {
    background: "linear-gradient(134.57deg, #FF4900 25.78%, #FF0080 39.24%, #8152FF 52.68%)",
    WebkitBackgroundClip: "text",
    WebkitTextFillColor: "transparent",
    backgroundClip: "text",
    textFillColor: "transparent",
  };

  return (
    <PageLayout title={"cardforme"}>
      <HStack spacing={0} w="100%">
        <Box width="50%" height="100vh">
          <HStack paddingLeft={10} paddingTop={6}>
            <Heading fontFamily="Monoton"
                     fontWeight="400"
                     fontSize="65px"
                     lineHeight="110%"
                     color="#FF8A00"
                     textShadow="0px 4px 4px rgba(0, 0, 0, 0.25)"
            >c</Heading>
            <Heading fontFamily="Monoton"
                     fontWeight="400"
                     fontSize="65px"
                     lineHeight="110%"
                     color="#FF00C7"
                     textShadow="0px 4px 4px rgba(0, 0, 0, 0.25)"
            >m</Heading>
          </HStack>
          <VStack align="left" paddingLeft="10" paddingTop="30" >
            <Heading fontFamily="Outfit"
                     fontWeight="700"
                     fontSize="100px"
                     lineHeight="90%"

            >
              find the
            </Heading>
            <Heading fontFamily="Outfit"
                     fontWeight="700"
                     fontSize="100px"
                     lineHeight="90%"
            >
              card for
            </Heading>
            <Heading fontFamily="Outfit"
                     fontWeight="700"
                     fontSize="100px"
                     lineHeight="90%"
                     style={gradientStyle}
            >
              you
            </Heading>
          </VStack>
        </Box>
        <Box width="50%" height="100vh">
          <Box style={{
            width: '100%',
            height: '100%',
            background: 'conic-gradient(from 180deg at 0.00% 100.00%, #5200FF 120deg, #FF8A00 360deg)'
          }}>
            <Box>
            </Box>
          </Box>
        </Box>

      </HStack>
    </PageLayout>
  );
};

export default Home;

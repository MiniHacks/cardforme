import type { NextPage } from "next";
import { Box, Heading, HStack } from "@chakra-ui/react";
import PageLayout from "../components/Layout/PageLayout";
import Head from 'next/head';

const Home: NextPage = () => {
  return (
    <PageLayout title={"geese, by minihacks"}>
      <Head>
        <link rel='preconnect' href='https://fonts.googleapis.com' />
        <link
            rel='preconnect'
            href='https://fonts.gstatic.com'
            crossOrigin='true'
        />
        <link
            href='https://fonts.googleapis.com/css2?family=Roboto+Mono:ital,wght@1,700&display=swap'
            rel='stylesheet'
        />
      </Head>
      <HStack spacing={0} w="100%">
        <Box width="50%" height="100vh">
          <Heading fontFamily="Roboto Mono" fontWeight="bold" fontStyle="italic">Your Text Here</Heading>
        </Box>
        <Box width="50%" height="100vh">
          <div style={{
            width: '100%',
            height: '100%',
            background: 'conic-gradient(from 180deg at 0.00% 100.00%, #5200FF 120deg, #FF8A00 360deg)'
          }}>
            test
          </div>
        </Box>
      </HStack>
    </PageLayout>
  );
};

export default Home;

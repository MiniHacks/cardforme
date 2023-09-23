import type { NextPage } from "next";
import { Box, Heading, HStack, VStack } from "@chakra-ui/react";
import PageLayout from "../components/Layout/PageLayout";
import ViewCard from "../components/ViewCard";

const Home: NextPage = () => {
  return (
    <Box backgroundColor="#06021C" height="100%">
    <ViewCard />
    </Box>
  );
};

export default Home;

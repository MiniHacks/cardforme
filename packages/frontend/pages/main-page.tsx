import type { NextPage } from "next";
import {
  Box,
  Flex,
  Heading,
  IconButton,
  Icon,
  HStack,
  Text,
  VStack,
} from "@chakra-ui/react";
import { ArrowLeftIcon, ArrowRightIcon } from "@chakra-ui/icons";
import React, { useEffect, useState } from "react";

import GradientSpotlight from "../components/GradientSpotlight";
import ViewCard from "../components/ViewCard";
import PieCard from "../components/PieCard";

const Home: NextPage = () => {
  const [transactions, setTransactions] = useState([]);

  useEffect(() => {
    async function fetchTransactions() {
      try {
        const response = await fetch("/api/get-transactions", {
          method: "POST",
          headers: {
            Authorization: window.localStorage.getItem("token"),
          },
        });

        if (!response.ok) {
          throw new Error("Failed to fetch transactions");
        }

        const transactionsData = await response.json();
        setTransactions(transactionsData);
      } catch (error) {
        console.error("Error fetching transactions:", error);
      }
    }

    // Fetch transactions when the component mounts
    fetchTransactions();
  }, []); // Empty dependency array ensures this runs once when the component mounts

  useEffect(() => {
    // Log transactions when it changes
    console.log(transactions);
  }, [transactions]);

  const cardsData = [
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    {
      imageSrc: "/images/amex_platinum.png",
      cardName: "Amex Platinum",
      cardDescription: "Travel & Hotel credit",
      link: "https://www.americanexpress.com/us/credit-cards/card/platinum/",
    },
    // Add more duplicates if needed
  ];

  const cardsPerSlide = 3;
  const [currentIndex, setCurrentIndex] = useState(0);

  const handleNext = () => {
    setCurrentIndex(
      (prevIndex) => (prevIndex + cardsPerSlide) % cardsData.length
    );
  };

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0
        ? cardsData.length - (cardsData.length % cardsPerSlide)
        : prevIndex - cardsPerSlide
    );
  };

  const pageStyle: React.CSSProperties = {
    backgroundColor: "#06021C",
    height: "150vh",
  };

  const carouselStyle: React.CSSProperties = {
    width: "100%",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    position: "relative",
  };

  const isLastPage = currentIndex + cardsPerSlide >= cardsData.length;

  return (
    <div style={pageStyle}>
      <Box>
        <Heading
          color={"#FFFFFF"}
          fontFamily={"Outfit"}
          ml={192}
          pt={25}
          pb={15}
        >
          Customer Favorites
        </Heading>
      </Box>
      <Box style={carouselStyle}>
        {/* GradientSpotlight components */}
        <Box
          position={"absolute"}
          left={"-80px"}
          top={"100px"}
          zIndex={0} // Set a lower zIndex
        >
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        <Box
          position={"absolute"}
          left={"400px"}
          top={"0px"}
          zIndex={0} // Set a lower zIndex
        >
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        <Box
          position={"absolute"}
          left={"1000px"}
          top={"-200px"}
          zIndex={0} // Set a lower zIndex
        >
          <GradientSpotlight /> {/* Use the GradientSpotlight component */}
        </Box>
        {/* Navigation Buttons */}
        <IconButton
          icon={<Icon as={ArrowLeftIcon} boxSize={4} />}
          aria-label={"Previous"}
          isDisabled={currentIndex === 0}
          onClick={handlePrevious}
          position={"absolute"}
          left={"20px"}
          top={"50%"}
          transform={"translateY(-50%)"}
        />
        <IconButton
          icon={<Icon as={ArrowRightIcon} boxSize={4} />}
          aria-label={"Next"}
          isDisabled={isLastPage}
          onClick={handleNext}
          position={"absolute"}
          right={"20px"}
          top={"50%"}
          transform={"translateY(-50%)"}
        />
        {/* Cards */}
        <Flex>
          {cardsData
            .slice(currentIndex, currentIndex + cardsPerSlide)
            .map((card, index) => (
              <Box
                key={index}
                zIndex={1}
                marginRight={"20px"} // Add margin between cards
              >
                <ViewCard
                  imageSrc={card.imageSrc}
                  cardName={card.cardName}
                  cardDescription={card.cardDescription}
                  cardNumber={currentIndex + index + 1}
                  onClick={() => window.open(card.link)}
                />
              </Box>
            ))}
        </Flex>
        {/* Add Next and Previous buttons here */}
      </Box>
      <Box>
        <Heading
          color={"#FFFFFF"}
          fontFamily={"Outfit"}
          ml={192}
          mt={50}
          pt={30}
          pb={15}
        >
          Your Data
        </Heading>
        <HStack justifyContent={"center"}>
          <Box pr={"10%"}>
            <VStack justifyContent={"left"}>
              <Heading
                fontFamily={"Outfit"}
                fontWeight={"600"}
                textAlign={"center"}
                fontSize={"50px"}
                lineHeight={"90%"}
                textColor={"#FFFFFF"}
              >
                Here’s a pie chart
              </Heading>
              <Heading
                fontFamily={"Outfit"}
                fontWeight={"600"}
                textAlign={"center"}
                fontSize={"50px"}
                lineHeight={"115%"}
                textColor={"#FFFFFF"}
              >
                of this month’s
              </Heading>
              <Heading
                fontFamily={"Outfit"}
                fontWeight={"600"}
                textAlign={"left"}
                fontSize={"50px"}
                pb={"20px"}
                lineHeight={"90%"}
                textColor={"#FFFFFF"}
              >
                spending.
              </Heading>
              <Box
                as={"button"}
                color={"white"}
                fontWeight={"bold"}
                borderRadius={"12px"}
                width={"200px"}
                height={"50px"}
                bgGradient={"linear(to-l, #5200FF,#FF0080, #FF8A00)"}
                marginTop={"50px"}
                zIndex={1}
                _hover={{
                  transform: "scale(1.02)",
                }} // Call the fetchTransactions function when the button is clicked
              >
                <Text>Fetch Transactions</Text>
              </Box>
            </VStack>
          </Box>
          <Box pr={"10px"}>
            <VStack>
              <Text
                fontFamily={"Outfit"}
                fontWeight={"500"}
                textAlign={"center"}
                fontSize={"30px"}
                lineHeight={"115%"}
                textColor={"#FFFFFF"}
                mt={-10}
              >
                Total Spending: <b>$1,000</b>
              </Text>
              <PieCard />
            </VStack>
          </Box>
        </HStack>
      </Box>
    </div>
  );
};

export default Home;

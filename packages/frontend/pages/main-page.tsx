import type { NextPage } from "next";
import { Box, Button, Flex, Heading, IconButton, Icon } from "@chakra-ui/react";
import { ArrowLeftIcon, ArrowRightIcon } from "@chakra-ui/icons";
import React from "react";
import ViewCard from "../components/ViewCard";

const Home: NextPage = () => {
  const numViewCards = 5; // Adjust this to the total number of ViewCards
  const cardsPerSlide = 3; // Number of cards to display at a time
  const [currentIndex, setCurrentIndex] = React.useState(0);

  const handleNext = () => {
    setCurrentIndex((prevIndex) => (prevIndex + cardsPerSlide) % numViewCards);
  };

  const handlePrevious = () => {
    setCurrentIndex((prevIndex) =>
      prevIndex === 0
        ? numViewCards - (numViewCards % cardsPerSlide)
        : prevIndex - cardsPerSlide
    );
  };

  const carouselStyle: React.CSSProperties = {
    backgroundColor: "#06021C",
    width: "100%",
    height: "100vh",
    display: "flex",
    flexDirection: "column", // Change to column layout
    alignItems: "center",
    justifyContent: "center",
    position: "relative", // Add relative positioning
  };

  const isLastPage = currentIndex + cardsPerSlide >= numViewCards;

  return (
    <Box style={carouselStyle}>
      {/* Left Icon */}
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

      {/* Right Icon */}
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

      {/* Header */}
      <Heading as={"h1"} size={"2xl"} mb={4}>
        Your Carousel Header
      </Heading>

      <Flex justifyContent={"center"} alignItems={"center"}>
        {Array.from({ length: cardsPerSlide }).map((_, index) => (
          <div
            key={currentIndex + index}
            style={{
              display: "block",
              marginRight: "10px", // Adjust the margin as needed
            }}
          >
            {currentIndex + index < numViewCards && <ViewCard />}
          </div>
        ))}
      </Flex>
    </Box>
  );
};

export default Home;

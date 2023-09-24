import type { NextPage } from "next";
import { Box, Button, Flex, Heading, IconButton, Icon } from "@chakra-ui/react";
import { ArrowLeftIcon, ArrowRightIcon } from "@chakra-ui/icons";
import ViewCard from "../components/ViewCard";
import React from "react";

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
  };

  const isLastPage = currentIndex + cardsPerSlide >= numViewCards;

  return (
    <Box style={carouselStyle}>
      {/* Header */}
      <Heading as="h1" size="2xl" mb={4}>
        Your Carousel Header
      </Heading>

      {/* Previous Button */}
      <IconButton
        icon={<Icon as={ArrowLeftIcon} boxSize={8} />}
        aria-label="Previous"
        isDisabled={currentIndex === 0}
        onClick={handlePrevious}
        mb={4}
      />

      <Flex justifyContent="center" alignItems="center">
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

      {/* Next Button */}
      <IconButton
        icon={<Icon as={ArrowRightIcon} boxSize={8} />}
        aria-label="Next"
        isDisabled={isLastPage}
        onClick={handleNext}
        mt={4}
      />
    </Box>
  );
};

export default Home;

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

  const pageStyle: React.CSSProperties = {
    backgroundColor: "#06021C", // Background color for the entire page
    height: "100vh", // Full viewport height
  };

  const carouselStyle: React.CSSProperties = {
    width: "100%",
    display: "flex",
    flexDirection: "column", // Change to column layout
    alignItems: "center",
    justifyContent: "center",
    position: "relative", // Add relative positioning
  };

  const isLastPage = currentIndex + cardsPerSlide >= numViewCards;

  return (
    <div style={pageStyle}>
      <Box>
        <Heading as="h1" size="2xl" mb={4} color="#FFFFFF" textAlign="left" ml={4}>
          Personal Picks
        </Heading>
      </Box>
      <Box style={carouselStyle}>
        {/* Left Icon */}
        <IconButton
          icon={<Icon as={ArrowLeftIcon} boxSize={4} />}
          aria-label="Previous"
          isDisabled={currentIndex === 0}
          onClick={handlePrevious}
          position="absolute"
          left="20px"
          top="50%"
          transform="translateY(-50%)"
        />

        {/* Right Icon */}
        <IconButton
          icon={<Icon as={ArrowRightIcon} boxSize={4} />}
          aria-label="Next"
          isDisabled={isLastPage}
          onClick={handleNext}
          position="absolute"
          right="20px"
          top="50%"
          transform="translateY(-50%)"
        />

        <div style={{ display: "flex", flexDirection: "row", overflowX: "auto" }}>
          {Array.from({ length: cardsPerSlide }).map((_, index) => (
            <div
              key={currentIndex + index}
              style={{
                display: "block",
                marginRight: "10px", // Adjust the margin as needed
                padding: "10px", // Add padding between ViewCards
              }}
            >
              {currentIndex + index < numViewCards && <ViewCard 
  imageTestId="amex_platinum.png" 
  textTestId={""} 
  onClick={() => {
    window.location.href = "https://www.americanexpress.com/us/credit-cards/card-application/apply/platinum-card/25330-10-0?pmccode=137&intlink=US-Acq-Shop-Consumer-PDP-Platinum-Prospect-Apply-intro#/";
  }} 
/>
}
            </div>
          ))}
        </div>
      </Box>
    </div>
  );
};

export default Home;

